from setuptools import find_packages,setup
from typing import List

Hypen_e_dot='-e .'
def get_requirements(filepath:str)->List[str]:
    """
    this function will return the list of requirements
    """
    requirements=[]
    with open(filepath) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("/n","") for req in requirements]
    if Hypen_e_dot in requirements:
        requirements.remove(Hypen_e_dot)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Bhanu',
    author_email='bhagbe025@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)