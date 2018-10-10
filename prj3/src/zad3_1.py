# -*- coding: utf-8 -*-
# @Author: Pavlo Boidachenko
# @Date:   2018-10-04 15:09:32
# @Last Modified by:   pavlo
# @Last Modified time: 2018-10-04 20:48:42


x=2 ; y=3;         # srednik po 'y=3' nie jest potrzebny
if(x>y):
	result = x;    # srednik nie jest potrzebny
else:
	result = y;    # srednik nie jest potrzebny
print(result)


# for i in "qwerty": if ord(i) < 100: print i
# po dwukropu mozna uzyc jednej prostej instrukcji
# poprawny wariant:
for i in 'qwerty':
	if ord(i) < 100: print(i)

# ten kod jest poprawny
for i in "axby": print(ord(i) if ord(i) < 100 else i)