import json
import difflib
from difflib import SequenceMatcher
data=json.load(open("data.json",'r'))
dkeys=list(data.keys())
def definition(key):      
    value=data[key]
    return value
def find(keys):
    keys=keys.lower()
    try:
        value=definition(keys)
        return value,1
    except:
        l={}
        j=0
        for i in dkeys:
            amt=SequenceMatcher(None,keys,i).ratio()
            if(amt>0.8):
                l[i]=data[i]    
        return l,3
            