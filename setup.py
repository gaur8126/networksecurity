"""
The Setup file is an essential part of packing and distributing Python projects. 
It is used by setuptools (or distributed in older Python versions)
to define the configuration of your project, such as its metadata , dependencies, and
more ...
"""


from setuptools import setup, find_packages
from typing import List

def get_requirements()->List[str]:
    """
    This function return the list of requirements 
    """
    requirement_lst:List[str] = []
    try: 
        with open("requirements.txt",'r') as file :
            # read the lines from the file 
            lines = file.readlines()
            # process each line 
            for line in lines:
                requirement = line.strip()
                ## ignore empty line and -e .
                if requirement and requirement != "-e .":
                    requirement_lst.append(requirement)
    except FileNotFoundError :
        print("requirements.txt file not found")

    return requirement_lst



setup(
    name="NetworkSecurity",
    version="0.0.1",
    author='lokesh',
    author_email='gaurlokesh1211@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements()
)