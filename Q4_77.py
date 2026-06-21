# -*- coding: utf-8 -*-
"""
@author: Kandidatnr: 77
Question 4.
"""

def main():
    print("== Palindrome Checker ==\n")
    
    while True:
        user_input = input("Enter a string: ")
        if user_input == "":
            print("Please enter a string.")
        else:
            break
        
    for char in user_input:
        if not(('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9') or char == ' '):
            print(f"Error: Character '{char}' is not recognized. Please only use letters from A-Z, numbers or space.")
            return
    
    cleaned = ""
    for char in user_input:
        if ('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9'):
            cleaned += char.lower()
            
    is_palindrome = True
    length = len(cleaned)
    for i in range(length // 2):
        if cleaned[i] != cleaned[length - 1 - i]:
            is_palindrome = False
            break
     
    if is_palindrome:
        print(f"\n'{user_input}' is a palindrome!")
    else:
        print(f"\nUnfortunately, '{user_input}' is not a palindrome!")
    
main()