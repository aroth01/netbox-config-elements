from setuptools import setup, find_packages

setup(
    name='netbox_config_elements',
    version='0.1',
    description='A plugin for NetBox that adds in additional router/switch config elements',
    url='https://github.com/aroth01/netbox-config-elements',
    author='Aaron Roth',
    author_email='aroth01@gmail.com',
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
)