from setuptools import setup, find_packages

setup(
    name="ml-preprocessor-cli",
    version="0.1.0",
    author="Suraj Nahak",
    author_email="surajnahak2016@gmail.com",
    description="A CLI-based Machine Learning Data Preprocessor",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Surajnahak48/ml-preprocessor-cli",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pandas",
        "scikit-learn"
    ],
    entry_points={
        "console_scripts": [
            "ml-preprocessor=main:main",
            "ml-preprocessor-gui=gui.gui_main:main",  
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
