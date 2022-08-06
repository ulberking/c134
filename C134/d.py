import pandas as pd
df=pd.read_csv('calculated.csv')
name=df['Name'].tolist()
radius = df['Radius'].tolist()
mass=df['Mass'].tolist()
G=df['Gravity'].tolist()
distance = df['Distance'].tolist()
new_name = []
new_radius = []
new_mass = []
new_gravity = []
new_distance = []
for i in range(0,25):
  d=float(distance[i])
  if(G[i]>=150 and G[i]<=350 and d<=100):
    new_gravity.append(G[i])
    new_radius.append(radius[i])
    new_mass.append(mass[i])
    new_name.append(name[i])
    new_distance.append(distance[i])
new_df=pd.DataFrame({'Name':new_name,'Radius':new_radius,'Mass':new_mass,'Gravity':new_gravity,'Distance':new_distance})
new_df.to_csv('filter.csv')