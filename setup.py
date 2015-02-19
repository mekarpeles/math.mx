"""
Mathd
-----

A comprehensive math graph
"""

import setuptools

setuptools.setup(
    name='mathd',
    version='0.0.01',
    url='',
    license='BSD',
    author='Mek Karpeles',
    author_email='michael.karpeles@gmail.com',
    description='Analysis of Numerical Topics',
    long_description=__doc__,
    packages=setuptools.find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'Flask-Routing'        
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ]
)
