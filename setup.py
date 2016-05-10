import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-token',
    version='0.1.2',
    packages=find_packages(),
    include_package_data=True,
    description='Simple token based authentication for Django',
    long_description=README,
    author='Jason Beverage',
    url="https://github.com/jasonbeverage/django-token",
    install_requires=["Django>=1.9"]
)
