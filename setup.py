from setuptools import setup, find_packages

setup(
    name='managed-identity-checker',
    version='0.1',
    packages=find_packages(include=['app', 'app.*']),
    install_requires=[
        'azure-identity',
        'azure-mgmt-authorization',
        'click',
    ],
    entry_points={
        'console_scripts': [
            'managed-identity-checker=app.cli:main',
        ],
    },
)
