from setuptools import setup, find_packages

setup(
    name="employee_analysis",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "matplotlib",
        "scipy"
    ],
    entry_points={
        "console_scripts": [
            "employee_analysis=employee_analysis.facade:main",
        ],
    },
)
