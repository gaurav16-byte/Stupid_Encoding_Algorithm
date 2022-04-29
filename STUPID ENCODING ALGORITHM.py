from random import randint, choice

string = input("Enter a string: ")

def encode(string):
    alpha_to_num = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
    num_to_alpha = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'}
    output = ""

    for i in string:
        current_alpha = i
        if current_alpha.isalpha() == False:
            output += 2 * current_alpha
        else:
            pos = alpha_to_num[current_alpha.lower()]
            final = choice((pos, pos + 26))
            if final == 1:
                if current_alpha.islower() == True:
                    output += choice(('az', 'za', 'Az', 'aZ', 'zA', 'Za'))
                elif current_alpha.isupper() == True:
                    output += choice(('AZ', 'ZA'))

            elif final < 26:
                num_1 = randint(1, pos - 1)
                num_2 = final - num_1
                if current_alpha.islower() == True:
                    tab = [num_to_alpha[num_1].lower(), num_to_alpha[num_1].upper()]
                    ch = choice(tab)
                    if ch.isupper() == True:
                        output += ch + num_to_alpha[num_2].lower()
                    else:
                        output += ch + choice([num_to_alpha[num_2].lower(), num_to_alpha[num_2].upper()])

                elif current_alpha.isupper() == True:
                    output += num_to_alpha[num_1].upper() + num_to_alpha[num_2].upper()

            elif final > 26:
                num_1 = randint(pos, 26)
                num_2 = final - num_1
                if current_alpha.islower() == True:
                    tab = [num_to_alpha[num_1].lower(), num_to_alpha[num_1].upper()]
                    ch = choice(tab)
                    if ch.isupper() == True:
                        output += ch + num_to_alpha[num_2].lower()
                    else:
                        output += ch + choice([num_to_alpha[num_2].lower(), num_to_alpha[num_2].upper()])

                elif current_alpha.isupper() == True:
                    output += num_to_alpha[num_1].upper() + num_to_alpha[num_2].upper()

    return output

def decode(string):
    alpha_to_num = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
    num_to_alpha = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'}
    output = ""
    for i in range(0, len(string), 2):
        piece = ""
        summ = 0
        for j in range(i, i+2):
            piece += string[j]
            
        if piece.isalpha() == False:
            output += piece[0]

        elif piece.isupper() == True:
            summ += alpha_to_num[piece[0].lower()]
            summ += alpha_to_num[piece[1].lower()]
            output += num_to_alpha[summ % 26].upper()

        else:
            summ += alpha_to_num[piece[0].lower()]
            summ += alpha_to_num[piece[1].lower()]
            output += num_to_alpha[summ % 26].lower()

    return output

print("ENCODED:", encode(string))
print("DECODED:", decode(encode(string)))
