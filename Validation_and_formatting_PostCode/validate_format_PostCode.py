#!/usr/bin/env python3

# Postcodes API is available at http://postcodes.io/
import requests
import json


def loadJsonResponse(url):
    try:
        return json.loads(requests.get(url).text)['result']
    except requests.exceptions.RequestException as e:
        print(e)

def validatePostcode(postcode):
    """
    Function to validate the post code
    input args: postcode data
    return: boolean (True or False)
    """
    try:
        url = 'https://api.postcodes.io/postcodes/{}/validate'.format(postcode)
        return loadJsonResponse(url)
    except requests.exceptions.RequestException as e:
        print(e)

def randomPostcode():
    """
    Function to generate random post code
    input args: None
    return: postcode data
    """
    try:
        url = 'https://api.postcodes.io/random/postcodes'
        return loadJsonResponse(url)['postcode']
    except requests.exceptions.RequestException as e:
        print(e)

def queryPostcode(postcode):
    """
    Function to query the post code
    input args: postcode data
    return: list
    """
    try:
        url = 'https://api.postcodes.io/postcodes?q={}'.format(postcode)
        return loadJsonResponse(url)
    except requests.exceptions.RequestException as e:
        print(e)

def getAutoCompletePostcode(postcode):
    """
    Function to get auto complete post code
    input args: postcode data
    return: list
    """
    try:
        url = 'https://api.postcodes.io/postcodes/{}/autocomplete'.format(postcode)
        return loadJsonResponse(url)
    except requests.exceptions.RequestException as e:
        print(e)

# Main function starts here
if __name__ == '__main__':
    print(validatePostcode('RG27 9HW'))
    print(randomPostcode())
    print(queryPostcode('RG27 9HW'))
    print(getAutoCompletePostcode('PL4 '))




