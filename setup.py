from setuptools import setup, find_packages

setup(
    name='my_python_package',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['httpx==0.27.2'],
)
