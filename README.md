# NPTEL-Programming-Data-Structures-and-Algorithms-using-Python-Week-4-Practice-Programming-Assignment
NPTEL Programming, Data Structures and Algorithms using Python Week 4 Practice Programming Assignment

# Week 4 Practice Programming Assignment
1. We represent scores of batsmen across a sequence of matches in a two level dictionary as follows:
```python
{'match1':{'player1':57, 'player2':38}, 'match2':{'player3':9, 'player1':42}, 'match3':{'player2':41, 'player4':63, 'player3':91}
```

Each match is identified by a string, as is each player. The scores are all integers. The names associated with the matches are not fixed (here they are 'match1','match2','match3'), nor are the names of the players. A player need not have a score recorded in all matches.

Define a Python function orangecap(d) that reads a dictionary d of this form and identifies the player with the highest total score. Your function should return a pair (playername,topscore) where playername is a string, the name of the player with the highest score, and topscore is an integer, the total score of playername.

The input will be such that there are never any ties for highest total score.

For instance:
```python
>>> orangecap({'match1':{'player1':57, 'player2':38}, 'match2':{'player3':9, 'player1':42}, 'match3':{'player2':41, 'player4':63, 'player3':91}})
('player3', 100)

>>> orangecap({'test1':{'Ashwin':84, 'Kohli':120}, 'test2':{'ashwin':59, 'Pujara':42}})
('Kohli', 120)
```

2. Let us consider polynomials in a single variable x with integer coefficients: for instance, 3x<sup>4</sup> - 17x<sup>2</sup> - 3x + 5. Each term of the polynomial can be represented as a pair of integers (coefficient,exponent). The polynomial itself is then a list of such pairs.

We have the following constraints to guarantee that each polynomial has a unique representation:
* Terms are sorted in descending order of exponent
* No term has a zero cofficient
* No two terms have the same exponent
* Exponents are always nonnegative

For example, the polynomial introduced earlier is represented as
```python
[(3,4),(-17,2),(-3,1),(5,0)]
```
The zero polynomial, 0, is represented as the empty list [], since it has no terms with nonzero coefficients.

Write Python functions for the following operations:
```python
addpoly(p1,p2)
multpoly(p1,p2)
```
that add and multiply two polynomials, respectively.

You may assume that the inputs to these functions follow the representation given above. Correspondingly, the outputs from these functions should also obey the same constraints.

Hint: You are not restricted to writing just the two functions asked for. You can write auxiliary functions to "clean up" polynomials – e.g., remove zero coefficient terms, combine like terms, sort by exponent etc. Build a library of functions that can be combined to achieve the desired format.

You may also want to convert the list representation to a dictionary representation and manipulate the dictionary representation, and then convert back.

Some examples:
```python
>>> addpoly([(4,3),(3,0)],[(-4,3),(2,1)])
[(2, 1),(3, 0)]
```
Explanation: (4x<sup>3</sup> + 3) + (-4x<sup>3</sup> + 2x) = 2x + 3
```python
>>> addpoly([(2,1)],[(-2,1)])
[]
```
Explanation: 2x + (-2x) = 0
```python
>>> multpoly([(1,1),(-1,0)],[(1,2),(1,1),(1,0)])
[(1, 3),(-1, 0)]
```
Explanation: (x - 1) * (x<sup>2</sup> + x + 1) = x<sup>3</sup> - 1

# Sample Test Cases
|              | Input                                                                                                                                                                                                                | Output                                |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| Test Case 1  | orangecap({'match1':{'player1':57, 'player2':38}, 'match2':{'player3':9, 'player1':42}, 'match3':{'player2':41, 'player4':63, 'player3':91}})                                                                        | ('player3', 100)                      |
| Test Case 2  | orangecap({'test1':{'Ashwin':84, 'Kohli':120}, 'test2':{'ashwin':59, 'Pujara':42}})                                                                                                                                  | ('Kohli', 120)                        |
| Test Case 3  | orangecap({'match1':{'player1':57, 'player2':38}, 'match2':{'player3':9, 'player1':42}, 'match3':{'player2':41, 'player4':63, 'player3':91},'test1':{'Ashwin':84, 'Kohli':120}, 'test2':{'ashwin':59, 'Pujara':42}}) | ('Kohli', 120)                        |
| Test Case 4  | orangecap({'match1':{'player1':57, 'player2':38}})                                                                                                                                                                   | ('player1', 57)                       |
| Test Case 5  | multpoly([(1,1),(-1,0)],[(1,2),(1,1),(1,0)])                                                                                                                                                                         | [(1, 3), (-1, 0)]                     |
| Test Case 6  | multpoly([(2,1)],[(-2,1)])                                                                                                                                                                                           | [(-4, 2)]                             |
| Test Case 7  | multpoly([(4,3),(3,0)],[(-4,3),(2,1)])                                                                                                                                                                               | [(-16, 6), (8, 4), (-12, 3), (6, 1)]  |
| Test Case 8  | addpoly([(4,3),(3,0)],[(-4,3),(2,1)])                                                                                                                                                                                | [(2, 1), (3, 0)]                      |
| Test Case 9  | addpoly([(2,1)],[(-2,1)])                                                                                                                                                                                            | []                                    |
| Test Case 10 | addpoly([(1,1),(-1,0)],[(1,2),(1,1),(1,0)])                                                                                                                                                                          | [(1, 2), (2, 1)]                      |
| Test Case 11 | orangecap({'match1':{'player1':57, 'player2':38}, 'match2':{'player3':9, 'player1':42}, 'match3':{'player2':41, 'player4':63, 'player3':91}})                                                                        | ('player3', 100)                      |
| Test Case 12 | orangecap({'test1':{'Ashwin':84, 'Kohli':120}, 'test2':{'ashwin':59, 'Pujara':42}})                                                                                                                                  | ('Kohli', 120)                        |
| Test Case 13 | orangecap({'match1':{'player1':57, 'player2':38}, 'match2':{'player3':9, 'player1':42}, 'match3':{'player2':41, 'player4':63, 'player3':91},'test1':{'Ashwin':84, 'Kohli':120}, 'test2':{'ashwin':59, 'Pujara':42}}) | ('Kohli', 120)                        |
| Test Case 14 | orangecap({'match1':{'player1':57, 'player2':38}})                                                                                                                                                                   | ('player1', 57)                       |
| Test Case 15 | multpoly([(1,1),(-1,0)],[(1,2),(1,1),(1,0)])                                                                                                                                                                         | [(1, 3), (-1, 0)]                     |
| Test Case 16 | multpoly([(2,1)],[(-2,1)])                                                                                                                                                                                           | [(-4, 2)]                             |
| Test Case 17 | multpoly([(4,3),(3,0)],[(-4,3),(2,1)])                                                                                                                                                                               | [(-16, 6), (8, 4), (-12, 3), (6, 1)]  |
| Test Case 18 | addpoly([(4,3),(3,0)],[(-4,3),(2,1)])                                                                                                                                                                                | [(2, 1), (3, 0)]                      |
| Test Case 19 | addpoly([(2,1)],[(-2,1)])                                                                                                                                                                                            | []                                    |
| Test Case 20 | addpoly([(1,1),(-1,0)],[(1,2),(1,1),(1,0)])                                                                                                                                                                          | [(1, 2), (2, 1)]                      |
