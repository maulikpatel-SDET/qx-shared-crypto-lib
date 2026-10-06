from setuptools import setup, find_packages

setup(
    name="qx-shared-crypto-lib",
    version="1.2.0",
    packages=find_packages(),
    install_requires=["cryptography>=42"],
)
