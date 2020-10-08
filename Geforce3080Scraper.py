#####
# This script looks at websites with 3080s and emails you to alert you when any are in stock
#####

from NeweggScrapeObject import NeweggStock
from SendEmailObject import EmailAlert

# Importing getpass for hidden password entry
import getpass

# Importing time to cause a delay
import time

fromAddress = input("Please input the yahoo email address you would like to use: ")
fromPassword = getpass.getpass("Please enter your password: ")
toAddress = input("Please input the email address you would like to send to: ")
neweggUrl = input('Paste the URL to the Filtered Newegg Site for 3080s:')

# Scraping Logic
while True:

    #Creating a neweggStock Class to cause it to request from the website and to parse the data
    neweggStockList = NeweggStock(neweggUrl)

    #checks if the stocklist is empty or not and sends an alert if it is not empty
    if neweggStockList.stock != []:
        print('Stock Found!')
        neweggAlert = EmailAlert(neweggStockList.stock,fromAddress,fromPassword,toAddress)
        neweggAlert.sendemail()

    else:
        print('No stock was found... :( ')
        pass

    # Delays for an amount of time in seconds, default 1hr ()
    time.sleep(3600)
