import pandas as pd


def generate_car_matrix(df)->pd.DataFrame:
    """
    Creates a DataFrame  for id combinations.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Matrix generated with 'car' values, 
                          where 'id_1' and 'id_2' are used as indices and columns respectively.
    """
    # Write your logic here
    import pandas as pd

    def generate_car_matrix():
    # Load the dataset-1.csv into a DataFrame
    df = pd.read_csv('/content/drive/MyDrive/Interns/MapUp-Data-Assessment-F-main/datasets/dataset-1.csv')

    # Create a pivot table to get the desired matrix
    car_matrix = pd.pivot_table(df, values='car', index='id_1', columns='id_2', fill_value=0)

    # Set diagonal values to 0
    for i in range(min(car_matrix.shape[0], car_matrix.shape[1])):
        car_matrix.iloc[i, i] = 0

    return car_matrix

    # Example usage
    result_matrix = generate_car_matrix()
    print(result_matrix)

    return df


def get_type_count(df)->dict:
    """
    Categorizes 'car' values into types and returns a dictionary of counts.

    Args:
        df (pandas.DataFrame)

    Returns:
        dict: A dictionary with car types as keys and their counts as values.
    """
    # Write your logic here
    import pandas as pd

    def get_type_count(df):
        # Add a new categorical column 'car_type' based on values of the 'car' column
        conditions = [
            (df['car'] <= 15),
            (df['car'] > 15) & (df['car'] <= 25),
            (df['car'] > 25)
        ]
        choices = ['low', 'medium', 'high']
        df['car_type'] = pd.cut(df['car'], bins=[float('-inf'), 15, 25, float('inf')], labels=choices, right=False)

        # Calculate the count of occurrences for each 'car_type' category
        type_counts = df['car_type'].value_counts().to_dict()

        # Sort the dictionary alphabetically based on keys
        sorted_type_counts = {key: type_counts[key] for key in sorted(type_counts)}

        return sorted_type_counts

    # Example usage
    df = pd.read_csv('/content/drive/MyDrive/Interns/MapUp-Data-Assessment-F-main/datasets/dataset-1.csv')  # Make sure to provide the correct path to your CSV file
    result_counts = get_type_count(df)
    print(result_counts)

    return dict()


def get_bus_indexes(df)->list:
    """
    Returns the indexes where the 'bus' values are greater than twice the mean.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of indexes where 'bus' values exceed twice the mean.
    """
    # Write your logic here
    import pandas as pd

    def get_bus_indexes(df):
        # Calculate the mean value of the 'bus' column
        mean_bus = df['bus'].mean()

        # Identify indices where 'bus' values are greater than twice the mean
        bus_indexes = df[df['bus'] > 2 * mean_bus].index.tolist()

        # Sort the indices in ascending order
        bus_indexes.sort()

        return bus_indexes

    # Example usage
    df = pd.read_csv('/content/drive/MyDrive/Interns/MapUp-Data-Assessment-F-main/datasets/dataset-1.csv')  # Make sure to provide the correct path to your CSV file
    result_indexes = get_bus_indexes(df)
    print(result_indexes)

    return list()


def filter_routes(df)->list:
    """
    Filters and returns routes with average 'truck' values greater than 7.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of route names with average 'truck' values greater than 7.
    """
    # Write your logic here
    import pandas as pd

    def filter_routes(df):
        # Group by 'route' and calculate the average of the 'truck' column
        route_avg_truck = df.groupby('route')['truck'].mean()

        # Filter routes where the average of 'truck' column is greater than 7
        selected_routes = route_avg_truck[route_avg_truck > 7].index.tolist()

        # Sort the list of selected routes
        selected_routes.sort()

        return selected_routes

    # Example usage
    df = pd.read_csv('/content/drive/MyDrive/Interns/MapUp-Data-Assessment-F-main/datasets/dataset-1.csv')  # Make sure to provide the correct path to your CSV file
    result_routes = filter_routes(df)
    print(result_routes)

    return list()


def multiply_matrix(matrix)->pd.DataFrame:
    """
    Multiplies matrix values with custom conditions.

    Args:
        matrix (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Modified matrix with values multiplied based on custom conditions.
    """
    # Write your logic here
    import pandas as pd

    def multiply_matrix(input_matrix):
        # Create a deep copy of the input matrix to avoid modifying the original DataFrame
        modified_matrix = input_matrix.copy()

        # Apply the specified logic to modify values
        modified_matrix[modified_matrix > 20] *= 0.75
        modified_matrix[modified_matrix <= 20] *= 1.25

        # Round values to 1 decimal place
        modified_matrix = modified_matrix.round(1)

        return modified_matrix

    # Example usage
    # Assuming result_matrix is the DataFrame from Question 1
    modified_result = multiply_matrix(result_matrix)
    print(modified_result)

    return matrix


def time_check(df)->pd.Series:
    """
    Use shared dataset-2 to verify the completeness of the data by checking whether the timestamps for each unique (`id`, `id_2`) pair cover a full 24-hour and 7 days period

    Args:
        df (pandas.DataFrame)

    Returns:
        pd.Series: return a boolean series
    """
    # Write your logic here
    def verify_time_completeness_for_row(row):
    # Create a DataFrame with the specific row
    df = pd.DataFrame([row], columns=[
        'id_1', 'name', 'id_2', 'startDay', 'startTime', 'endDay', 'endTime',
        'able2Hov2', 'able2Hov3', 'able3Hov2', 'able3Hov3', 'able5Hov2', 'able5Hov3', 'able4Hov2', 'able4Hov3'
    ])

    # Convert time columns to datetime objects
    df['startTime'] = pd.to_datetime(df['startTime'])
    df['endTime'] = pd.to_datetime(df['endTime'])

    # Convert startDay and endDay to the corresponding days of the week
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    start_day_index = days_of_week.index(df['startDay'].values[0])
    end_day_index = days_of_week.index(df['endDay'].values[0])

    # Calculate the number of days between the start and end days
    days_difference = end_day_index - start_day_index + 1 if end_day_index >= start_day_index else 7 + end_day_index - start_day_index + 1

    # Calculate the duration between startTime and endTime
    duration = (df['endTime'].values[0] - df['startTime'].values[0])

    # Check if the time period covers a full 24-hour period and spans all 7 days
    return duration >= pd.Timedelta(days=1) and days_difference == 7

    # Sample row data
    row_data = [1040000, 'Montgomery', -1, 'Monday', '5:00:00', 'Wednesday', '10:00:00', 3, 3, -1, -1, 3, 3, 3, 3]

    # Verify time completeness for the specific row
    time_completeness_row_check = verify_time_completeness_for_row(row_data)
    print("Time Completeness Check for Row:", time_completeness_row_check)
    return pd.Series()
