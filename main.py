# this is the main function of the data scrapping code
import argparse
import os
import sys
import requests
import urllib
import pandas as pd
import get_data
import make_data

if __name__ == "__main__":
    my_parser = argparse.ArgumentParser(description='parameters for the zomato api')

# Add the arguments
    my_parser.add_argument('api',type=str,help='enter your zomato api key')
    my_parser.add_argument('cityname',type=str,help='enter cityname')
    my_parser.add_argument('count',type=int,help='enter maximum results')
    args = my_parser.parse_args()

    print("the city name is ",args.cityname)
    print("the max results is ",args.count)

    user_key=args.api
    cityname=args.cityname
    count=args.count
    header = {'Accept': 'application/json', 'user-key':user_key}

    responses=get_data.searchResturant(cityname,count,header)
    df=make_data.makeResturantData(responses)

    df.to_csv('Restaurant.csv')




