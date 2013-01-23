'''
Created on Jan 20, 2013

@author: Noel
'''
import urllib.request
import re

class Crawler:
 def fetchLinks(self,url='http://python.org/'):
    try:
     response = urllib.request.urlopen(url)
     html = response.read()
     html_str=str(html)
     urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', html_str) #re expression to extract links
     return urls
    except IOError as e:
     print (e)
  
          
   
   
   
   
   
   
   
   