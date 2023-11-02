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
    while True:
        city = input("Please enter a city (Chicago, New York City, Washington): ").strip().lower()
        
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print("Invalid input. Please enter one of the specified cities.")
            
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Please enter a month (all, January, February, March, April, May, June): ").strip().lower()
        
        if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            break
        else:
            print("Invalid input. Please enter one of the specified months or 'all'.")
            
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Please enter a day of the week (all, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday):").strip().lower()
        
        if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            break
        else:
            print("Invalid input. Please enter one of the specified days of the week or 'all'.")

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
    # Load the data for the specified city into a Panda DataFrame named 'df'.
    df = pd.read_csv(CITY_DATA[city])
    
    # Convert the 'Date' column to a datetime object.
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # Extract month and day of week from Start Time to create new columns.
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['start hour'] = df['Start Time'].dt.hour
    
    # Filter by month if applicable.
    if month != "all":
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
        # Filter by month to create the new dataframe.    
        df = df[df['month'] == month]
        
    # Filter by day of the week.
    if day != "all":
        # Filter by day of the week to create a new dataframe.
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # TO DO: display the most common month
    most_common_month = df['month'].value_counts().idxmax()
    print("The most common month is:", most_common_month)
    
    # TO DO: display the most common day of week
    most_common_dow = df['day_of_week'].value_counts().idxmax()
    print("The most common day of the week is:", most_common_dow)
    
    # TO DO: display the most common start hour
    most_common_start_hour = df['start hour'].mode()[0]
    print("The most common start hour is:", most_common_start_hour)
                                
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].value_counts().idxmax()
    print("The most commonly used start station is:", most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].value_counts().idxmax()
    print("The most commonly used end station is:", most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    most_common_station_combination = (df['Start Station'] + " to " + df['End Station']).value_counts().idxmax()
    print("The most frequent station combination is:", most_common_station_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time for all trips:", total_travel_time, "seconds")

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time for all trips:", mean_travel_time, "seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_counts = df['User Type'].value_counts()
    print("Counts of user types:", user_type_counts)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print("Counts of gender:", gender_counts)
    else:
        print("Gender information is not available for this dataset.")

    # TO DO: Display earliest, most recent, and most common year of birth
    # TO DO: Display earliest, most recent, and most common year of birth (for Chicago and New York)
    if 'Birth Year' in df.columns:
        earliest_birth_year = df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max()
        most_common_birth_year = df['Birth Year'].mode().iloc[0]
    
        print("Earliest year of birth:", earliest_birth_year)
        print("Most recent year of birth:", most_recent_birth_year)
        print("Most common year of birth:", most_common_birth_year)
    else:
        print("Year of birth information is not available for this dataset.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
 

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        row_index = 0
        rows_to_display = 5
        
        while row_index < len(df):
            # Ask the user if they would like to see 5 lines of raw data.
            raw_data = input("Do you want to see 5 lines of raw data? (yes/no): ").strip().lower()
        
            if raw_data == 'yes':
                print(df[row_index:row_index + rows_to_display])
                row_index += rows_to_display
            else:
                break
            
        if row_index >= len(df):
            print("No more raw data to display.")
      
        else:
            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() != 'yes':
                break
if __name__ == "__main__":
	main()
