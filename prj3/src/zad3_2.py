# -*- coding: utf-8 -*-
# @Author: Pavlo Boidachenko
# @Date:   2018-10-04 20:49:32
# @Last Modified by:   pavlo
# @Last Modified time: 2018-10-04 20:55:17


L = [3, 5, 4] ; L = L.sort()
print(L)

# L.sort() nic nie zwraca. Metoda sort() działa bezpośrednio na L, więc
# nie trzeba robić przyrównania

# ----------------------------------------- 

x, y = 1, 2, 3

# Za dużo liczb do przepisania zmiennym. Trzeba albo usunąć liczbę do
# przepisania, albo dodać jedną zmienną 

# -----------------------------------------

# X = 1, 2, 3 ; X[1] = 4

# X jest krotką. Krotki są obiektami niezmiennymi, więc nie da się zrobić
# przepisania 'X[1]=4'

# -----------------------------------------

# X = [1, 2, 3] ; X[3] = 4

# Ostatni indeks w X jest '2'. Żeby dostać element 4 o indeksie 3. Trzeba
# użyć metodę 'X.append(4)'

# -----------------------------------------

# X = "abc" ; X.append("d")

# Obiekt string nie ma metody 'append()'. Jedno z możliwych rozwiazań:

		# >>> X = "abc" ; X+="d"
		# >>> X
		# 'abcd'

# -----------------------------------------

# list(map(pow, range(8)))

# Funkcja pow potrzebuje 2 argumenty

		# >>> list(map(pow, range(8), range(8)))
		# [1, 1, 4, 27, 256, 3125, 46656, 823543]

























