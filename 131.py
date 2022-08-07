import plotly.express as px
import pandas as pd
name1=[]
import csv
with open("dwarf_stars.csv",'r+') as file:
  f1=csv.reader(file)
  for a  in f1:
    name1.append(a)
star_data=name1[1:]
gravity=[]
mass=[]
radius=[]
star_name=[]
for i in star_data:
  mass.append(star_data[3])
  radius.append(star_data[4])
  name1.append(star_data[1])

star_gravity=[]

for index,name in enumerate(star_name):
  g=(float(mass[index])) *6.17/100000000000/(float(radius[index]) * float(radius[index]) ) 
  print(g)
  #g=(float(mass[index])*6.17/1000) /(float(radius[index]) * float(radius[index]) ) 
  star_gravity.append(g)
  
  
file.to_csv("star_with_gravity.csv",index=False) 

