from setuptools import setup
import re

VERSION = ''
with open("snipy/__init__.py") as f:
    VERSION = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not VERSION:
    raise RuntimeError('version is not set')

PACKAGES = [
    'snipy',
    'snipy.utils',
]

setup(
    name='snipy',
    author="PaulMarisOUMary",
    url="https://github.com/PaulMarisOUMary/Snipy",
    project_urls=
    {
        "Issue tracker": "https://github.com/PaulMarisOUMary/Snipy/issues"
    },
    version=VERSION,
    packages=PACKAGES,
    license="MIT",
    description="A sniffing tool."
)