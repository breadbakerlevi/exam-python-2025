# -*- coding: utf-8 -*-
"""
@author: Kandidatnr: 77
Question 1.
"""
import random

def read_file():
    words = []
    try:
        file = open("Q1_words.txt", "r")
        for line in file:
            words.append(line.strip().lower())
        file.close()
        return words
    except IOError:
        print("Error reading Q1_words.txt!")
        return []
    
    
def play_game(word):
    guessed = ['_'] * len(word)
    max_wrong = len(word)
    wrong_guesses = 0
    used_letters = []
    
    print(f"\nThe word you need to guess has '{len(word)}' characters.")
    print(f"\nYou have now {max_wrong} guesses.")
    print(' '.join(guessed))
    
    while wrong_guesses < max_wrong and '_' in guessed:
        guess = input("\nGuess a letter: ").lower()
        
        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single letter.")
            continue
        
        # Check for duplicated guesses
        if guess in used_letters:
            print(f"You have already guessed '{guess}'!")
            print(' '.join(guessed))
            print('-' * 34) 
            continue
        
        used_letters.append(guess)
        used_letters.sort()
        
        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed[i] = guess
            print("\n" + ' '.join(guessed))
            print('-' * 34) 
        else:
            wrong_guesses += 1 
            print(f"\nSorry '{guess}' is not in the word.")
            print("Guessed letters:", ', '.join(used_letters))
            print(f"You have {max_wrong - wrong_guesses} guess(es) left.\n") 
            print(' '.join(guessed))
            print('-' * 34)      
            
    if '_' not in guessed:
        print(f"\nYou found the word --> '{word}'\nCongratulations! You won!")
    else:
        print(f"\nSorry! You lost.\nThe word is --> '{word}'")
        
        
def main(): 
    words = read_file()
    
    print("=" * 34)
    print("Welcome to the Word Guessing Game!\nGuess letters between A-Z")
    print("=" * 34)
    
    while True:
        secret_word = random.choice(words)
        play_game(secret_word)
        
        replay = input("\nPlay again? (y/n) ").lower()
        if replay != 'y':
            print("Thanks for playing!")
            break
        print("\n" + "=" * 34 + "\n")
            
main()
