import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=input('which city you want to analyze: ').lower() 
    while city not in (CITY_DATA.keys()):
         print('invalid answer')
         city=input('which city you want:').lower()    
    # TO DO: get user input for month (all, january, february, ... , june)
    months=['january','february','june','may','march','april','all']
    month=input('which month you want to fillter with: ').lower() 
    while month not in months:
         print('no month to filter with')
         month=input('which month you want to fillter with: ').lower()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days=['monday','sunday','tuesday','friday','wednesday','thursday','saturday','all']
    day=input('which day to display: ').lower() 
    while day not in days:
         print('no day to display')
         day=input('which day to display: ').lower()   
    print('-'*40)
    return city, month, day


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
    df=pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months=['january','february','june','may','march','april','all']
    month=df['month'].mode()[0]
    print(f'the most common month is :{months[month-1]}')

    # TO DO: display the most common day of week
    days=['monday','sunday','tuesday','friday','wednesday','thursday','saturday','all']
    day=df['day_of_week'].mode()[0]
    print(f'most common day is : {day}')

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print(f'Most Popular Start Hour: {most_common_hour}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_station=df['Start Station'].mode()[0]
    print(f'the most common start station is :{most_common_station}')
    # TO DO: display most commonly used end station
    most_end_station=df['End Station'].mode()[0]
    print(f'the most end used station is; {most_end_station}')

    # TO DO: display most frequent combination of start station and end station trip
    frequent_trip=df['Start Station'] +'to'+df['End Station']
    print(f'the most frequent trip is:{frequent_trip.mode()[0]}')
                                              

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_duration=(pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])).sum()
    days=total_travel_duration.days
    hours=total_travel_duration.seconds //(60*60)
    minutes=total_travel_duration.seconds % (60*60)//60
    seconds=total_travel_duration.seconds %(60*60) %60
    print(f'total_travel_duration is :{days} days {hours} hours {minutes} minutes {seconds} seconds')
    # TO DO: display mean travel time
    mean_travel_time=(pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])).mean()
    days=mean_travel_time.days
    hours=mean_travel_time.seconds //(60*60)
    minutes=mean_travel_time.seconds % (60*60)//60
    seconds=mean_travel_time.seconds %(60*60) %60
    print(f'Mean travel time is : {days} days {hours} hours {minutes} minutes {seconds} seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())
    print('\n\n')

    # TO DO: Display counts of gender
    if 'gender' in (df.columns):
        print(df['gender'].value_counts())
        print('\n\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'brith day' in(df.columns):
        year=df['brith day'].fillna(0).astype(int64)
        print(f'earlist,most recent, most commmon is: {year.min():.0f}\ {year.max():.0f}\  {year.mode()[0]:.0f}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_raw_data(df):
    """if he want to raw data and print 5 rows at time."""
     
    raw = input('\nwould you like to dispaly raw data:\n').lower()
    if raw.lower() =='yes':
        count = 0
        while True:
            print(df.iloc[count:count+5])
            count+=5
            ask=input('next 5 raws?')
            if ask.lower() !='yes':
                break
                
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
