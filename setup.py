from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='mimingequipment',
    version='1.0',
    description='A package for managing mining equipment data',
    author='Jilani',
    author_email='jilani_basha_s@deployoptiqiq.in',
    packages=find_packages(),
    install_requires=requirements
)
