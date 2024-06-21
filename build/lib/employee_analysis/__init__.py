from .facade import EmployeeAnalysisFacade

def main():
    csv_file = "Uncleaned_employees_final_dataset (1).csv"  # Update with the path to your real dataset
    facade = EmployeeAnalysisFacade(csv_file)
    facade.run()
