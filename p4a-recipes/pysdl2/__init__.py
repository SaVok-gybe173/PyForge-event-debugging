from pythonforandroid.recipe import PythonRecipe


class PySDL2Recipe(PythonRecipe):
    version = '0.9.17'
    url = 'https://files.pythonhosted.org/packages/d7/ff/8704d84ad4d25f0a7bf7912504f64575e432e8d57dfba2fe35f5b2db7e04/pysdl2-0.9.17.tar.gz'
    site_packages_name = 'sdl2'
    depends = ['setuptools']
    call_hostpython_via_targetpython = False


recipe = PySDL2Recipe()