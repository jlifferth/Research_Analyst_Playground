#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pysb import *


# In[2]:


Model()


# In[3]:


Monomer('enzyme', ['binding1'])


# In[4]:


Monomer('protein', ['binding', 'state'], {'state': ['sub','pro']})


# In[5]:


Parameter('kf',0.003)
Parameter('kr',0.001)
Parameter('kc',0.002)


# In[6]:


Rule('binding', enzyme(binding1=None) + protein(state='sub', binding=None)
     | enzyme(binding1=1) % protein(state='sub', binding=1), kf, kr)


# In[7]:


Rule('dissociation', enzyme(binding1=1) % protein(state='sub', binding=1) 
     >> enzyme(binding1=None) + protein(state='pro', binding=None), kc)


# In[8]:


Parameter('enzyme_0', 100)
Parameter('protein_0', 50)
Initial(enzyme(binding1=None), enzyme_0 )
Initial(protein(binding=None, state='sub') , protein_0)


# In[9]:


Observable('e_total', enzyme())
Observable('e_free', enzyme(binding1=None))
Observable('substrate', protein(binding=None, state='sub'))
Observable('product', protein(binding=None, state='pro'))
Observable('complex', enzyme(binding1=1) % 
           protein(binding=1, state='sub'))


# In[10]:


from pysb.simulator import ScipyOdeSimulator
import numpy as np
import timeit
import matplotlib.pyplot as plt

tspan = np.linspace(0, 100, 100)

def time_func():
    y = ScipyOdeSimulator(model).run(tspan).all
 
timeit.Timer(time_func).timeit(number=100)/100


# In[12]:



y = ScipyOdeSimulator(model).run(tspan).all

plt.plot(tspan, y['substrate'], label="substrate")
plt.plot(tspan, y['e_total'], label="e_total")
plt.plot(tspan, y['e_free'], label="e_free")
plt.plot(tspan, y['product'], label="product")
plt.plot(tspan, y['complex'], label="complex")
plt.xlabel('time')
plt.ylabel('population')
plt.ylim(0,110)
plt.legend(loc=0)
plt.show()

