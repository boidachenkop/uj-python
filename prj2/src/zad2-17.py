# -*- coding: utf-8 -*-
# @Author: Pavlo Boidachenko
# @Date:   2018-10-03 17:42:45
# @Last Modified by:   pavlo
# @Last Modified time: 2018-10-03 17:43:43


line = "Hello, World! My name is Pavlo."
print(sorted(line.split()))
print(sorted(line.split(), key=str.__len__))