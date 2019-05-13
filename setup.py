from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='Startup',
    version='0.1.0',
    description='A python library to allow scripts to be added to startup easily',
    long_description=readme,
    author='Sam Redmond',
    author_email='sam@virtualstack.co.nz',
    url='https://github.com/SillySam/startup',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)