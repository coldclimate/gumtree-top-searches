#!/usr/bin/python
import os
import requests
import lxml.html

for place in ["bedfordshire", "berkshire", "bristol", "buckinghamshire", "cambridgeshire", "cheshire", "cornwall", "county-durham", "cumbria", "derbyshire", "devon", "dorset", "east-sussex", "east-yorkshire", "essex", "gloucestershire", "hampshire", "hertfordshire-", "isle-of-wight", "kent", "lancashire", "leicestershire", "lincolnshire", "london", "manchester", "merseyside", "norfolk", "north-yorkshire", "northamptonshire", "northumberland", "nottinghamshire", "oxfordshire", "rutland", "shropshire", "somerset", "south-yorkshire", "staffordshire", "suffolk", "surrey", "tyne-and-wear", "warwickshire", "west-midlands", "west-sussex", "west-yorkshire", "wiltshire", "worcestershire"]:
	req = requests.get("https://www.gumtree.com/all/%s" % place)
	root_page = req.content
	root = lxml.html.document_fromstring(root_page)
	links = root.xpath('//*[@id="header-bottom"]/div/div[2]/div/div/ul/li/a')
	searches=[]
	for link in links:
		searches.append(link.text_content())
	final_list = ",".join(searches)
	print ("%s:%s" % (place, final_list))
