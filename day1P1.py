import pandas as pd

df = pd.read_csv('/Users/oliverrelph/Desktop/input.csv')
df = df.values.tolist()
df = [item for sublist in df for item in sublist]
vals = []
counter_part_one = 0
counter = 0
    
for x in range(0, len(df)):
    if x >= 2:
         
        add = df[x] + df[x-1] + df[x-2]
        vals.append(add)

for x in range(0,len(vals)):
    if x!=0:
        if vals[x] > vals[x-1]:
            counter+=1

for x in range(len(df)):
    if x!=0:
        if df[x] > df[x-1]:
            counter_part_one += 1
print(counter_part_one)
print(counter)
             
           