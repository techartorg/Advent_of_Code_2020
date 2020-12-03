# -*- coding: utf-8 -*-
from pathlib import Path

def part_1( pwd_data ):
    """
    For each line in pwd_data:
    * element 0 contains the min/max counts. It is stored as <str>-<str> it will 
      need to be split and each of the 2 new elements cast to ints.
    * element 1 contains the character to count in the provided password string.
      It will have a trailing : character that will need to be stripped.
    * element 2 is the password string

    The character in element 1 must exist in the password a number of times 
    between the min and max values provided.

    Args:
        pwd_data ([list]): 
    """

    good_passwords = 0

    for x in pwd_data:
        min, max = x[ 0 ].split( '-' )
        if int( min ) <= x[ 2 ].count( x[ 1 ].rstrip( ':' ) ) <= int( max ):
            good_passwords += 1

    print( good_passwords )


def part_2( pwd_data ):
    """
    For each line in pwd_data:
    * element 0 contains the two positions within the password where the key 
      character must be found. 
      It is stored as <str>-<str> it will 
      need to be split and each of the 2 new elements cast to ints.
    * element 1 contains the character to count in the provided password string.
      It will have a trailing : character that will need to be stripped.
    * element 2 is the password string

    The key must exist in only one of the two index locations provided.
    
    NOTE: The toboggan place's password database must have been written in 
    MaxScript, as indexes are 1 based.

    Args:
        pwd_data ([list]): 
    """

    good_pwd_count = 0

    for x in pwd_data:
        # I'm sure some magic list-comp-foo could reduce these lines.
        idx1, idx2 = x[ 0 ].split( '-' )
        idx1 = int( idx1 ) - 1
        idx2 = int( idx2 ) - 1
        key = x[ 1 ].rstrip( ':' )
        password = x[ 2 ]

        a = password[ idx1 ]
        b = password[ idx2 ]
        if not( a == key and b == key ) and ( a == key or b == key ):
            good_pwd_count += 1

    print( good_pwd_count )



if __name__ == '__main__':
    pwd_data = [ x.split( ' ' ) for x in ( Path.cwd( ) / '2_input.txt' ).open( ).readlines( ) ]
    part_1( pwd_data )
    part_2( pwd_data )
