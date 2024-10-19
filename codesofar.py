import pandas as pd


homelessdata_df = pd.read_csv('HomelessPeople.csv')


def splitofmoney (x):
    
    a,b=0.4,0.6

    weights = {
        'homeless_people': 0.6,
        #'meanaffordability': 0.4,
        'noofshelters': a,
        'foodbanks': b
    }

    weightings = {
        data['homeless_people']*weights['homeless_people'],
        #data['meanaffordability']*weights['meanaffordability']
    }
    
    #Calculating the total number of homeless people in total in London
    total_homeless_people = data['homeless_people'].sum()
    
    #Create a new column in data frame that has proportion of homeless ppl in each borough of the total number of homeless ppl
    data['Proportion that is homeless'] = (data['homeless_people'] / total_homeless_people) * 100
    
    
