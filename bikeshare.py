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
    city = input("Would you like to see data for Chicago, New York city, or Washington?\n")
    while True:
        if city.lower() == "washington":
          print("Looks like you want to hear about Washington! If this is not true, restart the program now!")
          break
        if city.lower() == "chicago":
          print("Looks like you want to hear about Chicago! If this is not true, restart the program now!")
          break
        if city.lower() == "new york city":
          print("Looks like you want to hear about New York City! If this is not true, restart the program now!")
          break
        else:
          city = input("Invalid input. Would you like to see data for Chicago, New York, or Washington?\n")
    print()
    print()
    # TO DO: prompt user to input month (all, january, february, ... , june) till expected input is received
    day_or_month = input('Would you like to filter the data by month, day, or not at all? Type "none" for no time filter\n')
    while True:
        if day_or_month.lower() == "month":
          print("We will make sure to filter by month!")
          break
        elif day_or_month.lower() == "day":
          print("We will make sure to filter by day!")
          break
        elif day_or_month.lower() == "none":
          print("No time filter")
          break
        else:
          day_or_month = input('Invalid input. Would you like to filter the data by month, day, or not at all? Type "none" for no time filter\n')
    print()
    print()
    if day_or_month == "month":
      month = input('Which month? January, February, March, April, May, or June? Please type out the full month name.\n')
      while True:
        if month.lower() == "january":
          month = "january"
          break
        elif month.lower() == "february":
          month = "february"
          break
        elif month.lower() == "march":
          month = "march"
          break
        elif month.lower() == "april":
          month = "april"
          break
        elif month.lower() == "may":
          month = "may"
          break
        elif month.lower() == "june":
          month = "june"
          break
        else:
          month = input('Invalid input. Which month? January, February, March, April, May, or June? Please type out the full month name.\n')
      day = "all"
    print()
    print()
    # TO DO: prompt user to input for day of week (all, monday, tuesday, ... sunday) till expected input is received
    if day_or_month == "day":
      day = input('Which day? Please type a day M, Tu, W, Th, F, Sa, Su.\n')
      while True:
        if day.lower() == "m":
          day = "monday"
          break
        elif day.lower() == "tu":
          day = "tuesday"
          break
        elif day.lower() == "w":
          day = "wednesday"
          break
        elif day.lower() == "th":
          day = "thursday"
          break
        elif day.lower() == "f":
          day = "friday"
          break
        elif day.lower() == "sa":
          day = "saturday"
          break
        elif day.lower() == "su":
          day = "sunday"
          break
        else:
          day = input('Invalid input. Which day? Please type a day M, Tu, W, Th, F, Sa, Su.\n')
      month = "all"
    print()
    print()
    if day_or_month == "none":
      month = "all"
      day = "all"
    print()
    print()


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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
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

    print('\nCalculating The Most Frequent Times of Travel...')
    start_time = time.time()
    print()
    print()

    # TO DO: display the most common month
    print("Displaying the most common month for travel")
    print(df['month'].mode()[0])
    
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print()
    print()
    
    
    start_time = time.time()
    # TO DO: display the most common day of week
    print("Displaying the most common day of week for travel")
    print(df['day_of_week'].mode()[0])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print()
    print()
    
    
    
    start_time = time.time()
    # TO DO: display the most common start hour
    print("Displaying the most common start hour for travel")
    
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    
    # find the most common hour (from 0 to 23)
    popular_hour = df['hour'].mode()[0]
    print(popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print()
    print()
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    print()
    print()

    # TO DO: display most commonly used start station
    print("Which start station is most commonly used?")
    print(df['Start Station'].mode()[0])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print()
    print()


    # TO DO: display most commonly used end station
    start_time = time.time()
    print("Which end station is most commonly used?")
    print(df['End Station'].mode()[0])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print()
    print()


    # TO DO: display most frequent combination of start station and end station trip
    start_time = time.time()
    print("The most frequent combination of start station and end station trip is:")
    df = df.groupby(['Start Station','End Station']).size().reset_index().rename(columns={0:'count'})
    df = df[df['count'] == df['count'].max()]
    print(df.to_string(index=False))
    #print(df.loc[1:])
    #df[df["Courses"] == 'Spark']

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print()
    print()
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("The total travel time in seconds is:")
    print(df['Trip Duration'].sum())
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print()
    print()


    # TO DO: display mean travel time
    start_time = time.time()
    print("The average travel time is:")
    print(df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print()
    print()

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Here's the breakup of bikeshare user types:")
    print(df['User Type'].value_counts())
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print()
    print()

    # TO DO: Display counts of gender
    start_time = time.time()
    if 'Gender' in df.columns:
        print("Here's the available counts of gender:")
        print(df['Gender'].value_counts())
    else:
        print("No gender data to share.")
        print()
        print()
    
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print()
    print()
    
    # TO DO: Display earliest, most recent, and most common year of birth
    start_time = time.time()
    if 'Birth Year' in df.columns:
        print("The earliest year of birth is:")
        print(df['Birth Year'].min())
        print()
        print()
        print("The most recent year of birth is:")
        print(df['Birth Year'].max())
        print()
        print()
        print("The most common year of birth is:")
        print(df['Birth Year'].mode()[0])
        print()
        print()
    else:
        print("No birth year data to share.")
        print()
        print()


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print()
    print()

def raw_data(df):
    raw_data = input('Would you like to see raw data 5 lines at a time? Type "yes" or "no"\n')
    while True:
        if raw_data.lower() == "yes":
            break
        if raw_data.lower() == "no":
            break
        else:
            raw_data = input('Invalid input. Would you like to see raw data 5 lines at a time? Type "yes" or "no"\n')
    rows = df.shape[0]
    start_row = 0
    end_row = 5
    while True:
        if raw_data == "yes":
            if end_row < rows:
                print(df[start_row:end_row].to_string(index=False))
            if end_row > rows:
                break
            if raw_data == 'no':
                break
            else:
                raw_data = input('Would you like to see the next 5 lines of raw data? Type "yes" or "no"\n')
                while True:
                    if raw_data.lower() == "yes":
                        break
                    if raw_data.lower() == "no":
                        break
                    else:
                        raw_data = input('Invalid input. Would you like to see the next 5 lines of raw data? Type "yes" or "no"\n')
        else:
            break
                
        start_row += 5
        end_row += 5
    print()
    print()    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
