#Problem
You have three lists of words. Create all possible combinations of sentences by taking one element from each list.

#Hint
For each list, run a for loop for its len. This would be nested three for loops.
Under the last loop, access elements from each loop and show them as output.

#Solution
subjects=["I", "You"]
verbs=["Play", "Love"]
objects=["Hockey","Football"]
for i in range(len(subjects)):
   for j in range(len(verbs)):
       for k in range(len(objects)):
           print (subjects[i], verbs[j], objects[k])