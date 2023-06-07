"""
####################
### ALGORITHM ###
    Algorithm = a formula for solving a computational problem
    Algorithm =  a series of operations carried out using various data structures to solve a programming problem
####################

####################
### PROCEDURE ###
    1. Problem / task formulation
    2. Determining the input data
    3. Determining the result
    4. Finding a method to complete the task
    5. Expressing the algorithm by using the selected method
    6. Analysing and testing the algorithm
    7. Evaluating the effectiveness of the algorithm
####################

######################
### REPRESENTATION ###
    1. Natural language
        You are givena dictionary with MORSE DECODE (MORSE_TO_CHR -> code: letter) and a list of codes.
        Create a function for each task:
            a. create a dictionary with MORSE CODE (CHR_TO_MORSE -> letter:code)
            b. decode a list with morse codes and save it to another list
            c. code again the list generated at b. and see if it is the same as original
    2. Code
    3. Pseudocode
        ### FOR block from decode_morse function ###
        final_sentence = ""

        FOR EACH word IN my_words_list
            my_letters_list = word.split("   ")

            FOR EACH letter in my_letter_list
                IF letter == "" THEN
                    SKIP
                ELSE
                    IF letter NOT IN MORSE_TO_CHR then
                        print error

                ELSE
                    concatenate letter to final sentence
            END FOR
        END FOR
    4. Block Diagram -> https://www.diagrameditor.com/
        ### code_morse function code block ###
######################
"""

import time
import winsound

freq = 440 # Hz
dotLength = 500 # milliseconds
dashLength = dotLength * 3
spaceLength = dotLength * 6

MORSE_TO_CHR = {
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
    '--..': 'Z',
    '-----': '0',
    '.----': '1',
    '..---': '2',
    '...--': '3',
    '....-': '4',
    '.....': '5',
    '-....': '6',
    '--...': '7',
    '---..': '8',
    '----.': '9',
    '.-.-.-': '.',
    '--..--': ',',
    '..--..': '?',
    '.----.': "'",
    '-.-.--': "!",
    '-..-.-': "/",
    '-.--.': '(',
	'-.--.-': ')',
	'.-...': '&',
	'---...': ':',
	'-.-.-.': ';',
	'-...-': '=',
	'.-.-.': '+',
	'-....-': '-',
	'..--.-': '_',
	'.-..-.': '"',
	'...-..-': '$',
	'.--.-.': '@',
	'...---...': 'SOS'
}

def beep(dur):
    """
    makes noise for specific duration
    :param dur: duration of beep in milliseconds
    """
    winsound.Beep(freq, dur)
    print(f"This is a beep for {dur}.")

def pause(dur):
    """
    pauses audio for dur milliseconds
    :param dur: duration of pause in milliseconds
    """
    time.sleep(dur / 1000)
    print(f"This is a pause for {dur}")

def morseaudio(morse):
    """
    plays audio for dur milliseconds
    :param morse: morse code string
    """
    for char in morse:
        if char == ".":
            beep(dotLength)
        elif char == "-":
            beep(dashLength)
        else:
            pause(spaceLength)

def code_morse(normal_text):

    ###################################################
    ### split string by 1 spaces ###
    ### for each letter in each word ###
    ### search letter in MORSE_TO_CHR ###
    ### if letter not in dictionary then ERR ###
    ### if letter in dictionary then append letter to final sentence ###
    ###################################################

    ###################################################
    ### code area ###

    my_word_list = normal_text.split(" ")
    final_sentence = ""

    for word in my_word_list:

        for letter in word:

            if letter.upper() not in MORSE_TO_CHR.values():
                print(f"LETTER: {letter.upper()} was not found in dictionary!")
                return

            else:
                for key, value in MORSE_TO_CHR.items():
                    if value == letter.upper():
                        final_sentence += f"{key} "

        final_sentence += "   "

    print(f"\n{normal_text} = \n{final_sentence}\n")
    morseaudio(final_sentence)
    ###################################################


def main():
    winsound.Beep(440, 2000)
    my_text = input("Please insert the phrase to convert to Morse Code: \n=> ")
    code_morse(my_text)

if __name__ == '__main__':
    main()