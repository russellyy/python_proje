#!/usr/bin/env python
# coding: utf-8

# In[41]:


def flatten_list(nested_list):
    flat_list = []
    for item in nested_list:
        if type(item) == list:
            flat_list += flatten_list(item)
        else:
            flat_list.append(item)
    
    return flat_list

input_list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print(flatten_list(input_list))


# In[35]:


l = [[1, 2], [3, 4], [5, 6, 7]]

def new_list(l):
    for i in l:
        i.reverse()
    l.reverse()
    return(l)


# In[39]:


l


# In[40]:


new_list(l)

