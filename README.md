# Strava-Run-Report

## Project Overview
This project is a dynamic [dashboard](https://public.tableau.com/app/profile/peter.califano1707/viz/RunDataReportDarkMode/WeeklyDashboard) that visualizes activity data from Strava, providing insights into performance trends, training patterns, and progress over time. The dashboard combines the power of API integration, ETL (Extract, Transform, Load) pipelines, and advanced data visualization to deliver meaningful, interactive insights.

Explore the interactive Tableau dashboard here: [dark mode](https://public.tableau.com/app/profile/peter.califano1707/viz/RunDataReportDarkMode/WeeklyDashboard) [light mode](https://public.tableau.com/app/profile/peter.califano1707/viz/RunDataReportLightMode/WeeklyDashboard#1).

## Features
- **Comprehensive Activity Tracking**: Analyze data such as distance, duration, pace, elevation, and heart rate.
- **Performance Trends**: Visualize patterns over time, including training load and intensity distribution.
- **Interactive Visualizations**: User-friendly filtering for time period, week, and individual activites for insights into training and performance. 
  
## Technologies Used
- **Strava API**: Used to pull raw activity data programmatically.
- **Python**: Employed for data cleaning, transformation, and loading using libraries like `pandas`.
- **ETL Pipeline**: Automated processes to fetch, process, and store data.
- **Tableau**: Developed an interactive dashboard to display the processed data.

---

## Workflow

### 1. **Data Extraction**
   - Integrated with the Strava API to programmatically retrieve activity data.
   - Pulled data fields such as activity type, date, distance, duration, pace, elevation gain, and heart rate.

### 2. **Data Transformation**
   - Used Python and `pandas` to clean and preprocess raw data:
     - Handled missing values, inconsistent formats, and unit conversions.
     - Generated new calculated fields for time, pace, and date/time formats.
   - Stored cleaned data in an SQLite database for long-term access.
   - Utilize data scaffolding for visualization

### 3. **Data Loading**
   - Established an ETL pipeline to automate the regular fetching, transformation, and updating of data.
   - Ensured new activities are appended without duplicating existing records.

### 4. **Visualization**
   - Connected Tableau to the SQLite database for data visualization (Tableau Public visualization utilizes a .csv through google drive for easy updating).
   - Created a suite of dashboards:
     - **Overview Dashboard**: High-level summaries of weekly and monthly progress.
     - **Performance Trends**: Line charts and heatmaps to track key metrics over time.
     - **Custom Insights**: Filters for activity type, date range, and other dimensions.

---
