from setuptools import setup, find_packages


setup(
    name='netbox-aws',
    version='1.0.0',
    description='NetBox plugin for tracking AWS resources',
    url='https://github.com/lampwins/netbox-aws',
    author='John Anderson',
    license='Apache 2.0',
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
)
