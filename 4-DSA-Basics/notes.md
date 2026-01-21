# Big O Notation Notes

cheatsheet: https://www.bigocheatsheet.com

O(1) - constant

O(log n) - logarithmic

O(n) - linear

O(n ^ 2) - squared

O(2 ^ n) - exponential

O(n!) - factorial



O(1) == no matter the size of the input there is no growth in the runtime of the algorithm

O(n) == 1 for-loop

O(n ^ 2) == 2 for-loop


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