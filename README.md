<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            background-color: #f4f4f4;
            color: #333;
        }
        h1, h2, h3 {
            color: #0056b3;
        }
        code {
            background-color: #eaeaea;
            padding: 2px 4px;
            border-radius: 3px;
        }
        pre {
            background-color: #eaeaea;
            padding: 10px;
            border-radius: 3px;
            overflow-x: auto;
        }
        .container {
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        .highlight {
            background-color: #ffeeba;
            padding: 2px 4px;
            border-radius: 3px;
        }
    </style>
    <title>Employee Performance Categorization Project</title>
</head>
<body>
    <div class="container">
        <h1>Employee Performance Categorization Project</h1>
        <h2>Overview</h2>
        <p>This project aims to categorize employee performance ratings based on various metrics. It involves data cleaning, performance rating calculation, transformation to achieve normality, categorization, and visualization. The results are saved to a new CSV file with sorted categories.</p>
        
        <h2>Project Structure</h2>
        <ul>
            <li><code>Uncleaned_employees_final_dataset (1).csv</code>: The input CSV file containing raw employee data.</li>
            <li><code>categorized_employees.csv</code>: The output CSV file containing categorized employee data.</li>
            <li><code>transformation_histograms.png</code>: A histogram plot of various transformations applied to the performance ratings.</li>
            <li><code>performance_histogram.png</code>: A histogram plot of the original performance ratings.</li>
            <li><code>normal_distribution.png</code>: A normal distribution plot with categorized thresholds.</li>
        </ul>

        <h2>Requirements</h2>
        <p>Python 3.x</p>
        <p>Libraries: <code>numpy</code>, <code>pandas</code>, <code>matplotlib</code>, <code>scipy</code>, <code>csv</code></p>
        <pre><code>pip install numpy pandas matplotlib scipy</code></pre>

        <h2>Usage</h2>
        <ol>
            <li><strong>Data Preparation</strong>: Place the input CSV file (<code>Uncleaned_employees_final_dataset (1).csv</code>) in the project directory.</li>
            <li><strong>Run the Script</strong>: Execute the Python script to process the data and generate the output files.
                <pre><code>python employee_performance_categorization.py</code></pre>
            </li>
            <li><strong>Outputs</strong>: The script will generate:
                <ul>
                    <li><code>categorized_employees.csv</code>: Sorted categorized employee data.</li>
                    <li><code>transformation_histograms.png</code>: Histogram plots of various transformations.</li>
                    <li><code>performance_histogram.png</code>: Histogram plot of original performance ratings.</li>
                    <li><code>normal_distribution.png</code>: Normal distribution plot with categorized thresholds.</li>
                </ul>
            </li>
        </ol>

        <h2>Script Details</h2>
        <h3>Data Cleaning</h3>
        <ul>
            <li><span class="highlight">Missing Values</span>: Rows with missing values in required fields are dropped, and other NaNs are filled with 0.</li>
            <li><span class="highlight">Data Type Conversion</span>: Non-<code>employee_id</code> fields are converted to numeric types.</li>
            <li><span class="highlight">Outlier Handling</span>: Values above the 99th percentile are capped.</li>
        </ul>

        <h3>Performance Rating Calculation</h3>
        <p>The script calculates a total performance rating for each employee based on the sum of specific metrics.</p>

        <h3>Transformation and Normality Test</h3>
        <p>Various transformations (Log, Square Root, Box-Cox, Inverse) are applied to the ratings to achieve normality. The Shapiro-Wilk test is used to identify the best transformation method.</p>

        <h3>Categorization</h3>
        <p>Employees are categorized into four categories (Poor, Average, Good, Best) based on percentiles.</p>

        <h3>Visualization</h3>
        <p>Histogram plots of the original and transformed ratings are generated. A normal distribution plot with categorized thresholds is created.</p>

        <h3>Error Handling</h3>
        <p>The script includes comprehensive error handling for file operations and data processing steps to ensure robustness.</p>

        <h2>Functions</h2>
        <h3><code>clean_data(df)</code></h3>
        <p>Cleans the data by handling missing values, converting data types, and capping outliers.</p>

        <h3><code>calculate_ratings(df)</code></h3>
        <p>Calculates the total performance rating for each employee.</p>

        <h3><code>apply_transformations(ratings)</code></h3>
        <p>Applies various transformations to the ratings and performs normality tests.</p>

        <h3><code>categorize_employees(ratings)</code></h3>
        <p>Categorizes employees based on performance ratings and specified thresholds.</p>

        <h3><code>plot_normal_distribution(mean, std, thresholds)</code></h3>
        <p>Generates a normal distribution plot with categorized thresholds.</p>

        <h3><code>save_categorized_employees(categories)</code></h3>
        <p>Saves the categorized employee data to a new CSV file and sorts it by category.</p>

        <h2>Contact</h2>
        <p>For any questions or issues, please contact <strong>[Your Name]</strong> at <strong>[Your Email]</strong>.</p>
    </div>
</body>
</html>
