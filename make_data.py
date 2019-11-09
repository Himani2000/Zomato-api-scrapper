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
	
	
	
