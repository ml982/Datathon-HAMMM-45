import pandas as pd


data = pd.read_csv('HomelessPeople.csv')
# cleaning up the database to make it easier to use 
data.columns = data.iloc[1]
data.drop(columns=['ONS code','MCHLG Spotlight (2022)', 'MCHLG Spotlight (2023)','CHAIN (2022/23)'], inplace=True)
data = data.rename(columns={'CHAIN (2023/24)' : 'homeless_people'})

def splitofmoney (x):
    
    #defining a and b, where a is no. of shelters and b is no. of food banks
    a,b=0.4,0.6

    weights = {
        'homeless_people': 0.6,
        'meanaffordability': 0.4,
        'noofshelters': a,
        'foodbanks': b
    }

    weightings = {
        data['homeless_people']*weights['homeless_people'],
        data['meanaffordability']*weights['meanaffordability']
    }
    
    #Calculating the total number of homeless people in total in London
    total_homeless_people = data['homeless_people'].sum()
    
    #Create a new column in data frame that has proportion of homeless ppl in each borough of the total number of homeless ppl
    data['Proportion that is homeless'] = (data['homeless_people'] / total_homeless_people) * 100
    
    
