#!/usr/bin/env python
# coding: utf-8

# # Trends and Patterns in Central London Hire Bikes

# ### Abstract

# &ensp; In this paper, I delve into data provided by Transportation For London about hire bikes within London. These statistics allow for us to discover trends and patterns, which in relation to hire bikes can be used to help further spread the use of hire bikes, as well as increasing the safety of said bikes. Taking data from a large data set about when locals use hire bikes in relation to the weather will help establish how safe users are currently being, as well as helping to give an idea of where companies should go in the future to ensure further safety.

# ### Key Words

# ###### Hire Bikes

# - Hire bikes are bicycles scattered across cities owned and maintained by companies. These companies offer the service of renting a bicycle for a short period of time in exchange for small amounts of currency. The concept of Hire Bikes allows for a high level of independence by the user, allowing for users to use them in any weather condition.

# ###### London Boroughs

# - London Boroughs are divided areas in London. They are each around a similar size and all 32 of them compose the Greater London Area.

# ###### Pedestrian

# - A civilian traveling around an area by walking.

# ### Introduction

# &emsp; Getting from Point A to Point B in a city as big as London is a topic of great importance. London is an incredibly large city, spreading over approximately 1572 square kilometers and housing a population of approximately nine million individual human beings. Because of this, inner city transportation is a topic of great importance. 
# 
# &emsp; Public transportation is a large part of how Londoners travel on a daily basis. London is well known for being the home of ‘The Underground’, an expansive and highly efficient network of underground trains that transport nearly 300 million people each year. Londoners commonly make use of this subway system to get them where they need to go. Within the city, the Underground has a strong reputation for being cheap and reliable. The famous double decker buses also provide a popular means of public transportation, which completed over one billion passenger journeys in 2022. That being said, relying on someone else to get people where they need to go might not be to the entire city's liking. 
# 
# &emsp; Some locals may opt to get a driver’s license and choose to drive a car, but that may take a lot of time, parking is difficult, and gas is quite expensive. London also has a ‘congestion charge’ which costs extra money just for the privilege of driving within the city boundaries. Traffic is another major concern, with streets commonly being backed up several blocks, and collisions commonly occurring. According to Trust for London, nearly 24000 car crashes occurred in the city during 2022, demonstrating how dangerous driving in a tightly packed city can be. Driving can be more dangerous than other forms of transportation. This means many Londoners need another form of transportation when they have to travel a distance that is too far to be walked. 
# 
# &emsp; This concept was cleanly supplied with the creation of Hire Bikes. Hire Bikes are bikes owned by companies that are placed across the city. These companies then offer temporary use of the bicycles for a fee. This has given many Londoners a new way to get around the city. Due to the inherent ability to rent and operate these bikes independently, many Londoners may use these bikes in ways that . 
# 

# ### Data Cleaning

#  - Using Python, Pandas, and Plotly Express allows us to observe and analyze the data given in large files in a much simpler manner.

# In[1]:


import pandas as pd
import plotly.express as px

# Establish our csv file as a dataframe
info_csv = pd.read_csv('2022-Central.csv')

# ---------------------------------------------------------------------------------------------------

# Drop the duplicate entries from the file to ensure data integrity
# Variables
    # Subset = Which rows to apply the function to, in this case we do all of them so it is None
    # Keep = Should we keep the duplicates by changing them or should we just drop them altogether
    # Inplace = Do we modify the dataframe instead of creating a new one (True = New DataFrame)
    # Index = Do we label the rows by index
info_csv = info_csv.drop_duplicates(subset = None, keep = False, inplace = False, ignore_index = False)

# ---------------------------------------------------------------------------------------------------

# Only keep the variables necessary for our analysis
# That means that we can drop every series that is using a mode that doesnt involve using hire bikes
info_csv = info_csv[info_csv.Mode != 'Pedestrians']
info_csv = info_csv[info_csv.Mode != 'E-scooters']

# I can also drop the first column entirely, as every single series in the file has the same value for it
# That means that it is essentially useless, as we already know all the possible data from the file
info_csv = info_csv.drop(columns='Year')
# This same logic applies to the 'Round' category, as every single series in this file is under the same Round
info_csv = info_csv.drop(columns='Round')

# ---------------------------------------------------------------------------------------------------

# Ensuring Data Types are correct
# We can use the command .dtypes to check what the current data types are
info_csv.dtypes

# We should change the date and time to be under the datetime data type
# We then create new dataframes using the correct data type
correctDate = pd.to_datetime(info_csv.Date, dayfirst=True)
correctTime = pd.to_datetime(info_csv.Time)

# We then go ahead and replace the old versions of the columns with the new versions
info_csv['Date'] = correctDate
info_csv['Time'] = correctTime

# Finally for this step, we check the data types one more time
info_csv.dtypes

# If it is what we wanted, then we move on

# ---------------------------------------------------------------------------------------------------

# Final display of the CSV file after these edits
info_csv


# - Displayed above is the new cleaned version of the CSV file. It has dropped unnecessary details and is now ready to be analyzed to find patterns.

# ### Data Analysis

# In[63]:


# Analyzing Data - Number of Bikes rented in Weather

# Establish new CSV's that are only showing the data associated with dry days and with wet days
dry_weather_csv = info_csv[info_csv.Weather == 'Dry']
wet_weather_csv = info_csv[info_csv.Weather == 'Wet']

# Take the average count of people per day in each of these files
dry_weather_average = dry_weather_csv.Count.mean()
wet_weather_average = wet_weather_csv.Count.mean()

# Create a dataframe via a dictionary 
weather_average_dictionary = {'Average Number of Bikes': [dry_weather_average, wet_weather_average], 'Weather': ['Dry', 'Wet']}
weather_average_dataframe = pd.DataFrame(data = weather_average_dictionary)

# Plot this information as a bar graph which will compare the average number of bikes rented on a wet day to the average number of bikes rented on a dry day
# Variables
    # The y axis represents the average number of bikes
    # The x axis represents the different weather options
    # The rot helps display the labels so it is more readable
weather_average_dataframe.plot.bar(y='Average Number of Bikes', x='Weather', rot=45, title = 'Average Number of Bikes in Different Weather')

# ---------------------------------------------------------------------------------------------------

# Take the total number of bikers in dry weather and total number of bikers in dry weather
dry_biker_total = dry_weather_csv.Count.sum()
wet_biker_total = wet_weather_csv.Count.sum()

# Turn the data from above into a dictionary and then into a dataframe
weather_sums_dictionary = {'Total Number of Bikes': [dry_biker_total, wet_biker_total], 'Weather': ['Dry', 'Wet']}
weather_sums_dataframe = pd.DataFrame(data = weather_sums_dictionary)

# Convert the dataframe into a bar graph
# Variables are the same above, with the exception of switching the average number of bikes to total number of bikes
weather_sums_dataframe.plot.bar(y='Total Number of Bikes', x='Weather', rot=45, title='Total Number of Bikes in Different Weather')

# ---------------------------------------------------------------------------------------------------

# Use plotly express to create a pie chart with values found online from Britannica
pcd = {'Days': [150, 215], 'Weather': ["Wet", "Dry"]}
day_percent_df = pd.DataFrame(data = pcd)

# The variables used here are the variables Days and Weather, and I can change the color of the chart to show wet versus dry
dayfig = px.pie(day_percent_df, values='Days', names='Weather', color='Weather', color_discrete_map={'Wet':'royalblue','Dry':'orange'}, title='Weather Percentages in London 2022')

# Display the graph
dayfig.show()

# ---------------------------------------------------------------------------------------------------

# Use plotly express to create a pie chart with values found online from Britannica
pccd = {'Percent': [68, 32], 'Weather': ["Wet", "Dry"]}
crash_percent_df = pd.DataFrame(data = pccd)
crash_percent_df

# The variables used here are the variables Days and Weather, and I can change the color of the chart to show wet versus dry
crashfig = px.pie(crash_percent_df, values='Percent', names='Weather', color='Weather', color_discrete_map={'Wet':'royal_blue','Dry':'orange'}, title='Condition for Bike Crashes in London 2022')

