import plotly.express as px

name=[]
import csv
with open("dwarf_stars.csv",'r') as f:
  f1=csv.reader(f)
  for a  in f1:
    name.append(a)
star_data=name[1:]
gravity=[]
mass=[]
radius=[]
name=[]
for i in star_data:
  mass.append(i[3])
  radius.apeend(i[4])
  name.append(i[1])

for index,name in enumerate(name):
  g=(float(mass[index])) *6.17/100000000000/(float(radius[index]) * float(radius[index]) ) 
  gravity.append(g) 

