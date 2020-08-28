import numpy
import string
import random
print("### Please use Integer values, and strings only.")
def find_word():                                                                    # obtain word, checking word length, testing whether it needs a random extra character.
    global word
    word = input("Input Word: " )
    global word_length
    word_length = len(word)
    if(word_length % 2 == 0):
        print("### No additional letter required.")
    else:
        print("### Additional letter required.")
        string.ascii_letters 
        'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-=!@#$%^&*()_+'
        word = word + random.choice(string.ascii_letters)

def find_characterset():
    global ascii_list
    ascii_list = [x for x in word.encode("ascii")]
    print(ascii_list)

def get_matrix_count():                                                             # check for the amount of character matrices needed.
    global matrix_count
    matrix_count = len(ascii_list)
    matrix_count = int((matrix_count / 2))
    print("Matrices needed? " + str(int(matrix_count)))

def find_matrix():
    while True:                                                                     # repeat forever until determinant is no longer a factor of 128.
        invalid_det = [2, 8, 16, 32, 64]
        a = int(input("Insert encryption matrix value 'a': "))
        b = int(input("Insert encryption matrix value 'b': "))
        c = int(input("Insert encryption matrix value 'c': "))
        d = int(input("Insert encryption matrix value 'd': "))
        global encryption_matrix_det 
        encryption_matrix_det = (a * d) - (b * c)
        if encryption_matrix_det in invalid_det:
            print(encryption_matrix_det)
            print("Invalid determinant!")
            continue
            
        else:
            global encryption_matrix
            encryption_matrix = numpy.array([[a, b], [c, d]])
            global inverted_matrix
            inverted_matrix = numpy.array([[d, (b * -1)], [(c * -1), a]])
            global decryption_matrix
            decryption_matrix = inverted_matrix * encryption_matrix_det             # inverse
            return
def final_calc():
    for i in range(0, len(ascii_list), 2):
        if i >= len(ascii_list):
            print("Complete!")
            break
        else:
            x = ascii_list[i]
            y = ascii_list[i+1]
            final_matrix = numpy.matmul(encryption_matrix, numpy.array([[x], [y]])) % 128
            char1 = chr(final_matrix[0, 0])
            char2 = chr(final_matrix[1, 0])
            char_list = ["Word: "]
            char_list.append(char1)
            char_list.append(char2)
            print(char_list)
find_word()
find_characterset()
get_matrix_count()
find_matrix()
final_calc()
### get inverse matrix multiplied by all numbers inside matrix then modulo by 128 to decrypt
