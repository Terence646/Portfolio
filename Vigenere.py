#!/usr/bin/python3

from ast import Num
import sys
from collections import Counter

# Easier to Access than a Dictionary
l_freq = [0.08167,0.01492,0.02782,0.04253,0.12702,0.02228,0.02015,0.06094,0.06966,0.00153,0.00772,0.04025,0.02406,0.06749,0.07507,0.01929,0.00095,0.05987,0.06327,0.09056,0.02758,0.00978,0.02361,0.00150,0.01974,0.00074]

#taken from Wikipedia
letter_freqs = {
    'A': 0.08167,
    'B': 0.01492,
    'C': 0.02782,
    'D': 0.04253,
    'E': 0.12702,
    'F': 0.02228,
    'G': 0.02015,
    'H': 0.06094,
    'I': 0.06966,
    'J': 0.00153,
    'K': 0.00772,
    'L': 0.04025,
    'M': 0.02406,
    'N': 0.06749,
    'O': 0.07507,
    'P': 0.01929,
    'Q': 0.00095,
    'R': 0.05987,
    'S': 0.06327,
    'T': 0.09056,
    'U': 0.02758,
    'V': 0.00978,
    'W': 0.02361,
    'X': 0.00150,
    'Y': 0.01974,
    'Z': 0.00074
}
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 

def IOC(s): # Calculates the index of coincidence
    NumofOcc = [0]*26   # Initial Array of Zeros 
    i = 0
    sum = 0
    for char in s:
        NumofOcc[letters.index(char)] += 1.0
    for index in range(26):
        sum += NumofOcc[index]
        i += NumofOcc[index]*(NumofOcc[index] -1)
    return 26*i/(sum*(sum-1)) # Returns the index of occ.

def split_cypher(text, key_length): # Splits Cypher into portions based on the key length, returns a list 
    caesars = []
    for i in range(key_length):
        temp = text[i::key_length]
        caesars.append(temp) # Add to list
    return caesars

def pop_var(s):
    """Calculate the population variance of letter frequencies in given string."""
    freqs = Counter(s)
    mean = sum(float(v)/len(s) for v in freqs.values())/len(freqs)  
    return sum((float(freqs[c])/len(s)-mean)**2 for c in freqs)/len(freqs)

def find_key_length(s): # Calculates Key length based on IOC
    isfound = False
    length = 0
    while not isfound:
        length += 1
        ceasar_slices = [''] * length
        for i in range(len(s)):
            ceasar_slices[i % length] += s[i]
        total = 0
        for i in range(length):
            total += IOC(ceasar_slices[i])
        Index = total / length
        if Index > 1.6:
            isfound = True
    return length

def decript_ceasar(text): # Decripts Ceasar cypher and returns key
    numCount = [0] * 26
    sum = 0
    max_freq = 0 
    key = 0
    for char in text:
        numCount[letters.index(char)] += 1
    for i in range(len(numCount)):
        sum += numCount[i]
    for i in range(len(numCount)):
        numCount[i] = numCount[i]/sum
    for j in range(len(numCount)):
        curr_freq = 0 
        for i in range(len(numCount)):
            curr_freq += numCount[i]*l_freq[i]
        if(curr_freq >= max_freq):
            max_freq = curr_freq
            key = j
        numCount = numCount[1:] + numCount[:1] # Rotate through letter frequencies, (shift values by slicing list)
    return key


if __name__ == "__main__":
    # Read ciphertext from stdin
    # Ignore line breaks and spaces, convert to all upper case
    cipher = sys.stdin.read().replace("\n", "").replace(" ", "").upper()
    #################################################################
    # Your code to determine the key and decrypt the ciphertext here
    Encript_Key = [] #Initalize Empty List and String
    keys_letter = ''
    length = find_key_length(cipher)
    c_cipher = split_cypher(cipher, length)
    for k in range(length):
        letter = decript_ceasar(c_cipher[k])
        Encript_Key.append(letter)
        keys_letter = keys_letter + letters[letter]
    print(keys_letter) # Print Key Output
