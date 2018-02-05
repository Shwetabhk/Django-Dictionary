import json
import difflib
from difflib import SequenceMatcher
import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(THIS_FOLDER, 'data.json')
data=json.load(open(file,'r'))
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
            