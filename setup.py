import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='finna_client',
    version='0.1',
    url='https://github.com/NatLibFi/Finna-client',
    author='Osma Suominen',
    author_email='osma.suominen@helsinki.fi',
    description='Python client library for accessing Finna REST API',
    long_description=read('README.md'),
    py_modules=['finna_client'],
    install_requires=['requests'])
