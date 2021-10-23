# Daily Coding Problems

### [Problem #819 [Easy]](number_problems/problem_819.py)
This problem was asked by Facebook.

Given an array of numbers representing the stock prices of a company in chronological order, write a function that 
calculates the maximum profit you could have made from buying and selling that stock once. You must buy before 
you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it 
at 10 dollars.

### [Problem #814 [Easy]](number_problems/problem_814.py)
This problem was asked by Microsoft.

Let's represent an integer in a linked list format by having each node represent a digit in the number. The nodes make up 
the number in reversed order.

For example, the following linked list:

`1 -> 2 -> 3 -> 4 -> 5`

is the number 54321.

Given two linked lists in this format, return their sum in the same linked list format.

For example, given

`9 -> 9`

`5 -> 2`

return 124 (99 + 25) as:

`4 -> 2 -> 1`

### [Problem #809 [Easy]](string_problems/problem_809.py)
This problem was asked by Facebook.

Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string `([])[]({})`, you should return true.

Given the string `([)]` or `((()`, you should return false.

### [Problem #805 [Easy]](string_problems/problem_805.py)
This problem was asked by Dropbox.

Spreadsheets often use this alphabetical encoding for its columns: "A", "B", "C", ..., "AA", "AB", ..., "ZZ", "AAA", 
"AAB", ....

Given a column number, return its alphabetical column id. For example, given 1, return "A". Given 27, return "AA".

### [Problem #801 [Easy]](number_problems/problem_801.py)
This problem was asked by Zillow.

Let's define a "sevenish" number to be one which is either a power of `7`, or the sum of unique powers of `7`. 
The first few sevenish numbers are `1`, `7`, `8`, `49`, and so on. Create an algorithm to find the `n`th sevenish number.

### [Problem #797 [Easy]](number_problems/problem_797.py)
This problem was asked by Alibaba.

Given an even number (greater than 2), return two prime numbers whose sum will be equal to the given number.

A solution will always exist. See Goldbach’s conjecture.

Example:
```
Input: 4
Output: 2 + 2 = 4
```
If there are more than one solution possible, return the lexicographically smaller solution.

If [a, b] is one solution with a <= b, and [c, d] is another solution with c <= d, then

`[a, b] < [c, d]`

If a < c OR a==c AND b < d.

### [Problem #794 [Easy]](data_structures/problem_794.py)
This problem was asked by Amazon.

Implement a stack that has the following methods:

* push(val), which pushes an element onto the stack
* pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
* max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.

Each method should run in constant time.

### [Problem #786 [Medium]](number_problems/problem_786.py)
his problem was asked by Google.

Implement integer exponentiation. That is, implement the `pow(x, y)` function, where `x` and `y` are integers and 
returns `x^y`.

Do this faster than the naive method of repeated multiplication.

For example, `pow(2, 10)` should return 1024.

### [Problem #774 [Easy]](others/problem_774.py)
This problem was asked Microsoft.

Using a read7() method that returns 7 characters from a file, implement readN(n) which reads n characters.

For example, given a file with the content “Hello world”, three read7() returns “Hello w”, “orld” and then “”.

### [Problem #771 [Easy]](string_problems/problem_771.py)
This problem was asked by Bloomberg.

Determine whether there exists a one-to-one character mapping from one string `s1` to another `s2`.

For example, given `s1` = `abc` and `s2` = `bcd`, return `true` since we can map `a` to `b`, `b` to `c`, and `c` to `d`.

Given `s1` = `foo` and `s2` = `bar`, return `false` since the `o` cannot map to two characters.

### [Problem #766 [Medium]](string_problems/problem_766.py)
This problem was asked by LinkedIn.

You are given a string consisting of the letters `x` and `y`, such as `xyxxxyxyy`. In addition, you have an operation 
called `flip`, which changes a single `x` to `y` or vice versa.

Determine how many times you would need to apply this operation to ensure that all 
`x`'s come before all `y`'s. In the preceding example, it suffices to flip the second and sixth characters, 
so you should return `2`.

### [Problem #764 [Medium]](number_problems/problem_764.py)
This problem was asked by Twitter.

Given a list of numbers, create an algorithm that arranges them in order to form the largest possible integer. 
For example, given `[10, 7, 76, 415]`, you should return `77641510`.

### [Problem #759 [Medium]](string_problems/problem_759.py)
This problem was asked by Snapchat.

Given a string of digits, generate all possible valid IP address combinations.

IP addresses must follow the format A.B.C.D, where A, B, C, and D are numbers between `0` and `255`. 
Zero-prefixed numbers, such as `01` and `065`, are not allowed, except for `0` itself.

For example, given `2542540123`, you should return `['254.25.40.123', '254.254.0.123']`.

### [Problem #758 [Medium]](number_problems/problem_758.py)
This problem was asked by Facebook.

Write a function that rotates a list by k elements. For example, `[1, 2, 3, 4, 5, 6]` rotated by two becomes 
`[3, 4, 5, 6, 1, 2]`. Try solving this without creating a copy of the list. How many swap or move operations do you need?

### [Problem #752 [Easy]](graph_problems/problem_752.py)
This problem was asked by Microsoft.

Print the nodes in a binary tree level-wise. For example, the following should print `1, 2, 3, 4, 5`.
```
  1
 / \
2   3
   / \
  4   5
```

### [Problem #748 [Easy]](graph_problems/problem_748.py)
This problem was asked by Apple.

Given the root of a binary tree, find the most frequent subtree sum. The subtree sum of a node is the sum of all values 
under a node, including the node itself.

For example, given the following tree:
```
  5
 / \
2  -5
```
Return `2` as it occurs twice: once as the left leaf, and once as the sum of `2 + 5 - 5`.

### [Problem #747 [Easy]](string_problems/problem_747.py)
This problem was asked by Google.

Given two strings A and B, return whether or not A can be shifted some number of times to get B.

For example, if A is `abcde` and B is `cdeab`, return true. If A is `abc` and B is `acb`, return false.

### [Problem #742 [Easy]](others/problem_742.py)
This problem was asked by Stripe.

Write a function to flatten a nested dictionary. Namespace the keys with a period.

For example, given the following dictionary:
```
{
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}
```
it should become:
```
{
    "key": 3,
    "foo.a": 5,
    "foo.bar.baz": 8
}
```
You can assume keys do not contain dots in them, i.e. no clobbering will occur.