# Display the graph
crashfig.show()

# ----------------------------------------------------------------------------------------------------

# Use plotly express to create a graph of a couple days showing specific use amounts of bikes
    # We will use this graph to demonstrate the levels of people biking to prove that people use hire bikes for transport to work
# New CSV file showing only the reports from an individual date
date_csv = info_csv[info_csv.Date == "2022-06-28"]

# New CSV file showing only the reports from hire bikes on said date
short1_csv = date_csv[date_csv.Mode == "Cycle hire bikes"]

# New CSV file showing only the reports from a single hire bike
short_csv = short1_csv[short1_csv.UnqID == "CENCY049"]

# Create a line chart displaying the use of cycle hire bikes over time on a certain day 
line = px.line(short_csv, x='Time', y='Count', title='Renting of Hire Bikes over a Single Day')
line.show()


# ### Results

# &emsp; The weather in London adds to the often unsafe biking conditions that Hire Bikes customers may operate in. The weather in London is seldom dry. It is so often drizzling within and around the city that the city itself has gained a reputation of commonly being gray and having wet weather. Nearly every Londoner knows never to go anywhere without an umbrella or rain jacket on hand, as they never truly know when it may rain next. In 2022, there were over 150 days of precipitation. That means that a staggering 41% of all days in this year in London had some form of precipitation. This is demonstrated above with the pie chart titled "Weather Percentages in London 2022". Although it didn’t rain during the majority of the days, over 150 days or precipitation is still a noticeably larger amount than in other places in the world. Los Angeles averaged around 35 days of rain in 2022, and Paris averaged around 110. Due to this common precipitation, the streets of London are commonly in unfit conditions for bicycles. The reason behind this recurring drizzle is due to the location of the city. Because of its proximity to the Atlantic ocean, winds commonly blow in from the west carrying water that evaporated from the ocean. The water is then deposited over England, including London. Because of London's location on the east side of England, the majority of the water has already poured down over cities west of London. London's annual total precipitation is actually quite low when compared to other cities, yet it commonly drizzles due to the leftover water in the clouds from the Atlantic Ocean. This could cause the pavements and roads to get wet, which could be a large problem, as a decent amount of Londoners use hire bikes in order to get to work as well as to get home afterwards. This is shown above in the line chart titled "Renting of Hire Bikes in a Single Day", where we can see there is a sharp spike in rentings during the hours where people would be going to and from work. Despite this, the data published by the company Transport For London found that people are only slightly less likely to rent and operate a bicycle under improper conditions. According to statistics taken in May, June, and July of 2022; The average number of bikes rented every 15 minutes in dry weather was around three and half, while the number of bikes rented every 15 minutes in wet weather was around two and a half. This is shown above in the bar graph titled "Average Number of Bikes in Different Weather". There are multiple conclusions that could be taken from this data, and both of these points are valid arguments. If we look at the total number of bikes rented during dry days compared to the total number of bikes rented during wet days we can quickly see that the total number of bikes rented on dry days vastly outnumbered the total number of bikes rented on wet days. This is demonstrated above with the bar graph titled "Total Number of Bikes in Different Weather". The reason for this is due to the fact that the number of dry days outnumbered the number of wet days,  as well as because of the fact that people were less likely to rent a bike in unsafe conditions. This graph gives us a much better idea of how safe Londoners are in poor weather conditions, and shows that Londoners are far less likely to rent a bike in wet conditions. This is a very welcome statistic, as in 2022, 68% of all bike crashes occurred in wet conditions like rain or ice. This is shown above in the pie chart labeled "Condition for Bike Crashes in London in 2022". For a rainy location such as London, this statistic perfectly displays what Londoners evidently aim to avoid.

# ### References

# Weather conditions in London in 2022
# - https://weather-and-climate.com/average-monthly-Rainy-days,London,United-Kingdom
# 
# 
# Bike accident weather conditions in 2022
# - https://road-safety.transport.ec.europa.eu/system/files/2022-03/FF_cyclists_20220209.pdf
# 
# 
