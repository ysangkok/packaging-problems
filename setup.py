from setuptools import setup
setup(name='Packaging Problems',
    version='1.0',
    description='Python Packaging Issue',
    author='Janus Troelsen (Electrum Technologies GmbH)',
    author_email='ysangkok@gmail.com',
    url='http://github.com/ysangkok/packaging-problems',
    packages=['problems'],
    package_data={
        'problems': [
            'problems/sometimes_included/file.txt'
        ],
    },
)
