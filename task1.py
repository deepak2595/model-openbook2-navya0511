t=[]
data=[]
def opening_file(filename):
	fout=open(filename)
	for line in fout:
		f=tuple()
		line=line.split(",")
		data.append(line)
		str_name=line[2]
		full_name=line[4]
		from_str=line[6]
		to_str=line[7]
		f=(str_name,full_name,from_str,to_str)
		t.append(f)
	return data
def hist_maintenance(data):
	maintain_dictionary={}
	for datalist in data:
		if datalist[12] not in maintain_dictionary:
			maintain_dictionary[datalist[12]]=0
		else:
			maintain_dictionary[datalist[12]]+=1
	return maintain_dictionary

def unique_owners(data):
		owners=[]
		for datalist in data:
			owners.append(datalist[11])
		return owners

def street_classes(data):
	street_class={}
	for datalist in data:
		if datalist[10] not in street_class:
			street_class[datalist[10]]=datalist[2]
		else:
			street_class[datalist[10]].join(data[2])
	return street_class




d=opening_file("Street_Centrelines.csv")
print(hist_maintenance(d))
print(unique_owners(d))
print(street_classes(d))
