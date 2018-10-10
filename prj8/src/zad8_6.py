# -*- coding: utf-8 -*-
# @Author: Pavlo Boidachenko
# @Date:   2018-10-07 16:38:02
# @Last Modified by:   Pavlo Boidachenko
# @Last Modified time: 2018-10-07 17:35:14

# P(0, 0) = 0.5,
# P(i, 0) = 0.0 dla i > 0,
# P(0, j) = 1.0 dla j > 0,
# P(i, j) = 0.5 * (P(i-1, j) + P(i, j-1)) dla i > 0, j > 0

PVALUES = {} # dictionary

def P(i, j):
	if (i, j) in PVALUES:
		return PVALUES[i, j]

	if i == 0 and j == 0:
		PVALUES[i, j] = 0.5
	elif i > 0 and j == 0:
		PVALUES[i, j] = 0.0
	elif i == 0 and j > 0:
		PVALUES[i, j] = 1.0
	elif i > 0 and j > 0:
		PVALUES[i, j] = 0.5 * (P(i-1, j) + P(i, j-1))

	return PVALUES[i, j]


if __name__ == '__main__':
	print(P(1, 2))
	print(PVALUES)