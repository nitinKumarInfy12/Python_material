spam = ['apples', 'bananas', 'tofu', 'cats']
var = str(spam)

var = None
for item in spam:
    if var is not None:
        var=f"{var}, {item}"
    else:
        var=item

print(var)

# could be simplified with join() method