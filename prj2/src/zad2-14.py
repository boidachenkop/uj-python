# -*- coding: utf-8 -*-
# @Author: Pavlo Boidachenko
# @Date:   2018-10-03 13:25:17
# @Last Modified by:   pavlo
# @Last Modified time: 2018-10-03 16:05:07



S = "Welcome to the Jurassic Park"
Slen = [len(x) for x in S.split()]
print(S.split()[Slen.index(max(Slen))])

print(max(Slen))
