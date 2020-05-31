# importing the importantlibraries 
import requests
import json
import pandas as pd
import numpy as np
import urllib

def make_categorydata():
	results=get_categories()
	id=[]
	name=[]
	for result in results['categories']:
  	  id.append(result['categories']['id'])
  	  name.append(result['categories']['name'])
	df_id=pd.DataFrame({'id':id,'name':name})
	
def make_citydata():
	results=getcitydetail()
	country_name=[]
	country_code=[]
	city_id=[]
	city_name=[]
	for result in result['location_suggestions']:
   	 city_id.append(result['id'])
   	 country_name.append(result['country_name'])
   	 country_code.append(result['country_id'])
   	 city_name.append(result['name'])
	df2=pd.DataFrame({'city_id':city_id,'city_name':city_name,'country_name':country_name,'country_code':country_code})
	

def make_establishmentdata():
	results=get_establishments()
	est_id=[]
	est_name=[]
	for result in results['establishments']:
		est_id.append(result['establishment']['id'])
		est_name.append(result['establishment']['name'])
	df_est=pd.DataFrame({'establishment_id':est_id,'establishment_name':est_name})
	
	
def makeResturantData(responses):
    restaurant_ids=[]
    restaurant_names=[]
    restaurant_urls=[]
    restaurant_localitys=[]
    restaurant_cuisines=[]
    restaurant_timings=[]
    restaurant_averageCosts=[]
    restaurant_userRatings=[]
    for response in responses['restaurants']:
        restaurant_ids.append(response['restaurant']['id'])
        restaurant_names.append(response['restaurant']['name'])
        restaurant_urls.append(response['restaurant']['url'])
        restaurant_localitys.append(response['restaurant']['location']['locality'])
        restaurant_cuisines.append(response['restaurant']['cuisines'])
        restaurant_timings.append(response['restaurant']['timings'])
        restaurant_averageCosts.append(response['restaurant']['average_cost_for_two'])
        restaurant_userRatings.append(response['restaurant']['user_rating']['aggregate_rating'])

    df_restaurant=pd.DataFrame({'id':restaurant_ids,'name':restaurant_names,'url':restaurant_urls,'locality':restaurant_localitys,'cuisines':restaurant_cuisines,'timing':restaurant_timings,'averagecost':restaurant_averageCosts,'rating':restaurant_averageCosts})
    return df_restaurant

