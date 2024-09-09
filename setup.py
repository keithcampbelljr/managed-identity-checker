from setuptools import setup, find_packages

setup(
    name='mi-inspect',
    version='0.1',
    packages=find_packages(include=['app', 'app.*']),
    install_requires=[
        'azure-mgmt-authorization',
        'azure-mgmt-msi',
        'azure-identity',
        'azure-core',
        'click',
        'typing-extensions'
    ],
    entry_points={
        'console_scripts': [
            'mi-inspect=app.cli:main',
        ],
    },
    description='A tool for checking azure roles associated with a managed identity',
    author='Keith Campbell',
    author_email='keithcampbelljr@icloud.com',
)
