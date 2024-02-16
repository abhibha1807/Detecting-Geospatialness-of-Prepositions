import sys
import re
import test_stanford
from nltk.stem.porter import *


def geo_features(s):
	final_l=[]
	with open('geonouns-old.txt','r') as f:
		for word in f:
			word=word.strip()
			final_l.append(word)

	c=0
	r=[]
	split_s=s.split(' ')
	split_s[len(split_s)-1]=split_s[len(split_s)-1].replace('\"\n',"")
	for i in final_l:
		if i in s:
			split_i=i.split(' ')

			set_s=set()
			set_i=set()
			for l in split_s:
				set_s.add(l)
			for k in split_i:
				set_i.add(k)
			
			if set_i.issubset(set_s):
				r.append(i)
				c=c+1
				for j in split_i:
					s=s.replace(j,"",1)
		cnt=0
		for i in r:
			cnt=cnt+s.count(i)
			if s.count(i)>0:
				r.append(i)
				f=i.split(' ')
				for j in f:
					s=s.replace(j,"",1)
	
		
		return (s,c+cnt,r)
	

