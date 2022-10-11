# Problem
The beauty of a sequence of non-negative integers is computed in the following way: for each of its non-empty (not necessarily contiguous) subsequences, compute the XOR of all elements of this subsequence; then, sum up all the XORs you obtained.

Let F(N, B) denotes the number of non-negative integer sequences with length N which have beauty B. You are given three integers N, X and M. Find the smallest non-negative integer BB such that F(N, B) \bmod M = XF(N,B)modM=X, or determine that there is no such BB. Since even the smallest such BB might be very large, compute its remainder modulo 998,244,353998,244,353.

### Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first and only line of each test case contains three space-separated integers N, X and M.
### Output
For each test case, print a single line containing one integer ― the smallest valid B (modulo 998,244,353998,244,353), or -1 if there is no valid B.


##### NOTE: Codechef Problem
