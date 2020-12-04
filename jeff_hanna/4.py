# -*- coding: utf-8 -*-

from pathlib import Path

raw_data = ( Path.cwd( ) / '4_input.txt' ).open( ).read( ).split( '\n' )

valid_passports = 0
passport = { }

for i, rd in enumerate( raw_data ): 
    for x in rd.split( ' ' ):
        if ':' in x:
            kv = x.split( ':' )
            passport.update( { kv[ 0 ]: kv[ 1 ] } )
    
    if not rd or i == len( raw_data ) - 1:
        if len( passport ) == 8 or ( len( passport ) == 7 and not 'cid' in passport ):
            valid_passports += 1
            passport.clear( )
    
print( valid_passports )