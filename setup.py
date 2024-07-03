import os
from setuptools import find_packages, setup


def read(fname):
    """
    Utility function to read the README file.
    Used for the long_description.  It's nice, because now 1) we have a top
    level README file and 2) it's easier to type in the README file than to
    put a raw string in below.
    """
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="mesh_evaluator",
    packages=find_packages(include=["mesh_evaluator"]),
    version="0.1.0",
    description="Evaluates meshes using the F-score.",
    long_description=read("readme.md"),
    author="Yuhao Cao",
    install_requires=["numpy"],
)