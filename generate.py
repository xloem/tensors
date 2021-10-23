import os
spec_dir = 'array-api/spec/API_specification'
fn = 'creation_functions.md'

import mistletoe
class Renderer(mistletoe.base_renderer.BaseRenderer):
    def __enter__(self, *params):
        self.footnotes = []
        self.cur_obj_depth = 0
        self.cur_obj_type = None
        self.cur_obj_name = None
        self.cur_depth = 0
        self.opening_quotes = False
        self.single_indentation = '    '
        self.doc_quotes = '"""'
        self.indentation = ''
        self.list_depth = 0
        return self
    def render_document(self, token):
        with self:
            text = self.render_inner(token)
            self.add_footer()
            text += self.render_footnotes()
            return text
    def render_footnotes(self):
        #result = ''
        #for content in enumerate(self.footnotes):
        #    result += self.indentation + str(idx) + ': ' + content + '\n'
        result = '\n'.join(self.footnotes)
        self.footnotes = []
        return result
    def add_footer(self):
        if self.cur_obj_type is not None:
            self.cur_obj_type, self.cur_obj_name = None, None
            self.footnotes.append(self.doc_quotes + '\n' + self.single_indentation + 'raise NotImplemented\n\n')
    def set_indent(self, amnt):
        self.cur_depth = amnt
        if amnt < self.cur_obj_depth:
            amnt = 0
            self.add_footer()
        else:
            amnt -= self.cur_obj_depth
        self.indentation = self.single_indentation * amnt
    def bump_indent(self):
        self.cur_depth += 1
        if self.cur_depth > self.cur_obj_depth:
            self.indentation += self.single_indentation
    def drop_indent(self):
        if self.cur_depth > self.cur_obj_depth:
            self.indentation = self.indentation[:-len(self.single_indentation)]
        else:
            self.add_footer()
        self.cur_depth += 1
    def render_heading(self, token):
        if self.cur_obj_name is not None:
            text = self.render_footnotes()
            content = self.render_inner(token)
            if content.startswith(self.cur_obj_name):
                self.cur_obj_depth = token.level
                self.set_indent(token.level)
                text += dict(
                    function='def '
                )[self.cur_obj_type] + content + ':'

                self.bump_indent()
                self.opening_quotes = True
            else:
                self.set_indent(token.level)
                text += '\n\n' + self.indentation + content + '\n'
            return text
        else:
            return ''
    def render_list(self, token):
        text = self.render_footnotes()

        self.list_depth += 1
        #if self.list_depth > 1:
        text += self.render_inner(token)
        #else:
        #    self.set_indent(self.cur_obj_depth)
        #    text += self.render_inner(token)
        self.list_depth -= 1
        return text
    def render_list_item(self, token):
        self.set_indent(self.cur_obj_depth + self.list_depth)
        return self.render_inner(token)
    def render_paragraph_text(self, text):
        if text[0] == '(' and text[-2:] == ')=':
            self.add_footer()
            self.cur_obj_type, self.cur_obj_name = text[1:-2].split('-')
        elif self.cur_obj_type is not None:
            if text[:4] == ':::{' and text[-3:] == ':::' and text[text.index('\n')-1] == '}':
                tagidx = text.index('\n')
                tag = text[4:tagidx - 1]
                text = tag + ':\n' + text[tagidx+1:-3].strip()
            lines = text.split('\n')
            if self.opening_quotes:
                lines[0] = self.doc_quotes + lines[0]
            lines = [self.indentation + line for line in lines]
            text = '\n' + '\n'.join(lines)
            if self.opening_quotes:
                self.opening_quotes = False
            #else:
            #    text = '\n' + text
            return text
        return ''
    def render_block_code(self, token):
        return self.render_paragraph_text(':::' + token.language + '\n' + self.render_inner(token) + ':::')
        return self.render_paragraph(token)
    def render_paragraph(self, token):
        return self.render_paragraph_text(self.render_inner(token))
    def render_link(self, token):
        if self.cur_obj_type is not None:
            #num = str(len(self.footnotes))
            #ref = '[' + num + ']_'
            #self.footnotes.append(num + ': ' + token.target)
            #return self.render_inner(token) + ref
            return '`' + self.render_inner(token) + ' <' + token.target + '>`_'
        else:
            return ''
    def render_raw_text(self, token):
        return token.content.replace('&lt;','<').replace('&gt;','>')
    def render_line_break(self, token):
        return '\n'

