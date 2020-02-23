# copy() and deepcopy() methods from copy module allows copy the list instead of reference

import copy


#----------- without the copy module methods
lista= ['a','b','c']

listb = lista
listb[1] = 2


print(lista)
print(listb) # both the values will show same lists with the change
#====================================

# ----- with teh copy module and copy() method

lista= ['a','b','c']

listb = copy.copy(lista)
listb[1] = 2


print(lista)
print(listb) # both the values will show diff lists


# ----- with the copy module and deepcopy() method

lista= ['a','b','c',[1,2,3]]

listb = copy.deepcopy(lista)
listb[1] = 2

# deepcopy() should be used if teh reference list has another list as item
print(lista)
print(listb) # both the values will show diff lists



