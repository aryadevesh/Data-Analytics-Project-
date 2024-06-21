def load_data(csv_file):
    try:
        df = pd.read_csv(csv_file)
    except FileNotFoundError:
        print(f"Error: The file {csv_file} was not found.")
        exit()
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        exit()
    except pd.errors.ParserError:
        print("Error: Error parsing the file.")
        exit()
    return df
