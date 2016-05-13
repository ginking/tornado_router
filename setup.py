import re
import os
import sys
from setuptools import setup, find_packages

install_requires = ['tornado']

def read_version():
    regexp = re.compile(r"^__version__\W*=\W*'([\d.abrc]+)'")
    init_py = os.path.join(os.path.dirname(__file__),
                           'tornado_router', '__init__.py')
    with open(init_py) as f:
        for line in f:
            match = regexp.match(line)
            if match is not None:
                return match.group(1)
        raise RuntimeError('Cannot find version in aio_periodic_task/__init__.py')

classifiers = [
    'License :: OSI Approved :: MIT License',
    'Development Status :: 3 - Alpha',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Operating System :: POSIX',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries',
]

setup(name='tornado_router',
    version=read_version(),
    description='function-based router for Tornado Web Framework that supports asynchronous authentication, json request and more',
    classifiers=classifiers,
    platforms=["POSIX"],
    author="Sick Yoon",
    author_email="shicky@gmail.com",
    url="https://github.com/shicky/tornado_router",
    keywords=['tornado', 'router', 'asynchronous', 'authentication', 'decorator'],
    license="MIT",
    packages=find_packages(exclude=["tests"]),
    install_requires=install_requires,
    include_package_data=True)

