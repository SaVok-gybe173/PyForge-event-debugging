from pythonforandroid.recipe import CythonRecipe
from pythonforandroid.logger import shprint
import sh
from os import environ

class PyForgeRecipe(CythonRecipe):
    version = 'master'
    url = 'https://github.com/SaVok-gybe173/PyForge/archive/refs/heads/master.tar.gz'
    name = 'pyforge'  
    depends = ['setuptools', 'cython', 'sdl2', 'pysdl2', 'numpy']
    
    call_hostpython_via_targetpython = False
    install_in_hostpython = True

    hostpython_prerequisites = ['cython==3.1.8', 'numpy>=2.0', "pysdl2==0.9.17"]

    def build_arch(self, arch):
        # Дублируем установку на случай, если prerequisites не сработали
        hostpython = sh.Command(self.ctx.hostpython)
        shprint(hostpython, '-m', 'pip', 'install', 'cython==3.1.8', "pysdl2==0.9.17", 'numpy', _env=environ)
        super().build_arch(arch)



recipe = PyForgeRecipe()