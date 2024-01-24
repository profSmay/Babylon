def sqrt(a, precision=0.01):
    """
    This calculates the square root of a with a prescribed precision
    :param a: the number I want the square root of
    :param precision: the precision I want
    :return: the square root of a
    """

    """
    Algorithm (in English):
    1.	Desire to find the square root of a with a certain precision:   sqrt(a,precision)
    2.	Guess r0=a/2  # no good reason to start here, but I’ve got to start somewhere
    3.	Calculate next guess as:  r1=0.5(ro+a/ro).
    4.	Calculate difference:  Delta=abs(ro-r1)
    5.	Is Delta<precision?  Return r1
    6.	Set ro=r1 and calculate again until Delta<precision
    """
    #step 1: Desire to find the square root of a with a certain precision:   sqrt(a,precision)
    #step 2: Guess r0=a/2  # no good reason to start here, but I’ve got to start somewhere
    r0=a/2
    for i in range(0,100):
        #step 3: Calculate next guess as:  r1=0.5(ro+a/ro).
        r1 = 0.5*(r0+a/r0)
        #step 4: Calculate difference:  Delta=abs(ro-r1)
        Delta = abs(r0-r1)
        #step 5: Is Delta<precision?  Return r1
        if Delta<=precision:
            return r1
        #Step 6: Set ro=r1 and calculate again until Delta<precision
        r0=r1
    return r1

def main():
    R = sqrt(90, 0.00000001)
    print(R)
    print(R*R)
main()