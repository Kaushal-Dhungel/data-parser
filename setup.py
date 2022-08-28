from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

NAME = "data_parser"
DESCRIPTION = "A data parser and ngram creator"
URL = "https://github.com/Kaushal-Dhungel/data-parser"
EMAIL = "abc@gmail.com"
AUTHOR = "Kaushal Dhungel"
REQUIRES_PYTHON = ">=3.6.0"
VERSION = "0.0.1"

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=['data_parser'],
    license="MIT",
    keywords=['data parser','ngrams creator'],
    package_data={'data_parser': ['data/data.txt']}
)