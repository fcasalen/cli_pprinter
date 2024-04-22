from setuptools import setup, find_packages

name = "cli_pprinter"
version = "0.1.1"

setup(
    name=name,
    version=version,
    license="GNU GENERAL PUBLIC LICENSE",
    author="fcasalen",
    author_email="fcasalen@gmail.com",
    description="print in cli with colors (wrapper of termcolor)",
    packages=find_packages(),
    include_package_data=True,
    install_requires=open('requirements.txt').readlines(),
    long_description=open("README.md").read(),
    classifiers=[
        "Development Status :: 5 - Prodution/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.11"
    ]
)
