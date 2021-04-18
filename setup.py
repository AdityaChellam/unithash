from setuptools import find_packages, setup

setup(
    name='unithash',
    packages=find_packages(include=['unithash']),
    version='0.1.1',
    description='Find the unit digit hash of a number by recursively calling the sum of all digits in a number till reaching units place',
    long_description='This is the long description',
    long_description_content_type="text/markdown",
    author='Aditya Chellam',
    license='MIT',
    url = 'https://github.com/AdityaChellam/unithash',
    download_url = 'https://github.com/AdityaChellam/unithash/archive/refs/tags/v_011.tar.gz',
    keywords = ['HASHING','UNITSUM'],
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
