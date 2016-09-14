"""
xPython
====================

**xPython** provides a python-like syntax and converters to any language.

In other words - you write code on xPython and then convert it to
Python, JavaScript, Java, Swift, PHP and other languages.


Quick start
-------------

Read `Quick Start <https://github.com/1st/xpython>`_ on GitHub.
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


version = '1.0.0a2'


setup(
    name='xpython',
    version=version,
    url='https://github.com/1st/xpython',
    license='MIT',
    author='Anton Danilchenko',
    author_email='anton@danilchenko.me',
    description='xPython provides a python-like syntax and converters '
                'to any language.',
    keywords='python, compiler, xpython',
    long_description=__doc__,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    packages=[
        # 'xpython',
        # in future:
        # 'xpython.blocks',
    ],
    install_requires=[],
    include_package_data=True,
    zip_safe=False,
    platforms='any'
)
