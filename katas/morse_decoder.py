def decode(string):
    """
    ARGS:
    String - of morse code characters.
    Space between each char.  Four spaces between each word.

    RETURNS:
    String of decoded morse code characters.
    """
    if not isinstance(string, str):
        raise TypeError('String only!')

    morse_code_dict = {
        '.-': 'A',
        '-...': 'B',
        '-.-.': 'C',
        '-..': 'D',
        '.': 'E',
        '..-.': 'F',
        '--.': 'G',
        '....': 'H',
        '..': 'I',
        '.---': 'J',
        '-.-': 'K',
        '.-..': 'L',
        '--': 'M',
        '-.': 'N',
        '---': 'O',
        '.--.': 'P',
        '--.-': 'Q',
        '.-.': 'R',
        '...': 'S',
        '-': 'T',
        '..-': 'U',
        '...-': 'V',
        '.--': 'W',
        '-..-': 'X',
        '-.--': 'Y',
        '--..': 'Z'
    }

    decoded = []

    ls = string.split('    ')

    for word in ls:
        new_word = ''
        word_ls = word.split(' ')
        for letter in word_ls:
            if letter not in morse_code_dict:
                new_word += letter
            else:
                new_word += morse_code_dict[letter]
        decoded.append(new_word)

    return ' '.join(decoded)
