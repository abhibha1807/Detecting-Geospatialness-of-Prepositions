import json
import requests
import sys

def test_geonames(location):
	base_url="http://api.geonames.org/searchJSON?q="
	query=location
	url=base_url+query+"&maxRows=10&username=abhibha1807"
	response = requests.get(url)
	temp_l=[]
	todos = json.loads(response.text)
	items=todos.items()
	for i,j in items:
		if i=="geonames":
			if len(j)!=0:
				for k in j:
					d=k.items()
					for l,m in d:
						
						if l=="toponymName":
							y=m.split(' ')
							x=location.split(' ')
							
							for p in y:
								for q in x:
									if p==q:
										temp_l.append(d)	
								
	if len(temp_l)==0:
		return False
	else:
		return True

