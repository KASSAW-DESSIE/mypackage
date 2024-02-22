from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests']),
    license='MIt',
    description='EDSA python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/<KASSAW-DESSIE>/<package-name>',
    author='<KASSAW-DESSIE>',
    author_email='<dkas6610@gmail.com>'

)