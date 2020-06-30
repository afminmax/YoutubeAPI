# EXAMPLE 1
# here we run a block of code
# if it works, then we print the result via the else conditional block
# if it does not work, then we run a custom error statement
try:
    result = 10 + 50
except:
    print('The block does not work!')
else:
    print(result)

# EXAMPLE 2
try:
    f = open('blah.txt', 'r')  # error will be produced, read
    f.write('a test line')  # this is a write, an IO Error
except TypeError:
    print('there was a type error!')
except OSError:
    print('Hey you have an IO error!')
    # always runs no matter what
finally:
    print('i always run')

# EXAMPLE 3
try:
    filex = open('blah.txt', 'w')  # error will be produced, read
    filex.write('a test line')  # this is a write, an IO Error
except:
    print('All other exceptions')
    # always runs no matter what
finally:
    print('i always run')


# EXAMPLE 4 - with a more realistic function

def ask_for_int():
    while True:
        try:
            result = int(input('please provide a number: '))
        except:
            print('hey thats not a number')
            continue
        else:
            print('yes, ty for the NUMBER')
            break
        finally:
            print('end of TEF')
            print(result)


ask_for_int()
