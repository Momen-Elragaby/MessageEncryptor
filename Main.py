"""
Name: <Momen Elragaby>
Purpose:    To write a Python solution that will encrypt and decrypt a message
            using a Vigenère cipher. Pseudocode to encrypt a message:
            1. Initialize an empty string.
            2. For each letter in the plaintext message:
                a. Determine which letter of the key to use.
                b. Using the key letter, look up the ciphertext letter in the
                    Vigenère square in the plaintext character column.
                c. Add the ciphertext letter to the ciphertext message.
            3. Return the resulting string as the ciphertext message.
Input:
Output:
"""
#########################
# IMPORTS
#########################
from string import ascii_uppercase

#########################
# CONSTANTS
#########################
_ALPHABET = ascii_uppercase
_LETTERS_IN_ALPHABET = len(_ALPHABET)


def valid_phrase(message):
    """
    valid_phrase checks that each character in the message is a letter
    in the uppercase alphabet constant _ALPHABET or is a space. Calls the
    .find() function.
    Parameter message may have a space and letters of the alphabet.
    Returns a True if the message is alphabetic, and
    a False otherwise.
    :param message: a message to encrypt or decrypt
    :type message: a string
    :return: a boolean, False if any character in the message is not
    alphabetic, and True otherwise.
    :rtype: boolean
    """
    # TODO
    if message == "":

        return False

    for characters in message:

        if characters == " ":
            continue

        if _ALPHABET.find(characters) == -1:

            return False

    return True


def letter_to_index(letter):
    """
    letter_to_index returns the index of the letter in the alphabet constant
    _ALPHABET.
    Calls the .find() function.
    :param letter: one of the letters in the message
    :type letter: a string
    :return: the index of the parameter in the alphabet string
    :rtype: string
    """
    # TODO
    pass
    letter_to_index = _ALPHABET.find(letter)
    return letter_to_index


def index_to_letter(idx):
    """
    index_to_letter returns the letter of the alphabet constant
    _ALPHABET, based on the parameter index.
    Calls the .find() function.
    :param idx: the index of the parameter in the alphabet string
    :type idx: a string
    :return: the letter from the alphabet at the index provided
    :rtype: string
    """
    # TODO - remove the word "pass" and type your solution
    idx = str(idx)
    for characters in _ALPHABET:

        idx_to_letter = str(_ALPHABET.find(characters))
        if idx_to_letter == idx:

            return characters


def vigenere_index(key_letter, plain_text_letter):
    """
    vigenere_index takes a letter from the key and a plaintext letter,
    and returns the encrypted letter.
    Calls the functions letter_to_index() and index_to_letter().
    :param key_letter: one letter from the key
    :type key_letter: String
    :param plain_text_letter:  one letter from the plain_text
    :type plain_text_letter: String
    :return: a single character as a string representing the
    encrypted letter
    :rtype: string
    """
    # TODO - remove the word "pass" and type your solution
    plain_input = int(letter_to_index(plain_text_letter))
    key_input = int(letter_to_index(key_letter))
    encrypt_num = (plain_input + key_input) % _LETTERS_IN_ALPHABET
    encrypt_num = str(encrypt_num)
    encrypt_letter = index_to_letter(encrypt_num)
    return encrypt_letter


def undo_vig(key_letter, ct_letter):
    """
    undo_vig takes a letter from the key and a ciphertext letter,
    and returns the plaintext letter.
    Calls the functions letter_to_index() and index_to_letter().
    :param key_letter: one letter from the key
    :type key_letter: string
    :param ct_letter:  one letter from the cypher text
    :type ct_letter: string
    :return: a string representing the unencrypted letter
    :rtype: string
    """
    # TODO - remove the word "pass" and type your solution
    key_input = int(letter_to_index(key_letter))
    ct_input = int(letter_to_index(ct_letter))
    decrypt_num = ((ct_input - key_input + _LETTERS_IN_ALPHABET) %
                   _LETTERS_IN_ALPHABET)
    decrypt_letter = str(decrypt_num)
    return index_to_letter(decrypt_letter)


def decrypt_vigenere(key, cipher_text):
    """
    decrypt_vigenere takes a keyword, the cipher text for the
    message, and returns the plain text message.
    Remove the spaces in the key before calling undo_vig().
    Calls the function undo_vig().
    :param key: The decryption key
    :type key: string
    :param cipher_text:  The cipher text
    :type cipher_text: string
    :return: Returns a string representing the decrypted text
    :rtype: string
    """
    # TODO - remove the word "pass" and type your solution
    decrypted_msg = ""
    key_letter = 0

    for characters in cipher_text:
        if characters == " ":

            decrypted_msg = decrypted_msg + characters
            if key_letter == len(key):
                key_letter = 0
            key_letter += 1
            continue

        if key_letter < len(key):

            decrypted_letter = undo_vig(key[key_letter], characters)
            key_letter = key_letter + 1
            decrypted_msg = decrypted_msg + decrypted_letter
            continue
        key_letter = 0
        decrypted_letter = undo_vig(key[key_letter], characters)
        key_letter += 1
        decrypted_msg = decrypted_msg + decrypted_letter

    return decrypted_msg


