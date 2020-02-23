# An assertion is a sanity check to make sure your code isn’t doing something obviously
# wrong. These sanity checks are performed by assert statements. If the sanity check fails,
# then an AssertionError exception is raised. This exception mus not be handled in through the ty-except block
# In code, an assert statement consists of the following:
# -The assert keyword
# -A condition (that is, an expression that evaluates to True or False)
# -A comma
# -A string to display when the condition is False

# Assertion can be disabled by using with the -O option
"""
>>> podBayDoorStatus = 'open'
>>> assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
>>> podBayDoorStatus = 'I\'m sorry, Dave. I\'m afraid I can't do that.''
>>> assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
Traceback (most recent call last):
File "<pyshell#10>", line 1, in <module>
assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
AssertionError: The pod bay doors need to be "open"

"""

# trafic light similation
market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}

def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'
    assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)


switchLights(market_2nd)



