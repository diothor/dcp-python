# Daily Coding Problems

### [Problem #347 [EASY]](strings/problem_347.py)
This problem was asked by Yahoo.

You are given a string of length `N` and a parameter `k`. The string can be manipulated by taking one of the first `k` 
letters and moving it to the end.

Write a program to determine the lexicographically smallest string that can be created after an unlimited number of moves.

For example, suppose we are given the string `daily` and `k = 1`. The best we can create in this case is `ailyd`.

### [Problem #346 [Medium]](graphs/problem_346.py)
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

### [Problem #338 [Medium]](numbers/problem_338.py)
This problem was asked by Facebook.

Given an integer n, find the next biggest integer with the same number of 1-bits on. For example, given the number 6 
(`0110` in binary), return 9 (`1001`).

### [Problem #334 [Easy]](numbers/problem_334.py)
This problem was asked by Twitter.

The 24 game is played as follows. You are given a list of four integers, each between `1` and `9`, in a fixed order. 
By placing the operators `+`, `-`, `*`, and `/` between the numbers, and grouping them with parentheses, determine 
whether it is possible to reach the value 24.

For example, given the input `[5, 2, 7, 8]`, you should return True, since `(5 * 2 - 7) * 8 = 24`.

Write a function that plays the 24 game.

### [Problem #255 [Easy]](graphs/problem_255)
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

### [Problem #252 [Easy]](numbers/problem_252.py)
This problem was asked by Palantir.

The ancient Egyptians used to express fractions as a sum of several terms where each numerator is one. For example, 
`4 / 13` can be represented as `1 / 4 + 1 / 18 + 1 / 468`.

Create an algorithm to turn an ordinary fraction `a / b`, where `a < b`, into an Egyptian fraction.

### [Problem #224 [Easy]](numbers/problem_224.py)
This problem was asked by Amazon.

Given a sorted array, find the smallest positive integer that is not the sum of a subset of the array.

For example, for the input `[1, 2, 3, 10]`, you should return `7`.

Do this in `O(N)` time.

### [Problem #29 [Easy]](strings/problem_029.py)
This problem was asked by Amazon.

Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive 
characters as a single count and character. For example, the string `"AAAABBBCCDAA"` would be encoded as `"4A3B2C1D2A"`.

Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely
of alphabetic characters. You can assume the string to be decoded is valid.

### [Problem #23 [Easy]](graphs/problem_023.py)
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