# Big O Notation Notes

cheatsheet: https://www.bigocheatsheet.com

O(1)        - constant (best) : the algorithm always takes the same amount of time, regardless of how much data there is i.g. looking up an item in a list by index

O(log n)    - logarithmic (great) : algorithms that remove a percentage of the total steps with each iteration, very fast i.g. binary search

O(n)        - linear (good) : i.g. unsorted array search

O(n log n)  - "linearithmic" (okay) : slightly worse than linear i.g. mergesort and other "fast" sorting algorithms

O(n ^ 2)    - quadratic (slow) : i.g. nested for loop to find all the ordered pairs in a list

O(n ^ 3)    - cubic (slower) : i.g. a triple nested for loop to find all the ordered triples in a list

O(2 ^ n)    - exponential (bad) : i.g. brute force guessing results of a sequence of "n" coin flips

O(n!)       - factorial (terrible) : i.g. generating all the permutations of a list



O(1) == no matter the size of the input there is no growth in the runtime of the algorithm

O(n) == 1 for-loop

O(n ^ 2) == two for-loops


Algorithm Time Complexity:
- merge sort        -> O(n log n) 
- insertion sort    -> O(n^2): best used in small data sets that are "semi-sorted"
- quick sort        -> O(n * log(n))
- selection sort    ->

---

Algorithms can be classified into two categories:
- Polynomial
  - O(1)
  - O(n)
  - O(n * log(n))
  - O(n ^ x)
- Exponential
  - O(x ^ n)
  - O(n ^ n)
  - O(n!)