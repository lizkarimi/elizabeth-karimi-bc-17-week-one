def data_type(n):
  if type(n)==int:
    if n>100:
      return 'more than 100'
    elif n<100:
      return 'less than 100'
    else:
      return 'equal to 100'
    elif type(n) == str:
  		return len(n)
  	elif n==None:
  		return "no value"
  	elif type(n)==bool:
  		return n
  	elif type(n)==list:
  		try:
  			return n[2]
  		except Exception as e:
  			return None
