import setuptools
import os

from egcdn import __version__

BASE_DIR = os.path.dirname(__file__)

REQ_FILE_PATH = os.path.join(BASE_DIR, 'requirements.txt')
README_FILE_PATH = os.path.join(BASE_DIR, 'README.md')

# configure application specifics
APP_NAME = 'egcdn'
APP_VERSION = __version__
AUTHOR = 'Asif Mahmud Shimon'
AUTHOR_EMAIL = 'shimon@embeddedgamers.com'
APP_URL = 'https://www.embeddedgamers.com'
APP_LICENSE = 'GPLv2'
DESCRIPTION = 'A Glue application between CDN servers and Web Applications'
REQUIREMENTS = []
TESTS_REQUIREMENTS = [
    'pytest',
]
CLASSIFIERS = [
    'Development Status :: 1-Alpha',
    'Intended Audience :: Developers',
    'Topic :: CDN',
    'License :: GPL version 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.4',
]
KEY_WORDS = 'CDN'
PYTHON_VERSIONS = '>=2.7, >=3.4'
LONG_DESCRIPTION = ''

with open(REQ_FILE_PATH, 'r') as f:
    REQUIREMENTS.extend(f.readlines())

with open(README_FILE_PATH, 'r') as f:
    LONG_DESCRIPTION = f.read()

setuptools.setup(
    name=APP_NAME,
    version=APP_VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=APP_URL,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    license=APP_LICENSE,
    classifiers=CLASSIFIERS,
    packages=setuptools.find_packages(),
    keywords=KEY_WORDS,
    include_package_data=True,
    python_requires=PYTHON_VERSIONS,
    install_requires=REQUIREMENTS,
    tests_require=TESTS_REQUIREMENTS,
)
