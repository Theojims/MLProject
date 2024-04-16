from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT ="-e ."
def get_requirements(file_path:str)->list[str]
    '''
    This function will return the list of requirements
    
    '''
    requirements = []
    with open(file_path) as file_object:
        requirements = file_object.readLines()
        requirements = [reg.strip() for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
name = 'MLProject',
version = "0.0.1",
author ='Theojims',
author_email = 'theophilus.nwuchiola@eng.uniben.edu',
packages = find_packages(),
install_requires = get_requirements(requirement.txt)


)