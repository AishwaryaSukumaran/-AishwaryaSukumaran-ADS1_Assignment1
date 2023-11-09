# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 10:35:22 2023

@author: aishw
"""
#importing library

import pandas as pd
import matplotlib.pyplot as plt
        
#read file into dataframe and print
df_UK = pd.read_excel("UK_rainfall.xlsx")
df_seasonal = pd.DataFrame(df_UK[(df_UK["year"]>=2000) & (df_UK["year"]<=2022)],
                           columns=["year", "win", "spr" , "sum", "aut" ])

#calculating max and min rainfall during the seasons over the years(2000-2022)
df_seasonal["max"] = df_seasonal[["win", "spr" , "sum", "aut"]].max(axis=1)
df_seasonal["min"] = df_seasonal[["win", "spr" , "sum", "aut"]].min(axis=1)

#renaming the columns
df_seasonal.rename(columns = {"year":"Year", 
                              "win":"Winter",
                              "spr":"Spring",
                              "sum":"Summer",
                              "aut":"Autumn",
                              "max":"Maximum_rainfall",
                              "min":"Minimum_rainfall"}, inplace=True)

print(df_seasonal)

#line plots
plt.figure(figsize=(30,8))

# plot the max and min rainfall during seasons with lables and customising visualization
plt.subplot(1, 2, 1)
plt.plot(df_seasonal["Year"], df_seasonal["Maximum_rainfall"], marker="o", label="Maximum rainfall", color="green")
plt.plot(df_seasonal["Year"], df_seasonal["Minimum_rainfall"], marker="o", label="Minimum rainfall", color="red")

# set title & label and show the legend for lineplot1
plt.legend(title ="Max and Min rainfall", borderpad=0.5, fontsize=9)
plt.title("Max and Min seasonal rainfall in UK")
plt.xlabel("Years") 
plt.ylabel("Rainfall precipitation in millimetres (mm)") 
plt.xticks(df_seasonal["Year"])

# plot the four seasons with lables and customising visualization
plt.subplot(1, 2, 2)
plt.plot(df_seasonal["Year"], df_seasonal["Winter"], label="winter", color="green")
plt.plot(df_seasonal["Year"], df_seasonal["Spring"], label="spring", color="red")
plt.plot(df_seasonal["Year"], df_seasonal["Summer"], label="summer", color="orange")
plt.plot(df_seasonal["Year"], df_seasonal["Autumn"], label="autumn", color="brown")

# set title & label and show the legend for lineplot2
plt.legend(title ="Sesonal Rainfall", borderpad=0.5, fontsize=9)
plt.title("Seasonal rainfall in UK")
plt.xlabel("Years") 
plt.ylabel("Rainfall precipitation in millimetres (mm)") 
plt.xticks(df_seasonal["Year"])

# save as png
plt.savefig("UK_seasonal_rainfall.png")

# show the plot
plt.show() 

