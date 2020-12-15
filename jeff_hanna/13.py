# -*- coding: utf-8 -*-

from pathlib import Path

_TEST_DATA = [ '939', '7,13,x,x,59,x,31,19' ]


def _part_1( earliest_departure, bus_routes ):
    '''
    Your ferry can make it safely to a nearby port, but it won't get much further. When you call to book another ship, you discover that no ships embark from that port to your vacation island. You'll need to get from the port to the nearest airport.

    Fortunately, a shuttle bus service is available to bring you from the sea port to the airport! Each bus has an ID number that also indicates how often the bus leaves for the airport.

    Bus schedules are defined based on a timestamp that measures the number of minutes since some fixed reference point in the past. At timestamp 0, every bus simultaneously departed from the sea port. After that, each bus travels to the airport, then various other locations, and finally returns to the sea port to repeat its journey forever.

    The time this loop takes a particular bus is also its ID number: the bus with ID 5 departs from the sea port at timestamps 0, 5, 10, 15, and so on. The bus with ID 11 departs at 0, 11, 22, 33, and so on. If you are there when the bus departs, you can ride that bus to the airport!

    Your notes (your puzzle input) consist of two lines. The first line is your estimate of the earliest timestamp you could depart on a bus. The second line lists the bus IDs that are in service according to the shuttle company; entries that show x must be out of service, so you decide to ignore them.

    To save time once you arrive, your goal is to figure out the earliest bus you can take to the airport. (There will be exactly one such bus.)
    '''

    closest = [ earliest_departure *2, -1 ] # 2x earliest_departure just to get a number sufficiently larger than the desired departure time as a max.
    
    for bus_id in bus_routes:
        q, r = divmod( earliest_departure, bus_id )
        earliest = ( q + 1 ) * bus_id
        if earliest < closest[ 0 ]:
            closest = [ earliest, bus_id ]

    return ( closest[ 0 ] - earliest_departure ) * closest[ -1 ]


def _part_2( earliest_departure, bus_routes ):
    '''
    The shuttle company is running a contest: one gold coin for anyone that can find the earliest timestamp such that the first bus ID departs at that time and each subsequent listed bus ID departs at that subsequent minute. (The first line in your input is no longer relevant.)

    For example, suppose you have the same list of bus IDs as above:

    7,13,x,x,59,x,31,19
    An x in the schedule means there are no constraints on what bus IDs must depart at that time.

    This means you are looking for the earliest timestamp (called t) such that:

    Bus ID 7 departs at timestamp t.
    Bus ID 13 departs one minute after timestamp t.
    There are no requirements or restrictions on departures at two or three minutes after timestamp t.
    Bus ID 59 departs four minutes after timestamp t.
    There are no requirements or restrictions on departures at five minutes after timestamp t.
    Bus ID 31 departs six minutes after timestamp t.
    Bus ID 19 departs seven minutes after timestamp t.
    The only bus departures that matter are the listed bus IDs at their specific offsets from t. Those bus IDs can depart at other times, and other bus IDs can depart at those times. For example, in the list above, because bus ID 19 must depart seven minutes after the timestamp at which bus ID 7 departs, bus ID 7 will always also be departing with bus ID 19 at seven minutes after timestamp t.

    In this example, the earliest timestamp at which this occurs is 1068781:
    '''

    pass
    


if __name__ == '__main__':
    # bus_data = _TEST_DATA
    bus_data = [ x.strip( ) for x in ( Path.cwd( ) / '13_input.txt' ).open( ).readlines( ) ]
    earliest_departure = int( bus_data [ 0 ] )
    bus_routes = sorted( [ int( x ) for x in bus_data[ -1 ].split( ',' ) if x.isdigit( ) ] )
    
    # Part 1
    print( _part_1( earliest_departure, bus_routes ) )


    # Part 2
    print( _part_2( earliest_departure, bus_routes ) )
