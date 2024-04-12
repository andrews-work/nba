# visualize.py

import plotly.express as px

def visualize_salary_vs_performance(data):
    fig = px.scatter(data, x='Salary', y='overall_performance_score', hover_data=['Player Name'])
    fig.update_layout(
        xaxis_title='Salary',
        yaxis_title='Overall Performance Score (z)',
        title='Salary vs Overall Performance Score'
    )
    fig.show()
