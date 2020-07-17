# Daily Coding Problems

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

### [Problem #342 [Medium]](problem_342.py)
This problem was asked by Stripe.

`reduce` (also known as `fold`  ) is a function that takes in an array, a combining function, and an initial value and 
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

### [Problem #340 [Easy]](problem_340.py)
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

### [Problem #257 [Easy]](problem_257.py)
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

### [Problem #224 [Easy]](number_problems/problem_224.py)
This problem was asked by Amazon.

Given a sorted array, find the smallest positive integer that is not the sum of a subset of the array.

For example, for the input `[1, 2, 3, 10]`, you should return `7`.

Do this in `O(N)` time.

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

### [Problem #21 [Easy]](problem_021.py)
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