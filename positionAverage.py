# positionAverage.py

# import libraries
import pandas as pd


def calculate_average_metric(data, metric_column):
    # Calculate overall average for the given metric
    overall_avg_metric = data[metric_column].mean()

    # Calculate average metric for each player position
    avg_metric_by_position = data.groupby('Position')[metric_column].mean()

    # Combine the overall average with the average for each position
    avg_metric_combined = pd.DataFrame({
        'Position': ['Overall'] + avg_metric_by_position.index.tolist(),
        f'average_{metric_column}': [overall_avg_metric] + avg_metric_by_position.values.tolist()
    })

    return avg_metric_combined

def average_metrics_by_position_and_salary_range(data, position, salary, salary_range):
    # Filter data for players in the same position and within the specified salary range
    filtered_data = data[(data['Position'] == position) & (data['Salary'].between(salary * (1 - salary_range), salary * (1 + salary_range)))]

    # Calculate average metrics for the filtered data
    avg_metrics = filtered_data.mean()

    return avg_metrics

def average_points_by_position(data):
    return calculate_average_metric(data, 'PTS')

def average_assists_by_position(data):
    return calculate_average_metric(data, 'AST')

def average_rebounds_by_position(data):
    return calculate_average_metric(data, 'TRB')

def average_turnovers_by_position(data):
    return calculate_average_metric(data, 'TOV')

def average_fouls_by_position(data):
    return calculate_average_metric(data, 'PF')

def average_age_by_position(data):
    return calculate_average_metric(data, 'Age')

def average_minutes_by_position(data):
    return calculate_average_metric(data, 'MP')

def average_salary_by_position(data):
    return calculate_average_metric(data, 'Salary')

def average_steals_by_position(data):
    return calculate_average_metric(data, 'STL')

def average_per_by_position(data):
    return calculate_average_metric(data, 'PER')

def average_games_played_by_position(data):
    return calculate_average_metric(data, 'GP')
