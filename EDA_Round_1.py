###### ----------------- IMPORTS ----------------- ######
import pandas as pd
import matplotlib.pyplot as plt

###### ------------------------------------------- ######

# Read file in
drinks = pd.read_csv('drinks.csv')


# Drop multi-language support columns
dropColumns = ['strDrinkES', 'strDrinkFR', 'strDrinkZH-HANS', 'strDrinkZH-HANT', 'strInstructionsES', 'strInstructionsDE', 'strInstructionsFR', 'strInstructionsZH-HANS', 'strInstructionsZH-HANT', 'strDrinkDE']

for column in dropColumns :
    drinks.drop([column], axis=1, inplace=True)
    
########################################################################################## 
###### EDA Rabbit Hole # 1 -  Drink Complexity Based on Number of Ingredients ######
##########################################################################################

## Build dataframe of number of drinks requiring atleast the associated number of ingredients 
temp = []
for i in range(15) :
    
    # Convert zero start to one to match ingredient column name in dataframe
    ingredientNum = i + 1
    
    ingredient = f"strIngredient{ingredientNum}"
    numOfDrinks = drinks[ingredient].count()
    
    temp.append([ingredientNum,numOfDrinks ])
    
# Convert temp list into a dataframe
drinkIngredients = pd.DataFrame(temp, columns=["NumOfIngredients", "NumOfDrinks"])


## Add column denoting the number of drinks requiring exactly that number of ingredients 
drinkIngredients['NumofDrinks2'] = drinkIngredients['NumOfDrinks'] - drinkIngredients['NumOfDrinks'].shift(-1)


## Quick and dirty plot to show dataframe 
drinkIngredients.plot(kind='bar', x='NumOfIngredients', y=['NumOfDrinks','NumofDrinks2'] )
plt.legend(["# of Drinks Requiring Atleast x Ingredients", "# of Drinks Requiring Exactly x Ingredients"])

plt.show()

########################################################################################## 
###### EDA Rabbit Hole # 2 -  Most Popular Ingredients ######
##########################################################################################

topNumToShow = 20

## Build dataframe of number of drinks requiring that ingredient
ingredients = pd.DataFrame()
for i in range(15) :
    
    # Convert zero start to one to match ingredient column name in dataframe
    ingredientNum = i + 1
    
    # Ingredient column string 
    ingredient = f"strIngredient{ingredientNum}"

    # Ingredient count per ingredient column
    ingredientCounts = pd.DataFrame(drinks[ingredient].value_counts().reset_index())
    ingredientCounts.columns = ['ingredient','NumOfDrinks']
    
    # Add ingredient count per ingredient column to main ingredient dataframe
    ingredients = ingredients.append(ingredientCounts) 
   
# Calculate Final counts across all ingredient columns    
finalCountDrinksPerIngredient = ingredients.groupby('ingredient')[['NumOfDrinks']].agg(sum).reset_index()

            
# Quick and dirty plot to show dataframe (n largest values)
finalCountDrinksPerIngredient.nlargest(topNumToShow,'NumOfDrinks').plot(kind='bar', x='ingredient', y='NumOfDrinks' )


plt.show()






















    



