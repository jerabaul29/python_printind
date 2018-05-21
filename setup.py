from setuptools import setup, find_packages


setup(
    name='printind',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='4.0',

    description='Print function indented by the calling function stack depth using the traceback module',
    #long_description=long_description,

    # The project's main homepage.
    url='https://github.com/jerabaul29/python_printind',

    # Author details
    author='jerabaul29',
    author_email='jean.rblt@gmail.com',

    # Choose your license
    license='MIT',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(),
)
