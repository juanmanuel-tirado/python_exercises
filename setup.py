from setuptools import find_packages, setup

setup(
    name='exercises',
    install_requires=['regex'],
    packages=find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
)

