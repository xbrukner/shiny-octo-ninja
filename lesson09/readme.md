# Monty hall problem simulation
[The program](montyhall.py) shows the result of hundred iterations of Monty Hall problem. Three strategies are chosen - stay, change and random. 

Simulation method shows nicely the probabilities. If we decide to stay, the winning probability is 1/3, because we chose randomly from three choices. However, if one wrong door is opened and we decide to change, it is the same as if we chose the opposite of the first door (because now there are only two options, one right and one wrong), and therefore the winning probability is 2/3.

The resulting values correlate with probabilities - approximately 1/3 for stay, 2/3 for change, 1/2 for random (I wrote manually multiple results):

```
Staying:
32, 41, 34, 31, 34, 38, 42, 42, 27, 34 successful (mean = 35.5%)
Changing:
68, 69, 60, 64, 68, 71, 75, 70, 63, 66 successful (mean = 67.4%)
Random:
50, 43, 53, 48, 53, 46, 54, 53, 50, 53 successful (mean = 50.3%)
```