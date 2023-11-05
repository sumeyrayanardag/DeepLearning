#!/usr/bin/env python
# coding: utf-8

# In[16]:


import random


# In[24]:


print("Welcome to the guessing game! You will have a maximum of 5 attempts to guess the correct number and the numbers are between 1 and 100")


# In[18]:


number = random.randint(1, 100)


# In[20]:


username = input("Please enter your name: ")


# In[23]:


flag = 0
for x in range(5):
    guess = int(input("Please enter your %d. guess: " %(x+1)))
    if number == guess:
        print("Congratulations " + username + "! The number is %d" %number)
        flag = 1
        break
    elif number - guess > 0:
        print("Too low!")
    else:
        print("Too high!")
        
if(flag == 0):
    print("You lost " + username + "! The number is %d" %number)


# In[ ]:


input("If you want to exit, please press the enter")

