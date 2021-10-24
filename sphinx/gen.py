from os import path
from collections import defaultdict
from sphinxcontrib.writers.rst import RstTranslator
import docutils.nodes
import sphinx.builders
import unidecode

class RstTranslatorTweak(RstTranslator):
    # bugfix https://github.com/sphinx-contrib/restbuilder/pull/28
    def visit_colspec(self, node):
        self.table[0].append(round(node['colwidth']))
        raise docutils.nodes.SkipNode

    # skips id labels
    # if the source of RstTranslator.visit_target is viewed, it is also possible to skip target output via minor document mutation
    def visit_target(self, node):
        raise docutils.nodes.SkipNode

class Builder(sphinx.builders.Builder):
    name = __name__
    out_suffix = '.py'
    indentation = '    '
    def doc2targetpath(self, docname):
        return path.join(self.outdir, path.basename(docname) + self.out_suffix)
    def get_outdated_docs(self):
        for docname in self.env.found_docs:
            if docname not in self.env.all_docs:
                yield docname
                continue
            targetname = self.doc2targetpath(docname)
            try:
                targetmtime = path.getmtime(targetname)
            except Exception:
                targetmtime = 0
            try:
                srcmtime = path.getmtime(self.env.doc2path(docname))
                if srcmtime > targetmtime:
                    yield docname
            except OSError:
                # source doesn't exist anymore
                pass
    def prepare_writing(self, docnames):
        pass
    def get_target_uri(self, docname : str, typ : str = None) -> str:
        return ''
    @staticmethod
    def node_has_name(node, predicate):
        return hasattr(node, 'attributes') and any((predicate(name) for name in node.attributes['names']))
    def write_stub(self, file, indent, sig, document, *docnodes):
        file.write(indent + 'def ' + unidecode.unidecode(sig) + ':\n')
        indent2 = indent + self.indentation
        lines = []
        for docnode in docnodes:
            doc = self.node_to_rst(document, docnode).strip()
            if len(doc):
                lines.extend(doc.split('\n'))
        lines[0] = '"""' + lines[0]
        lines[-1] += '"""'
        lines.append('raise NotImplementedError\n')
        for line in lines:
            file.write(indent2 + line + '\n')
    def node_to_rst(self, document, node):
        self.config.rst_indent = len(self.indentation)
        trans = RstTranslatorTweak(document, self)
        trans.visit_document(document)
        node.walkabout(trans)
        trans.depart_document(document)
        return trans.body
    def write_doc(self, docname: str, doctree: 'docutils.nodes.document'):
        with open(self.doc2targetpath(docname), 'wt') as output:
            for node in doctree.traverse():
                if self.node_has_name(node, lambda name: name.startswith('constant-')):
                    const_name = node[0].rawsource
                    const_descr = node[1].rawsource
                    if type(node[2]) is docutils.nodes.literal_block:
                        const_example = node[2].rawsource.strip().rstrip('.')
                    else:
                        const_example = const_name + ' = float("' + const_name + '")'
                    output.write(const_example + '\n')
                    output.write('"""' + self.node_to_rst(doctree, node).strip() + '"""\n\n')
                elif self.node_has_name(node, lambda name: name == 'data-types'):
                    for section in node.traverse(docutils.nodes.section, include_self=False):
                        dt_name = section[0].astext()
                        if ' ' not in dt_name:
                            output.write(dt_name + ' = NotImplemented\n')
                            output.write('"""' + self.node_to_rst(doctree, section) + '"""\n\n')
                        else:
                            break
                elif self.node_has_name(node, lambda name: name.startswith('function-')):
                    sig = node[0].astext()
                    if '(' in sig:
                        self.write_stub(output, '', sig, doctree, *node[1:])
                elif self.node_has_name(node, lambda name: name.endswith('-object')):
                    object_name = node[0].astext().split(' ')[0]
                    write = self.WritingObject(self, output, doctree, object_name)
                    for node in node.traverse():
                        if self.node_has_name(node, lambda name: name.startswith('attribute-')):
                            write.add_member('prop', node[0].astext() + '(self)', node)#*node.children[1:])
                        elif self.node_has_name(node, lambda name: name.startswith('method-')):
                            write.add_member('func', node[0].astext(), node)#*node.children[1:])
                        elif isinstance(node, docutils.nodes.list_item):
                            list_item = node
                            text = list_item.astext()
                            # documented later in file
                            #if text.startswith('operator.'):
                            #    write.add_member('func', text[len('operator.'):], list_item.parent.parent[0][0], list_item[0])
                            if 'May be implemented via ' in text:
                                write.add_member('func', text[text.rindex(' ') + 1:-1] + '(self, other)', list_item[0])
                            elif text.startswith('__r') and text.endswith('__'):
                                write.add_member('func', text + '(self, other)', list_item[0])
                    write.write()
    def finish(self):
        modules = [path.basename(docname) for docname in self.env.all_docs]
        with open(self.doc2targetpath('__init__'), 'wt') as output:
            for docname in self.env.all_docs:
                modname = path.basename(docname)
                output.write('from .' + modname + ' import *\n')
            output.write('__all__ = dir()')
    
    class WritingObject:
        def __init__(self, builder, file, doc, objectname):
            self.builder = builder
            self.output = file
            self.doc = doc
            self.objectname = objectname
            
            self.members = defaultdict(list)
            self.sigs = {}
        def add_member(self, type, sig, *docnodes):
            title = sig.split('(')[0]
            self.members[title].extend(docnodes)
            self.sigs[title] = (type, sig)
        def write(self):
            indent = self.builder.indentation
            indent2 = indent * 2

            self.output.write('class ' + self.objectname + ':\n\n')

            for title, docnodes in self.members.items():
                type, sig = self.sigs[title]
                assert type in ('prop', 'func')
                if type == 'prop':
                    self.output.write(indent + '@property\n')
                self.builder.write_stub(self.output, indent, sig, self.doc, *docnodes)

def setup(app):
    app.add_builder(Builder)
    
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True
    }
