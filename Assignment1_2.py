# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 11:31:23 2023

@author: aishw
"""

#importing library
import pandas as pd
import matplotlib.pyplot as plt

#read file into dataframe and print
df_diversity = pd.read_csv("Diversity.csv")
df_ethnicity = pd.DataFrame(df_diversity[df_diversity["Ethnicity"]=="Asian"], 
                           columns=["Ethnicity", 
                                    "Region"   , 
                                    "percentage of ethnic group"])
                        
print(df_ethnicity)

# Extract the region & percentage of ethnic group of the segments
region, per_ethnic = df_ethnicity["Region"],df_ethnicity["percentage of ethnic group"]
explode = (0, 0, 0.1, 0, 0, 0, 0, 0, 0, 0, 0)
         
# Pie Plot
plt.figure(figsize=(40,20))
plt.pie(per_ethnic, explode=explode, labels=region, startangle=45, autopct='%1.1f%%')

# set title and show the legend
plt.legend(region, title ="Region", borderpad=1, fontsize=11)
plt.title("Ethnicity Percentage of Asians in England and Wales Regions", fontsize=25)

# save as png
plt.savefig("Ethnicity_Percentage.png")

# show the plot
plt.show() 

