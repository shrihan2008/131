

import plotly.express as px
import pandas as pd
name1=[]
import csv
f=pd.read_csv('total_stars.csv')
star_data=name1[1:]
gravity=[]
mass=f['Mass'].to_list()
radius =f['Radius'].to_list()
for i in range(0,len(radius)-1): 
    radius[i] = radius[i]*6.957e+8 
    mass[i] = mass[i]*1.989e+30 


star_name=[]
for i in star_data:
  mass.append(star_data[3])
  radius.append(star_data[4])
  name1.append(star_data[1])

star_gravity=[]

for index,name in enumerate(star_name):
  g=(float(gravity))*float(mass)/float(radius**2)
  print(g)
  star_gravity.append(g)

print(len(star_gravity))
  
  
f.to_csv("star_with_gravity.csv",index=False) 
    