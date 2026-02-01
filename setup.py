from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path:str) -> List[str]:
    '''
    Returns 'requirements.txt' file in List format
    '''

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

        if '-e .' in requirements:
            requirements.remove('-e .')

        return requirements
    
setup(
    name='TurboFan Engine RUL',
    description='Deep Learning Framework for Predictive Maintenance of Aircraft Turbofan Engines',
    version='0.0.1',
    author='Atharva',
    author_email='atharvakhandelwal19@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)

#CREATE PULL REQUEST FOR GITIGNORE
