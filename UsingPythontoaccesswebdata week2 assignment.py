"""
Week 2 Assignment
Finding Numbers in a Haystack

Data Format
The file contains much of the text from the introduction of the textbook except that random numbers
are inserted throughout the text. Here is a sample of the output you might see:

Why should you learn to write programs? 7746
12 1929 8827
Writing programs (or programming) is a very creative
7 and rewarding activity.  You can write programs for
many reasons, ranging from making your living to solving
8837 a difficult data analysis problem to having fun to helping 128
someone else solve a problem.  This book assumes that
everyone needs to know how to program ...

The sum for the sample text above is 27486. The numbers can appear anywhere in the line.
There can be any number of numbers in each line (including none).

Handling The Data
The basic outline of this problem is to read the file, look for integers using the re.findall(),
looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers
and summing up the integers.
"""

import re

#Extracting Digits and Summing them
hand = open("regex_sum_1697962.txt")
numlist = []

for line in hand:
    line = line.rstrip()
    extract = re.findall('[0-9]+',line)

    if len(extract) < 1: continue

    for i in range(len(extract)):
        num = float(extract[i])
        numlist.append(num)

print(sum(numlist))




