def convert_to_si(radius,mass): 
  for i in range(0,len(radius)-1): 
    radius[i] = radius[i]*6.957e+8 
    mass[i] = mass[i]*1.989e+30 

import plotly.express as px
import pandas as pd
name1=[]
import csv
f=pd.read_csv('total_stars.csv')
star_data=name1[1:]
gravity=[]
mass=f['Mass'].to_list()
radius =f['Radius'].to_list()
star_name=[]
for i in star_data:
  mass.append(star_data[3])
  radius.append(star_data[4])
  name1.append(star_data[1])

star_gravity=[]

for index,name in enumerate(star_name):
  g=convert_to_si(radius,mass)
  print(g)
  #g=(float(mass[index])*6.17/1000) /(float(radius[index]) * float(radius[index]) ) 
  star_gravity.append(g)
  
  
f.to_csv("star_with_gravity.csv",index=False) 
    