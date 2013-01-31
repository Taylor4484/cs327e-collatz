#!/usr/bin/env python

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2013
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

def collatz_read (r, a) :
    """
    reads two ints into a[0] and a[1]
    r is a  reader
    a is an array of int
    return true if that succeeds, false otherwise
    """
    s = r.readline()
    if s == "" :
        return False
    l = s.split()
    a[0] = int(l[0])
    a[1] = int(l[1])
    assert a[0] > 0
    assert a[1] > 0
    return True

# ------------
# collatz_cache
# ------------

#create list cache
c = [0] * 200000


def collatz_cache (x, cl):
    """
    Take a given number and store it's cycle length
    """
    global c

    if c[x] == 0:
        c[x] = cl
        
    else:
        return c[x]


# ------------
# collatz_eval
# ------------



def collatz_eval (i, j) :
    """
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    return the max cycle length in the range [i, j]
    """
    assert i > 0
    assert j > 0

    max_cycle_length = 0

    #fix input range if needed
    if i > j:
        i, j = j, i

    
    for x in range(i, j+1):

        global c
        
        if c[x] !=0:
            count = c[x]

        else:
            count = 1
            range_number = x
            
            while x != 1:
                
                count += 1
                
                if (x % 2) == 0:
                    x = int( x / 2 )

                    if x < 200000:
                        if c[x] != 0:
                            count += c[x]-1
                            x = 1
                    
                else:
                    x = 3 * x + 1
                    
            collatz_cache(range_number, count)

            
        #maintain max_cycle_length
        if count > max_cycle_length:
            max_cycle_length = count
    
    return max_cycle_length


# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    prints the values of i, j, and v
    w is a writer
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    v is the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    read, eval, print loop
    r is a reader
    w is a writer
    """
    a = [0, 0]
    while collatz_read(r, a) :
        v = collatz_eval(a[0], a[1])
        collatz_print(w, a[0], a[1], v)



# ------------------------------
# projects/collatz/RunCollatz.py
# Copyright (C) 2013
# Glenn P. Downing
# -------------------------------

"""
To run the program
    % python RunCollatz.py < RunCollatz.in > RunCollatz.out
    % chmod ugo+x RunCollatz.py
    % RunCollatz.py < RunCollatz.in > RunCollatz.out

To document the program
    % pydoc -w Collatz
"""

# -------
# imports
# -------

import sys

# ----
# main
# ----

collatz_solve(sys.stdin, sys.stdout)
