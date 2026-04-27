from setuptools import find_packages, setup 

"""
Long description means the detailed meta data of the project. So most of the times, we just use Readme as long description
    """
    
# open readme file, and push the content to the variable.
with open("README.md",'r', encoding="utf-8") as file:
    long_readme = file.read()
    
    
# get the requirements.txt contents.
with open("requirements.txt") as f:
    required = f.read().splitlines() # converts to list


setup(
    name = "MLOPS_FULL_PIPELINE",
    version = "0.1.0",
    author= "Md Nazmun Hasan Nafees",
    email = "nafeeshasan365@gmail.com",
    description= "Full end to end MLOps project",
    long_description= long_readme,
    long_description_content_type = "text/markdown",
    url = "https://github.com/blue-jays/MLOps_full_pipeline",
    packages = find_packages(),
    classifiers=[
        "Developement Status :: 3 - Beta",
        "Intended Audience :: ML Engineers",
        "Programming Language :: Python >= 3.8",
        "Operating System :: OS Independent",
    ],
    
    python_requires = ">=3.8",
    install_requires = required,
    extras_require = {
        'dev':[
            "pytest>=7.1.1",
            "pytest-cov>=2.12.1",
            "flake8>=3.9.0",
            "black>=22.3.0",
            "isort >=5.10.1",
            "mypy >=0.942"
        ]
    }
    
)