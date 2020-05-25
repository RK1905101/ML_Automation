#!/usr/bin/env python
# coding: utf-8

# In[4]:


programfile = open('/automation_proj/code/Model_train.py','r')
code = programfile.read()   

if 'keras' or 'tensorflow' in code:
    if 'Conv2D' or 'Convolution' in code:
        print('CNN')
    else:
        print(' keras')
else:
    print(' Machine learning')


# In[ ]:
