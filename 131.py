import plotly.express as px

name=[]
import csv
with open("merged1.csv",'r') as f:
  f1=csv.reader(f)
  for a  in f1:
    name.append(a)

gravity=[]
  
mass=[]
radius=[]
name=[]
for index,name in enumerate(name):
  g=(float(mass[index]) * 5.972e+24)/(float(radius[index]) * float(radius[index]) * (6371000**2)) *6.674e-11
  gravity.append(g) 

fig=px.scatter(x=radius,y=mass,size=gravity,hover_data=[name])
fig.show()