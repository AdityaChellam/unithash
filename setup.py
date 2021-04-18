from setuptools import find_packages, setup

setup(
    name='unithash',
    packages=find_packages(include=['unithash']),
    version='0.1.0',
    description='Find the unit digit hash of a number by recursively calling the sum of all digits in a number till reaching units place',
    author='Aditya Chellam',
    license='MIT',
    install_requires=['regex',],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)