from pythonforandroid.recipe import CompiledComponentsPythonRecipe

class CythonRecipe(CompiledComponentsPythonRecipe):
    version = '3.1.8'
    url = 'https://github.com/cython/cython/archive/refs/tags/{version}.tar.gz'
    name = 'cython'
    depends = ['setuptools']
    call_hostpython_via_targetpython = False
    install_in_hostpython = True

recipe = CythonRecipe()