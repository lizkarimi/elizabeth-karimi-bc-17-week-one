def word_count(string):
	astring = string.lower().split()
	adict = {}
	for item in astring:
		adict[item] = astring.count(item)
	print "\n".join(["%s: %s" % (key, ('%('+key+')s') % adict) for key in adict])

word_count("olly olly in come free")