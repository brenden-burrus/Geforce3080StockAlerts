#####
# Contains the class that handles all the data from a newegg URL dealing with 3080s
#####

# Important web scraping imports
import requests
import bs4


# class that takes a URL to a website and determines wheter items are in stock or not
# class returns a list of tuples that contain the url, name, and promos of any in stock items
# URL should point to a filtered list of items
# This class is specific to newegg. if it is not a newegg url, it will fail

class NeweggStock:
    
    def __init__(self,url):
        self.url = url
        self.stock = []
        self.urlreq = ''
        self.soup = ''

    def checkStock(self):
        self.urlreq = requests.get(self.url)
        self.soup = bs4.BeautifulSoup(self.urlreq.text,'lxml')
        i = 0
        for item in self.soup.select(".item-info"):
            if 'OUT OF STOCK' not in item.text:
                self.stock.append((self.soup.select(".item-title")[i].text,self.soup.select(".item-title")[i]['href'],self.soup.select(".item-promo")[i].text))
            i += 1


