import csv
import math

##############################################################
# File: bulletproof_me.py
# Date: June 6 2015
# Purpose: 
##############################################################

##############################################################
# Global Variables
##############################################################
adver_data = {}
column_names = []

##############################################################
# Helper Functions
##############################################################

def convertCostData():    
  cost_column = column_names.index('cost')
  
  for (customer_name, customer_data) in adver_data.iteritems():
    cost = adver_data[customer_name][cost_column]
    cost = cost.strip('$')
    try:
      adver_data[customer_name][cost_column] = float(cost)
    except ValueError:
        print('cannot read string to float')
    
def getDataList(column_name):
  column_index = column_names.index(column_name)
  data_list = []
  
  for customer_data in adver_data.values():
    data_list.append(customer_data[column_index])
  
  return data_list
  
def getCostData():
  return getDataList('cost')
      
def getMailingList():
  return ', '.join(getDataList('email'))
  
def getCustomerList():
  return ', '.join(sorted(adver_data.keys()))
  
def getCountrySet():
  country_list = getDataList('country')
  country_set = set(country_list)
  return ', '.join(list(country_set))
    
def getCustomerData(customer_name):
  data_list = []
  for column_index in range(len(column_names)):
    data_list.append('{}: {}'.format(column_names[column_index], 
                         adver_data[customer_name][column_index]))
                         
    return ', '.join(data_list)
  
def printDataSummary():
  try:
    print ('Advertising Total Cost: {}\n'.format(math.fsum(getCostData())))
    print ('Mailing List:\n\t{}\n'.format(getMailingList()))
    print ('Countries:\n\t{}\n'.format(getCountrySet()))
  except AttributeError:
    print('error printing data')



##############################################################
# Main Program
##############################################################
# TODO: Bulletproof me!

# Read in the advertising customer information.
with open('advertising_data.csv', 'r') as csvfile:
  adver_reader = csv.reader(csvfile)
  column_names = next(adver_reader)
  for customer_row in adver_reader:
    customer_name = customer_row[1] + ' ' + customer_row[2]
    adver_data[customer_name] = customer_row

# Perform Data Conversions
convertCostData()

# Start the interactive program
print ('Advertising Data Info')

options = ['Get a customer list', 'Get customer data', 'Get a mailing list',
       'Get a country list', 'Get a data summary', 'Quit']
       
while True:
  print ('\nSelect an action:')
  
  # Make the number options 1-based to make it more intuitive for users
  for option_number in range(0, len(options)):
    print (str(option_number + 1) + ': ' + options[option_number])
  print ('') # print a blank line to break up the output
    
  # Retrieve the user action
  action = input('')
  try:
    action = int(action.strip())
  except AttributeError:
    print('AttributeError')
  
  print ('\nYou selected: ' + options[action - 1])

  if action == options.index('Get a customer list') + 1:
    print ('Customer List:\n\t{}\n'.format(getCustomerList()))

  elif action == options.index('Get customer data') + 1:
    try:
      customer_name = input('Customer Name: ')
      print (getCustomerData(customer_name))
    except SyntaxError:
      'Wrong input'

    
  elif action == options.index('Get a mailing list') + 1: 
    print ('Mailing List:\n\t{}\n'.format(getMailingList()))
    
  elif action == options.index('Get a country list') + 1: 
    print ('Countries:\n\t{}\n'.format(getCountrySet()))
    
  elif action == options.index('Get a data summary') + 1:
    printDataSummary()
    
  elif action == options.index('Quit') + 1:
    break
