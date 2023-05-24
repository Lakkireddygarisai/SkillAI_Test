# Create a python code using Pandas to filter a dataset CSV file and group the results to find the most cities with Male population.

"""City,Gender,Population
New York,Male,4125000
New York,Female,4300000
Los Angeles,Male,1985000
Los Angeles,Female,2070000
Chicago,Male,1350000
Chicago,Female,1400000
Houston,Male,1100000
Houston,Female,1120000
Phoenix,Male,800000
Phoenix,Female,810000
Philadelphia,Male,750000
Philadelphia,Female,770000"""

import pandas as pd





def get_highest_male_population(df):

    
    #print(df)

    total_data= df

    only_Male  = df[df['Gender']=='Male']
    #print(only_Male)

    heighest_pop_city = only_Male['Population '].max()

    get_city_and_pop = df[df['Population ']== heighest_pop_city]

    return(get_city_and_pop)

df = pd.read_csv('Book1.csv')
print(get_highest_male_population(df))

