# key value pair
# pprint 
d = {'first_name':'Nitin', 'Last_name':'kumar', 'age':32}
print(d['first_name'])

print(d)

print (d.keys())

print (d.values())

d.pop('age')

print (d)
d['age'] = 35

print (d)

d.popitem()

print (d)
#=========

spam = {'color': 'red', 'age': 42}
for v in spam.values():
    print(v)

for k in spam.keys():
    print(spam[k])

for i in spam.items():
    print(i)

#----------------

spam = {'color': 'red', 'age': 42}
spam.keys()
dict_keys(['color', 'age'])
list(spam.keys())
#['color', 'age']

#=============
spam = {'color': 'red', 'age': 42}
for k, v in spam.items():
    print('Key: ' + k + ' Value: ' + str(v))

#-----------------

spam = {'color': 'red', 'age': 42}
for k, v in spam.items():
    print('Key: ' + k + ' Value: ' + str(v))


#----- get() method
picnicItems = {'apples': 5, 'cups': 2}

'I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.'
# 'I am bringing 2 cups.'
'I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.'
#'I am bringing 0 eggs.'

# ----- setdefault()
>>> spam = {'name': 'Pooka', 'age': 5}
>>> spam.setdefault('color', 'black')
'black'
>>> spam
{'color': 'black', 'age': 5, 'name': 'Pooka'}
>>> spam.setdefault('color', 'white')
'black'
>>> spam
{'color': 'black', 'age': 5, 'name': 'Pooka'}

#  zip method on dictionary
def row_as_dict(cursor):
    '''Generate rows as dictionaries'''
    column_names = [desc[0] for desc in cursor.description]
    for row in cursor.fetchall():
        row_dict = dict(zip(column_names, row))
        yield row_dict



#-------------======
import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

#pprint.pprint(count)
#print(pprint.pformat(count))
#pprint.pformat(count)
