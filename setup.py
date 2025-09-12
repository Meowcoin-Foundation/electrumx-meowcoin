import setuptools

import electrumx

version = electrumx.version.rsplit(' ', maxsplit=1)[-1]

with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name='electrumX-meowcoin',
    version=version,
    scripts=['electrumx_server', 'electrumx_rpc', 'electrumx_compact_history'],
    python_requires='>=3.8',
    install_requires=requirements,
    extras_require={
        'rocksdb': ['python-rocksdb>=0.6.9'],
        'uvloop': ['uvloop>=0.17'],
    },
    packages=setuptools.find_packages(include=('electrumx*',)),
    description='ElectrumX Meowcoin Server',
    author='Topper',
    author_email='topper@topper.site',
    license='MIT Licence',
    url='https://github.com/Meowcoin-Foundation/electrumx-meowcoin',
    long_description='Meowcoin server implementation for the Electrum protocol',
    download_url=('https://github.com/Meowcoin-Foundation/electrumx-meowcoin/archive/'
                  f'{version}.tar.gz'),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: AsyncIO',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        "Programming Language :: Python :: 3.8",
        "Topic :: Database",
        'Topic :: Internet',
    ],
)
