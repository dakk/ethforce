# ethforce

You have lost your presale password, but you remember a list of possible pieces of it?
No worries, ethforce will find it.



## Install

First, checkout this repo:

```
	git clone https://github.com/dakk/ethforce
```

Then checkout pyethpresaletools, move ethforce.py to pyethsaletools:

```
	git clone https://github.com/ethereum/pyethsaletool.git
	cp ethforce/ethforce.py pyethsaletool
```


## Usage

Edit ethforce.py; in slices put the list of possible partial password, 
your encseed in the seed variable and your ethereum address in addr. 
Now start the script:

```
	cd pyethsaletool
	python ethforce.py
```


The software will try every combination of slices, using a cartesian product
with incremental repeating. When the software find the password, it stops displaying
the correct password.