def encrypt_vigenere(key, plain_text):
    """
    encrypt_vigenere take a keyword and the plain text for the message,
    and returns the encrypted Vigenere cipher text.
    Remove the spaces in the key before calling undo_vig().
    Do not encode the spaces, simply copy them to the cipher text.
    Calls the function vigenere_index().
    Pseudocode to encrypt a message:
    1. Initialize an empty string.
    2. For each letter in the plaintext message:
        a. Determine which letter of the key to use.
        b. Using the key letter, look up the ciphertext letter in the
            Vigenère square in the plaintext character column.
        c. Add the ciphertext letter to the ciphertext message.
    3. Return the resulting string as the ciphertext message.
    :param key: The encryption key
    :type key: string
    :param plain_text:  The plain text
    :type plain_text: string
    :return: Returns a string representing the encrypted text
    :rtype: string
    """
    # TODO - remove the word "pass" and type your solution

    encrypted_msg = ""
    key_letter = 0

    for characters in plain_text:
        if characters == " ":

            encrypted_msg = encrypted_msg + characters
            if key_letter == len(key):

                key_letter = 0

            key_letter += 1
            continue
        if key_letter < len(key):

            encrypted_letter = vigenere_index(key[key_letter], characters)
            key_letter = key_letter + 1
            encrypted_msg = encrypted_msg + encrypted_letter
            continue

        key_letter = 0
        encrypted_letter = vigenere_index(key[key_letter], characters)
        key_letter += 1
        encrypted_msg = encrypted_msg + encrypted_letter

    return encrypted_msg


def get_message():
    """
    Prompts the user for the message to be encrypted.
    Calls the.upper() function to convert to uppercase.
    Returns the message to be encrypted.
    :return: the message to be encrypted
    :rtype: string
    """
    # TODO - remove the word "pass" and type your solution

    message = input("Enter the message to be encrypted: ").upper()
    return message


def get_cyphertext():
    """
    Prompts the user for the cipher text to decrypt.
    Returns the cipher text to decrypt.
    Calls the.upper() function to convert to uppercase.
    :return: the cipher text to decrypt
    :rtype: string
    """
    # TODO - remove the word "pass" and type your solution

    cypher_text = input("Enter the cypher text to decrypt: ").upper()

    return cypher_text


def get_key():
    """
    Prompts the user for the Vigenere key.
    Returns the Vigenere key in uppercase letters.
    Calls the .upper() function.
    :return: the Vigenere key
    :rtype: string
    """
    # TODO - remove the word "pass" and type your solution

    key = input("Enter the Vigenere key: ").upper()
    return key


def get_choice():
    """
    Prompts the user for their choice of E, Q, or D.
    Convert the response to uppercase letters, and remove the white space
    by using strip().
    Calls the .input(),.upper() and .strip() functions.
    Returns the choice.
    :return: A string "E", "Q", or "D" representing the choice
    :rtype: string
    """
    # TODO - remove the word "pass" and type your solution

    choice = input("Enter an E to encrypt a message, a D to decrypt a message, "
                   "and Q to quit: ").upper().strip()
    return choice


def main():
    """
    To write a Python solution that will encrypt and decrypt a message
    using a Vigenère cipher.
    Pseudocode:
    1. Get the choice from the user
    2. Validate the choice - must be an Q, E, or D
    3. Loop until the choice is Q
        a. get the key
        b. validate the key
        c. if choice is E
            1. get the plain text message
            2. validate the plain text message
            3. encrypt the message into cipher text
            4. print the cipher text message
        d. if choice is D
            1. get the cipher text message
            2. validate the cipher text message
            3. decrypt the message into plain text message
            4. print the plain text message
        e. Get the choice from the user
        f.  Validate the choice - must be an Q, E, or D
    """
    # TODO - remove the word "pass" and type your solution

    characters = get_choice()
    while characters != "":
        if characters == 'E':
            key = get_key()
            valid = valid_phrase(key)
            while not valid:
                print("Not a valid key! Letters must be in the alphabet.")
                key = get_key()
                valid = valid_phrase(key)
            encrypt_msg = get_message()
            valid = valid_phrase(encrypt_msg)
            while not valid:
                print("Not a valid key! Letters must be in the alphabet.")
                encrypt_msg = get_message()
                valid = valid_phrase(encrypt_msg)
            encrypt_msg = encrypt_vigenere(key, encrypt_msg)
            print(encrypt_msg)

        elif characters == 'D':
            key = get_key()
            valid = valid_phrase(key)
            while not valid:
                print("Not a valid key! Letters must be in the alphabet.")
                key = get_key()
                valid = valid_phrase(key)
            encrypt_msg = get_cyphertext()
            valid = valid_phrase(encrypt_msg)
            while not valid:
                print("Not a valid cypher! Letters must be in the alphabet.")
                encrypt_msg = get_cyphertext()
                valid = valid_phrase(encrypt_msg)
            encrypt_msg = decrypt_vigenere(key, encrypt_msg)
            print(encrypt_msg)

        elif characters == 'Q':
            break
        else:
            print("Invalid response!")
        characters = get_choice()
    return False


if __name__ == '__main__':
    main()
