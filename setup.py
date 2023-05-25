from setuptools import setup, find_packages

setup(
        # the name must match the folder name 'verysimplemodule'
        name="Quran_sbu", 
        version='1',
        author="Masoud_shafiei",
        author_email="masoudshafiei625@gmail.com",
        description='Quran_simple',
        long_description='My first Python package with a slightly longer description',
        packages=find_packages(),
        
        # add any additional packages that 
        # needs to be installed along with your package.
        install_requires=[], 
        
        keywords=['quran', 'sbu'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: all of student",
            "Programming Language :: Python :: 3",
            
        ]
)
