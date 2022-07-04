from distutils.command.sdist import sdist as sdist_orig
from setuptools import find_packages, setup
import pathlib
import pkg_resources

with pathlib.Path('requirements.txt').open() as txt:
    install_requires = [
        str(requirement)
        for requirement in pkg_resources.parse_requirements(txt)
    ]
    
class SDistCommand(sdist_orig):
    def run(self):
        try:
            self.spawn(['python', '-m', 'nltk.download', 'punkt'])
        except:
            self.spawn(['python3', '-m', 'nltk.download', 'punkt'])
        super().run()


with open("README.md", "r") as fh:
    LONG_DESC = fh.read()

    setup(
        long_description=LONG_DESC,
        long_description_content_type='text/markdown',
        name='preln',
        packages=find_packages(include=['Preln', 'Preln.core']),
        version='0.3.6',
        description='A preprocessing libray for text in spanish',
        author='Adrián H.S & Raúl M.R',
        author_email='adrihs.dev@gmail.com',
        license='MIT',
        install_requires=install_requires,
        setup_requires=['pytest-runner'],
        url='https://github.com/Adri-Hdez/Preln',
        tests_require=['pytest'],
        test_suite='tests',
        include_package_data=True,
        cmdclass={
            'sdist': SDistCommand
        }
)
