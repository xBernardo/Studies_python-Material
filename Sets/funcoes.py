conj1 = {1, 3, 4, 5, 7}
conj2 = {2, 4, 5, 9, 0}

#conj3 = conj1.union(conj2)
#print(conj3)

#conj3 = conj1.intersection(conj2)
#print(conj3)

#conj1.intersection_update(conj2)
#print(conj1)

conj1.symmetric_difference_update(conj2)
print(conj1)
