#!/usr/bin/env python

import funcds

def treetest():
	t1 = funcds.LookupTree({0:0, 32:32, 4:4})
	assert t1.get(0) == 0
	t2 = t1.assoc(36, 36)
	assert t1.get(36) == None
	assert t2.get(36) == 36
	t3 = t2.assoc(36, 35)
	assert t3.get(36) == 35

def vectortest():
	v1 = funcds.ImmutableVector([0,1,2])
	v2 = v1.conj(3)
	v3 = v1.pop()
	assert len(v1) == 3
	assert len(v2) == 4
	assert len(v3) == 2
	assert v2[3] == 3
	assert list(v2) == [0, 1, 2, 3]

def dicttest():
	d1 = funcds.ImmutableDict(hello="world")
	d2 = d1.assoc("goodbye", "moon")
	d3 = d2.remove("hello")
	assert d1["hello"] == "world"
	assert d2["goodbye"] == "moon"
	assert d1.get("goodbye") == None
	assert d3.get("hello") == None
	assert dict(d2) == {"hello":"world", "goodbye":"moon"}

if __name__ == "__main__":
	treetest()
	vectortest()
	dicttest()

