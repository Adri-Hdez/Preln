from setuptools import find_packages, setup

setup(
    long_description_content_type='text/markdown',
    name='preln',
    packages=find_packages(include=['Preln', 'Preln.core']),
    version='0.3.5',
    description='A preprocessing libray for text in spanish',
    author='Adrián H.S & Raúl M.R',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
    include_package_data=True
)
