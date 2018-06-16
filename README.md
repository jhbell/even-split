# EvenSplit

Find the easiest way to pay everyone back using EvenSplit. EvenSplit will take
into account how much each person has paid, and figure out how to make
everyone square again.

## Motivation

You are on a trip with your friends. You get a cab ride, but you can't split
the check so you pay for it. The next cab ride, one of your friends pays.
Another friend covers the cost of dinner. Everyone paid different amounts, but
how do you get even?

Lets say we split the cost for each person. So everyone pays John a fraction
of his total cost, then everyone pays George a fraction of his costs, and so
on for each individual involved. There are now some unnecessary transactions.
(N(N-1)/2 [if you want to get technical][complete-graph].)

EvenSplit can remove these redundant transactions by analyzing the amount owed
between each person and redirecting some of the payments.

## Examples

_Example 1:_ Let's say you owe John $20, and John owes you $30. The easiest
thing to do would be for John to pay you $10.

_Example 2:_ You owe John $30, and Ashley $10. John also owes Ashley $10.
Notice that this would be three different transactions. The optimal solution,
however, is for you to pay Ashley $40 and pay John $20. We have saved one
transaction. What happened here? You can pay to Ashley the money that John
would immediately turn around and pay to Ashley. Because you owe John more than
he owes Ashley, you save a transaction.

## Usage

The input format for the program is as follows:

```
<number of people>
Person1
Person2
Person3
.
.
.
<number of transactions>
<person who paid> <amount paid>
<person who paid> <amount paid>
.
.
.
```

Here is an example input file:

```
4
Ashley
Jeff
John
Susan
5
Jeff 22.32
Susan 34.19
Susan 19.85
Susan 44.83
Ashley 8.35
```

[complete-graph]: https://en.wikipedia.org/wiki/Complete_graph
