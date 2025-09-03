import pandas as pd
import numpy as np
fruits=["apple","banana","grape","kiwi","orange"]
for i in range(5):
    if (len(fruits[i])>=5):
        print(fruits[i])
for i in range(5):
    print("The fruit "+fruits[i]+" has "+str(len(fruits[i]))+" characters")