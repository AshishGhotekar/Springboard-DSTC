def c_cipher(message, shift):    if type(message) != str:        print('The message is not a string.')    elif type(shift) != int:        print('The shift is not an integer.')    else:        new_message = ''        for char in message:            new_char = chr(ord(char) + shift)            new_message += new_char        print(new_message)