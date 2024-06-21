import unittest
from employee_analysis.facade import EmployeeAnalysisFacade

class TestEmployeeAnalysis(unittest.TestCase):
    def test_clean_data(self):
        facade = EmployeeAnalysisFacade("sample_dataset.csv")
        facade.clean_data()
        self.assertIsNotNone(facade.df)

    # Add more tests for other methods

if __name__ == "__main__":
    unittest.main()
