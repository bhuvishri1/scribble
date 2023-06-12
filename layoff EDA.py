#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Now we are going to analyse the BELOW DATASET  and come up with an insight 
#of how the countries are affected with the layoffs 
#And what are the industries that are highly affected.  


# In[39]:


get_ipython().system('pip install matplotlib')
get_ipython().system('pip install seaborn')


# In[2]:


#importing important libraries for DATA ANALYSIS and DATA VISUALIZATION
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


#DATA ANALYSIS
df=pd.read_csv("C:/Users/Home/Downloads/archive.zip")
df.head()  #gives sample of 5 datas


# In[4]:


df.shape


# In[5]:


df.info()


# In[5]:


df.isnull().sum()


# In[6]:


df.describe()


# In[6]:


df["industry"].unique()   #we can see the list of industries that laidoff people due to recession


# In[10]:


#HANDLING MISSING VALUES
#Because of the null values present in the dataset the data is skewed here. 
#with skewed data we cannot get proper information so i am replacing the null values.
#Since the value in total_laid_off column and percentage_laid_off column is unique and important for our analysis we cannot remove that column
#so replacing it with zeroes

df1 = df.fillna({'total_laid_off':0,
                 'percentage_laid_off':0,
                 'industry':0,
                 'stage':0,
                'funds_raised':0,
                 'date':0})



# In[9]:


df1.isnull().sum()


# In[11]:


df1.head()


# In[ ]:


#top tech companies that laid off people


# In[12]:


top_companies = df1.nlargest(10,["total_laid_off"])
print(top_companies)

#from the chart its clear that google ,meta,microsoft,amazon are the companies with major layoffs


# In[11]:


plt.figure(figsize=(8,5))
sns.barplot(x=top_companies.company,y=top_companies.total_laid_off,color="green",alpha=1)
plt.title("LAY-OFF IN TOP COMPANIES")
plt.xlabel("COMPANIES")
plt.ylabel("NO of LAYOFFS")
plt.show()


# In[13]:


#checking the sectors that are mostly affected by layoff
industries=df1.groupby("industry")
industries


# In[50]:


len(industries)


# In[51]:


len(df1) # since the dataframes have varying row length we didnt get result


# In[15]:


industries.size().sort_values(ascending=False) #displays each industry with total no of companies


# In[71]:


#industries.last()


# In[17]:


#industries.groups #--------> gives the group of industries in dictionary with values as list of rows
#df1.iloc[951,:]    --------> locate the 951 st row with all columns


# In[59]:


#industries.get_group("Marketing") -------> gives the list of companies in marketing industries


# In[44]:


df1.groupby("industry")["total_laid_off"].sum().sort_values(ascending=False).plot(kind="bar")
plt.figure(figsize=(7,5))
plt.bar(sector,industries, color="#ed8e11",alpha=1)
plt.title("LAY OFF BY SECTORS")
plt.xlabel("SECTORS")
plt.ylabel("NO OF LAYOFFs")
plt.show()


# In[43]:


df1["country"].unique()


# In[18]:


# checking the first five countries that are affected by layoffs
countries = df1.groupby("country")["total_laid_off"].sum().sort_values(ascending=False)
countries


# In[19]:


#countries that are affected by layoffs
countries = np.array(df1.groupby("country")["total_laid_off"].sum().sort_values(ascending=False).head())
layoff = ["United States","India","Netherlands","Germany","Sweden"]
color = ["#ffcf24","#f0ff1c","#7bff1c","#28fcfc","#e028fc"]
plt.pie(countries,colors = color, labels = layoff)
plt.title("LAY OFF BY COUNTRIES")
plt.show()


# In[23]:


''' United states tops the chart of mostly affected countries,followed by india,netherlands,germany,and sweden'''


# In[20]:


#LOCATION with most no of layoffs
location = df1.groupby("location")["total_laid_off"].sum().sort_values(ascending=False).head()
location


# In[26]:


location = df1.groupby("location")["total_laid_off"].sum().sort_values(ascending=False).head()
layoff_cities = ["SF Bay Area","Seattle","New York City","Bengaluru","Amsterdam"]
sns.barplot(x = location, y = layoff_cities)
plt.title("LOCATION with most no of layoffs")


# In[ ]:


#San Fransisco Bay area has been mostly affected by layoffs


# In[21]:


df1["date"] = pd.to_datetime(df1["date"])
df1["date"]


# In[23]:


#To get more insight about the data we'll split the date column and lets check on which years the layoffs have happend

df2 = df1.copy()

df2["year"] = df2["date"].dt.year
df2["month"] = df2["date"].dt.month
df2["day"] = df2["date"].dt.day
df2



# In[25]:


#df2.drop(columns=["date"])
#df2


# In[20]:


df2["year"].unique()


# In[65]:


#comparison of layoff in previous years
df2["year"].value_counts(sort=True)



# In[62]:


sns.catplot(x="year",y="total_laid_off",data=df2,hue="year",palette=sns.color_palette(['green', 'blue','red','yellow',"cyan"]))
plt.title("comparison of layoff in previous years")
plt.xlabel("years")
plt.ylabel("no of layoffs")
plt.show()


# In[21]:


#TOTAL NO OF LAYOFF
tlo_2022 = df2[df2["year"]==2022]
tlo_2021 = df2[df2["year"]==2021]
tlo_2020 = df2[df2["year"]==2020]

total_laidoff_2022 = tlo_2022["total_laid_off"].sum()
total_laidoff_2021 = tlo_2021["total_laid_off"].sum()
total_laidoff_2020 = tlo_2020["total_laid_off"].sum()


# In[41]:


total_layoffs = (total_laidoff_2020,total_laidoff_2021,total_laidoff_2022)
labels = ["2020","2021","2022"]
plt.figure(figsize=(8,4))
plt.legend(labels=labels, bbox_to_anchor = (1,1))

plt.pie(total_layoffs, labels = labels,explode=(0,0.1,0))
plt.title("Total Layoffs in RECENT YEARS")


# In[54]:


df2.drop(["date"],axis=1)


# In[26]:


companies = df2["industry"].drop_duplicates(keep ='first')
companies


# In[27]:


df2_pivot = companies.pivot_tables[index="company",columns="year",values='total_laid_off']
df2_pivot.plot(kind="bar")


# In[74]:


df_India = df2[df2["country"]=="India"]
plt.bar(x=df_India["industry"],y=df_India["total_laid_off"].s,data=df_India)
plt.show()


# In[ ]:




