from setuptools import setup, find_packages

setup(
    name='vaultpy',  # Name of your package
    version='0.1',  # Version number
    packages=find_packages(),  # Automatically find packages in the current directory
    install_requires=['requests'],  # List any dependencies your package needs
    description='Python package for working with vault',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Ben Gonzalez',
    author_email='gonzalezben393@gmail.com',
    url='https://github.com/gonzalezben81/vaultpy.git',  # URL to your package repository
)
