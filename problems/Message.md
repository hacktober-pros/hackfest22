# Problem

One day, you decided to write a message to your girl friend consisting of N uppercase English letters.

Your girlfriend's alphabet is limited to only two letters: 'A' and 'B'. She recognizes only the words that are of length M containing letters from her alphabet.

There are some words that your girlfriend hates. You are given two strings X and Y, which represent some two words she recognizes. Your girlfriend hates words X, Y and also each word that she recognizes and is lexicographically greater than X and smaller than Y .

For example, if M = 3, X = "ABA" and Y = "BBA" then all words the girlfriend hates are: "ABA", "ABB", "BAA", "BAB" and "BBA". Note that she doesn't hate words "AAA", "BB", "AC" or "BCAD".

The message that you will send to the girlfriend should not contain any of words she hates as a substring. Note that the message can contain letters the girl doesn't recognize. The message will contain N uppercase English letters. Find the number of different messages you can send. Since the answer can be large, output it modulo (109 + 7).

## Input
The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows.

The first line of each test case contains two integers N and M.

The second line contains the string X and the third line contains the string Y, both of length M.

## Output
For each test case, output a single line containing the answer to the corresponding test case, modulo (109 + 7).

#### NOTE: Codechef problem
