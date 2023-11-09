# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 12:11:00 2023

@author: aishw
"""
#importing library
import pandas as pd
import matplotlib.pyplot as plt


        
#read file into dataframe and print
df_UK = pd.read_excel("UK_rainfall.xlsx")
df_yearly = pd.DataFrame(df_UK[(df_UK["year"]>=2000) & (df_UK["year"]<=2022)],
                         columns=["year", "jan", "feb", 
                                  "mar", "apr", "may", 
                                  "jun", "jul", "aug", 
                                  "sep", "oct", "nov", "dec"])

#calculating average per year
df_yearly["Avg"] = df_yearly[["jan", "feb", "mar", 
                              "apr", "may", "jun", 
                              "jul", "aug", "sep", 
                              "oct", "nov", "dec"]].mean(axis=1)

#renaming the columns
df_yearly.rename(columns = {"year":"Year",
                            "jan":"January", 
                            "feb":"February",
                            "mar":"March",
                            "apr":"April",
                            "may":"May",
                            "jun":"June",
                            "jul":"July",
                            "aug":"August",
                            "sep":"September",
                            "oct":"October",
                            "nov":"November",
                            "dec":"December",
                            "Avg":"Average"}, inplace=True)
print(df_yearly)

# Bar Plot
plt.figure(figsize=(20,8))

#plt.bar(region,population, label = "region")
plt.bar(df_yearly["Year"], df_yearly["Average"])

# set title 
plt.title("Average precipitation of rainfall per years(2000 - 2022)", fontweight='bold', fontsize=10)

# show the legend
plt.legend(df_yearly["Year"], title="Max Average rainfall", borderpad=1, fontsize=11)

#set labels in X-axis and y-axis
plt.xlabel("years (200-2022)", fontweight='bold', fontsize=13) 
plt.ylabel("Rainfall precipitation in (mm)", fontweight='bold', fontsize=13)
plt.xticks(df_yearly["Year"])

# save as png
plt.savefig("Average rainfall per year.png")

# show the plot
plt.show() 


