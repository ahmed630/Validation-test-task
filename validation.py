# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 15:00:54 2020

@author: Ahmed
"""
import json
import re 
  
email_regular_expression = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
phone_regular_expression = r'^[0-9]{3}[\- ]?[0-9]{3}[\- ]?[0-9]{4}$'


def validate(entry):
    email_isvalid = re.search(email_regular_expression, entry['emailAddress'])
    phone_isvalid = re.search(phone_regular_expression, entry['phoneNumber'])
    if phone_isvalid and email_isvalid:
        return 'Valid'
    elif phone_isvalid:
        return 'Email is invalid.'
    elif email_isvalid:
        return 'Phone is invalid.'
    else:
        return 'Email and Phone are invalid.'
    
    
def list_contacts(data):
    asc_data = sorted(data, key=lambda x: x['fullName'])
    print('\n\n\n'+'Step 1: contact records'+'\n')
    for entry in asc_data:
        text = entry['fullName'] + ': ' + validate(entry)    
        print( text) 
        
        
def list_cities(data):
    dict = {}
    for entry in data:
        if validate(entry) != 'Valid':
            if entry['cityName'] not in dict.keys():
                dict[entry['cityName']] = 1
            else:
                dict[entry['cityName']] += 1

    dict = sorted(dict.items(), key=lambda x: x[1],  reverse=True)
    
    for entry in dict:
        print(f'{entry[0]} : {entry[1]}')
    

def main():
    
    with open('Contacts.json') as f:
        data = json.load(f)
        
        
        list_contacts(data)
        print('\n\n' + 'Step 2: Cities in descending order'+'\n')
        list_cities(data)
      
  
          
if __name__ == '__main__':
    main()
      
      