#class md2py(mistletoe.base_renderer.BaseRenderer):
#    def __init__(self, inner_renderer):
#        self._inner_renderer = inner_renderer
#    class ListsAndHeadings(list):
#        def __init__(self):
#            super().__init__()
#            self.headings = {}
#        def __getattr__(self, name):
#            return self[name]
#        def __getitem__(self, name):
#            result = self.headings.get(name)
#            if result is None:
#                result = self.lists[name]
#            return result
#        def __setitem__(self, name, value):
#            self.headings[name] = value
#            self.append(value)
#        def items(self):
#            return self.headings.items()
#        def keys(self):
#            return self.headings.keys()
#        def values(self):
#            return self
#        def __del__(self, name):
#            raise NotImplemented
#    def __getattr__(self, name):
#        attr = getattr(self._inner_renderer, name)
#        def wrap(token):
#            rendered = attr(token)
#            self._stack[-1].text += rendered
#            return rendered
#        return wrap
#    def __enter__(self, *params):
#        super().__enter__(*params)
#        self._root = dict(
#            text = '',
#            children = md2py.ListsAndHeadings()
#        )
#        self._stack = [self._root]
#    def render_list(self, token):
#        rendered = self._inner_renderer.render_list(token)
#        new = dict(
#            type = 'list',
#            text = '',
#            rendered = rendered,
#            children = md2py.ListsAndHeadings()
#        )
#        self._stack[-1].append(new)
#        self._stack.append(new)
#    def render_heading(self, token):
#        heading = self.render_inner(token)
#        depth = token.level
#        while depth < len(self._stack):
#            self._stack.pop()
#        assert heading not in self._stack[-1]
#        rendered = self._inner_renderer.render_heading(token)
#        new = dict(
#            type = 'heading',
#            name = heading,
#            text = '',
#            rendered = rendered,
#            children = md2py.ListsAndHeadings()
#        )
#        self._stack[-1][heading] = new
#        self._stack.append(new)
#        return rendered
        
#def md2py(*path):
#    path = os.path.join(*path)
#    text = open(path).read()
#    doc = mistletoe.Document(text)
#
#    root = {}
#
#    handlers = {
#        mistletoe.block_token.Heading:
#            lambda 
#    }
#    
#    for elem in doc.children:
#        if type(

with open(os.path.join(spec_dir, fn)) as fin:
    doc = mistletoe.Document(fin)
    renderer = Renderer()
    with renderer:
        print(renderer.render(doc))
#    with md2py(
#    rendered = mistletoe.markdown(fin, md2py)
#    print(rendered)

#import mistune
#class md2py(mistune.renderers.BaseRenderer):
#    NAME = 'py'
#    def __init__(self, inner_renderer):
#        super().__init__()
#        self._inner_renderer = inner_renderer
#    def __call__(self, *path):
#        path = os.path.join(*path)
#        text = open(path).read()
#        md = mistune.create_markdown(renderer=self)
#        self.base = {}
#        self.state = []
#        return md(text)
#    def heading(self, text, level):
#        # each heading would be a dict
#        state = ('heading', level)
#        self.heading = 
#    def list(self, text, ordered, level, start=None):
#    def list_item(self, text, level):
#    def _get_method(self, syntax_type):
#        try:
#            return getattr(self, syntax_type)
#        except Exception:
#            return self._inner_renderer._get_method(syntax_type)
#    def finalize(self, data):
#        data = list(data)
#        print('finalize:', *data)
#        #for item in data:
#        #    if item[0] == 'heading':
#        #        return data
#        #return ''.join(data)
#        return data

#parse = md2py()
#parsed = parse(spec_dir, fn)
#print(parsed)
    
#def md2dict(*pathelems):
#    class Section:
#        def __init__(self, depthstr, name, parent = None, content = '', children = None):
#            self.depthstr = depthstr
#            self.name = name
#            self.parent = parent
#            self.content = content
#            self.preamble = ''
#            self.children = children if children is not None else {}
#        def __iadd__(self, content):
#            if type(content) is str:
#                self.preamble += content
#            else:
#                if content.name is self.children:
#                    raise AssertionError('duplicate subsection name', content.name)
#                if content.parent is not None:
#                    raise AssertionError('duplicate supersection')
#                self.children[content.name] = content
#                content.parent = self
#            return self
#        def __str__(self):
#            return (
#                self.preamble +
#                '\n'.join([
#                    child.depthstr + ' ' + child.name + '\n' + str(child)
#                    for child in self.children.values()
#                ])
#            )
#        @property
#        def depth(self):
#            return len(self.depthstr)
#
#    path = os.path.join(*(
#        os.path.join(*elem.split('/'))
#        for elem in pathelems
#    ))
#    root = Section('', os.path.basename(path))
#    cur = root
#    for line in open(path):
#        if line[0] == '#' or line.strip()[:1] == '- ':
#            if line[0] == ' ':
#                for idx, char in enumerate(line):
#                    if char not in '- ':
#                        break
#                depthstr = line[:idx-1]
#
#            depthstr, name = line.split(' ', 1)  
#            section = Section(depthstr, name.strip())
#            while section.depth <= cur.depth:
#                cur = cur.parent
#            cur += section
#            cur = section
#        else:
#            cur += line
#    if len(root.children) == 1:
#        root = [*root.children.values()][0]
#    return root
#
#creation_functions = md2dict(spec_dir, 'creation_functions.md')
#for funcsec in creation_functions.children['Objects in API'].children.values():
#    name = funcsec.name
#    descr = funcsec.preamble
#    params = funcsec.children['Parameters']
#    rets = funcsec.children['Returns']
#    print('''{name}
#
#    {descr}
#
#    Parameters
#''')
#    print(params)
#    print('''
#    Returns
#''')
#    print(rets)
#    break
