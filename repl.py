import pkgutil

def list_user_defined_modules(package_name):
    user_modules = []
    package = __import__(package_name)
    for importer, modname, ispkg in pkgutil.iter_modules(package.__path__):
        user_modules.append(modname)
    return user_modules

modules = list_user_defined_modules('src')
print("src modules:", modules)
