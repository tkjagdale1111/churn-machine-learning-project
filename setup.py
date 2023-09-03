from setuptools import setup, find_packages
from typing import List


PROJECT_NAME="MAchine Learning Project"
VERSION="0.0.1"
DESCRIPTION="This is our sunburn internship project"
AUTHOR_NAME="Tukaram Jagdale"
AUTHOR_EMAILID="tukaramjagdale1111@gmail.com"
REQUIRMENTS= "requirements.txt"
HYPEN_E_DOT="-e ."


def get_required_list()-> List[str]:
    with open(REQUIRMENTS) as requirment_file:
        requirment_list=requirment_file.readlines()
        requirment_list=[requirment_name.replace("\n","") for requirment_name in requirment_list]
        if HYPEN_E_DOT in requirment_list:
            requirment_list.remove(HYPEN_E_DOT)
        return requirment_list
        
           

setup(name=PROJECT_NAME,
      version=VERSION,
      description=DESCRIPTION,
      author=AUTHOR_NAME,
      author_email=AUTHOR_EMAILID,
      packages=find_packages(),
      install_requires =get_required_list()
      )