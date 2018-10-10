# Processing tool for Ingress raw data
import numpy as np
import csv

upv_ops = ['hacked enemy portal', 'hacked neutral portal', 'hacked friendly portal', 'mod deployed', 'resonator deployed', 'resonator upgraded']
with open('game_log.tsv','r') as log_file:
	count = 0
	upc_list = list()
	upv_list = list()
	log_file = csv.reader(log_file, delimiter='\t')
	for row in log_file:
		count += 1
		if row[3]=='captured portal':
			upc_list.append((row[1], row[2]))
		if row[3] in upv_ops:
			upv_list.append((row[1], row[2]))

print(count)
upv_set = set(upv_list)
upc_set = set(upc_list)
diff_set = upv_set-upc_set
print(len(upv_set))
print(len(upc_set))

with open('upc_list.txt','w') as upc_file:
	upc_file.write('[')
	while(True):
		lat, lng = upc_set.pop()
		line = '{{"latLng":{{"lat":{0},"lng":{1}}},"color":"#ff00ff","radius":20,"type":"circle"}}'.format(lat,lng)
		upc_file.write(line)
		if len(upc_set)>0:
			upc_file.write(',')
		else:
			break
	upc_file.write(',')
	while(True):
		lat, lng = diff_set.pop()
		line = '{{"latLng":{{"lat":{0},"lng":{1}}},"color":"#00ffff","radius":20,"type":"circle"}}'.format(lat,lng)
		upc_file.write(line)
		if len(diff_set)>0:
			upc_file.write(',')
		else:
			break
	upc_file.write(']')
