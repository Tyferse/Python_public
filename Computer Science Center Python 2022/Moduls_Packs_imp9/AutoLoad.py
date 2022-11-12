import subprocess
import sys
from importlib.util import find_spec
from importlib.abc import MetaPathFinder


class AutoInstall(MetaPathFinder):
    _loader = set()

    @classmethod
    def find_spec(cls, name, path=None, target=None):
        if path is None and name not in cls._loader:
            print('Installing', name)
            cls._loader.add(name)
            try:
                subprocess.check_output([
                    sys.executable, '-m', 'pip', 'install', name])
                return find_spec(name)
            except Exception:
                print('Failed')

