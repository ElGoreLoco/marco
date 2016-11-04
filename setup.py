import sys

try:
    from setuptools import setup

    try:
        from PIL import Image
    except ImportError:
        print("You need to have Pillow installed. Try running \"sudo pip3 install pillow\".")
        sys.exit(1)

except ImportError:
    from distutils.core import setup

if sys.version < "3":
    print("You need to have python 3 installed. Try installing and running python3.")
    sys.exit(1)


config = {
    "description": "Pone un marco de un color y grosor espec\xc3fico a fotos.",
    "author": "ElGoreLoco",
    "version": "0.1",
    "packages": ["marco"],
    "scripts": ["marco/marco"],
#   "entry_points": {
#       "console_scripts": ["marco=marco:main"]
#   },
    "name": "marco",
    "install_requires": ["pillow"]
}

setup(**config)
