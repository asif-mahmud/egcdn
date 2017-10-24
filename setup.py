import setuptools
import os

BASE_DIR = os.path.dirname(__file__)

REQ_FILE_PATH = os.path.join(BASE_DIR, 'requirements.txt')

# configure application specifics
APP_NAME = 'egcdn'
APP_VERSION = '0.0.1'
AUTHOR = 'Asif Mahmud Shimon'
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

with open(REQ_FILE_PATH, 'r') as f:
    REQUIREMENTS.extend(f.readlines())

REQUIREMENTS.extend(TESTS_REQUIREMENTS)

setuptools.setup(
    name=APP_NAME,
    version=APP_VERSION,
    author=AUTHOR,
    url=APP_URL,
    description=DESCRIPTION,
    license=APP_LICENSE,
    classifiers=CLASSIFIERS,
    packages=setuptools.find_packages(),
    keywords=KEY_WORDS,
    include_package_data=True,
    python_requires=PYTHON_VERSIONS,
    install_requires=REQUIREMENTS,
)
