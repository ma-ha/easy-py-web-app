import os
from setuptools import setup

with open('README.rst') as reader:
    readme = reader.read()
    
setup(
    name='easy-web-app',
    version = "0.3.0",
    packages = ["easywebapp"],
    #scripts = ['webapp.py'],
    package_data = {
        'easywebapp': ['templates/*.html'],
    },
    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires = ['web.py','nose','WebTest'],

    #package_data = {
    #    # If any package contains *.txt or *.rst files, include them:
    #    '': ['*.txt', '*.rst'],
    #    # And include any *.msg files found in the 'hello' package, too:
    #    'hello': ['*.msg'],
    #},

    # metadata for upload to PyPI
    author = "ma-ha",
    author_email = "ma@mh-svr.de",
    description='Create web applications easily by defining them in JSON format.',
    keywords = "GUI web app browser AJAX easy portal REST RESTful web service form table I/O content serverless API centric",
    url = "https://github.com/ma-ha/easy-py-web-app",
    license='MIT',
    long_description=readme,
    test_suite = 'nose.collector',
         
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 2",
        "Topic :: Internet :: WWW/HTTP",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

)