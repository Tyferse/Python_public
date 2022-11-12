import re
import sys
from importlib.abc import PathEntryFinder
from importlib.util import spec_from_loader
from urllib.request import urlopen


def url_hook(url):
    if not url.startswith(('http', 'https')):
        raise ImportError

    with urlopen(url) as page:
        data = page.read().decode('utf-8')
        
    filenames = re.findall('[a-zA-Z_][a-zA-Z0-9_]*.py', data)

    modnames = {name[:-3] for name in filenames}
    return URLFinder(url, modnames)


sys.path_hooks.append(url_hook)


class URLFinder(PathEntryFinder):
    def __init__(self, url, available):
        self.url = url
        self.available = available

    def find_spec(self, name, target=None):
        if name in self.available:
            origin = '{}/{}.py'.format(self.url, name)
            loader = URLLoader()
            return spec_from_loader(name, loader, origin=origin)


class URLLoader:
    def create_module(self, target):
        return None

    def exec_module(self, module):
        with urlopen(module.__spec__.origin) as page:
            source = page.read()

        code = compile(source, module.__spec__.origin, mode='exec')
        exec(code, module.__dict__)
