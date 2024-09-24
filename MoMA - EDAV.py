#!/usr/bin/env python
# coding: utf-8

# The Museum of Modern Art (MoMA) Collection - Exploratory Data Analysis and Visualization 

# In[ ]:


# Dataset Licensing: 

# Dataset from: The Museum of Modern Art (MoMA) Collection 
# Source: https://github.com/MuseumofModernArt/collection 
# License: CC0 1.0 Universal (Public Domain Dedication)


# In[3]:


# Work to do: 

# Check the missing values in all your columns. Pay attention that not all missing values will be NaNs. Make sure that non-nan values are valid.
# Check data type of all your columns and make sure they corresponde with what you expect them to be. 
# Dates should be of datetime format, numbers should be of either int or float.
# Plot distribution of numeric columns and histogram of categorical columns.
# Calculate and visualize top 5 nationalities of artists.
# Calculate and visualize top 5 nationalities of artists by gender.
# Merge two dataframes using ConstituentID as the key.
# Pick a nationality and filter the merged data to find all artworks done by artists of that nationality. How do you handle artworks that have multiple artists?
# Do one extra analysis of your data that picked your interest.


# In[5]:


# Dataset info: 

# Research dataset contains 156,633 records, representing all of the works that have been accessioned into MoMA’s collection and cataloged in our database. It includes basic metadata for each work, including:
# Title, artist, date made, medium, dimensions, and date acquired by the Museum. 

# Artists dataset contains 15,595 records, representing all the artists who have work in MoMA's collection and have been cataloged in our database. It includes basic metadata for each artist, including: 
# Artist name, nationality, gender, birth year, death year, Wiki QID, and Getty ULAN ID.


# In[7]:


get_ipython().system('pip install pandas')


# In[8]:


import pandas as pd


# In[15]:


# Load csv from computer 

path_artworks = '/Users/lenaivian/Downloads/Artworks-2.csv'
artworks = pd.read_csv(path_artworks)

path_artists = '/Users/lenaivian/Downloads/Artists-2.csv'
artists = pd.read_csv(path_artists)


# In[16]:


# Check column names

print(artworks.columns)
print(artists.columns)


# In[17]:


# Check datatypes

print(artworks.dtypes)
print(artists.dtypes)


# In[18]:


# Checking missing values in columns

artworks.isnull().sum()
artists.isnull().sum()


# In[ ]:


# Code only showed artists missing values ^


# In[19]:


artworks.isnull().sum()


# In[20]:


artists.isnull().sum()


# In[21]:


#Dates should be of datetime format

artists['BeginDate'] = pd.to_datetime(artists['BeginDate'], format='%Y', errors='coerce')
artists['EndDate'] = pd.to_datetime(artists['EndDate'], format='%Y', errors='coerce')

artworks['BeginDate'] = pd.to_datetime(artists['BeginDate'], format='%Y', errors='coerce')
artworks['EndDate'] = pd.to_datetime(artists['EndDate'], format='%Y', errors='coerce')


# In[22]:


print(artworks.head())


# In[24]:


print(artists.head())


# In[25]:


# Check datatypes

print(artworks.dtypes)
print(artists.dtypes)


# In[27]:


# Change ConstituentID in artists to be an int, similar to how it is in artworks

numeric_columns = ['ConstituentID']

# Apply pd.to_numeric to columns and change to int
artworks[numeric_columns] = artworks[numeric_columns].apply(pd.to_numeric, errors='coerce').astype('Int64')


# In[28]:


print(artworks.head())


# In[29]:


# Check datatypes

print(artworks.dtypes)
print(artists.dtypes)


# In[30]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[32]:


# Artworks dataset that contain floats

numeric_columns = ['Circumference (cm)','Depth (cm)', 'Diameter (cm)', 'Height (cm)', 'Length (cm)', 'Weight (kg)','Width (cm)', 'Seat Height (cm)','Duration (sec.)','ULAN' ]


# In[35]:


print(artworks.dtypes)


# In[37]:


# Artworks dataset that contain object for categorical columns

category_columns = ['Title','Nationality', 'Gender', 'Medium']


# In[ ]:




