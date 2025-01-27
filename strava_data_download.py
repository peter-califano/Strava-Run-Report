#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import urllib3
import pandas as pd
import sys
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

auth_url = "https://www.strava.com/oauth/token"
activities_url = "https://www.strava.com/api/v3/athlete/activities"

payload = {
    'client_id': "XXX",
    'client_secret': 'XXX',
    'refresh_token': 'XXX',
    'grant_type': "refresh_token",
    'scope': 'activity:read',
    'f': 'json'
}

print("Requesting Token...\n")
res = requests.post(auth_url, data=payload, verify=False)
access_token = res.json()['access_token']
print("Access Token = {}\n".format(access_token))

# Set up pagination parameters
per_page = 200  # Strava API allows up to 200 results per page
header = {'Authorization': 'Bearer ' + access_token}
all_activities = []  # List to store all activities
page = 1  # Start with the first page

# Fetch data page by page until no data is returned
while True:
    print(f"Fetching page {page}...")
    param = {'per_page': per_page, 'page': page}
    response = requests.get(activities_url, headers=header, params=param)
    data = response.json()
    
    # Check if there's no more data to fetch
    if not data:
        print("All activity data has been pulled.")
        break
    
    # Append the data to the main list
    all_activities.extend(data)
    
    # Increment the page number to fetch the next page
    page += 1

# Convert the list of activities to a DataFrame
df = pd.DataFrame(all_activities)
print(df)


# In[2]:


df.columns
df = df.loc[:,['name', 'distance', 'moving_time',
       'elapsed_time', 'total_elevation_gain', 'sport_type',
        'id', 'start_date', 'start_date_local', 'timezone',
       'utc_offset',
       'achievement_count', 'kudos_count',  'map', 'manual', 
        'start_latlng', 'end_latlng',
       'average_speed', 'max_speed', 'elev_high', 'elev_low', 'upload_id',
        'pr_count']]


df.to_csv('strava_api_data.csv')


