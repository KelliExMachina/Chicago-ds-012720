#!/usr/bin/env python
# coding: utf-8

# ![matplotlib](https://matplotlib.org/_static/logo2.png)
# # Data Visualization with Matplotlib
# 
# 
# ### Activation: Why is visualization important?
# ### What types of visualizations are we familiar with already?

# ![](https://media.giphy.com/media/l49JZfMbxMA7r5vZm/giphy.gif)

# ### Learning Goals:
# 
# After today, you will be able to:
# 
# - Explain and understand different types plots and their use cases
# - Identify and adjust the anatomy of a matplotlib plot
# - Explain the difference between plot types and justify their use cases:
#     - barplots
#     - histogram
#     - scatter plot
#     - pie chart
#     - boxplots
# - Visualize data using the matplotlib library in python 
# 
# 
# ### Step 1: Types of plots
# 
# Before we start creating, let's take a look at some [types](https://datavizproject.com/) of visualizations.
# 
# If you had to break these up into subgroups that fulfill a certain purpose, how would you break them up? Talk with your neighbors.
# 
# 
# Let's look at some [examples from python graphs](https://python-graph-gallery.com/)
# 
# The Matplotlib plotting library provides a range of built in functions to start visualizing data with minimum effort. Let's import the module pyplot in matplotlib as well as numpy to generate some sample data before creating plots from our animal shelter data.

# In[ ]:


# import libraries

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# Set plot space as inline for inline plots display
get_ipython().run_line_magic('matplotlib', 'inline')


# 
# ![msatplot](https://python-graph-gallery.com/wp-content/uploads/Logo_PGG_full-3.jpg)
# 
# The [Python Graph Gallery](https://python-graph-gallery.com/matplotlib/) has some great resources to guide you through the code needed to create each type of matplotlib plot. 
# 
# ### Plot Anatomy
# Let's spend some time on the terminology of a plot. There are a lot of options to set in matplotlib plots, so let's identify some common terminology. 
# 
# The sequence of events with matplotlib are:
# 
# | Step | Code Example |
# | :---- | :------------ |
# | 1. Create axis object | `ax = plt.subplot()` |
# | 2. Create figure | `plt.bar` |
# | 3. Make adjustments | `plt.title`, `ax.set_xticks`, etc |
# | 4. Show final plot | `plt.show()` . |
# 
# 
# The [Pyplot tutorial](https://matplotlib.org/tutorials/introductory/pyplot.html) shows a list of options you can set within a plot.
# 
# ![matplotlib anatomy](https://matplotlib.org/_images/sphx_glr_anatomy_001.png)
# 
# 
# Let's look [how they created this plot.](https://matplotlib.org/gallery/showcase/anatomy.html)

# ### 1 Barplots
# Barplots are used for displaying __one dimensional__, __discrete__ data. You call plt.bar with two arguments:
# - the x — a list of x-positions for each bar
# - the y-values — a list of heights for each bar

# In[ ]:


# an example of a bar plot 
ax = plt.subplot() # create an axis object, which the plot object which we can customize
our_dogs = ["dengue", "dolce", "murray", "dog_a", "dog_b", "dog_c"] 
dogs_age =  [5, 8, 5, 4, 6, 7]

plt.bar(range(len(our_dogs)), dogs_age)

plt.show()


# What is this plot missing? 
# 
# 

# ## Axis Labels
# `
# plt.xlabel()
# plt.ylabel()
# `

# ## Title
# `plt.title('age of random dogs')`

# ## X and Y ticks
# `
# ax.set_xticks() 
# ax.set_xticklabels() 
# `
# 

# ## Legend
# `
# plt.legend(['cats, dogs'])
# `
# 
# 

# In[ ]:





# [What is ax and figure?](https://stackoverflow.com/questions/34162443/why-do-many-examples-use-fig-ax-plt-subplots-in-matplotlib-pyplot-python)

# In[ ]:


# utilizing the subplot function and creating subplots
our_cats = ["cat_1", "cat_2", "cat_3", "cat_4", "cat_5", "cat_6"]
cats_age =  [14, 16, 17, 20, 18, 24]
plt.figure(figsize = (8,10))
plt.subplot(2,1,1)
plt.bar(range(len(our_dogs)),dogs_age, color = 'pink')


plt.title('dog age')
plt.subplot(2,1,2)
plt.bar(range(len(our_cats)),cats_age, color = 'green')
plt.title('cat age')
plt.xticks(ticks = range(len(our_cats)), labels = our_cats)
plt.show()


# What is something that you notice here that needs to be fixed?

# In[ ]:


# we can create overlaid or side-by-side bargraph. You need to shift the x value by width to accommodate for two graphs.
from matplotlib import pyplot as plt
fig = plt.figure()
n = 1 # This is our first dataset (out of 2) 
t = 2 # Number of datasets 
d = 6 # Number of sets of bars 
w = 0.8 # Width of each bar 
dog_values = [t*element + w*n for element in range(d)] # essentially, this list comprehension gives us the position
# of the position of dogs
plt.bar(dog_values,dogs_age, color='green')
n = 2  # This is our second dataset (out of 2)
t = 2 # Number of datasets
d = 6 # Number of sets of bars
w = 0.8 # Width of each bar
cat_values = [t*element + w*n for element in range(d)]
plt.bar(cat_values, cats_age, color = 'purple')
plt.legend(["dogs", "cats"])
n = 1


# In[ ]:


# stacked barplots 
ax = plt.subplot()
music_festivals = ["Coachella", "Govball", "EDC", "Ultra"]
ticket_sales_in_millon =  [114, 62, 120, 116]
people_attended_in_thousands = [126, 114 , 130, 110]

plt.bar(range(len(music_festivals)), ticket_sales_in_millon)
plt.bar(range(len(music_festivals)), people_attended_in_thousands, bottom=ticket_sales_in_millon)

plt.legend(["tix sales", "number of people"])
ax.set_xticks(range(0,len(music_festivals)))
ax.set_xticklabels(music_festivals)
plt.show()


# ### Bar plot - animal shelter dataset
# 
# Let's make a bar plot comparing dogs and cats by month when they are admitted to the shelter.

# ### 2 Histogram
# Histograms are like barplots in the sense that it describe __one-dimensional__ data. A histogram divides the variable into bins, counts the number of observations in each bin, and shows the bins on the x-axis and the frequency on the y-axis. It is used for visualizing __continuous__ variables. <br>
# 
# From the documentation: compute and draw the histogram of x. The return value is a tuple (__n, bins, patches__) or ([n0, n1, ...], bins, [patches0, patches1,...]) if the input contains multiple data.

# Comparison of barplots and histogram
# ![Screen%20Shot%202019-02-03%20at%2010.13.45%20PM.png](attachment:Screen%20Shot%202019-02-03%20at%2010.13.45%20PM.png)

# In[ ]:


# Set seed for reproducability
np.random.seed(2018)

# Generate 1000 values from 0 standard normal distribution
x = np.random.randn(100000)

#Plot the distogram with hist() function
plt.hist(x, bins = 1000)

plt.xlabel('Normal random distribution')
plt.ylabel('Frequency of Values')
plt.title('Histograms')
plt.show()


# In[ ]:


# overlaid histograms for two distributions
# plotting two histograms 
mu1, sigma1 = 0, 0.1 # mean and standard deviation
s1 = np.random.normal(mu1, sigma1, 1000)
mu2, sigma2 = 0.5, 0.1
s2 = np.random.normal(mu2, sigma2, 1000)
plt.figure(figsize = (10,8))
plt.hist(s1, bins = 20)
plt.hist(s2, bins = 20)


# ### Histogram - animal shelter dataset
# 
# Let's make a **histogram** looking at the sex upon outcomes of dogs in the shelter.

# In[ ]:


from data_cleaner import clean_df

df = clean_df(pd.read_csv('animals.csv'))
df.head()


# ### 3. Scatterplot - visualizing two dimensional data
# Scatterplots are usually used for visualizing two dimensional data (observations with two variables). It allows us to examine the relationship between two variables, thus it is sometimes called a correlation plot. 

# In[ ]:


# generate some data -> the sine wave
x = np.linspace(0, 10, 30)
y = np.sin(x)
plt.scatter(x, y, label = "Function: sin(x)")
plt.title('Scatter Plot in Matplotlib')
plt.legend()


# In[ ]:


# examining correlation with height and weight 
height = [63,62,60,63,64,65,68,67,64,71,72,70,73]
weight = [120,115,114,119,125,130,135,140,128,140,150,165,180]
plt.scatter(height, weight,color = 'r')


# Scatterplots, again, are great for examining the relationship between two variables. We can create pair-wise scatterplot for variables in a dataframe if we want to find their the correlations between variables. Later in this course, we will learn about correlation heatmap. 
# 

# In[ ]:





# ### 4 - Pie Charts

# In[ ]:


# pie chart 
music_genre = ['R&B', 'Rock', 'Country', 'House', 'Hip Pop', 'Techno']
num_people_like = [15, 5, 3, 7, 18, 3]

#Make your plot here
plt.figure(figsize=(10,8))
plt.pie(num_people_like ,labels=music_genre, autopct="%1d%%")

plt.axis('equal')
plt.title('Music Preference')

plt.show()
plt.savefig("music_pie_chart.jpeg")
# saves the image to the directory


# ### Pie chart - animal shelter data
# 
# While pie charts are frowned upon, people might still ask you to make them.
# 
# Make a pie chart of top 10 dog breeds.

# ## Putting it together:
# 
# If at any point you have questions about what a matplotlib function does, you have the `help()` function. 

# In[ ]:


help(plt.axis)

