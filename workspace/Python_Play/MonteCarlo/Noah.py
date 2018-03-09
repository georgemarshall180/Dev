' Filename:   '
' Created by: George Marshall '
import sys

def first_name(str) -> object:

    first = len(str)/2
    num = int(first)
    # print('first is: ' + repr(num))

    if first < 1:
        return str

    return str[:num]

def main():
# start of main
    x = first_name('whoo')
    y = first_name('oooo')
    z = first_name('haaa')

    print(x)
    print(y)
    print(z)

# runs this file if it is main
if __name__ == "__main__":
    main()
    
    
    
    
    
    
    