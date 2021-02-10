###### ----------------- IMPORTS ----------------- ######
import requests
import pandas as pd
import string as s 

###### ------------------------------------------- ######


### Blank DataFrame initialized to be used later in loop ###
allDrinks = pd.DataFrame()

### Loop throw all letters of the alphabet to be used when calling endpoint
for letter in s.ascii_lowercase:

    # Call Endpoint with current letter and convert response to JSON object
    response = requests.get(f"https://www.thecocktaildb.com/api/json/v1/1/search.php?f={letter}")
    jsonResponse = response.json()
    
    # Pull out the list of drinks
    drinkResponse = jsonResponse['drinks']
    
    # Error handling in case reponse for letter yields no drinks
    try:
        # Flatten all objects in the drinks array and save to temporary dataframe
        drinks = pd.json_normalize(drinkResponse, max_level=1)
    
        # Concatenate temporary dataframe and main dataframe
        allDrinks = pd.concat([allDrinks, drinks])
        
    except: 
        pass





