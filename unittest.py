#!/usr/bin/env python

import funktown

def treetest():
	t1 = funktown.LookupTree({0:0, 32:32, 4:4})
	assert t1.get(0) == 0
	t2 = t1.assoc(36, 36)
	assert t1.get(36) is None
	assert t2.get(36) == 36
	t3 = t2.assoc(36, 35)
	assert t3.get(36) == 35
	t4 = t2.multi_assoc([(15,15), (14,14)])
	assert t4.get(15) == 15
	assert t4.get(14) == 14

def vectortest():
	v1 = funktown.ImmutableVector([0,1,2])
	v2 = v1.conj(3)
	v3 = v1.pop()
	assert len(v1) == 3
	assert len(v2) == 4
	assert len(v3) == 2
	assert v2[3] == 3
	assert list(v2) == [0, 1, 2, 3]
	v4 = v1 + v2
	assert list(v4) == [0,1,2,0,1,2,3]
	assert list(v4[0:4]) == [0,1,2,0]

def dicttest():
	d1 = funktown.ImmutableDict(hello="world")
	d2 = d1.assoc("goodbye", "moon")
	d3 = d2.remove("hello")
	assert d1["hello"] == "world"
	assert d2["goodbye"] == "moon"
	assert d1.get("goodbye") is None
	assert d3.get("hello") is None
	assert dict(d2) == {"hello":"world", "goodbye":"moon"}
	d4 = d2.update(funktown.ImmutableDict({"a":"b", "c":"d"}))
	assert len(d4) == 4
	assert d4['a'] == 'b'
	assert d4['c'] == 'd'
	d5 = d1.update(hola="mundo")
	assert d5['hola'] == 'mundo'

if __name__ == "__main__":
	treetest()
	vectortest()
	dicttest()


