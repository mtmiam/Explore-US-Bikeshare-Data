#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import pandas as pd
import numpy as np
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
Cities = ['chicago','new york city','washington']
Months = ['all','january','february','march','april','may','june']
Days = ['all','sunday','monday','tuesday','wednesday','thursday','friday','saturday' ]


# In[2]:


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = input("What is the name of the city to analyze data? (chicago,new york city,washington).\n").lower()
    while (city not in CITY_DATA):
        print("Erorr,Please Enter a valid choice")
        city = input("What is the name of the city to analyze data? (chicago,new york city,washington).\n").lower()

        
    # get user input for month (all, january, february, ... , june)

    month = input('What is the name month that you want to analyze in it ? ([january, february,march,april,may,june] or enter all to not specify any month).\n').lower()
    while (month not in Months and month != 'all' ):
        print('please enter a valid choice')
        month = input('What is the name month that you want to analyze in it ? ([january, february,march,april,may,june] or enter all to not specify any month).\n').lower()
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("What is the name of the day to analyze data? ([sunday,monday,tuesday,wednesday,thursday,friday,saturday']or enter all to select no day).\n").lower()

    while (day not in Days and day != 'all'):
        print("Erorr,Please Enter a valid choice")
        day = input("What is the name of the day to analyze data? ([sunday,monday,tuesday,wednesday,thursday,friday,saturday']or enter all to select no day).\n").lower() 
    print('-'*40)
    return city, month, day
    


# In[3]:


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #Upload data for the selected city
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    #here
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    if month != 'all':
            month = Months.index(month)
            df = df.loc[df['month'] == month]
    if day != 'all':
         df = df.loc[df['day_of_week'] == day.title()]

    return df


# In[4]:


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print("The most common month from the given fitered data is: " + Months[common_month].title())

    # display the most common day of week
    The_common_day_of_week = df['day_of_week'].mode()[0]
    print("The most common day of week from the given fitered data is: " + The_common_day_of_week)

    # display the most common start hour
    The_common_start_hour = df['hour'].mode()[0]
    print("The most common start hour from the given fitered data is: " + str(The_common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[5]:


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station is: " + most_common_start_station)

    # display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station is: " + most_common_end_station)

    # display most frequent combination of start station and end station trip
    the_most_frequent_combination = df.groupby(['Start Station','End Station']).size().idxmax()
    print("The most frequent combination of start station and end station trip is : " + str(the_most_frequent_combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[6]:


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time  is: " + str(total_travel_time))

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time  is: " + str(mean_travel_time))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[7]:


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The count of user types is: \n" + str(user_types))

    # Display counts of gender
    if city != 'washington':
            Gender= df['Gender'].value_counts()
            print("The count of gender is: \n" + str(Gender))
    # Display earliest, most recent, and most common year of birth
            most_common_year_of_birth = df['Birth Year'].mode()[0]
            print('Most Common Year:',most_common_year_of_birth)
            most_recent_year_of_birth = df['Birth Year'].max()
            print('Most Recent Year:',most_recent_year_of_birth)
            earliest_year_of_birth = df['Birth Year'].min()
            print('Earliest Year:',earliest_year_of_birth)
    else:
          print("there is no available data for gender")



    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[8]:


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


# In[ ]:





# In[ ]:




