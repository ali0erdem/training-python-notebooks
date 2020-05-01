from math import log
import sys

DIGIT_MAP = {
'zero' : '0',
'one' : '1',
'two' : '2',
'three' : '3',
'four' : '4',
'five' : '5',
'six' : '6',
'seven' : '7',
'eight' : '8',
'nine' : '9'
}

def convert6(s):
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        return int(number)
    
    except (KeyError, TypeError) as e:
        print(f"Conversion error: {e!r}",
              file=sys.stderr)
        raise

def string_log(s):
    v = convert6(s)
    return log(v)