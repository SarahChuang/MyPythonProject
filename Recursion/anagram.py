"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    This program recursively finds all the anagram(s)
    for the word input by user and terminates when the
    input string matches the EXIT constant.
    """
    print("Welcome to stanCode ''Anagram Generator'' (or -1 to quit)")
    s = input("Find anagrams for: ")
    start = time.time()
    while True:
        if s == EXIT:
            break
        else:
            anagrams = find_anagrams(s)
            print(str(len(anagrams)) + " anagrams: ", end="")
            print(anagrams)
            end = time.time()
            s = input("Find anagrams for: ")
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    lst = []
    with open(FILE, "r")as f:
        for line in f:
            line = line.strip()
            lst.append(line)
    return lst


def list_to_str(the_list):
    word = ""
    for c in the_list:
        word += c
    return word


def find_anagrams(s):
    """
    :param s: str, the word that user input
    :return: lst, the result of anagram
    """
    ch_used = []
    answer = []
    answer_list = []
    d = read_dictionary()
    for i in range(0, len(s)):
        ch_used.append(0)
        answer.append("")
    find_anagrams_helper(s, 0, answer, answer_list, ch_used, d)
    return answer_list


def find_anagrams_helper(s, index, answer, answer_lst, ch_used, d):
    if index == len(s):
        word = list_to_str(answer)
        if word not in answer_lst:
            if word in d:
                answer_lst.append(word)
                print("Searching...")
                print("Found: " + word)
    else:
        for i in range(0, len(s)):
            if ch_used[i] == 0:
                ch_used[i] = 1
                answer[index] = s[i]
                if index == 1:
                    word = list_to_str(answer)[0:2]
                    if has_prefix(word):
                        find_anagrams_helper(s, index+1, answer, answer_lst, ch_used, d)
                else:
                    find_anagrams_helper(s, index+1, answer, answer_lst, ch_used, d)
                ch_used[i] = 0


def has_prefix(sub_s):
    """
    :param sub_s: str, the words that are composed with the alphabet that user input
    :return: bool, the word in dictionary which is start with sub_s
    """
    d = read_dictionary()
    result = has_prefix_helper(sub_s, d)
    return result


def has_prefix_helper(sub_s, d):
    r = False
    for s in d:
        if s.startswith(sub_s):
            r = True
            break
    return r


if __name__ == '__main__':
    main()
