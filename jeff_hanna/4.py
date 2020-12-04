# -*- coding: utf-8 -*-

from copy import deepcopy
from pathlib import Path


def validate_passport_keys( raw_data ):
    valid_passports = [ ]
    passport = { }

    for i, rd in enumerate( raw_data ): 
        for x in rd.split( ' ' ):
            if ':' in x:
                kv = x.split( ':' )
                passport.update( { kv[ 0 ]: kv[ 1 ] } )
        
        if not rd or i == len( raw_data ) - 1:
            if len( passport ) == 8 or ( len( passport ) == 7 and not 'cid' in passport ):
                valid_passports.append( deepcopy( passport ) )
                passport.clear( )

    return valid_passports


def validate_passport_values( passports ):
    """
    Validate based on these rules
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.

    Args:
        valid_passports ( [ ]dict ):

    Returns:
        [ ]dict:
    """

    def _int_validator( val, min, max ):
        if val.isdigit( ) and min <= int( val ) <= max:
            return True
        
        return False


    valid_passport_count = 0

    for p in passports:
        byr = p.get( 'byr', None )
        if not _int_validator( byr, 1920, 2002):
            continue
            
        iyr = p.get( 'iyr', None )
        if not _int_validator( iyr, 2010, 2020 ):
            continue

        eyr = p.get( 'eyr', None )
        if not _int_validator( eyr, 2020, 2030 ):
            continue

        hgt = p.get( 'hgt', None )
        val = hgt[ : -2 ]
        units = hgt[ -2 : ]
        if val.isdigit( ):            
            if units == 'cm':
                if not _int_validator( val, 150, 193 ):
                    continue
            elif units == 'in':
                if not _int_validator( val, 59, 76 ):
                    continue
            else:
                continue
        else:
            continue

        hcl = p.get( 'hcl', None )
        if not len( hcl ) == 7 or not hcl.startswith( '#' ):
            continue
        else:
            for x in hcl[ 1: ]:
                if not x.isdigit( ) or x in 'abcdef':
                    continue
        
        ecl = p.get( 'ecl', None )
        if not len( ecl ) == 3 or ecl not in ( 'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth' ):
            continue

        pid = p.get( 'pid', None )
        if not len( pid ) == 9 or not pid.isdigit( ):
            continue
        
        valid_passport_count += 1        
        
    return valid_passport_count
    

if __name__ == '__main__':
    raw_data = ( Path.cwd( ) / '4_input.txt' ).open( ).read( ).split( '\n' )
    valid_passports = validate_passport_keys( raw_data )
    
    # Part 1
    print( len( valid_passports ) )

    # Part 2
    print( validate_passport_values( valid_passports ) )
