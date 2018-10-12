# -*- coding: utf-8 -*-
# @Author: Pavlo Boidachenko
# @Date:   2018-10-03 13:21:55
# @Last Modified by:   Pavlo Boidachenko
# @Last Modified time: 2018-10-12 15:18:40


S = 'abcabc xyzxyz kjikji'
print(" ".join([s[:1] for s in S.split()]))