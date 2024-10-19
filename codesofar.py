import pandas as pd


data = pd.read_csv('.csv')

def splitofmoney (x):
    
    a,b=0.4,0.6

    weights = {
        'homeless_people': 0.6,
        'meanaffordability': 0.4,
        'noofshelters': a,
        'foodbanks': 0.6
    }

    weightings = {
        data['homeless_people']*weights['homeless_people'],
        data['meanaffordability']*weights['meanaffordability']
    }

