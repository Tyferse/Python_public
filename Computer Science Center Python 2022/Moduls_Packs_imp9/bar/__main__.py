print('What are we doing here?')
print(__import__)


def import_wrapper(name, *args, imp=__import__):
    print('Importing ', name)
    return imp(name, *args)

