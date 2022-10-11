# Problem

For a non-empty array CC containing positive integers, let BB be a subsequence of array CC of size MM (1≤M≤∣C∣). We are going to play a drawing game based on the sequence BB:

Select MM points with positive integer coordinates on the XYXY -− plane such that the points (B_i, 0), (0, B_i ) and the i<sup>th</sup>
  selected point are collinear. Please note that multiple selected points can have the same coordinates.


Next, draw MM line segments. i<sup>th</sup>
  line segment should connect the origin (0, 0)(0,0) with the i<sup>th</sup> selected point.
The beauty of a line segment is equal to the number of points on the line segment that have integer coordinates. We want to maximize the sum of beauty over all line segments.

Let W(B)W(B) denote the number of ways to select MM points based on the sequence BB such that the sum of beauty over all line segments is maximized. Let SS be the sum of W(B)W(B) over all non-empty subsequences BB of the array CC.

You are given an array AA of size NN and QQ queries. In each query:

LL RR : Given two integers LL and RR (1≤L≤R≤N), define the array CC by keeping some elements in the range <sub>L…R</sub>
  and deleting the rest of the elements from AA without changing the order. Find out the number of distinct values of SS you can obtain over all the arrays CC.
Note that the array CC cannot be empty. In other words, you must keep at least one element from the range A_<sub>L…R</sub>
Since this number can be quite large, output your answer modulo 10<sup>9</sup>+7
## Input Format
The first line contains two space-separated integers NN and QQ.
The second line contains NN positive integers A<sub>1</sub>,..., A<sub>N</sub>
  where A<sub>i</sub>
  is the i<sup>th</sup>
  integer of the array AA.
Each of the next QQ lines contains two integers L<sub>j</sub>
  and R<sub>j</sub>
  denoting the j<sup>th</sup>
  query.
  
## Output Format
For each query, print the number of distinct values of SS you can obtain, if you can keep some elements in the range A<sub>L…R</sub> and then delete the rest from AA without changing the order modulo (10^9+7)
 
