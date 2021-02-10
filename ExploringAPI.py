# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 20:28:55 2021

@author: mdixon2

API Documentation: https://www.thecocktaildb.com/api.php
"""

import requests
import pprint
import pandas as pd
import string as s 

allDrinks = pd.DataFrame()

for letter in s.ascii_lowercase:

    #response = requests.get(f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita")
    response = requests.get(f"https://www.thecocktaildb.com/api/json/v1/1/search.php?f={letter}")
    jsonResponse = response.json()
    
    
    drinkResponse = jsonResponse['drinks']
    
    try:
        drinks = pd.json_normalize(drinkResponse, max_level=1)
    
        allDrinks = pd.concat([allDrinks, drinks])
    except: 
        pass





