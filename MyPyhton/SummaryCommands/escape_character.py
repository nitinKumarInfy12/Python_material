# '\' is the escape charatcter
# r'' is the raw string notation to python
#Typing r'\d\d\d-\d\d\d-\d\d\d\d' is much easier than typing '\\d\\d\\d-\\d\\d\\d-\\d\\d\\d\\d'
"""
Remember that escape characters in Python use the backslash (\). The string value '\n' represents a single newline
character, not a backslash followed by a lowercase n. You need to enter the escape character \\ to print a single
backslash. So '\\n' is the string that represents a backslash followed by a lowercase n. However, by putting an r
before the first quote of the string value, you can mark the string as a raw string, which does not escape characters.
Since regular expressions frequently use backslashes in them, it is convenient to pass raw strings to the re.compile()
function instead of typing extra backslashes. Typing r'\d\d\d-\d\d\d-\d\d\d\d' is much easier than typing
'\\d\\d\\d-\\d\\d\\d-\\d\\d\\d\\d'. """