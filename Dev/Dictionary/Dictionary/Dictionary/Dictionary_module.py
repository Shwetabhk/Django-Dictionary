import json
import difflib
from difflib import SequenceMatcher
data=json.load(open("data.json",'r'))
def definition(key):      
    value=data[key]
    return value
def find(key):
    key=key.lower()
    try:
        value=definition(key)
        return value
    except:
        flag=0
        for i in data:
            amt=SequenceMatcher(None,key,i).ratio()
            if(amt>0.7):
                print("Did you mean "+i+" ? Input yes or no")
            #    flag=1
             #   answer=input().lower()
              #  if answer=="yes":
               #     return definition(i)
        #if(flag==0):
         #   return "Word not found"