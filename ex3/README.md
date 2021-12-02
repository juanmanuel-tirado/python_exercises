# Anagrams

It is often fun to see if rearranging the letters of a name gives an amusing anagram. For example, the
letters of ‘WILLIAM SHAKESPEARE’ rearrange to form ‘SPEAK REALISM AWHILE’.
Write a program that will read in a dictionary and a list of phrases and determine which words from
the dictionary, if any, form anagrams of the given phrases. Your program must find all sets of words in
the dictionary which can be formed from the letters in each phrase. Each word
from the dictionary can only be used once. If no anagram is present, do not write anything, not even a blank line.

## Input
Input will consist of two parts. The first part is the dictionary in alphabetical order, the second part is the set of phrases
for which you need to find anagrams. The dictionary part of the file will be terminated by a line consisting of a
single ‘#’. 

## Output
Output will consist of a series of lines. Each line will consist of the original phrase, a space, an equal
sign (=), another space, and the list of words that together make up an anagram of the original phrase,
separated by exactly one space. These words must appear in alphabetic order.

## Sample Input
```
IS
THIS
SPARTA
#
ATRAPS
ATRAPS SI
THIS IS SPARTA
#
```

## Sample Output
```
ATRAPS = SPARTA
ATRAPS SI = IS SPARTA
ATRAPS SI = SPARTA IS
THIS IS SPARTA = IS SPARTA THIS
THIS IS SPARTA = IS THIS SPARTA
THIS IS SPARTA = SPARTA IS THIS
THIS IS SPARTA = SPARTA THIS IS
THIS IS SPARTA = THIS IS SPARTA
THIS IS SPARTA = THIS SPARTA IS
```