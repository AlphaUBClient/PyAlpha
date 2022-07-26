from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.2'
DESCRIPTION = 'PyAlpha UserBot Modules'
LONG_DESCRIPTION = 'A package that allows to build simple userbot.'

# Setting up
setup(
    name="PyTgAlpha",
    version=VERSION,
    author="Team Alpha",
    author_email="<vgishan2006@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['pyautogui', 'pyrogram', 'telethon'],
    keywords=['python', 'ub', 'userbot', 'UB', 'PyAlpha', 'Alpha'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
