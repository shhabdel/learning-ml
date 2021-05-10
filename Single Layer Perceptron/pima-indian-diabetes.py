#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np, random, os
from numpy import genfromtxt


# In[2]:


my_data = genfromtxt('pima-indian-diabetes.csv', delimiter=',')
random.shuffle(my_data)
attr_len = len(my_data[0])-1


# In[3]:


avgs = np.zeros(attr_len)
i = 0
for col in my_data.T[:-1]: 
    avgs[i] = np.mean(col)
    i += 1
for i in range(len(my_data)):
    for j in range(attr_len):
        if my_data[i][j] == 0:
            my_data[i][j] = avgs[j]


# In[4]:


training = my_data[:461]
test = my_data[461:]


# In[5]:


my_data.T


# In[6]:


weights = np.zeros(attr_len)
for i in range(0,attr_len):
    weights[i] = random.uniform(-1, 1)
bias = 1


# In[7]:


def Perceptron(data_row, bias):
    output = data_row[-1]
    data_row = data_row[:-1]
    pred = 0
    for i in range(len(data_row)):
        pred += data_row[i]*weights[i]
        
    pred += bias
    
    # Activation Code
    if pred > 0: pred = 1
    else: pred = 0
        
    error = output - pred 
    for i in range(len(data_row)):
        weights[i] += error*data_row[i]
    
    bias += error


# In[8]:


for i in range(50):
    for i in range(len(training)):
        Perceptron(training[i], bias)


# In[9]:


def Predict(new_data, bias):
    pred = 0
    for i in range(len(new_data)):
        pred += new_data[i]*weights[i]
    pred += bias
    if pred > 0: pred = 1
    else: pred = 0
    return pred
    


# In[10]:


training_error = 0
for i in range(len(training)):
    pred = Predict(training[i][:-1], bias)
    training_error += abs(training[i][-1] - pred)


# In[11]:


test_error = 0
for i in range(len(test)):
    pred = Predict(test[i][:-1], bias)
    test_error += abs(test[i][-1] - pred)


# In[12]:


(1 - (training_error / len(training))) * 100


# In[13]:


(1 - (test_error / len(test))) * 100

