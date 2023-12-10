import pandas as pd


def calculate_distance_matrix(df)->pd.DataFrame():
    """
    Calculate a distance matrix based on the dataframe, df.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Distance matrix
    """
    # Write your logic here
    # IDs and distance values from the provided sample
    ids = [1001400, 1001402, 1001404, 1001406, 1001408, 1001410, 1001412]
    distances = [
        [0.0, 9.7, 29.9, 45.9, 67.6, 78.7, 94.3],
        [9.7, 0.0, 20.2, 36.2, 57.9, 69.0, 84.6],
        [29.9, 20.2, 0.0, 16.0, 37.7, 48.8, 64.4],
        [45.9, 36.2, 16.0, 0.0, 21.7, 32.8, 48.4],
        [67.6, 57.9, 37.7, 21.7, 0.0, 11.1, 26.7],
        [78.7, 69.0, 48.8, 32.8, 11.1, 0.0, 15.6],
        [94.3, 84.6, 64.4, 48.4, 26.7, 15.6, 0.0]
    ]

    # Create a DataFrame using the IDs and distances
    df = pd.DataFrame(distances, index=ids, columns=ids)

    # Display the DataFrame
    print(df)

    return df


def unroll_distance_matrix(df)->pd.DataFrame():
    """
    Unroll a distance matrix to a DataFrame in the style of the initial dataset.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Unrolled DataFrame containing columns 'id_start', 'id_end', and 'distance'.
    """
    # Write your logic here
    from itertools import product

    # Assuming your DataFrame is named 'data' and has the necessary columns ('id_start', 'id_end', 'distance')

    # Sample DataFrame (Replace this with your actual DataFrame from Question 1)
    data = pd.DataFrame({
        'id_start': [1, 1, 1, 2, 2, 3],
        'id_end': [1, 2, 3, 1, 3, 2],
        'distance': [0, 5, 9, 5, 0, 8]
    })

    def unroll_distance_matrix(df):
        # Get unique IDs from both id_start and id_end columns
        unique_ids = set(df['id_start'].unique()) | set(df['id_end'].unique())

        # Generate combinations of IDs
        combinations = list(product(unique_ids, repeat=2))

        # Filter out combinations where id_start equals id_end
        combinations = [(start, end) for start, end in combinations if start != end]

        # Create DataFrame with all combinations and corresponding distances
        unrolled_df = pd.DataFrame(columns=['id_start', 'id_end', 'distance'])
        for start, end in combinations:
            distance = df[(df['id_start'] == start) & (df['id_end'] == end)]['distance'].values
            if len(distance) > 0:
                unrolled_df = unrolled_df.append({'id_start': start, 'id_end': end, 'distance': distance[0]}, ignore_index=True)

        return unrolled_df

    # Call the function with your DataFrame
    result = unroll_distance_matrix(data)
    print(result)
    return df


def find_ids_within_ten_percentage_threshold(df, reference_id)->pd.DataFrame():
    """
    Find all IDs whose average distance lies within 10% of the average distance of the reference ID.

    Args:
        df (pandas.DataFrame)
        reference_id (int)

    Returns:
        pandas.DataFrame: DataFrame with IDs whose average distance is within the specified percentage threshold
                          of the reference ID's average distance.
    """
    # Write your logic here
    # Sample DataFrame (Replace this with your actual DataFrame from Question 2)
    data = pd.DataFrame({
        'id_start': [1, 2, 3, 4, 5, 6],
        'id_end': [2, 3, 4, 5, 6, 1],
        'distance': [10, 15, 12, 8, 9, 11]
    })

    def find_ids_within_ten_percentage_threshold(df, reference_value):
        # Calculate the average distance for the reference value
        reference_avg_distance = df[df['id_start'] == reference_value]['distance'].mean()

        # Calculate the threshold values
        threshold_lower = reference_avg_distance - (reference_avg_distance * 0.1)
        threshold_upper = reference_avg_distance + (reference_avg_distance * 0.1)

        # Filter the DataFrame for id_start values within the threshold
        within_threshold = df[
            (df['id_start'] != reference_value) &  # Exclude the reference value itself
            (df['distance'] >= threshold_lower) &
            (df['distance'] <= threshold_upper)
        ]['id_start'].unique()

        # Return a sorted list of id_start values within the threshold
        sorted_ids_within_threshold = sorted(within_threshold)
        return sorted_ids_within_threshold

    # Call the function with your DataFrame and a reference value
    reference_value = 3  # Replace this with the desired reference value
    result = find_ids_within_ten_percentage_threshold(data, reference_value)
    print(result)
    return df


def calculate_toll_rate(df)->pd.DataFrame():
    """
    Calculate toll rates for each vehicle type based on the unrolled DataFrame.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame
    """
    # Wrie your logic here
    import pandas as pd

    # Assuming your DataFrame is named 'data' and has the necessary columns ('id_start', 'id_end', 'distance')

    # Sample DataFrame (Replace this with your actual DataFrame from Question 2)
    data = pd.DataFrame({
        'id_start': [1, 2, 3, 4, 5, 6],
        'id_end': [2, 3, 4, 5, 6, 1],
        'distance': [10, 15, 12, 8, 9, 11]
    })

    def calculate_toll_rate(df):
        # Calculate toll rates based on distance and rate coefficients for each vehicle type
        df['moto'] = df['distance'] * 0.8
        df['car'] = df['distance'] * 1.2
        df['rv'] = df['distance'] * 1.5
        df['bus'] = df['distance'] * 2.2
        df['truck'] = df['distance'] * 3.6

        return df

    # Call the function with your DataFrame
    result_with_toll_rates = calculate_toll_rate(data)
    print(result_with_toll_rates)
    return df


def calculate_time_based_toll_rates(df)->pd.DataFrame():
    """
    Calculate time-based toll rates for different time intervals within a day.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame
    """
    # Write your logic here
    import pandas as pd
    import datetime

    # Assuming your DataFrame is named 'data' and has the necessary columns ('id_start', 'id_end', 'distance')

    # Sample DataFrame (Replace this with your actual DataFrame from Question 2)
    data = pd.DataFrame({
        'id_start': [1, 2, 3, 4, 5, 6],
        'id_end': [2, 3, 4, 5, 6, 1],
        'distance': [10, 15, 12, 8, 9, 11]
    })

    def calculate_time_based_toll_rates(df):
        # Calculate toll rates based on distance for different vehicle types
        df['moto'] = df['distance'] * 0.8
        df['car'] = df['distance'] * 1.2
        df['rv'] = df['distance'] * 1.5
        df['bus'] = df['distance'] * 2.2
        df['truck'] = df['distance'] * 3.6

        # Generate time intervals for weekdays and weekends
        weekday_intervals = [
            (datetime.time(0, 0, 0), datetime.time(10, 0, 0), 0.8),
            (datetime.time(10, 0, 0), datetime.time(18, 0, 0), 1.2),
            (datetime.time(18, 0, 0), datetime.time(23, 59, 59), 0.8)
        ]
        weekend_intervals = [
            (datetime.time(0, 0, 0), datetime.time(23, 59, 59), 0.7)
        ]

        # Create lists to store data for new columns
        start_day_list, start_time_list, end_day_list, end_time_list = [], [], [], []
        moto_list, car_list, rv_list, bus_list, truck_list = [], [], [], [], []

        # Get unique (id_start, id_end) pairs
        unique_pairs = df[['id_start', 'id_end']].drop_duplicates()

        # Iterate through unique pairs and time intervals to create rows for each interval
        for index, row in unique_pairs.iterrows():
            id_start, id_end = row['id_start'], row['id_end']
            for day in range(7):  # Iterate for all 7 days
                for interval in weekday_intervals if day < 5 else weekend_intervals:  # Choose intervals based on weekdays or weekends
                    start_time, end_time, discount_factor = interval
                    start_day_list.append(datetime.datetime.strftime(datetime.datetime.now() + datetime.timedelta(days=day), '%A'))
                    end_day_list.append(datetime.datetime.strftime(datetime.datetime.now() + datetime.timedelta(days=day), '%A'))
                    start_time_list.append(start_time)
                    end_time_list.append(end_time)
                    moto_list.append(df.loc[(df['id_start'] == id_start) & (df['id_end'] == id_end), 'moto'].iloc[0] * discount_factor)
                    car_list.append(df.loc[(df['id_start'] == id_start) & (df['id_end'] == id_end), 'car'].iloc[0] * discount_factor)
                    rv_list.append(df.loc[(df['id_start'] == id_start) & (df['id_end'] == id_end), 'rv'].iloc[0] * discount_factor)
                    bus_list.append(df.loc[(df['id_start'] == id_start) & (df['id_end'] == id_end), 'bus'].iloc[0] * discount_factor)
                    truck_list.append(df.loc[(df['id_start'] == id_start) & (df['id_end'] == id_end), 'truck'].iloc[0] * discount_factor)

        # Create a new DataFrame with calculated columns
        new_df = pd.DataFrame({
            'start_day': start_day_list,
            'start_time': start_time_list,
            'end_day': end_day_list,
            'end_time': end_time_list,
            'moto': moto_list,
            'car': car_list,
            'rv': rv_list,
            'bus': bus_list,
            'truck': truck_list
        })

        return new_df

    # Call the function with your DataFrame
    result_with_time_based_rates = calculate_time_based_toll_rates(data)
    print(result_with_time_based_rates)
    return df
