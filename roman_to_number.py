import re

"""
convert roman to integer
"""
def roman_integer(roman):
    roman = roman.upper() # for taking care of upper or lower case letters
    integer_rep = 0
    roman_to_integer_map = tuple()
    roman_to_integer_map = (('M',1000),
                            ('CM',900),
                            ('D',500),
                            ('CD',400),
                            ('C',100),
                            ('XC',90),
                            ('L',50),
                            ('XL',40),
                            ('X',10),
                            ('IX',9),
                            ('V',5),
                            ('IV',4),
                            ('I',1))
    roman_numeral_pattern = re.compile("""
    ^                   # beginning of string
    M{0,4}              # thousands - 0 to 4 M's
    (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 C's),
                        #            or 500-800 (D, followed by 0 to 3 C's)
    (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 X's),
                        #        or 50-80 (L, followed by 0 to 3 X's)
    (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 I's),
                        #        or 5-8 (V, followed by 0 to 3 I's)
    $                   # end of string
    """ ,re.VERBOSE)

    if not roman_numeral_pattern.search(roman):
        return 0
    index = 0
    for numeral, integer in roman_to_integer_map:
        while roman[index:index+len(numeral)] == numeral:
            #print numeral, integer, 'matched'
            integer_rep += integer
            index += len(numeral)
    return integer_rep

def test():
	L = roman_integer
	assert L('iii') == 3
	assert L('iiv') == 0
	assert L('iv') == 4
	assert L('ix') == 9
	assert L('xl') == 40
	assert L('xc') == 90
	print 'Roman numerals: pass test'

test()