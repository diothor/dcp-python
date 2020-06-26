# Daily Coding Problems

### [Problem #347 [EASY]](strings/problem_347.py)
This problem was asked by Yahoo.

You are given a string of length `N` and a parameter `k`. The string can be manipulated by taking one of the first `k` 
letters and moving it to the end.

Write a program to determine the lexicographically smallest string that can be created after an unlimited number of moves.

For example, suppose we are given the string `daily` and `k = 1`. The best we can create in this case is `ailyd`.

### [Problem #346 [Medium]](graph/problem_346.py)
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