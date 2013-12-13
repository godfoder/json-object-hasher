import hashlib

def hash(hash_type,data,sort_arrays=False,sort_keys=True):
	h = hashlib.new(hash_type)

	s = ""
	if isinstance(data,list):
		sa = []
		for i in data:
			sa.append(hash(hash_type,i,sort_arrays=False,sort_keys=True))
		if sort_arrays:
			sa.sort()
		s = "".join(sa)

	elif isinstance(data,str) or isinstance(data,unicode):
		s = data;
	elif isinstance(data,int) or isinstance(data,float):
		s = str(data);
	elif isinstance(data,dict):
		ks = data.keys()
		if sort_keys:
			ks.sort()

		for k in ks:
			s += k + hash(hash_type,data[k],sort_arrays=False,sort_keys=True)

	else:
		print type(data);

	# print s
	h.update(s)
	return h.hexdigest()
