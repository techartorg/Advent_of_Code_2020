# -*- coding: utf-8 -*-

from collections import Counter
from pathlib import Path

def total_answers( forms ):
    total_yes = 0
    group_answers = set( )

    for form in forms:
        if form:
            group_answers = group_answers.union( form )
        else:
            total_yes += len( group_answers )
            group_answers.clear( )
            continue

    return total_yes


def total_all_group_answer( forms ):
    total_yes = 0
    group_answers = ''
    num_group_members = 0
    for form in forms:
        if form:
            num_group_members += 1
            group_answers += form
        else:
            counts = Counter( group_answers )
            total_yes += sum( [ 1 for x in counts.values( ) if x == num_group_members ] )
            group_answers = ''
            num_group_members = 0
            continue

    return total_yes
        

if __name__ == '__main__':
    forms = [ x.strip( ) for x in ( Path.cwd( ) / '6_input.txt' ).open( ).readlines( ) ]
    if forms[ -1 ]:
        forms.append( '' )

    # Part 1
    print( total_answers( forms ) )

    # Part 2
    print( total_all_group_answer( forms ) )