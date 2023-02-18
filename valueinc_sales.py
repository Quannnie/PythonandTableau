# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 15:34:45 2022

@author: Quang
"""
import pandas as pd

# file_name = pd.read_csv('file.csv') <------ format of read_csv

data = pd.read_csv('transaction.csv', sep = ';')

#sumary of the data

data.info() 

#working with calculations

#defiding variables
CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberofItemsPurchased = 6

#mathematical Operations on Tableau
ProfitPerItem = 21.11-11.73

ProfitPerItem = SellingPricePerItem - CostPerItem
ProfitPerTransaction = NumberofItemsPurchased*ProfitPerItem
CostPerTransaction = NumberofItemsPurchased*CostPerItem
SellingPricePerTransaction=NumberofItemsPurchased*NumberofItemsPurchased



# CostPerTransaction Calulation
# CostPerTransaction = NumberofItemsPurchased*CostPerItem
# Variable = dataframe['Column_name']
CostPerItem = data['CostPerItem']
# Data type of "ConstperItem" is "Series" that means 1 column in data frame
NumberOfItemsPurchased = data['NumberOfItemsPurchased']

#CostPerTransaction = CostPerItem *NumberOfItemsPurchased
## Creating a new column in data frame: data_frame['Name_of_new_column']
data['CostPerTransaction'] = CostPerItem * NumberOfItemsPurchased
'''
You can code like this
data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']
'''

#SellingPerTransaction = SellingPricePerItem *NumberOfItemsPurchased
data['SellingPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#ProfitPerTransaction = SellingPerTransaction - CostPerTransaction
data['ProfitPerTransaction'] = data['SellingPerTransaction'] - data['CostPerTransaction']

#Markup = ProfitPerTransaction /CostPerTransaction
data['Markup'] = data['ProfitPerTransaction'] / data['CostPerTransaction'] 



#using split to split the ClientKeywords field
#  new_var = column.str.split('sep' , expand = True)
split_col = data['ClientKeywords'].str.split(',' , expand = True)
## the result is a new dataframe


#Đưa cột mới vào DataFrame trước đó
data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthOfContract'] = split_col[2]


#using Replace function
#column = column.str.replce('what_you_wanna_replace','to_something')
data['ClientAge']=data['ClientAge'].str.replace('[','')
data['LengthOfContract'] = data['LengthOfContract'].str.replace(']','')

#using lower function to change ItemDescription into lowercase
data['ItemDescription'] = data['ItemDescription'].str.lower()

#merging
#open new dataframe
seasons = pd.read_csv('1.4 value_inc_seasons.csv', sep = ';')
#merging format = df= df.merge(df_old, df_new, on = 'key')
data = data.merge(data, seasons, on = 'Month')


#drop column

#drop 1 column
#data=data.drop('ClientKeywords', axis = 1)

#drop more 1 column
#data= data.drop (['Day','Month','Year'], axis = 1)

#export to csv

data.to_csv('Value_Inc_Cleaned1.csv', index = False)

# If there is some erros in your code, double click on this erros.
#It will take you to the line having erros and you can fix this.























