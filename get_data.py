# importing the importantlibraries 
import requests
import json
import pandas as pd
import numpy as np
import urllib

# to get the categories of different ways of taking the food 

def get_categories():
	url="https://developers.zomato.com/api/v2.1/categories"
	response=requests.get(url,headers=header)
	
	results=response.json()
	return results
	
def getcitydetail(city_name,count=1):
    # by default taking the city Delhi,India 
    url="https://developers.zomato.com/api/v2.1/cities?q=Delhi"
    if count is None:
        params={}
    else:
        params={'count':count}
    
    url_parts=list(urllib.parse.urlparse(url))
    query = dict(urllib.parse.parse_qsl(url_parts[4]))
    query['q']=city_name
    query.update(params)
    url_parts[4] = urllib.parse.urlencode(query)
    url_updated=urllib.parse.urlunparse(url_parts)
    response=requests.get(url_updated,headers=header)
    return response.json()
    
def get_establishments(city_id=1):
    url="https://developers.zomato.com/api/v2.1/establishments?city_id=1"
    url_parts=list(urllib.parse.urlparse(url))
    query = dict(urllib.parse.parse_qsl(url_parts[4]))
    query['city_id']=city_id
    url_parts[4] = urllib.parse.urlencode(query)
    url_updated=urllib.parse.urlunparse(url_parts)
    response=requests.get(url_updated,headers=header)
    return response.json()
    
