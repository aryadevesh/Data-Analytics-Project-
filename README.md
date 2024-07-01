# Employee Analysis Package Documentation

## Table of Contents

1. [Introduction]
2. [Installation]
3. [Project Structure]
4. [Usage]
5. [Modules]
    - [Employee Analysis Facade]
    - [Transformations]
    - [Utilities]
6. [Testing]
7. [Examples]
8. [License]

## Introduction

The Employee Analysis package analyzes employee performance data, applies various transformations, and categorizes employees based on their performance ratings. This package uses design patterns like Strategy, Factory, and Facade to ensure modularity and maintainability.

## Installation

To install the package, navigate to the root directory (where setup.py is located) and run:
pip install .

## Usage
To use the Employee Analysis package in your project, you can use the EmployeeAnalysisFacade class to run the complete workflow:

### python
from employee_analysis import EmployeeAnalysisFacade

csv_file = "path/to/your/dataset.csv"
facade = EmployeeAnalysisFacade(csv_file)
facade.run()

## Modules
Employee Analysis Facade
The EmployeeAnalysisFacade class provides a simplified interface to run the entire employee analysis process.

## Methods
1. __init__(self, csv_file): Initializes the facade with the specified CSV file.
2. load_data(self): Loads the data from the CSV file.
3. clean_data(self): Cleans the data by handling missing values and outliers.
4. calculate_ratings(self): Calculates performance ratings for employees.
5. apply_transformations(self, ratings): Applies various transformations to the ratings.
6. find_best_p_value(self, transformations): Finds the best p-value for the Shapiro-Wilk test.
7. categorize_employees(self, ratings): Categorizes employees based on their ratings.
8. plot_normal_distribution(self, mean, std, thresholds): Plots the normal distribution of employee performance.
9. save_categorized_employees(self, categories): Saves the categorized employees to a CSV file.
10. run(self): Executes the complete workflow.

## Transformations
The transformations module contains classes implementing different transformation strategies using the Strategy design pattern.

## Base Class
- TransformationStrategy: Abstract base class for transformations.
- apply(self, data): Abstract method to apply the transformation.
- name(self): Abstract method to return the name of the transformation.
- test_normality(self, data): Tests the normality of the data using the Shapiro-Wilk test.
### Concrete Classes
- OriginalTransformation: Applies no transformation.
- LogTransformation: Applies a logarithmic transformation.
- SqrtTransformation: Applies a square root transformation.
- BoxCoxTransformation: Applies a Box-Cox transformation.
- InverseTransformation: Applies an inverse transformation.
### Factory Class
- TransformationFactory: Provides a method to get all transformation strategies.
- get_transformations(): Returns a list of all available transformation strategies.
### Utilities
The utils module contains utility functions used by the package.

## Functions
- load_data(csv_file): Loads data from the specified CSV file.
## Testing
- Unit tests are provided in the tests module. To run the tests, use a test runner like unittest:

python -m unittest discover tests

