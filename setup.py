from setuptools import setup, find_packages

setup(
    name = 'minimalpackage',
    version = '0.0.1',
    url = 'https://github.com/monicast/minimal_package.git',
    author = 'Monica Stewart',
    author_email = 'mostew@microsoft.com',
    description = 'Description of my package',
    packages = find_packages(),
    package_data={'minimalpackage':['hellofile/names.txt']},
    install_requires = ['matplotlib >= 1.5.1'],
)