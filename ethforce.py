import pyethsaletool
import itertools

slices = [ 'hello', 'world', '91', 'dakk' ]
seed = ""
addr = ""

def check (pw):
	key = pyethsaletool.pbkdf2(pw)
	try:
		pyethsaletool.getseed (seed, key, addr)
		return True
	except Exception as e:
		return False

found = False

for i in range (12):
	if found: break

	for c in itertools.product (slices, repeat=i):
		if found: break

		pw = ''.join (c)
		r = check (pw)
		if r:
			found = True
		print i,pw,r
