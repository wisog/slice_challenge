# Pizzabot

Python cli script that prints the steps needed to deliver pizza in a list of houses marked as points

### Requirements:
Python3

### Usage:

```
Print the bot route to deliver all the pizzas.

positional arguments:
  grid        Grid size followed by points on the format: MxN (X1,Y1)...

optional arguments:
  -h, --help  show this help message and exit
  -s [S]      A boolean to define if we should sort the points before
              delivery
```

#### Examples:
python pizzabot.py '5x5 (1, 3) (4, 4) (2,3)'

python pizzabot.py '5x5 (1, 3) (4, 4) (2,3)' --sort=True
