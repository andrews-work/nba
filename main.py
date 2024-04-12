# main.py

# import libraries
import pandas as pd
from clean import clean_data
from positionAverage import (
    average_points_by_position,
    average_assists_by_position,
    average_rebounds_by_position,
    average_turnovers_by_position,
    average_fouls_by_position,
    average_age_by_position,
    average_minutes_by_position,
    average_salary_by_position,
    average_steals_by_position,
    average_per_by_position,
    average_games_played_by_position
)
from visualise import visualize_salary_vs_performance

# Load data
nba_data = pd.read_csv('nba_stats.csv')
print(nba_data.columns)

# Step 1 - Prepare Data
cleaned_data = clean_data(nba_data)

# Step 2 - Calculate Average Metrics by Position

avg_points = average_points_by_position(cleaned_data)
print("Average Points by Position:")
print(avg_points)

avg_assists = average_assists_by_position(cleaned_data)
print("Average Assists by Position:")
print(avg_assists)

avg_rebounds = average_rebounds_by_position(cleaned_data)
print("Average Rebounds by Position:")
print(avg_rebounds)

avg_turnovers = average_turnovers_by_position(cleaned_data)
print("Average Turnovers by Position:")
print(avg_turnovers)

avg_fouls = average_fouls_by_position(cleaned_data)
print("Average Fouls by Position:")
print(avg_fouls)

avg_age = average_age_by_position(cleaned_data)
print("Average Age by Position:")
print(avg_age)

avg_minutes = average_minutes_by_position(cleaned_data)
print("Average Minutes by Position:")
print(avg_minutes)

avg_salary = average_salary_by_position(cleaned_data)
print("Average Salary by Position:")
print(avg_salary)

avg_steals = average_steals_by_position(cleaned_data)
print("Average Steals by Position:")
print(avg_steals)

avg_per = average_per_by_position(cleaned_data)
print("Average PER by Position:")
print(avg_per)

avg_games_played = average_games_played_by_position(cleaned_data)
print("Average Games Played by Position:")
print(avg_games_played)

# Step 3 - Normalize Performance Metrics

def calculate_z_score(data, metric_column):
    # Calculate z-score for the given metric
    z_scores = (data[metric_column] - data[metric_column].mean()) / data[metric_column].std()
    return z_scores

def normalize_metrics(data):
    # Normalize the desired metrics using z-scores
    normalized_data = data.copy()
    normalized_data['z_points'] = calculate_z_score(data, 'PTS')
    normalized_data['z_assists'] = calculate_z_score(data, 'AST')
    normalized_data['z_rebounds'] = calculate_z_score(data, 'TRB')
    normalized_data['z_offensive_rebounds'] = calculate_z_score(data, 'ORB')
    normalized_data['z_defensive_rebounds'] = calculate_z_score(data, 'DRB')
    normalized_data['z_fg_percentage'] = calculate_z_score(data, 'FG%')
    normalized_data['z_minutes'] = calculate_z_score(data, 'MP')
    normalized_data['z_turnovers'] = calculate_z_score(data, 'TOV')
    normalized_data['z_steals'] = calculate_z_score(data, 'STL')
    normalized_data['z_personal_fouls'] = calculate_z_score(data, 'PF')
    # Add other metrics as needed
    return normalized_data


# Step 4 - Calculate Overall Performance Score (z)

def calculate_overall_performance_score(data, weights):
    # Calculate the weighted sum of normalized metrics
    data['overall_performance_score'] = weights['z_points'] * data['z_points'] + \
                                        weights['z_assists'] * data['z_assists'] + \
                                        weights['z_rebounds'] * data['z_rebounds'] + \
                                        weights['z_offensive_rebounds'] * data['z_offensive_rebounds'] + \
                                        weights['z_defensive_rebounds'] * data['z_defensive_rebounds'] + \
                                        weights['z_fg_percentage'] * data['z_fg_percentage'] + \
                                        weights['z_minutes'] * data['z_minutes'] + \
                                        weights['z_turnovers'] * data['z_turnovers'] + \
                                        weights['z_steals'] * data['z_steals'] + \
                                        weights['z_personal_fouls'] * data['z_personal_fouls']
    return data

# Set the weights for each metric
weights = {
    'z_points': 0.1,
    'z_assists': 0.1,
    'z_rebounds': 0.1,
    'z_offensive_rebounds': 0.15,  # Offensive rebounds are weighted more than defensive rebounds
    'z_defensive_rebounds': 0.1,
    'z_fg_percentage': 0.1,
    'z_minutes': 0.1,
    'z_turnovers': -0.1,  # Turnovers are negative because they decrease performance
    'z_steals': 0.1,
    'z_personal_fouls': -0.1,  # Personal fouls are negative because they decrease performance
}


# Normalize the metrics
normalized_data = normalize_metrics(cleaned_data)

# Calculate the overall performance score (z)
overall_performance_data = calculate_overall_performance_score(normalized_data, weights)

# Step 5 - Visualize Salary vs Overall Performance Score

# Visualize the data
visualize_salary_vs_performance(overall_performance_data)