import importlib
import pkgutil
import os

def list_all_user_defined_modules(base_directory):
    user_modules = []
    for root, dirs, files in os.walk(base_directory):
        # skip venv
        if any(venv_dir in root for venv_dir in ['.venv', 'venv', 'env', '.env']):
            continue
        if '__init__.py' in files:
            package_name = os.path.relpath(root, base_directory).replace(os.path.sep, '.')
            try:
                package = importlib.import_module(package_name)
                for _, modname, _ in pkgutil.iter_modules(package.__path__):
                    full_module_name = f"{package_name}.{modname}"
                    user_modules.append(full_module_name)
            except ImportError:
                pass
        else:
            for file in files:
                if file.endswith('.py') and file != '__init__.py':
                    module_path = os.path.relpath(os.path.join(root, file), base_directory)
                    module_name = module_path[:-3].replace(os.path.sep, '.')
                    user_modules.append(module_name)
    return user_modules

modules = list_all_user_defined_modules(os.getcwd())
print('user-defined modules:', modules)

