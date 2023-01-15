from setuptools import setup , find_packages
from typing import List

NAME="Concrete Strength Prediction"
AUTHOR="Suhasini Gupta"
VERSION="0.0.3"
DESCRIPTION="ML project to predict concrete compressive strength"
HYPHEN_E_DOT ="-e ."

def get_requirements_list()->List[str]:

    """This function returns list of requirements.txt file"""

    with open("requirements.txt") as req_file:
        requirement_list = req_file.readlines()
        
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list

setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=get_requirements_list()
)
    
