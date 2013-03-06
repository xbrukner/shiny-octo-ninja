# Lesson 2

## Generation of permutations, combinations, variations

[This code](generovani.py) shows how to generate all permutations, combinations (with and without repetition) and variations (also with and without repetition). It is all in one function, which shows what is the difference in generation for each situation. Program itself takes two parameters - first is a number elements (printed elements will be from range [0 .. number) ). Second is the number of elements in variations and combinations.

## Power

[Power of rational numbers](mocneni.py) is done via two methods - Using a simple formula a^(b/c) = nth-root(a^b, c) and via Taylor series. N-th root is guessed via binary search, which makes its complexity dependend on the numbers given. Taylor series, on the other hand, uses constant number of iterations (100 for calculating logarithm, 99 for calculating the actual power), which makes its complexity constant. The program also prints result via pow method, for comparison.

First approach may be faster when the exponent is natural number, because then only small number of operations is needed. But when it is not, the calculation itself may take a long time (guessing 1000-th root of a number requires to calculate n^1000 repeatedly). That is why I prefer the second approach, where I can say how many iterations I need.

## Generation of pi

[Pi](pi.py) can be generated via many different approaches. I chose five of them (Gregory-Leibnitz, Nilakantha, Archimedes, Gauss-Legedre, Monte Carlo). I found three of them interesting:

 - Archimedes (which is a simple to rememeber, does not produce large numbers and gives correct results quite fast)
 - Gauss-Legedre (which gives 45 million valid numbers of PI after just 25 iterations, although it produces larger numbers with a lot of iterations)
 - Monte Carlo (which does not give a very accurate result, but it shows another way how probability may help us, if we are able to decide, whether some result is correct or not)