### [Problem #740 [Medium]](number_problems/problem_740.py)
This problem was asked by Google.

A regular number in mathematics is defined as one which evenly divides some power of `60`. Equivalently, we can say that 
a regular number is one whose only prime divisors are `2`, `3`, and `5`.

These numbers have had many applications, from helping ancient Babylonians keep time to tuning instruments according 
to the diatonic scale.

Given an integer `N`, write a program that returns, in order, the first `N` regular numbers.

### [Problem #735 [Easy]](number_problems/problem_735.py)
This problem was asked by Sumo Logic.

Given an unsorted array, in which all elements are distinct, find a "peak" element in `O(log N)` time.

An element is considered a peak if it is greater than both its left and right neighbors. It is guaranteed that the first 
and last elements are lower than all others.

### [Problem #723 [Medium]](number_problems/problem_723.py)
This problem was asked by Google.

Given a set of closed intervals, find the smallest set of numbers that covers all the intervals. If there are multiple 
smallest sets, return any of them.

For example, given the intervals `[0, 3], [2, 6], [3, 4], [6, 9]`, one set of numbers that covers all these intervals 
is `{3, 6}`.

### [Problem #714 [Easy]](data_structures/problem_714.py)
This problem was asked by Google.

Given the head of a singly linked list, swap every two nodes and return its head.

For example, given `1 -> 2 -> 3 -> 4`, return `2 -> 1 -> 4 -> 3`.

### [Problem #678 [Easy]](number_problems/problem_678.py)
This problem was asked by IBM.

Given an integer, find the next permutation of it in absolute order. For example, given `48975`, the next permutation 
would be `49578`.

### [Problem #677 [Easy]](number_problems/problem_677.py)
This problem was asked by Square.

The Sieve of Eratosthenes is an algorithm used to generate all prime numbers smaller than `N`. The method is to take 
increasingly larger prime numbers, and mark their multiples as composite.

For example, to find all primes less than `100`, we would first mark `[4, 6, 8, ...]` (multiples of two), then 
`[6, 9, 12, ...]` (multiples of three), and so on. Once we have done this for all primes less than `N`, the unmarked 
numbers that remain will be prime.

Implement this algorithm.

Bonus: Create a generator that produces primes indefinitely (that is, without taking `N` as an input).

### [Problem #674 [Easy]](number_problems/problem_674.py)
This problem was asked by Google.

A girl is walking along an apple orchard with a bag in each hand. She likes to pick apples from each tree as she goes 
along, but is meticulous about not putting different kinds of apples in the same bag.

Given an input describing the types of apples she will pass on her path, in order, determine the length of the longest 
portion of her path that consists of just two types of apple trees.

For example, given the input `[2, 1, 2, 3, 3, 1, 3, 5]`, the longest portion will involve types `1` and `3`, 
with a length of four.

### [Problem #672 [Easy]](number_problems/problem_672.py)
This problem was asked by Google.

You are given an array of arrays of integers, where each array corresponds to a row in a triangle of numbers. 
For example, `[[1], [2, 3], [1, 5, 1]]` represents the triangle:
```
1
2 3
1 5 1
```
We define a path in the triangle to start at the top and go down one row at a time to an adjacent value, eventually 
ending with an entry on the bottom row. For example, `1 -> 3 -> 5`. The weight of the path is the sum of the entries.

Write a program that returns the weight of the maximum weight path.

### [Problem #668 [Easy]](others/problem_668.py)
This problem was asked by Google.

In linear algebra, a Toeplitz matrix is one in which the elements on any given diagonal from top left to bottom right 
are identical.

Here is an example:
```
1 2 3 4 8
5 1 2 3 4
4 5 1 2 3
7 4 5 1 2
```
Write a program to determine whether a given input is a Toeplitz matrix.

### [Problem #663 [Easy]](others/problem_663.py)
This question was asked by Riot Games.

Design and implement a HitCounter class that keeps track of requests (or hits). It should support the following operations:

* `record(timestamp)` records a hit that happened at `timestamp`
* `total()` returns the total number of hits recorded
* `range(lower, upper)` returns the number of hits that occurred between timestamps `lower` and `upper` (inclusive)

Follow-up: What if our system has limited memory?

### [Problem #657 [Easy]](number_problems/problem_657.py)
This problem was asked by Google.

The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

For example, given the set `{1, 2, 3}`, it should return `{{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}`

### [Problem #655 [Easy]](number_problems/problem_655.py)
This problem was asked by Facebook.

Given a 32-bit integer, return the number with its bits reversed.

For example, given the binary number `1111 0000 1111 0000 1111 0000 1111 0000`, return 
`0000 1111 0000 1111 0000 1111 0000 1111`.

### [Problem #653 [Easy]](geometry/problem_653.py)
This problem was asked by Google.

You are given a list of rectangles represented by min and max x- and y-coordinates. Compute whether a pair of rectangles 
overlap each other. If one rectangle completely covers another, it is considered overlapping.

For example, given the following rectangles:
```
{
"top_left": (1, 4),
"dimensions": (3, 3) # width, height
},
{
"top_left": (-1, 3),
"dimensions": (2, 1)
},
{
"top_left": (0, 5),
"dimensions": (4, 3)
}
```
return `true` as the first and third rectangle overlap each other.

### [Problem #649 [Easy]](string_problems/problem_649.py)
This problem was asked by Google.

Given a string, return the first recurring character in it, or null if there is no recurring character.

For example, given the string "acbbac", return "b". Given the string "abcdef", return null.

### [Problem #646 [Easy]](graph_problems/problem_646.py)
This problem was asked by Twitter.

A classroom consists of `N` students, whose friendships can be represented in an adjacency list. For example, 
the following descibes a situation where `0` is friends with `1` and `2`, `3` is friends with `6`, and so on.
```
{0: [1, 2],
 1: [0, 5],
 2: [0],
 3: [6],
 4: [],
 5: [1],
 6: [3]}
```
Each student can be placed in a friend group, which can be defined as the transitive closure of that student's 
friendship relations. In other words, this is the smallest set such that no student in the group has any friends outside 
this group. For the example above, the friend groups would be `{0, 1, 2, 5}`, `{3, 6}`, `{4}`.

Given a friendship list such as the one above, determine the number of friend groups in the class.

