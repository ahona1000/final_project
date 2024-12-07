from shiny import App, render, ui
import pandas as pd
import matplotlib.pyplot as plt

# Sample data
salary_data = pd.DataFrame({
    'ID': [1, 2, 3, 4, 5],
    'Experience_Years': [5, 1, 3, 2, 1],
    'Age': [28, 21, 23, 22, 17],
    'Gender': ['Female', 'Male', 'Female', 'Male', 'Male'],
    'Salary': [250000, 50000, 170000, 25000, 10000]
})

# Define the UI
app_ui = ui.page_fluid(
    ui.panel_title("Salary Analysis by Gender"),
    ui.input_select("gender", "Gender", choices=['All', 'Male', 'Female']),  # Gender filter
    ui.output_plot("salary_plot"),
)

# Define the server logic
def server(input, output, session):
    @output
    @render.plot
    def salary_plot():
        selected_gender = input.gender()
        
        # Filter dataset based on gender
        if selected_gender != 'All':
            filtered_data = salary_data[salary_data['Gender'] == selected_gender]
        else:
            filtered_data = salary_data
        
        # Group by Gender and calculate average salary
        salary_by_gender = filtered_data.groupby('Gender')['Salary'].mean().reset_index()

        # Plotting a simple bar chart
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.bar(salary_by_gender['Gender'], salary_by_gender['Salary'], color=['skyblue', 'lightcoral'])
        ax.set_title("Average Salary by Gender")
        ax.set_xlabel('Gender')
        ax.set_ylabel('Average Salary')

        return fig

# Run the Shiny app
app = App(app_ui, server)
