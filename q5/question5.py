#!/usr/bin/env python
# coding: utf-8

# In[8]:


def main():
    string1 = "Two roads diverged in a yellow wood, And sorry I could not travel both And be one traveler, long I stood And looked down one as far as I could To where it bent in the undergrowth;"
    string2 = "Then took the other, as just as fair, And having perhaps the better claim, Because it was grassy and wanted wear; Though as for that the passing there Had worn them really about the same,"
    print(string1)
    print("\n")
    reverse_words(string1)
    print("\n")
    print(string2)
    print("\n")
    reverse_words(string2)
    
    
def reverse_words(string):
    str_list = string.split(" ")
    string3 = ""
    for i in range(len(str_list)-1,-1,-1):
        string3 += str_list[i]
        if(i != 0):
            string3 += " "
            
        
    print(string3)
        
    
    
    
if __name__ == '__main__':
    main()
    

                                


# In[ ]:




