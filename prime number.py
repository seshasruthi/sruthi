#!/usr/bin/env python
# coding: utf-8

# ## PRIME NUMBER

# In[5]:


number = int(input("enter a number: "))
if number > 1:
    for i in range(2,number):
        if (number % i) == 0:
            print(number,"is not a prime number")
            break
    else:
        print(number,"is a prime number")
else:
    print(number,"is not a prime number")


# In[ ]:




