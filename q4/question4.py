#!/usr/bin/env python
# coding: utf-8

# In[1]:


def main():
    print(factorial(0))
    print(factorial(2))
    print(factorial(4))
    print(factorial(6))
    print(factorial(8))
    print(factorial(10))
    print(factorial(12))
    print(factorial(14))
        
        

    
def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num*factorial(num-1)
    
    
    
    
    

if __name__ == '__main__':
    main()


# In[ ]:




