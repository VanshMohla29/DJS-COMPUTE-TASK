import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("ufc-fighters-statistics.csv")
df.info()  #seeing the columns of the dataframe to analyze redundant cols
df.drop(labels=["nickname","date_of_birth"],axis=1,inplace=True) #dropping redundant cols to clean data
print(df.isna().sum())  #checking cols with nan values to fill with mean values
for i in ['height_cm', 'reach_in_cm', 'weight_in_kg']:  #filling nan values in required columns with means
    df[i]=df[i].fillna(df[i].mean())
for j in ["stance"]:
    df[j]=df[j].fillna("Switch")
print(df.isna().sum()) 

plt.hist(df["wins"],bins=50,label="Wins")
plt.title("Trend in wins and losses")
plt.hist(df["losses"],bins=50,label="Losses")
plt.xlabel("No. of Wins/Losses")
plt.ylabel("No. of Fighters")
plt.legend(loc=1)
plt.show()
plt.scatter(df["weight_in_kg"],df["height_cm"])
plt.title("Height vs Weight Ratio of fighters")
plt.xlabel("Weight")
plt.ylabel("Height")
plt.show()
plt.scatter(df["average_submissions_attempted_per_15_minutes"],df["wins"],s=12,label="Jiu Jitsu Base")
plt.scatter(df["average_takedowns_landed_per_15_minutes"],df["wins"],s=8,label="Wrestling Base")
plt.scatter(df["significant_strikes_landed_per_minute"],df["wins"],s=4,label="Striking Base")
plt.legend(loc=1)
plt.xlabel("No. of Submissions/Takedowns/Strikes")
plt.ylabel("Wins")
plt.title("Jiu Jitsu vs Wrestling vs Striking WIN Ratio")
plt.show()
plt.hist(df["significant_strikes_absorbed_per_minute"],bins=50,label="Absorbed")
plt.hist(df["significant_strikes_landed_per_minute"],bins=50,label="Landed")
plt.legend(loc=1)
plt.show()
plt.scatter([df["takedown_accuracy"]],df["wins"])
plt.title("Takedown Accuracy vs Wins")
plt.xlabel("Takedown Accuracy")
plt.ylabel("Wins")
plt.show()


