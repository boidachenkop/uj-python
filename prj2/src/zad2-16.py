# -*- coding: utf-8 -*-
# @Author: Pavlo Boidachenko
# @Date:   2018-10-03 17:38:15
# @Last Modified by:   pavlo
# @Last Modified time: 2018-10-03 17:42:11


line  = 'GvR'
to_add = "uido an ossum"
print(' '.join([a+b for a, b in zip(line, to_add.split())]))
