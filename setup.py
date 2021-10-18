import setuptools

setuptools.setup(
    name='tensors',
    verison='0.0.1',
    license='GPLv3+',
    classifiers = [
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 or Later (GPLv3+)',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Software Development :: Libraries',
    ],
    install_requires = [],
    extras_require = {
        'all': [ 'torch', 'jax' ],
    },
    packages = ['tensors'],
)
