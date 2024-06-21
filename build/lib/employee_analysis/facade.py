import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, shapiro
import csv
from .transformations import TransformationFactory

class EmployeeAnalysisFacade:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.df = self.load_data()
        self.required_fields = ['employee_id', 'no_of_trainings', 'previous_year_rating', 'KPIs_met_more_than_80', 'awards_won', 'avg_training_score']

    def load_data(self):
        try:
            df = pd.read_csv(self.csv_file)
        except FileNotFoundError:
            print(f"Error: The file {self.csv_file} was not found.")
            exit()
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
            exit()
        except pd.errors.ParserError:
            print("Error: Error parsing the file.")
            exit()
        return df

    def clean_data(self):
        df = self.df
        try:
            # Handle missing values
            df = df.dropna(subset=self.required_fields)  # Remove rows with missing values in required fields
            df = df.fillna(0)  # Fill other NaNs with 0

            # Convert data types
            for field in self.required_fields:
                if field != 'employee_id':
                    df[field] = pd.to_numeric(df[field], errors='coerce')

            # Handle outliers (example: capping at 99th percentile)
            for field in self.required_fields[1:]:
                upper_limit = df[field].quantile(0.99)
                df[field] = np.where(df[field] > upper_limit, upper_limit, df[field])
        except Exception as e:
            print(f"Error in data cleaning: {e}")
            exit()

        self.df = df

    def calculate_ratings(self):
        try:
            ratings = []
            for _, row in self.df.iterrows():
                rating = sum([row[field] for field in self.required_fields[1:]])
                ratings.append((row['employee_id'], rating))
        except Exception as e:
            print(f"Error in calculating ratings: {e}")
            exit()
        return ratings

    def apply_transformations(self, ratings):
        ratings_values = np.array([rating for _, rating in ratings])
        transformations = TransformationFactory.get_transformations()

        shapiro_results = {}
        for transformation in transformations:
            transformed_data = transformation.apply(ratings_values)
            stat, p_value = transformation.test_normality(transformed_data)
            shapiro_results[transformation.name()] = (stat, p_value)

        best_method = max(shapiro_results, key=lambda x: shapiro_results[x][1])
        best_transformation = next(filter(lambda t: t.name() == best_method, transformations))

        print("Shapiro-Wilk Test Results:")
        for method, result in shapiro_results.items():
            print(f"{method} Data: Statistic={result[0]:.4f}, p-value={result[1]:.4f}")

        print(f"\nBest Transformation Method: {best_method}")

        plt.figure(figsize=(15, 10))
        for i, transformation in enumerate(transformations, 1):
            plt.subplot(2, 3, i)
            data = transformation.apply(ratings_values)
            plt.hist(data, bins=20, density=True, alpha=0.6)
            plt.title(f'{transformation.name()} Data')
            plt.xlabel('Performance Rating')
            plt.ylabel('Density')

        plt.tight_layout()
        plt.savefig("transformation_histograms.png")  # Save the histogram plot as PNG
        plt.show()

        return best_transformation.apply(ratings_values)

    def find_best_p_value(self, transformations):
        try:
            p_values = np.linspace(0.01, 0.1, 100)  # Test p-values from 0.01 to 0.1
            best_p = 0.05
            best_stat = 0

            for p in p_values:
                for transformation in transformations:
                    data = transformation.apply(self.ratings_values)
                    stat, current_p = shapiro(data)
                    if current_p > p and stat > best_stat:
                        best_stat = stat
                        best_p = p

            print(f"Optimal p-value: {best_p}")
        except Exception as e:
            print(f"Error in finding best p-value: {e}")
            exit()

        return best_p

    def categorize_employees(self, ratings):
        try:
            ratings_values = np.array([rating for _, rating in ratings])
            thresholds = {
                'Poor': np.percentile(ratings_values, 30),
                'Average': np.percentile(ratings_values, 60),
                'Good': np.percentile(ratings_values, 80),
                'Best': np.percentile(ratings_values, 90)
            }

            categories = []
            for emp_id, rating in ratings:
                if rating >= thresholds['Best']:
                    category = 'Best'
                elif thresholds['Good'] <= rating < thresholds['Best']:
                    category = 'Good'
                elif thresholds['Average'] <= rating < thresholds['Good']:
                    category = 'Average'
                else:
                    category = 'Poor'
                categories.append((emp_id, category, rating))
        except Exception as e:
            print(f"Error in categorizing employees: {e}")
            exit()

        return categories, thresholds

    def plot_normal_distribution(self, mean, std, thresholds):
        try:
            x = np.linspace(mean - 2.5 * std, mean + 2.5 * std, 100)
            bell_curve = norm.pdf(x, mean, std)

            plt.plot(x, bell_curve, color='blue', label='Whole Dataset')
            colors = {'Poor': 'red', 'Average': 'orange', 'Good': 'yellow', 'Best': 'green'}
            for category, threshold in thresholds.items():
                plt.axvline(x=threshold, color=colors[category], linestyle='--', label=f'{category}: {threshold:.2f}')

            plt.legend()
            plt.xlabel('Performance Rating')
            plt.ylabel('Probability Density')
            plt.title('Normal Distribution of Employee Performance for Whole Dataset')
            plt.savefig("normal_distribution.png")  # Save the normal distribution plot as PNG
            plt.show()
        except Exception as e:
            print(f"Error in plotting normal distribution: {e}")
            exit()

    def save_categorized_employees(self, categories):
        try:
            # Sort the categories by 'Category' and then by 'Total Rating' within each category
            categories.sort(key=lambda x: (x[1], -x[2]))  # Sorting primarily by category and then by rating descending

            output_file = "categorized_employees.csv"
            with open(output_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['employee_id', 'Category', 'Total Rating'])
                for emp_id, category, rating in categories:
                    writer.writerow([emp_id, category, rating])
        except Exception as e:
            print(f"Error in saving categorized employees: {e}")
            exit()

    def run(self):
        self.clean_data()
        ratings = self.calculate_ratings()

        plt.hist([rating for _, rating in ratings], bins=20, density=True, alpha=0.6, color='g')
        plt.xlabel('Performance Rating')
        plt.ylabel('Frequency')
        plt.title('Histogram of Performance Ratings')
        plt.grid(True)
        plt.savefig("performance_histogram.png")  # Save the histogram plot as PNG
        plt.show()

        ratings_values = np.array([rating for _, rating in ratings])
        ratings_values = ratings_values[~np.isnan(ratings_values) & ~np.isinf(ratings_values)]  # Remove NaN and Inf
        statistic, p_value = shapiro(ratings_values)
        print(f'Shapiro-Wilk Test:\nStatistic: {statistic}, p-value: {p_value}')

        if p_value > 0.05:
            print("Data follows a normal distribution. Proceeding with categorization.")
        else:
            print("Data does not follow a normal distribution. Applying transformations.")

        # Apply transformations regardless of initial normality test result
        transformed_ratings = self.apply_transformations(ratings)

        # Find the best p-value for Shapiro-Wilk test
        best_p = self.find_best_p_value(TransformationFactory.get_transformations())

        statistic, p_value = shapiro(transformed_ratings)
        print(f'Post-Transformation Shapiro-Wilk Test with best p={best_p}:\nStatistic: {statistic}, p-value: {p_value}')

        categories, thresholds = self.categorize_employees(ratings)
        self.save_categorized_employees(categories)

        mean, std = np.mean(ratings_values), np.std(ratings_values)
        self.plot_normal_distribution(mean, std, thresholds)
