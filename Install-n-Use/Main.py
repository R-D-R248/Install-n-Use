import os

def install(package):
    try:
        __import__(package)
    except ImportError:
        try:
            os.system(f"pip install {package}")
            __import__(package)
        except ImportError:
            raise Exception("PyPIError : Package not Found on PyPI")
    globals()[package] = __import__(package)


def install_specific(package, version, name):
    try:
        __import__(package)
    except ImportError:
        try:
            os.system(f"pip install {package}=={version}")
            __import__(package)
        except ImportError:
            raise Exception("PyPIError : Package not Found on PyPI")
    globals()[name] = __import__(package)


def upgrade(package):
    try:
        __import__(package)
    except ImportError:
        try:
            os.system(f"pip install {package}")
            __import__(package)
        except ImportError:
            raise Exception("PyPIError : Package not Found on PyPI")
    os.system(f"pip install --upgrade {package}")
    globals()[package] = __import__(package)


def upgrade_specific(package, version, name):
    try:
        __import__(package)
    except ImportError:
        try:
            os.system(f"pip install {package}=={version}")
            __import__(package)
        except ImportError:
            raise Exception("PyPIError : Package not Found on PyPI")
    os.system(f"pip install --upgrade {package}")
    globals()[name] = __import__(package)
