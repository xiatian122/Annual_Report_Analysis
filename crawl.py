import os, sys, urllib, re;
#form urlparse import urlparse;
from BeautifulSoup import BeautifulSoup

def  crawl_list(CIK):
	root_url="http://www.sec.gov"
	url= "http://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=%s&type=DEF+14A&dateb=&owner=include" % (CIK) ;
	
	# Retrive web page data
	dlist_page_html = urllib.urlopen(url).read();

	list_soup = BeautifulSoup(dlist_page_html);

	
	#tmp_page = soup.find("td", {"nowrap": "nowap"});

	page_list = list_soup.findAll(id="documentsbutton");

	for tmp_page in page_list:
		#print root_url + tmp_page['href'];
		obj_page = urllib.urlopen(root_url + tmp_page['href']).read();
		my_soup = BeautifulSoup(obj_page);
		txt_obj =  my_soup.find('a', href=re.compile('[A-Za-z0-9]*\.txt'));
		print root_url + txt_obj['href'];

if __name__=="__main__":
	crawl_list("0001326801"); 