### [Problem #645 [Easy]](others/problem_645.py)
This problem was asked by Microsoft.

Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found in 
the matrix by going left-to-right, or up-to-down.

For example, given the following matrix:
```
[['F', 'A', 'C', 'I'],
['O', 'B', 'Q', 'P'],
['A', 'N', 'O', 'B'],
['M', 'A', 'S', 'S']]
```
and the target word 'FOAM', you should return true, since it's the leftmost column. Similarly, given the target 
word 'MASS', you should return true, since it's the last row.

### [Problem #644 [Easy]](graph_problems/problem_644.py)
This problem was asked by Google.

An unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:
```
  0
 / \
1   0
   / \
  1   0
 / \
1   1
```

### [Problem #639 [Easy]](string_problems/problem_639.py)
This problem was asked by Yelp.

Given a mapping of digits to letters (as in a phone number), and a digit string, return all possible letters the number 
could represent. You can assume each valid number in the mapping is a single digit.

For example if {“2”: [“a”, “b”, “c”], 3: [“d”, “e”, “f”], …} then “23” should return 
[“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf"].

### [Problem #638 [Medium]](string_problems/problem_638.py)
This problem was asked by Google.

Given a string of words delimited by spaces, reverse the words in string. For example, given "hello world here", 
return "here world hello"

Follow-up: given a mutable string representation, can you perform this operation in-place?

### [Problem #637 [Easy]](number_problems/problem_637.py)
This problem was asked by Snapchat.

Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping intervals have 
been merged.

The input list is not necessarily ordered in any way.

For example, given `[(1, 3), (5, 8), (4, 10), (20, 25)]`, you should return `[(1, 3), (4, 10), (20, 25)]`.

### [Problem #636 [Medium]](number_problems/problem_636.py)
This problem was asked by Uber.

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand. Find the minimum element 
in O(log N) time. You may assume the array does not contain duplicates.

For example, given [5, 7, 10, 3, 4], return 3.

### [Problem #632 [Medium]](number_problems/problem_632.py)
This problem was asked by Snapchat.

You are given an array of length `N`, where each element `i` represents the number of ways we can produce `i` units 
of change. For example, `[1, 0, 1, 1, 2]` would indicate that there is only one way to make `0`, `2`, or `3` units, 
and two ways of making `4` units.

Given such an array, determine the denominations that must be in use. In the case above, for example, there must be 
coins with value `2`, `3`, and `4`.

### [Problem #627 [Medium]](others/problem_627.py)
This problem was asked by Google.

Given an `iterator` with methods `next()` and `hasNext()`, create a wrapper iterator, `PeekableInterface`, which also 
implements `peek()`. `peek` shows the next element that would be returned on `next()`.

Here is the interface:
```
class PeekableInterface(object):
def __init__(self, iterator):
pass

    def peek(self):
        pass

    def next(self):
        pass

    def hasNext(self):
        pass
```

### [Problem #626 [Easy]](number_problems/problem_626.py)
This problem was asked by Facebook.

Given a list of integers, return the largest product that can be made by multiplying any three integers.

For example, if the list is `[-10, -10, 5, 2]`, we should return `500`, since that's `-10 * -10 * 5`.

You can assume the list has at least three integers.

### [Problem #625 [Easy]](number_problems/problem_625.py)
This problem was asked by Stripe.

Given an integer `n`, return the length of the longest consecutive run of `1s` in its binary representation.

For example, given `156`, you should return `3`.

### [Problem 624 [Medium]](others/problem_624.py)
This problem was asked by Google.

Given a string of parentheses, write a function to compute the minimum number of parentheses to be removed to make 
the string valid (i.e. each open parenthesis is eventually closed).

For example, given the string `()())()`, you should return 1. Given the string `)(`, you should return 2, 
since we must remove all of them.

### [Problem #622 [Easy]](graph_problems/problem_622.py)
This problem was asked by Google.

Given the root of a binary tree, return a deepest node. For example, in the following tree, return d.
```
    a
   / \
  b   c
 /
d
```

### [Problem #619 [Easy]](graph_problems/problem_619.py)
This problem was asked by Coursera.

Given a 2D board of characters and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example, given the following board:
```
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
```
`exists(board, "ABCCED")` returns `true`,  
`exists(board, "SEE")` returns `true`,  
`exists(board, "ABCB")` returns `false`.

### [Problem #617 [Medium]](number_problems/problem_617.py)
This problem was asked by Facebook.

Given a number in Roman numeral format, convert it to decimal.

The values of Roman numerals are as follows:
```
{
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}
```
In addition, note that the Roman numeral system uses subtractive notation for numbers such as `IV` and `XL`.

For the input `XIV`, for instance, you should return `14`.

### [Problem #614 [Medium]](graph_problems/problem_614.py)
This problem was asked by Twitter.

A network consists of nodes labeled `0` to `N`. You are given a list of edges `(a, b, t)`, describing the time `t` 
it takes for a message to be sent from node `a` to node `b`. Whenever a node receives a message, it immediately passes 
the message on to a neighboring node, if possible.

Assuming all nodes are connected, determine how long it will take for every node to receive a message that begins 
at node 0.

For example, given `N = 5`, and the following edges:
```
edges = [
    (0, 1, 5),
    (0, 2, 3),
    (0, 5, 4),
    (1, 3, 8),
    (2, 3, 1),
    (3, 5, 10),
    (3, 4, 5)
]
```
You should return `9`, because propagating the message from `0 -> 2 -> 3 -> 4` will take that much time.


### [Problem #613 [Easy]](data_structures/problem_613.py)
This problem was asked by Google.

Implement a PrefixMapSum class with the following methods:

* `insert(key: str, value: int)`: Set a given key's value in the map. If the key already exists, overwrite the value.
* `sum(prefix: str)`: Return the sum of all values of keys that begin with a given prefix.

For example, you should be able to run the following code:
```
mapsum.insert("columnar", 3)
assert mapsum.sum("col") == 3

mapsum.insert("column", 2)
assert mapsum.sum("col") == 5
```

### [Problem #612 [Easy]](number_problems/problem_612.py)
This problem was asked by Stripe.

Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of 
the intervals non-overlapping.

Intervals can "touch", such as `[0, 1]` and `[1, 2]`, but they won't be considered overlapping.

For example, given the intervals `(7, 9), (2, 4), (5, 8)`, return 1 as the last interval can be removed and 
the first two won't overlap.

The intervals are not necessarily sorted in any order.

### [Problem #602 [Easy]](others/problem_602.py)
This problem was asked by Facebook.

Suppose you are given two lists of `n` points, one list p1, p2, ..., pn on the line y = 0 and the other list 
q1, q2, ..., qn on the line y = 1. Imagine a set of `n` line segments connecting each point pi to qi. 
Write an algorithm to determine how many pairs of the line segments intersect.

### [Problem #598 [Easy]](number_problems/problem_598.py)
This problem was asked by Microsoft.

You have `n` fair coins and you flip them all at the same time. Any that come up tails you set aside. The ones that come up 
heads you flip again. How many rounds do you expect to play before only one coin remains?

Write a function that, given `n`, returns the number of rounds you'd expect to play until one coin remains.

### [Problem #597 [Easy]](number_problems/problem_597.py)
This problem was asked by Netflix.

Given an array of integers, determine whether it contains a Pythagorean triplet. Recall that a Pythogorean triplet 
`(a, b, c)` is defined by the equation `a^2 + b^2 = c^2`.

### [Problem #594 [Easy]](graph_problems/problem_594.py)
This problem was asked by Google.

You are given an N by N matrix of random letters and a dictionary of words. Find the maximum number of words that can be 
packed on the board from the given dictionary.

A word is considered to be able to be packed on the board if:

* It can be found in the dictionary
* It can be constructed from untaken letters by other words found so far on the board
* The letters are adjacent to each other (vertically and horizontally, not diagonally).

Each tile can be visited only once by any word.

For example, given the following dictionary:

`{ 'eat', 'rain', 'in', 'rat' }`

and matrix:
```
[['e', 'a', 'n'],
 ['t', 't', 'i'],
 ['a', 'r', 'a']]
```
Your function should return 3, since we can make the words 'eat', 'in', and 'rat' without them touching each other. 
We could have alternatively made 'eat' and 'rain', but that would be incorrect since that's only 2 words.

### [Problem #588 [Easy]](data_structures/problem_588.py)
This problem was asked by Facebook.

You have a large array with most of the elements as zero.

Use a more space-efficient data structure, SparseArray, that implements the same interface:

* `init(arr, size)`: initialize with the original large array and size.
* `set(i, val)`: updates index at `i` with `val`.
* `get(i)`: gets the value at index `i`.


### [Problem #584 [Easy]](string_problems/problem_584.py)
This problem was asked by IBM.

Given a string with repeated characters, rearrange the string so that no two adjacent characters are the same. 
If this is not possible, return `None`.

For example, given "aaabbc", you could return "ababac". Given "aaab", return `None`.

### [Problem #581 [Easy]](others/problem_581.py)
This problem was asked by Google.

Given two rectangles on a 2D graph, return the area of their intersection. If the rectangles don't intersect, return 0.

For example, given the following rectangles:
```
{
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
}
```
and
```
{
    "top_left": (0, 5),
    "dimensions": (4, 3) # width, height
}
```
return 6.

### [Problem #580 [Easy]](graph_problems/problem_580.py)
This question was asked by Apple.

Given a binary tree, find a minimum path sum from root to a leaf.

For example, the minimum path in this tree is [10, 5, 1, -1], which has sum 15.
```
  10
 /  \
5    5
 \     \
   2    1
       /
     -1
```

### [Problem #578 [Easy]](string_problems/problem_578.py)
This problem was asked by Bloomberg.

Determine whether there exists a one-to-one character mapping from one string `s1` to another `s2`.

For example, given `s1 = abc` and `s2 = bcd`, return `true` since we can map `a` to `b`, `b` to `c`, and `c` to `d`.

Given `s1 = foo` and `s2 = bar`, return `false` since the `o` cannot map to two characters.

### [Problem #568 [Easy]](number_problems/problem_568.py)
This problem was asked by Google.

Given a sorted list of integers, square the elements and give the output in sorted order.

For example, given `[-9, -2, 0, 2, 3]`, return `[0, 4, 4, 9, 81]`.

### [Problem #543 [Medium]](data_structures/problem_543.py)
This problem was asked by Google.

Given a singly linked list and an integer `k`, remove the `kth` last element from the list. `k` is guaranteed to be 
smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

### [Problem #534 [Easy]](string_problems/problem_534.py)
This problem was asked by Amazon.

Given a string, determine whether any permutation of it is a palindrome.

For example, `carrace` should return true, since it can be rearranged to form `racecar`, which is a palindrome. `daily` 
should return false, since there's no rearrangement that can form a palindrome.

### [Problem #530 [Easy]](string_problems/problem_530.py)
This problem was asked by Google.

The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions 
required to change one string to the other. For example, the edit distance between `“kitten”` and `“sitting”` is three: 
substitute the `“k”` for `“s”`, substitute the `“e”` for `“i”`, and append a `“g”`.

Given two strings, compute the edit distance between them.

### [Problem #505 [Easy]](number_problems/problem_505.py)
This problem was asked by Amazon.

Given an array and a number `k` that's smaller than the length of the array, rotate the array to the right `k` 
elements in-place.

### [Problem #504 [Easy]](data_structures/problem_504.py)
You run an e-commerce website and want to record the last `N` `order` ids in a log. Implement a data structure to 
accomplish this, with the following API:
* `record(order_id)`: adds the `order_id` to the log
* `get_last(i)`: gets the `ith` last element from the log. `i` is guaranteed to be smaller than or equal to `N`.

You should be as efficient with time and space as possible.

### [Problem #502 [Easy]](graph_problems/problem_502.py)
This problem was asked by PayPal.

Given a binary tree, determine whether or not it is height-balanced. A height-balanced binary tree can be defined as one 
in which the heights of the two subtrees of any node never differ by more than one.

### [Problem #491 [Easy]](number_problems/problem_491.py)
This problem was asked by Palantir.

Write a program that checks whether an integer is a palindrome. For example, `121` is a palindrome, as well as `888`. 
`678` is not a palindrome. Do not convert the integer into a string.

### [Problem #489 [Easy]](number_problems/problem_489.py)
This problem was asked by Google.

Given an array of elements, return the length of the longest subarray where all its elements are distinct.

For example, given the array `[5, 1, 3, 5, 2, 3, 4, 1]`, return `5` as the longest subarray of distinct elements is 
`[5, 2, 3, 4, 1]`.

### [Problem #487 [Medium]](graph_problems/problem_487.py)
This problem was asked by Yext.

Two nodes in a binary tree can be called cousins if they are on the same level of the tree but have different parents. 
For example, in the following diagram `4` and `6` are cousins.
```
    1
   / \
  2   3
 / \   \
4   5   6
```
Given a binary tree and a particular node, find all cousins of that node.

### [Problem #486 [Medium]](others/problem_486.py)
This problem was asked by Pinterest.

At a party, there is a single person who everyone knows, but who does not know anyone in return (the "celebrity"). 
To help figure out who this is, you have access to an `O(1)` method called `knows(a, b)`, which returns `True` 
if person `a` knows person `b`, else `False`.

Given a list of `N` people and the above operation, find a way to identify the celebrity in `O(N)` time.

### [Problem #484 [Medium]](graph_problems/problem_484.py)
This problem was asked by Dropbox.

Given the root to a binary search tree, find the second largest node in the tree.

### [Problem #483 [Easy]](number_problems/problem_483.py)
This problem was asked by Bloomberg.

There are `N` prisoners standing in a circle, waiting to be executed. The executions are carried out starting with 
the kth person, and removing every successive kth person going clockwise until there is no one left.

Given `N` and `k`, write an algorithm to determine where a prisoner should stand in order to be the last survivor.

For example, if `N = 5` and `k = 2`, the order of executions would be `[2, 4, 1, 5, 3]`, so you should return `3`.

Bonus: Find an `O(log N)` solution if `k = 2`.

### [Problem #482 [Medium]](graph_problems/problem_482.py)
This problem was asked by Google.

Given a binary search tree and a range `[a, b]` (inclusive), return the sum of the elements of the binary search tree 
within the range.

For example, given the following tree:
```
    5
   / \
  3   8
 / \ / \
2  4 6  10
```
and the range `[4, 9]`, return `23` `(5 + 4 + 6 + 8)`.

### [Problem #480 [Medium]](string_problems/problem_480.py)
This problem was asked by Microsoft.

Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. 
If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, 
then return null.

For example, given the set of words `'quick'`, `'brown'`, `'the'`, `'fox'`, and the string `"thequickbrownfox"`, 
you should return `['the', 'quick', 'brown', 'fox']`.

Given the set of words `'bed'`, `'bath'`, `'bedbath'`, `'and'`, `'beyond'`, and the string `"bedbathandbeyond"`, 
return either `['bed', 'bath', 'and', 'beyond]` or `['bedbath', 'and', 'beyond']`.

### [Problem #479 [Easy]](number_problems/problem_479.py)
This problem was asked by Microsoft.

Given a number in the form of a list of digits, return all possible permutations.

For example, given `[1,2,3]`, return `[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]`.

### [Problem #476 [Medium]](number_problems/problem_476.py)
This problem was asked by Google.

You are given an array of length `n + 1` whose elements belong to the set `{1, 2, ..., n}`. By the pigeonhole principle, 
there must be a duplicate. Find it in linear time and space.

### [Problem #473 [Medium]](graph_problems/problem_473.py)
This problem was asked by Yahoo.

Write an algorithm that computes the reversal of a directed graph. For example, if a graph consists of 
`A -> B -> C`, it should become `A <- B <- C`.

### [Problem #472 [Medium]](string_problems/problem_472.py)
This problem was asked by Facebook.

Given the mapping `a = 1, b = 2, ... z = 26`, and an encoded message, count the number of ways it can be decoded.

For example, the message `'111'` would give 3, since it could be decoded as `'aaa'`, `'ka'`, and `'ak'`.

You can assume that the messages are decodable. For example, `'001'` is not allowed.

### [Problem #470 [Medium]](number_problems/problem_470.py)
This problem was asked by Google.

Given an array of numbers and an index `i`, return the index of the nearest larger number of the number at index `i`, 
where distance is measured in array indices.

For example, given `[4, 1, 3, 5, 6]` and index `0`, you should return `3`.

If two distances to larger numbers are the equal, then return any one of them. If the array at i doesn't have a nearest 
larger integer, then return null.

Follow-up: If you can preprocess the array, can you do this in constant time?

### [Problem #465 [Easy]](data_structures/problem_465.py)
This problem was asked by Google.

Given the head of a singly linked list, reverse it in-place.

### [Problem #449 [Easy]](number_problems/problem_449.py)
This problem was asked by Alibaba.

Given an even number (greater than 2), return two prime numbers whose sum will be equal to the given number.

A solution will always exist. See [Goldbach’s conjecture](https://en.wikipedia.org/wiki/Goldbach%27s_conjecture).

Example:
```
Input: 4
Output: 2 + 2 = 4
```
If there are more than one solution possible, return the lexicographically smaller solution.

If `[a, b]` is one solution with `a <= b`, and `[c, d]` is another solution with `c <= d`, then

`[a, b] < [c, d]`

If `a < c OR a==c AND b < d`.

### [Problem #416 [Easy]](graph_problems/problem_416.py)
This problem was asked by Google.

You are in an infinite 2D grid where you can move in any of the 8 directions:
```
 (x,y) to
    (x+1, y),
    (x - 1, y),
    (x, y+1),
    (x, y-1),
    (x-1, y-1),
    (x+1,y+1),
    (x-1,y+1),
    (x+1,y-1)
```
You are given a sequence of points and the order in which you need to cover the points. Give the minimum number of steps in which you can achieve it. You start from the first point.

Example:
```
Input: [(0, 0), (1, 1), (1, 2)]
Output: 2
```
It takes 1 step to move from `(0, 0)` to `(1, 1)`. It takes one more step to move from `(1, 1)` to `(1, 2)`.

### [Problem #404 [Easy]](number_problems/problem_404.py)
This problem was asked by Snapchat.

Given an array of time intervals `(start, end)` for classroom lectures (possibly overlapping), find the minimum number of
rooms required.

For example, given `[(30, 75), (0, 50), (60, 150)]`, you should return `2`.

### [Problem #403 [Easy]](number_problems/problem_403.py)
This problem was asked by Two Sigma.

Using a function `rand5()` that returns an integer from 1 to 5 (inclusive) with uniform probability, implement a function 
`rand7()` that returns an integer from 1 to 7 (inclusive).

### [Problem #401 [Easy]](others/problem_401.py)
This problem was asked by Twitter.

A permutation can be specified by an array `P`, where `P[i]` represents the location of the element at `i` in 
the permutation. For example, `[2, 1, 0]` represents the permutation where elements at the index `0` and `2` are swapped.

Given an array and a permutation, apply the permutation to the array. For example, given the array `["a", "b", "c"]` and 
the permutation `[2, 1, 0]`, return `["c", "b", "a"]`.

### [Problem #376 [Easy]](graph_problems/problem_376.py)
This problem was asked by Google.

You are writing an AI for a 2D map game. You are somewhere in a 2D grid, and there are coins strewn about over the map.

Given the position of all the coins and your current position, find the closest coin to you in terms of Manhattan 
distance. That is, you can move around up, down, left, and right, but not diagonally. If there are multiple possible
closest coins, return any of them.

For example, given the following map, where you are `x`, coins are `o`, and empty spaces are `.` (top left is 0, 0):

    ---------------------
    | . | . | x | . | o |
    ---------------------
    | o | . | . | . | . |
    ---------------------
    | o | . | . | . | o |
    ---------------------
    | . | . | o | . | . |
    ---------------------

return `(0, 4)`, since that coin is closest. This map would be represented in our question as:
````
Our position: (0, 2)
Coins: [(0, 4), (1, 0), (2, 0), (3, 2)]
````

### [Problem #375 [Medium]](number_problems/problem_375.py)
This problem was asked by Google.

The h-index is a metric used to measure the impact and productivity of a scientist or researcher.

A scientist has index `h` if `h` of their `N` papers have at least `h` citations each, and *\*the other `N - h` papers 
have no more than `h` citations each*. If there are multiple possible values for `h`, the maximum value is used.

Given an array of natural numbers, with each value representing the number of citations of a researcher's paper, 
return the h-index of that researcher.

For example, if the array was:

`[4, 0, 0, 2, 3]`

This means the researcher has 5 papers with 4, 1, 0, 2, and 3 citations respectively. The h-index for this researcher 
is 2, since they have 2 papers with at least 2 citations and *\*the remaining 3 papers have no more than 2 citations*.

*Note:<br/> 
According to [the wiki definition](https://en.wikipedia.org/wiki/H-index) the `N-h` condition is not required. 
The example seems to prove it. I treat it as a mistake in the task description, then.*

### [Problem #374 [Hard]](number_problems/problem_374.py)
This problem was asked by Amazon.

Given a sorted array `arr` of distinct integers, return the lowest index `i` for which `arr[i] == i`. Return `null` 
if there is no such index.

For example, given the array `[-5, -3, 2, 3]`, return `2` since `arr[2] == 2`. Even though `arr[3] == 3`, we return `2` 
since it's the lowest index.

### [Problem #373 [Hard]](number_problems/problem_373.py)
This problem was asked by Facebook.

Given a list of integers L, find the maximum length of a sequence of consecutive numbers that can be formed using 
elements from L.

For example, given `L = [5, 2, 99, 3, 4, 1, 100]`, return `5` as we can build a sequence `[1, 2, 3, 4, 5]` which has 
length `5`.

### [Problem #372 [Easy]](number_problems/problem_372.py)
This problem was asked by Amazon.

Write a function that takes a natural number as input and returns the number of digits the input has.

Constraint: don't use any loops.

### [Problem #370 [Easy]](number_problems/problem_370.py)
This problem was asked by Postmates.

The “active time” of a courier is the time between the pickup and dropoff of a delivery. Given a set of data formatted 
like the following:

`(delivery id, timestamp, pickup/dropoff)`

Calculate the total active time in seconds. A courier can pick up multiple orders before dropping them off. 
The timestamp is in unix epoch seconds.

For example, if the input is the following:
````
(1, 1573280047, 'pickup')
(1, 1570320725, 'dropoff')
(2, 1570321092, 'pickup')
(3, 1570321212, 'pickup')
(3, 1570322352, 'dropoff')
(2, 1570323012, 'dropoff')
````
The total active time would be 1260 seconds.

### [Problem #366 [Medium]](string_problems/problem_366.py)
This problem was asked by Flexport.

Given a string `s`, rearrange the characters so that any two adjacent characters are not the same. If this is not possible, 
return `null`.

For example, if `s = yyz` then return `yzy`. If `s = yyy` then return `null`.

### [Problem #362 [Easy]](number_problems/problem_362.py)
This problem was asked by Twitter.

A strobogrammatic number is a positive number that appears the same after being rotated 180 degrees. For example, 
`16891` is strobogrammatic.

Create a program that finds all strobogrammatic numbers with N digits.

### [Problem #359 [Easy]](string_problems/problem_359.py)
This problem was asked by Slack.

You are given a string formed by concatenating several words corresponding to the integers zero through nine and then 
anagramming.

For example, the input could be `'niesevehrtfeev'`, which is an anagram of `'threefiveseven'`. Note that there can be 
multiple instances of each integer.

Given this string, return the original integers in sorted order. In the example above, this would be `357`.

### [Problem #348 [EASY]](string_problems/problem_348.py)
This problem was asked by Zillow.

A ternary search tree is a trie-like data structure where each node may have up to three children. Here is an example 
which represents the words `code`, `cob`, `be`, `ax`, `war`, `and` `we`.
```
       c
    /  |  \
   b   o   w
 / |   |   |
a  e   d   a
|    / |   | \ 
x   b  e   r  e  
```
The tree is structured according to the following rules:

* left child nodes link to words lexicographically earlier than the parent prefix
* right child nodes link to words lexicographically later than the parent prefix
* middle child nodes continue the current word

For instance, since `code` is the first word inserted in the tree, and `cob` lexicographically precedes `cod`, `cob` is 
represented as a left child extending from `cod`.

### [Problem #347 [EASY]](string_problems/problem_347.py)
This problem was asked by Yahoo.

You are given a string of length `N` and a parameter `k`. The string can be manipulated by taking one of the first `k` 
letters and moving it to the end.

Write a program to determine the lexicographically smallest string that can be created after an unlimited number of moves.

For example, suppose we are given the string `daily` and `k = 1`. The best we can create in this case is `ailyd`.

### [Problem #346 [Medium]](graph_problems/problem_346.py)
This problem was asked by Airbnb.

You are given a huge list of airline ticket prices between different cities around the world on a given day. 
These are all direct flights. Each element in the list has the format  
`(source_city, destination, price)`.

Consider a user who is willing to take up to `k` connections from their origin city `A` to their 
destination `B`. Find the cheapest fare possible for this journey and print the itinerary for that journey.

For example, our traveler wants to go from `JFK` to `LAX` with up to `3` connections, and our input flights are as follows:

```
[
    ('JFK', 'ATL', 150),  
    ('ATL', 'SFO', 400),
    ('ORD', 'LAX', 200),
    ('LAX', 'DFW', 80),
    ('JFK', 'HKG', 800),
    ('ATL', 'ORD', 90),
    ('JFK', 'LAX', 500),
]
```

Due to some improbably low flight prices, the cheapest itinerary would be `JFK -> ATL -> ORD -> LAX`, costing $440.

### [Problem #342 [Medium]](others/problem_342.py)
This problem was asked by Stripe.

`reduce` (also known as `fold`) is a function that takes in an array, a combining function, and an initial value and 
builds up a result by calling the combining function on each element of the array, left to right. For example, 
we can write `sum()` in terms of `reduce`:
```
def add(a, b):
    return a + b

def sum(lst):
    return reduce(lst, add, 0)
```
This should call `add` on the initial value with the first element of the array, and then the result of that with 
the second element of the array, and so on until we reach the end, when we return the sum of the array.

Implement your own version of `reduce`.

### [Problem #340 [Easy]](others/problem_340.py)
This problem was asked by Google.

Given a set of points (x, y) on a 2D cartesian plane, find the two closest points. For example, given the points 
`[(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)]`, return `[(-1, -1), (1, 1)]`.

### [Problem #339 [Easy]](number_problems/problem_339)
This problem was asked by Microsoft.

Given an array of numbers and a number `k`, determine if there are three entries in the array which add up to 
the specified number `k`. For example, given `[20, 303, 3, 4, 25]` and `k = 49`, return true as `20 + 4 + 25 = 49`.

### [Problem #338 [Medium]](number_problems/problem_338.py)
This problem was asked by Facebook.

Given an integer n, find the next biggest integer with the same number of 1-bits on. For example, given the number 6 
(`0110` in binary), return 9 (`1001`).

### [Problem #334 [Easy]](number_problems/problem_334.py)
This problem was asked by Twitter.

The 24 game is played as follows. You are given a list of four integers, each between `1` and `9`, in a fixed order. 
By placing the operators `+`, `-`, `*`, and `/` between the numbers, and grouping them with parentheses, determine 
whether it is possible to reach the value 24.

For example, given the input `[5, 2, 7, 8]`, you should return True, since `(5 * 2 - 7) * 8 = 24`.

Write a function that plays the 24 game.

### [Problem #332 [Easy]](number_problems/problem_332.py)
This problem was asked by Jane Street.

Given integers `M` and `N`, write a program that counts how many positive integer pairs `(a, b)` satisfy the following 
conditions:

* `a + b = M`
* `a XOR b = N`

### [Problem #331 [Medium]](string_problems/problem_331.py)
This problem was asked by LinkedIn.

You are given a string consisting of the letters `x` and `y`, such as `xyxxxyxyy`. In addition, you have an operation 
called `flip`, which changes a single `x` to `y` or vice versa.

Determine how many times you would need to apply this operation to ensure that all `x`'s come before all `y`'s. 
In the preceding example, it suffices to flip the second and sixth characters, so you should return `2`.

### [Problem #324 [Easy]](number_problems/problem_324.py)
This problem was asked by Amazon.

Consider the following scenario: there are `N` mice and `N` holes placed at integer points along a line. Given this, 
find a method that maps mice to holes such that the largest number of steps any mouse takes is minimized.

Each move consists of moving one mouse one unit to the left or right, and only one mouse can fit inside each hole.

For example, suppose the mice are positioned at `[1, 4, 9, 15]`, and the holes are located at `[10, -5, 0, 16]`. 
In this case, the best pairing would require us to send the mouse at `1` to the hole at `-5`, so our function should 
return `6`.

### [Problem #320 [Medium]](string_problems/problem_320.py)
This problem was asked by Amazon.

Given a string, find the length of the smallest window that contains every distinct character. Characters may appear 
more than once in the window.

For example, given "jiujitsu", you should return `5`, corresponding to the final five letters.

### [Problem #312 [Medium]](number_problems/problem_312.py)
This problem was asked by Wayfair.

You are given a `2 x N` board, and instructed to completely cover the board with the following shapes:
* Dominoes, or 2 x 1 rectangles.
* Trominoes, or L-shapes.

For example, if `N = 4`, here is one possible configuration, where `A` is a domino, and `B` and `C` are trominoes.
```
A B B C
A B C C
```
Given an integer `N`, determine in how many ways this task is possible.

### [Problem #310 [Medium]](number_problems/problem_310.py)
This problem was asked by Pivotal.

Write an algorithm that finds the total number of set bits in all integers between `1` and `N`.

### [Problem #303 [Easy]](number_problems/problem_303.py)
This problem was asked by Microsoft.

Given a clock time in `hh:mm` format, determine, to the nearest degree, the angle between the hour and the minute hands.

Bonus: When, during the course of a day, will the angle be zero?

### [Problem #272 [Medium]](number_problems/problem_272)
Write a function, `throw_dice(N, faces, total)`, that determines how many ways it is possible to throw `N` dice with 
some number of faces each to get a specific total.

For example, `throw_dice(3, 6, 7)` should equal `15`.

### [Problem #270 [Medium]](graph_problems/problem_270.py)
This problem was asked by Twitter.

A network consists of nodes labeled `0` to `N`. You are given a list of edges `(a, b, t)`, describing the time `t` 
it takes for a message to be sent from node `a` to node `b`. Whenever a node receives a message, it immediately passes 
the message on to a neighboring node, if possible.

Assuming all nodes are connected, determine how long it will take for every node to receive a message that begins at node `0`.

For example, given N = 5, and the following edges:
````
edges = [
    (0, 1, 5),
    (0, 2, 3),
    (0, 5, 4),
    (1, 3, 8),
    (2, 3, 1),
    (3, 5, 10),
    (3, 4, 5)
]
````
You should return `9`, because propagating the message from `0 -> 2 -> 3 -> 4` will take that much time.

### [Problem #269 [Easy]](problem_269.py)
This problem was asked by Microsoft.

You are given an string representing the initial conditions of some dominoes. Each element can take one of three values:

    L, meaning the domino has just been pushed to the left,
    R, meaning the domino has just been pushed to the right, or
    ., meaning the domino is standing still.

Determine the orientation of each tile when the dominoes stop falling. Note that if a domino receives a force from 
the left and right side simultaneously, it will remain upright.

For example, given the string `.L.R....L`, you should return `LL.RRRLLL`.

Given the string `..R...L.L`, you should return `..RR.LLLL`.

### [Problem #266 [Easy]](string_problems/problem_266.py)
This problem was asked by Pivotal.

A step word is formed by taking a given word, adding a letter, and anagramming the result. For example, starting with 
the word `"APPLE"`, you can add an `"A"` and anagram to get `"APPEAL"`.

Given a dictionary of words and an input word, create a function that returns all valid step words.

### [Problem #265 [Easy]](number_problems/problem_265.py)
This problem was asked by Atlassian.

MegaCorp wants to give bonuses to its employees based on how many lines of codes they have written. They would like to 
give the smallest positive amount to each worker consistent with the constraint that if a developer has written more 
lines of code than their neighbor, they should receive more money.

Given an array representing a line of seats of employees at MegaCorp, determine how much each one should get paid.

For example, given `[10, 40, 200, 1000, 60, 30]`, you should return `[1, 2, 3, 4, 2, 1]`.

### [Problem #258 [Easy]](graph_problems/problem_258.py)
This problem was asked by Morgan Stanley.

In Ancient Greece, it was common to write text with the first line going left to right, the second line going right to left, 
and continuing to go back and forth. This style was called "boustrophedon".

Given a binary tree, write an algorithm to print the nodes in boustrophedon order.

For example, given the following tree:
````
       1
    /     \
  2         3
 / \       / \
4   5     6   7
````
You should return `[1, 3, 2, 4, 5, 6, 7]`.

### [Problem #257 [Easy]](number_problems/problem_257.py)
This problem was asked by WhatsApp.

Given an array of integers out of order, determine the bounds of the smallest window that must be sorted in order for 
the entire array to be sorted. For example, given `[3, 7, 5, 6, 9]`, you should return `(1, 3)`.

### [Problem #255 [Easy]](graph_problems/problem_255)
This problem was asked by Microsoft.

The transitive closure of a graph is a measure of which vertices are reachable from other vertices. It can be represented 
as a matrix M, where `M[i][j] == 1` if there is a path between vertices `i` and `j`, and otherwise `0`.

For example, suppose we are given the following graph in adjacency list form:
````
graph = [
    [0, 1, 3],
    [1, 2],
    [2],
    [3]
]
````
The transitive closure of this graph would be:
````
[1, 1, 1, 1]
[0, 1, 1, 0]
[0, 0, 1, 0]
[0, 0, 0, 1]
````
Given a graph, find its transitive closure.

### [Problem #252 [Easy]](number_problems/problem_252.py)
This problem was asked by Palantir.

The ancient Egyptians used to express fractions as a sum of several terms where each numerator is one. For example, 
`4 / 13` can be represented as `1 / 4 + 1 / 18 + 1 / 468`.

Create an algorithm to turn an ordinary fraction `a / b`, where `a < b`, into an Egyptian fraction.

### [Problem #245 [Easy]](number_problems/problem_245.py)
This problem was asked by Yelp.

You are given an array of integers, where each element represents the maximum number of steps that can be jumped going 
forward from that element. Write a function to return the minimum number of jumps you must take in order to get from 
the start to the end of the array.

For example, given `[6, 2, 4, 0, 5, 1, 1, 4, 2, 9]`, you should return `2`, as the optimal solution involves jumping 
from `6` to `5`, and then from `5` to `9`.

### [Problem #224 [Easy]](number_problems/problem_224.py)
This problem was asked by Amazon.

Given a sorted array, find the smallest positive integer that is not the sum of a subset of the array.

For example, for the input `[1, 2, 3, 10]`, you should return `7`.

Do this in `O(N)` time.

### [Problem #071 [Easy]](number_problems/problem_071.py)
This problem was asked by Two Sigma.

Using a function `rand7()` that returns an integer from 1 to 7 (inclusive) with uniform probability, implement 
a function `rand5()` that returns an integer from 1 to 5 (inclusive).

### [Problem #050 [Easy]](graph_problems/problem_050.py)
This problem was asked by Microsoft.

Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of 
`+`, `−`, `∗`, or `/`.

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:
````
    *
   / \
  +    +
 / \  / \
3  2  4  5
````
You should return `45`, as it is `(3 + 2) * (4 + 5)`.

### [Problem #29 [Easy]](string_problems/problem_029.py)
This problem was asked by Amazon.

Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive 
characters as a single count and character. For example, the string `"AAAABBBCCDAA"` would be encoded as `"4A3B2C1D2A"`.

Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely
of alphabetic characters. You can assume the string to be decoded is valid.

### [Problem #23 [Easy]](graph_problems/problem_023.py)
This problem was asked by Google.

You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall. 
Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach 
the end coordinate from the start. If there is no possible path, then return null. You can move up, left, down, and right. 
You cannot move through walls. You cannot wrap around the edges of the board.

For example, given the following board:
```
[
    [f, f, f, f],
    [t, t, f, t],
    [f, f, f, f],
    [f, f, f, f]
]
```
and `start = (3, 0)` (bottom left) and `end = (0, 0)` (top left), the minimum number of steps required to reach the end 
is `7`, since we would need to go through `(1, 2)` because there is a wall everywhere else on the second row.

### [Problem #21 [Easy]](number_problems/problem_021.py)
This problem was asked by Snapchat.

Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), 
find the minimum number of rooms required.

For example, given `[(30, 75), (0, 50), (60, 150)]`, you should return `2`.

### [Problem #20 [Easy]](data_structures/problem_020.py)
This problem was asked by Google.

Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given `A = 3 -> 7 -> 8 -> 10` and `B = 99 -> 1 -> 8 -> 10`, return the node with value `8`.

In this example, assume nodes with the same value are the exact same node objects.

Do this in `O(M + N)` time (where M and N are the lengths of the lists) and constant space.