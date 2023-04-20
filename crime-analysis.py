#!/usr/bin/env python
# coding: utf-8

# # Crime Analysis

# In[1]:


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))


# 

# In[2]:


import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
#get_ipython().run_line_magic('matplotlib', 'inline')
import warnings
warnings.filterwarnings('ignore')
from plotly.offline import download_plotlyjs, init_notebook_mode , plot,iplot
import plotly.express as px
import plotly.graph_objects as go
from plotly.colors import n_colors
from plotly.subplots import make_subplots
init_notebook_mode(connected=True)
import cufflinks as cf
cf.go_offline()


# In[49]:


victims = pd.read_csv('../input/crime-in-india/20_Victims_of_rape.csv')
police_hr = pd.read_csv('../input/crime-in-india/35_Human_rights_violation_by_police.csv')
auto_theft = pd.read_csv('../input/crime-in-india/30_Auto_theft.csv')
prop_theft = pd.read_csv('../input/crime-in-india/10_Property_stolen_and_recovered.csv')
shp_gdf = gpd.read_file('../input/india-gis-data/India States/Indian_states.shp')


# In[5]:


victims.head()


# In[6]:


rape_victims= victims[victims['Subgroup']=='Victims of Incest Rape']


# In[7]:


rape_victims.head()


# In[8]:


g= pd.DataFrame(rape_victims.groupby(['Year'])['Rape_Cases_Reported'].sum().reset_index())


# In[9]:


g.head()


# In[10]:


g.columns=['Year','Cases Reported']


# In[11]:


g.columns


# In[12]:


g


# In[13]:


fig= px.bar(g,x='Year',y='Cases Reported',color_discrete_sequence=['blue'])
fig.show()


# In[14]:


g1= pd.DataFrame(rape_victims.groupby(['Area_Name'])['Rape_Cases_Reported'].sum().reset_index())


# In[48]:


g1.head()


# In[16]:


g1.columns=['State/UT','Cases Reported']


# In[17]:


g1.columns


# In[18]:


g1.replace(to_replace='Arunachal Pradesh',value='Arunanchal Pradesh',inplace=True)


# In[19]:


g1


# In[21]:


shp_gdf


# In[22]:


merge =shp_gdf.set_index('st_nm').join(g1.set_index('State/UT'))


# In[23]:


merge


# In[24]:


fig,ax=plt.subplots(1, figsize=(10,10))

ax.set_title('State-wise Rape-Cases Reported (2001-2010)',
             fontdict={'fontsize': '15', 'fontweight' : '3'})
fig = merge.plot(column='Cases Reported', cmap='Reds', linewidth=0.5, ax=ax, edgecolor='0.2',legend=True)


# 

# In[26]:


above_50 = rape_victims['Victims_Above_50_Yrs'].sum()
ten_to_14 = rape_victims['Victims_Between_10-14_Yrs'].sum()
fourteen_to_18 = rape_victims['Victims_Between_14-18_Yrs'].sum()
eighteen_to_30 = rape_victims['Victims_Between_18-30_Yrs'].sum()
thirty_to_50 = rape_victims['Victims_Between_30-50_Yrs'].sum()
upto_10 = rape_victims['Victims_Upto_10_Yrs'].sum()


# In[27]:


age_grp = ['Upto 10','10 to 14','14 to 18','18 to 30','30 to 50','Above 50']
age_group_vals = [upto_10,ten_to_14,fourteen_to_18,eighteen_to_30,thirty_to_50,above_50]

fig = go.Figure(data=[go.Pie(labels=age_grp, values=age_group_vals,sort=True,
                            marker=dict(colors=px.colors.qualitative.G10),textfont_size=12)])

fig.show()


# In[28]:


g2= pd.DataFrame(police_hr.groupby(['Area_Name'])['Cases_Registered_under_Human_Rights_Violations'].sum().reset_index())


# In[29]:


g2.columns= ['State/UT','Cases Reported']


# In[47]:


g2.head()


# In[31]:


g2.replace(to_replace='Arunachal Pradesh',value='Arunanchal Pradesh',inplace=True)

shp_gdf = gpd.read_file('../input/india-gis-data/India States/Indian_states.shp')
merged = shp_gdf.set_index('st_nm').join(g2.set_index('State/UT'))


# In[32]:


shp_gdf


# In[33]:


fig, ax = plt.subplots(1, figsize=(10, 10))
ax.axis('off')
ax.set_title('State-wise Property Stolen-Cases Reported',
             fontdict={'fontsize': '15', 'fontweight' : '3'})
fig = merged.plot(column='Cases Reported', cmap='RdPu', linewidth=0.5, ax=ax, edgecolor='0.2',legend=True)


# In[34]:


g3 = pd.DataFrame(police_hr.groupby(['Year'])['Cases_Registered_under_Human_Rights_Violations'].sum().reset_index())
g3.columns = ['Year','Cases Registered']

fig = px.bar(g3,x='Year',y='Cases Registered',color_discrete_sequence=['black'])
fig.show()


# In[35]:


