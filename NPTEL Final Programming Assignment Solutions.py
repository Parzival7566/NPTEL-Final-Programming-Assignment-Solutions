#NPTEL Final Programming Assignment Solutions
#By Parzival7566
'''Q1 Here is a function isprimebad that takes a positive integer as input and
 returns True if the number is prime and False otherwise. There is an error in 
 this function. Provide an input n, which is a positive integer, for which isprimebad 
 produces an incorrect output.'''
 #soln=4
 
'''Q2 Here is a function lexsortbad that takes a list of pairs of integers as input 
 and returns them in lexicographically sorted order (i.e., dictionary order). There is 
 an error is this function. Provide an input for which lexsortbad produces an incorrect
 output. Your input should be a list of pairs of integers of the form [(i1,j1),(i2,j2),...,(in,jn)].'''
  #soln=[(1,2),(2,1)]
  
'''Q3 Here is a function to compute the smallest of three input integers.
  You have to fill in the missing lines.'''
  #soln
'''     else:
      minimum=z
  elif y<=z and y<=x:
    minimum=y
  else:
    minimum=z'''
    
'''Q4 A list is a non-decreasing if each element is at least as big as the preceding one.
 For instance [], [7], [8,8,11] and [3,19,44,44,63,89] are non-decreasing, while
 [3,18,4] and [23,14,3,14,3,23] are not. Here is a recursive function to check if a list is 
 non-decreasing. You have to fill in the missing argument for the recursive call.'''
 #soln
'''l[0]<=l[1] and nondecreasing(l[1:])'''
   
'''Q5 A positive integer n is a sum of squares if n = i2 + j2 for integers i,j 
 such that i ≥ 1 and j ≥ 1. For instance, 10 is a sum of squares because 10 = 12 + 32,
 and so is 25 (32 + 42). On the other hand, 11 and 3 are not sums of squares.

Write a Python function sumofsquares(n) that takes a positive integer argument and 
returns True if the integer is a sum of squares, and False otherwise.'''
 #soln
import math
def sumofsquares(n) : 
  i = 1
  while math.pow(i,2) <= n : 
    j = 1
    while(math.pow(j,2)<= n) : 
      if (math.pow(i,2) + math.pow(j,2) == n) : 
        return True
      j+=1
    i+=1  
  return False

'''Q6 Write a Python function subsequence(l1,l2) that takes two sorted lists as 
 arguments and returns True if the the first list is a subsequence of the second 
 list, and returns False otherwise.

A subsequence of a list is obtained by dropping some values. 
Thus, [2,3,4] and [2,2,5] are subsequences of [2,2,3,4,5], but [2,4,4] and [2,4,3] are not'''
 #soln
def subsequence(l1, l2):
  count = 0
  for i in l1:
    if i in l2:
      l2.remove(i)
      count += 1
  if count == len(l1):
    return(True)
  else:
    return(False)

'''Q7 Write a Python program that reads input from the keyboard (standard input). 
 The input will consist of some number of lines of text. The input will be terminated 
 by a blank line. The first line will consist of a single word to be interpreted as a pattern,
 after discarding the new line character. Your program should print every line from the second 
 line onward that contains an occurrence of the pattern. You can assume that the input will
 have a non-empty pattern line. Recall that for a string s and a pattern p, s.find(p) returns
 the first position in s where p occurs, and returns -1 if p does not occur in s.
'''
 #soln
x = input()
y =x
l =[]
while x != "":
    x = input()
    l.append(x)
for i in range(0,len(l)):
    if l[i].find(y) != -1:
        print(l[i])
        
'''Q8 Write a Python function maxaggregate(l) that takes a list of pairs of the form 
 (name,score) as argument, where name is a string and score is an integer. Each pair is to 
 be interpreted as the score of the named player. For instance, an input of the form 
 [('Kohli',73),('Ashwin',33),('Kohli',7),('Pujara',122),('Ashwin',90)] represents two scores 
 of 73 and 7 for Kohli, two scores of 33 and 90 for Ashwin and one score of 122 for Pujara.
 Your function should compute the players who have the highest aggregate score 
 (aggegrate = total, so add up all scores for that name) and return the list of names 
 of these players as a list, sorted in alphabetical order. If there is a single player, the 
 list will contain a single name.

For instance, maxaggregate([('Kohli',73),('Ashwin',33),('Kohli',7),('Pujara',122),('Ashwin',90)]) 
should return ['Ashwin'] because the aggregate score of Kolhi is 80, of Ashwin is 123 and of 
Pujara is 122, of which 123 is the highest.'''
 #soln
def maxaggregate(l):
  tracker = {}
  for i in l:
    if i[0] in tracker:
      tracker[i[0]] += i[1]
    else:
      tracker[i[0]] = i[1]
  m = max(list(tracker.values()))
  x = []
  for i in tracker:
    if tracker[i] == m:
      x.append(i)
  return sorted(x)
