#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import sys

# In[2]:


strava_act = pd.read_csv("strava_api_data.csv",  encoding = "windows_1258", index_col = 0)


# In[3]:


#strava_act.drop(strava_act[strava_act['manual'] == True].index, inplace=True) ###removes manual activities

strava_act = strava_act[strava_act['sport_type'].isin(['Run', 'TrailRun'])] ### keeps activities that are runs or trail runs
strava_act.reset_index(drop=True, inplace = True) ###resets index after removing data
print(len(strava_act))


# In[4]:


pd.options.display.float_format = '{:.0f}'.format
### changes display  to avoid scientific notation of Id #s

strava_act['distance'] = round(strava_act['distance'] / 1609.34, 2) 
### takes distance column (in meters) and divides by 1609.34 to get miles rounded to 2 decimaal places

strava_act['moving_minutes'] = strava_act['moving_time'] / 60
strava_act['elapsed_minutes'] = strava_act['elapsed_time'] / 60
###time in seconds divided to get minutes

strava_act['moving_int_minutes'] = strava_act['moving_minutes'].astype(int)  # integer part as minutes
strava_act['moving_remaining_seconds'] = ((strava_act['moving_minutes'] - strava_act['moving_int_minutes']) * 60).round()  # remaining seconds
###converts minutes to an integer, then subtracts that from non-int minutes, giving the remaining seconds 
strava_act['elapsed_int_minutes'] = strava_act['elapsed_minutes'].astype(int)  # integer part as minutes
strava_act['elapsed_remaining_seconds'] = ((strava_act['elapsed_minutes'] - strava_act['elapsed_int_minutes']) * 60).round()  # remaining seconds

strava_act.loc[:,'average_speed'] = (1 / (strava_act.loc[:,'average_speed'] / 1609.34)) / 60 
### converts avg speed from meters per second to minutes per mile 
print(strava_act['average_speed'])
strava_act.drop(strava_act[strava_act['average_speed'] > 20].index, inplace=True) 
#Drops activities with an avg speed > 20 mins per mile as it is too slow to be considered a run

strava_act.head()


# In[5]:


strava_act['parsed_date'] = pd.to_datetime(strava_act['start_date_local']) ##parses date to standard format
strava_act['calendar_date'] = pd.to_datetime(strava_act['start_date_local']).dt.date

# Get the minimum and maximum years from the dataset
min_year = strava_act['calendar_date'].min().year
max_year = strava_act['calendar_date'].max().year

# Generate the full-year date range for all years in the range
date_range = pd.date_range(start=f'{min_year}-01-01', end=f'{max_year}-12-31')

# Create a DataFrame for the full-year date range
date_range_df = pd.DataFrame({'Date': date_range})

# Export the full-year date range to a CSV file
output_file = 'date_range_output.csv'
date_range_df.to_csv(output_file, index=False)

# Create a DataFrame for the date range
date_range_df = pd.DataFrame({'Date': date_range})

# Export the date range to a CSV file
output_file = 'date_range_output.csv'
date_range_df.to_csv(output_file, index=False)

strava_act.to_csv('strava_data_processed.csv') ##sends to csv




