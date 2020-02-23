#!/usr/bin/env python3

with open("DATA/presidents.txt") as pres_in:
    for pres_line in pres_in:
        print("INSERT INTO presidents (termnum, lastname, firstname, birthdate, deathdate, birthplace, birthstate, termstart, termend, party) VALUES ( " + \
                "%s, \"%s\", \"%s\", \"%s\", \"%s\", \"%s\", \"%s\", \"%s\", \"%s\", \"%s\"" % tuple((pres_line.rstrip('\r').rstrip('\n').split(sep=":"))) + \
                ");")




                #', '.join(pres_line.rstrip('\r').rstrip('\n').split(sep=":")) + \
                #"{0}, '{1}', '{2}', '{7}', '{8}', '{5}', '{6}', '{3}', '{4}', '{9}'".format(pres_line.rstrip('\r').rstrip('\n').split(sep=":")) + \
                #"{0}, '{1}', '{2}', '{7}', '{8}', '{5}', '{6}', '{3}', '{4}', '{9}'".format(pres_line.rstrip('\r').rstrip('\n').split(sep=":")) + \


#(number, last_name, first_name, birth_date, death_date, birth_city, birth_state, term_start, term_end, party) = pres_line.rstrip('\r').rstrip('\n').split(sep=":")
