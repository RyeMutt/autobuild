from pathlib import Path

import setuptools

setuptools.setup(
    name='autobuild',
    url='http://wiki.secondlife.com/wiki/Autobuild',
    description='Linden Lab Automated Package Management and Build System',
    long_description=(Path(__file__).parent / "README.md").read_text(),
    long_description_content_type="text/markdown",
    platforms=['any'],
    packages=setuptools.find_packages(exclude=['tests']),
    use_scm_version={
        'write_to': 'autobuild/version.py',
        'write_to_template': 'AUTOBUILD_VERSION_STRING = \'{version}\'',
        'local_scheme': 'no-local-version', # disable local-version to allow uploads to test.pypi.org
    },
    setup_requires=['setuptools_scm'],
    entry_points={
        'console_scripts': ['autobuild=autobuild.autobuild_main:main']
    },
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Unix',
    ],
    install_requires=['llbase', 'pydot'],
    extras_require={
        'dev': ['pytest'],
        'build': ['build', 'setuptools_scm'],
    },
    python_requires='>=3.7',
)
