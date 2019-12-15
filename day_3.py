# crossed wires
from collections import defaultdict

wire_movements = []
for line in open('./input/day3_input.txt'):
    wire_movements.append(line.split(','))

wire1, wire2 = wire_movements


def get_visited_locations(movements: list):
    visited = defaultdict()
    x = 0
    y = 0
    steps = 0

    for movement in movements:
        dir_indicator = movement[0]
        magnitude = int(movement[1:])
        move_x = move_y = 0
        if dir_indicator == 'U':
            move_y = +1
        if dir_indicator == 'D':
            move_y = -1
        if dir_indicator == 'R':
            move_x = +1
        if dir_indicator == 'L':
            move_x = -1

        for i in range(0, magnitude):
            steps += 1
            x += move_x
            y += move_y

            # only add the num steps for the first time it gets here
            if (x, y) not in visited.keys():
                visited[(x, y)] = steps

    return visited


def get_shortest_distance(intersections: list):
    distances = []
    for intersection in intersections:
        dist = abs(intersection[0]) + abs(intersection[1])
        distances.append(dist)
    return min(distances)


def get_fewest_steps(intersections: list, wire1_visited: dict, wire2_visited: dict):
    fewest_steps = None
    steps = 0
    for intersection in intersections:
        w1_steps = wire1_visited.get(intersection)
        w2_steps = wire2_visited.get(intersection)
        steps = w1_steps + w2_steps
        if fewest_steps is None or steps < fewest_steps:
            fewest_steps = steps

    return fewest_steps


def get_closest_intersection_distance(wire1, wire2):
    wire1_visited = get_visited_locations(wire1)
    wire2_visited = get_visited_locations(wire2)

    intersections = list(set(wire1_visited.keys()) & set(wire2_visited.keys()))
    return get_shortest_distance(intersections)


def get_fewest_steps_intersection_distance(wire1, wire2):
    wire1_visited = get_visited_locations(wire1)
    wire2_visited = get_visited_locations(wire2)

    intersections = list(set(wire1_visited.keys()) & set(wire2_visited.keys()))
    return get_fewest_steps(intersections, wire1_visited, wire2_visited)


assert (get_closest_intersection_distance(
    ['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72'],
    ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83'])
) == 159

assert (get_closest_intersection_distance(
    ['R98', 'U47', 'R26', 'D63', 'R33', 'U87',
     'L62', 'D20', 'R33', 'U53', 'R51'],
    ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7'])
) == 135

# part 1 solution
print(get_closest_intersection_distance(wire1, wire2))

assert (get_fewest_steps_intersection_distance(
    ['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72'],
    ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83'])
) == 610

assert (get_fewest_steps_intersection_distance(
    ['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51'],
    ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7'])
) == 410

# part 2 solution
print(get_fewest_steps_intersection_distance(wire1, wire2))
