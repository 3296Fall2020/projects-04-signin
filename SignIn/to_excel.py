import pandas as pd
import numpy as np

df = pd.read_csv("data.txt", sep= ' ', names = ['Date', 'Time', 'Name', 'Office', 'Activity', 'Purpose'])

df.to_excel('SignInData.xlsx', 'Data', index = False)