
import json
import requests
import sys

def test_osm(location):
	base_url="https://geocoder.tilehosting.com/q/"
	key='zjHdrAD8A6tMYePMBF2t' # <- insert own key
	# place=sys.argv[1]
	place=location
	url=base_url+place+'.js?key='+key
	response = requests.get(url)
	print(url)
	temp_l=[]
	todos = json.loads(response.text)
	items=todos.items()
	for i,j in items:
		if i=="results":
			if len(j)!=0:
				for k in j:
					d=k.items()
					for l,m in d:
						if l=="display_name":
							x=location.split(' ')
							y=m.split(' ')
							# if y==x:
							for p in y:
								for q in x:
									if p==q:
										print('ppppppppppp:',p,q)
							
	if len(temp_l)==0:
		return False
	else:
		return True
			
	
