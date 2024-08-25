from setuptools import setup, find_packages

setup(
    name='mi-inspect',
    version='0.1',
    packages=find_packages(include=['app', 'app.*']),
    install_requires=[
        'azure-identity',
        'azure-mgmt-authorization',
        'click',
    ],
    entry_points={
        'console_scripts': [
            'mi-inspect=app.cli:main',
        ],
    },
)
