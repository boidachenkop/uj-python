# -*- coding: utf-8 -*-
# @Author: Pavlo Boidachenko
# @Date:   2018-10-04 21:04:06
# @Last Modified by:   pavlo
# @Last Modified time: 2018-10-05 14:09:04


A = [[], [4], (1, 2), [3, 4], (5, 6, 7)]
result = []
for L in A:
	result.append(sum(L))
print(result)