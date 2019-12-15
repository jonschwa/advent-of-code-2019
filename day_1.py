import math

input = [int(line.rstrip()) for line in open('./input/day1_input.txt')]

# Part 1:
# Fuel required to launch a given module is based on its mass.
# Specifically, to find the fuel required for a module,
# take its mass, divide by three, round down, and subtract 2.

# Part 2:
# Fuel itself requires fuel just like a module - take its mass, divide by
# three, round down, and subtract 2. However, that fuel also requires fuel,
# and that fuel requires fuel, and so on. Any mass that would require negative
# fuel should instead be treated as if it requires zero fuel; the remaining
# mass, if any, is instead handled by wishing really hard, which has no mass
# and is outside the scope of this calculation.

# So, for each module mass, calculate its fuel and add it to the total.
# Then, treat the fuel amount you just calculated as the input mass and
# repeat the process, continuing until a fuel requirement is zero or negative.


def get_total_required_fuel(mass):
    total_req_fuel = required_extra_fuel = get_required_fuel(mass)
    while required_extra_fuel > 0:
        required_extra_fuel = get_required_fuel(required_extra_fuel)
        if required_extra_fuel > 0:
            total_req_fuel += required_extra_fuel
    return total_req_fuel


def get_required_fuel(mass):
    return math.floor(mass / 3) - 2


assert get_required_fuel(12) == 2
assert get_required_fuel(14) == 2
assert get_required_fuel(1969) == 654
assert get_required_fuel(100756) == 33583

assert get_total_required_fuel(12) == 2
assert get_total_required_fuel(14) == 2
assert get_total_required_fuel(1969) == 966
assert get_total_required_fuel(100756) == 50346

print(sum(get_total_required_fuel(mass) for mass in input))
