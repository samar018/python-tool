# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 02:08:31 2019
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html
https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
https://www.geeksforgeeks.org/reading-writing-text-files-python/
https://www.digitalocean.com/community/tutorials/how-to-construct-for-loops-in-python-3
https://www.shanelynn.ie/select-pandas-dataframe-rows-and-columns-using-iloc-loc-and-ix/
https://www.shanelynn.ie/select-pandas-dataframe-rows-and-columns-using-iloc-loc-and-ix/#ix-selection
https://data36.com/python-nested-loops-if-statements-combined-data-sciene/
https://stackoverflow.com/questions/33686747/save-a-list-to-a-txt-file/33686762
@author: samar
"""

import pandas as pd
#xlsx = pd.read_excel('Database.xlsx', sheetname=0,index_col=0,header=0,skiprows=0,na_values=0,mangle_dupe_cols=1)  
#"""nrows=0(to parse the rows)
#
#dtype={'Name': str, 'Value': float}
#na_values=['string1', 'string2']
#"""
##
#print(xlsx.head())
#
##with open(“hello.txt”, “w”) as f: 
##f.write(“Hello World”)
#
#    
#    
    
    
 

dataset = pd.read_excel('Database.xlsx')
X = dataset.iloc[:, 3].values
y = dataset.iloc[:,12].values

##print(X.shape)
##print(y.shape)
##print(X.shape[0] != y.shape[0])
##
print(dataset.head())
print(X[4])

#print(y)


#'''make necessary changes in the dataframe'''


#   print(email)
with open("Database.txt","w") as f: 
     for email in X :
        if email !='nan': 
           f.write(str(email) + '\n')
         else:
          continue:
with open("Database.txt","r") as file: 
        print(file.read()) 
 