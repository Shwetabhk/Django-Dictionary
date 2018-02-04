import json
import difflib
from difflib import SequenceMatcher
data=json.load(open("data.json",'r'))
dkeys=list(data.keys())
def definition(key):      
    value=data[key]
    return value
def find(key):
    key=key.lower()
    try:
        value=definition(key)
        return value,1
    except:
        l=[]
        j=0
        for i in dkeys:
            amt=SequenceMatcher(None,key,i).ratio()
            if(amt>0.8):
                l.insert(j,i)
                j=j+1
        return l,None
            