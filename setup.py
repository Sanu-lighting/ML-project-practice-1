from setuptools import find_packages,setup
from typing import List

H_E_dot='-e .'
def get_requieremnts(file_path:str)->List[str]:
    req=[]
    with open(file_path) as file_obj:
        req=file_obj.readlines()
        [reqi.replace("\n", "") for reqi in req]
        if H_E_dot in req:
            req.remove(H_E_dot)
        return req
    
setup(
    name='mlproject-0',
    version='0.0.1',
    author='The Sanu',
    author_email='sanuroy56apd@gmail.com',
    packages=find_packages(), #will search for __init__.py in folders.. those wich has that __init__.py, will be considered as the package since src folder has it here 
    # so it will build the src folder and can be imported
    install_requires=get_requieremnts('requirements.txt')
)