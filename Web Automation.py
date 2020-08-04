#!/usr/bin/env python
# coding: utf-8

# ## Web Automation
# 

# In[1]:


## Project - To automate the process of submitting a problem on codechef 


# In[2]:


## I will use Selenium which is widely used for web automation and testing


# In[3]:


get_ipython().system('pip install selenium')


# In[58]:


from selenium import webdriver


# In[59]:


browser = webdriver.Chrome("Desktop/chromedriver.exe")


# In[60]:


browser.get("https://codechef.com")


# In[61]:


username_element = browser.find_element_by_id("edit-name")


# In[62]:


username_element.send_keys("akshats6399")


# In[63]:


password_element = browser.find_element_by_id("edit-pass")


# In[64]:


from getpass import getpass


# In[ ]:


password_element.send_keys(getpass("Enter Password: "))


# In[ ]:


browser.find_element_by_id("edit-submit").click()


# In[ ]:


browser.get("http://www.codechef.com/submit/TEST")


# In[ ]:


browser.find_element_by_id("edit_area_toggle_checkbox_edit-program").click()


# In[ ]:


with open("ans.cpp",'r') as f:
    code = f.read()
code


# In[ ]:


code_element = browser.find_element_by_id("edit-program")


# In[ ]:


code_element.send_keys(code)


# In[ ]:


browser.find_element_by_xpath(''//*[@id="edit-language"]/option[2]').click()


# In[ ]:


browser.find_element_by_id("edit-submit").click()


# In[ ]:




