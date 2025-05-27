import os
from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(path: str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

# Get absolute path for requirements.txt relative to this file
here = os.path.abspath(os.path.dirname(__file__))
req_path = os.path.join(here, 'requirements.txt')

setup(
    name='MLproject',
    version='0.0.0.1',
    author='Hitesh Panghal',
    author_email='hiteshpanghal900@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements(req_path)
)
