'''
Created on Jan 20, 2013

@author: Noel
'''
from crawler import Crawler 
no_of_links=1000
def main():
    c=Crawler()
    url_list=c.fetchLinks()
    for urls in url_list:
        print ("url:",urls,"\n")
        temp_list=c.fetchLinks(urls)  #fetch the links from each url from the url_list
        print(temp_list)
        url_list+=temp_list           #merge the the two list
        list_size=len(url_list)
        if list_size > no_of_links:   #process stops after given no of links are fetched
            print ("process stopped size > ",no_of_links)
            break
        print ("size",list_size)
if __name__=="__main__":main()