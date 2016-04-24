import math

def prime_gen():
    """
    A prime number generator using generators in Python.
    Tested on Python3 but should work on any Python version that supports generators

    Purpose: Generate prime numbers
    Usage Example:
    prime_gen = prime_generator()
    for prime in prime_gen:
        ...

    OR

    prime = next(prime_gen)

    Params: None
    Return Type: Integer

    Algorithm:
    Based on Sieve of Erasthotenes https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    """

    prime_list = []
    tracked_list = [[2,False]]
    offset_track = 2
    prime_track = 0

    while True:
        if len(prime_list) == 0:
            prime_list.append(2)

        # if this is not the last prime, then retrieve it
        if prime_track != len(prime_list):
            yield prime_list[prime_track]
            prime_track += 1
            continue

        # extend tracked_list, if it's too big, then resize it
        if len(tracked_list) < 1000000:
            track_ptr = len(tracked_list) - 1
            tracked_list.extend([[x,False] for x in range(tracked_list[-1][0]+1, tracked_list[-1][0]*2)])
        else:
            track_ptr = 0
            tracked_list = [[x,False] for x in range(tracked_list[-1][0]+1, tracked_list[-1][0]*2)]
            offset_track += len(tracked_list) - 2

        # attempt to create primes  
        for prime in prime_list:
            # get starting point for this prime
            start_point = math.ceil(tracked_list[track_ptr][0] / prime) * prime - offset_track
            while start_point < len(tracked_list):
                # if the current number has not been visited yet
                # and can be divided by a prime number
                if not tracked_list[start_point][1] and \
                   tracked_list[start_point][0] % prime == 0:
                    tracked_list[start_point][1] = True

                start_point += prime

        # find new primes
        while track_ptr != len(tracked_list):
            if not tracked_list[track_ptr][1]:
                prime_list.append(tracked_list[track_ptr][0])
            track_ptr+= 1