police_hr.Group_Name.value_counts()


# In[36]:


fake_enc_df = police_hr[police_hr['Group_Name']=='HR_Fake encounter killings'] 
fake_enc_df.Cases_Registered_under_Human_Rights_Violations.sum()


# In[37]:


false_imp_df = police_hr[police_hr['Group_Name']=='HR_False implication'] 
false_imp_df.Cases_Registered_under_Human_Rights_Violations.sum()


# In[38]:


g4 = pd.DataFrame(police_hr.groupby(['Year'])['Policemen_Chargesheeted','Policemen_Convicted'].sum().reset_index())


# In[39]:


g4


# In[40]:



year=['2001','2002','2003','2004','2005','2006','2007','2008','2009','2010']

fig = go.Figure(data=[
    go.Bar(name='Policemen Chargesheeted', x=year, y=g4['Policemen_Chargesheeted'],
           marker_color='purple'),
    go.Bar(name='Policemen Convicted', x=year, y=g4['Policemen_Convicted'],
          marker_color='red')
])

fig.update_layout(barmode='group',xaxis_title='Year',yaxis_title='Number of policemen')
fig.show()


# In[41]:


g5 = pd.DataFrame(auto_theft.groupby(['Area_Name'])['Auto_Theft_Stolen'].sum().reset_index())
g5.columns = ['State/UT','Vehicle_Stolen']
g5.replace(to_replace='Arunachal Pradesh',value='Arunanchal Pradesh',inplace=True)

shp_gdf = gpd.read_file('../input/india-gis-data/India States/Indian_states.shp')
merged = shp_gdf.set_index('st_nm').join(g5.set_index('State/UT'))

fig, ax = plt.subplots(1, figsize=(10, 10))
ax.axis('off')
ax.set_title('State-wise Auto Theft Cases Reported(2001-2010)',
             fontdict={'fontsize': '15', 'fontweight' : '3'})
fig = merged.plot(column='Vehicle_Stolen', cmap='YlOrBr', linewidth=0.5, ax=ax, edgecolor='0.2',legend=True)


# In[42]:


auto_theft_traced = auto_theft['Auto_Theft_Coordinated/Traced'].sum()
auto_theft_recovered = auto_theft['Auto_Theft_Recovered'].sum()
auto_theft_stolen = auto_theft['Auto_Theft_Stolen'].sum()

vehicle_group = ['Vehicles Stolen','Vehicles Traced','Vehicles Recovered']
vehicle_vals = [auto_theft_stolen,auto_theft_traced,auto_theft_recovered]

colors = ['hotpink','purple','red']

fig = go.Figure(data=[go.Pie(labels=vehicle_group, values=vehicle_vals,sort=False,
                            marker=dict(colors=colors),textfont_size=12)])

fig.show()


# In[43]:


g5 = pd.DataFrame(auto_theft.groupby(['Year'])['Auto_Theft_Stolen'].sum().reset_index())

g5.columns = ['Year','Vehicles Stolen']

fig = px.bar(g5,x='Year',y='Vehicles Stolen',color_discrete_sequence=['#00CC96'])
fig.show()


# In[44]:


vehicle_list = ['Motor Cycles/ Scooters','Motor Car/Taxi/Jeep','Buses',
               'Goods carrying vehicles (Trucks/Tempo etc)','Other Motor vehicles']

sr_no = [1,2,3,4,5]

fig = go.Figure(data=[go.Table(header=dict(values=['Sr No','Vehicle type'],
                                          fill_color='turquoise',
                                           height=30),
                 cells=dict(values=[sr_no,vehicle_list],
                            height=30))
                     ])
fig.show()


# In[45]:


motor_c = auto_theft[auto_theft['Sub_Group_Name']=='1. Motor Cycles/ Scooters']

g8 = pd.DataFrame(motor_c.groupby(['Area_Name'])['Auto_Theft_Stolen'].sum().reset_index())
g8_sorted = g8.sort_values(['Auto_Theft_Stolen'],ascending=True)
fig = px.scatter(g8_sorted.iloc[-10:,:], y='Area_Name', x='Auto_Theft_Stolen',
             orientation='h',color_discrete_sequence=["red"])
fig.show()


# In[46]:


g7 = pd.DataFrame(prop_theft.groupby(['Area_Name'])['Cases_Property_Stolen'].sum().reset_index())
g7.columns = ['State/UT','Cases Reported']
g7.replace(to_replace='Arunachal Pradesh',value='Arunanchal Pradesh',inplace=True)

shp_gdf = gpd.read_file('../input/india-gis-data/India States/Indian_states.shp')
merged = shp_gdf.set_index('st_nm').join(g7.set_index('State/UT'))

fig, ax = plt.subplots(1, figsize=(10, 10))
ax.axis('off')
ax.set_title('State-wise Property Stolen-Cases Reported',
             fontdict={'fontsize': '15', 'fontweight' : '3'})
fig = merged.plot(column='Cases Reported', cmap='spring', linewidth=0.5, ax=ax, edgecolor='0.2',legend=True)

