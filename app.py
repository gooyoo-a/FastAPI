#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 16:14:02 2021

@author: gooyoo
"""




# Importing Necessary modules
from fastapi import FastAPI;
import uvicorn;


# Declaring our FastAPI instance
app = FastAPI()




# Defining path operation for root endpoint
@app.get('/')
def main():
	return {'message': 'Welcome to room!, My name is gooyoo'};


# Defining path operation for /name endpoint
@app.get('/{name}')
def hello_name(name : str):
	# Defining a function that takes only string as input and output the
	# following message.
	return {'message': f'Welcome to room!, {name}'};


