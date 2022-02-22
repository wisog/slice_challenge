import re
import argparse


def init_argparse():
    parser = argparse.ArgumentParser(
        description="Print the bot route to deliver all the pizzas.",
        usage="pizzabot.py '5x5 (1, 3) (4, 4)' --sort=True"
    )
    parser.add_argument(
        "--sort", default=False, help='A boolean to define if we should sort the points before delivery', nargs='?',
        type=bool
    )
    parser.add_argument('grid', help='Grid size followed by points on the format: MxN (X1,Y1)...', nargs='+', type=str)
    return parser.parse_args()


def validate_grid_points_format(grid_points):
    """Looks for a valid input format or exit program with an error message

    @param grid_points: The user provided input string
    """
    valid_input = re.fullmatch('^\d+x\d+(\(\d+,\d+\))+$', grid_points)
    if not valid_input:
        exit("invalid format")


def validate_grid_point_limits(m, n, target):
    """
    Check if the target point is out of range and finish the script with an error message
    @param m: M size of grid
    @param n: N size of grid
    @param target: tuple representing point on the grid
    @return: None
    """
    if target[0] > int(m) - 1 or target[1] > int(n) - 1:
        exit('House is out of my limits')


def get_ordered_houses(houses, x, y):
    """Receives a list of points and returns the sorted list of those points compared to (x,y)

    @param houses: List of tuples with valid point coordinates
    @param x: X position to be used on distance calculation
    @param y: Y position to be used on distance calculation
    """
    houses.sort(key=lambda p: (int(p[0]) - x) ** 2 + (int(p[1]) - y) ** 2)
    return houses


class Pizzabot:

    def __init__(self, positionX, positionY):
        """
        @param positionX Initial X axis position of the bot
        @param positionY Initial Y axis position of the bot
        """
        self.positionX = positionX
        self.positionY = positionY
        self.mouvements = []
        self.destination = None

    def destination_reached(self):
        """
        @return: bool this indicates if pizzabot arrived to target house
        """
        return self.positionX == self.destination[0] and self.positionY == self.destination[1]

    def move_to_point(self, destination):
        """
        @param destination: a tuple representing the target house to deliver the pizza
        @return: None
        """
        self.destination = destination
        while not (self.destination_reached()):
            if destination[0] > self.positionX:
                self.positionX += 1
                self.mouvements.append('E')
            elif destination[0] < self.positionX:
                self.positionX -= 1
                self.mouvements.append('W')
            elif destination[1] > self.positionY:
                self.positionY += 1
                self.mouvements.append('N')
            elif destination[1] < self.positionY:
                self.positionY -= 1
                self.mouvements.append('S')
        self.mouvements.append('D')


if __name__ == "__main__":
    """
    testing values:
        python pizzabot.py '5x5 (0, 0) (1, 3) (4, 4) (4, 2) (4, 2) (0, 1) (3, 2) (2, 3) (4, 1)'
        python pizzabot.py '5x5 (0, 0) (1, 3) (4, 4) (4, 2) (4, 2) (0, 1) (3, 2) (2, 3) (4, 1)' --sort=True
        python pizzabot.py '5x5 (1, 3) (4, 4) (2,3)'
        python pizzabot.py '5x5 (1, 3) (4, 4) (2,3)' --sort=True
    """
    args = init_argparse()
    grid = args.grid[0]

    # input cleaning and validations
    input = grid.replace(' ', '').replace('.', '')
    validate_grid_points_format(input)

    values = input.replace(')', '').split('(')
    grid_M, grid_N = values[0].split('x')

    points = [(int(coordinate.split(',')[0]), int(coordinate.split(',')[1])) for coordinate in values[1:]]
    if args.sort:  # --sort=True
        points = get_ordered_houses(points, 0, 0)  # This will help the bot to save time and battery

    bot = Pizzabot(0, 0)
    for point in points:
        validate_grid_point_limits(grid_M, grid_N, point)
        bot.move_to_point(point)

    print(''.join(bot.mouvements))
