from setuptools import find_packages, setup

setup(
    name='unithash',
    packages=find_packages(include=['unithash']),
    version='1.2.5',
    description='Hashing Algorithm | Python',
    long_description='Compute the unit hash digest of a string by segmenting the string into blocks of a specified size and recursively computing the sum of all digits in each block.\nIn order to use this hashing algorithm in your code, do a pip install for the library.\n\n\tpip install unithash\n\n',
    long_description_content_type="text/markdown",
    author='Aditya Chellam',
    license='MIT',
    url = 'https://github.com/AdityaChellam/unithash',
    project_urls={
        "Documentation": "https://www.codeofcoffee.com/2021/04/creating-my-own-python-library-and.html",
    },
    download_url = 'https://github.com/AdityaChellam/unithash/archive/refs/tags/v_125.tar.gz',
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
