# intcode

input = [1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 10, 1, 19, 1, 19, 9, 23, 1, 23, 6, 27, 2, 27, 13, 31, 1, 10, 31, 35, 1, 10, 35, 39, 2, 39, 6, 43, 1, 43, 5, 47, 2, 10, 47, 51, 1, 5, 51, 55, 1, 55, 13, 59, 1, 59, 9, 63, 2, 9, 63, 67, 1, 6, 67, 71, 1, 71, 13, 75, 1, 75, 10, 79, 1, 5, 79, 83, 1, 10,
         83, 87, 1, 5, 87, 91, 1, 91, 9, 95, 2, 13, 95, 99, 1, 5, 99, 103, 2, 103, 9, 107, 1, 5, 107, 111, 2, 111, 9, 115, 1, 115, 6, 119, 2, 13, 119, 123, 1, 123, 5, 127, 1, 127, 9, 131, 1, 131, 10, 135, 1, 13, 135, 139, 2, 9, 139, 143, 1, 5, 143, 147, 1, 13, 147, 151, 1, 151, 2, 155, 1, 10, 155, 0, 99, 2, 14, 0, 0]


class IntCodeComputer():
    def __init__(self, intcode: list):
        self.input = intcode
        self.current_index = 0

    def set_next_program(self):
        self.current_program = self.input[self.current_index:self.current_index+4]
        self.current_index += 4

    def run_current_program(self):
        program, idx_a, idx_b, res_index = self.current_program

        if program == 1:
            self.input[res_index] = self.input[idx_a] + self.input[idx_b]

        if program == 2:
            self.input[res_index] = self.input[idx_a] * self.input[idx_b]

    def run(self):
        while self.input[self.current_index] != 99:
            self.set_next_program()
            self.run_current_program()

        return self.input


def run_int_code(intcode: list):
    computer = IntCodeComputer(intcode)
    return computer.run()


assert run_int_code([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]
assert run_int_code([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99]
assert run_int_code([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801]
assert run_int_code([1, 1, 1, 4, 99, 5, 6, 0, 99]) == [
    30, 1, 1, 4, 2, 5, 6, 0, 99]

# Once you have a working computer, the first step is to restore the gravity
# assist program (your puzzle input) to the "1202 program alarm" state it had
# just before the last computer caught fire. To do this, before running the
# program, replace position 1 with the value 12 and replace position 2 with
# the value 2. What value is left at position 0 after the program halts?

# input[1] = 12 (noun)
# input[2] = 2 (verb)

# print(run_int_code(input))

# part 2
# The inputs should still be provided to the program by replacing the values at
# addresses 1 and 2, just like before. In this program, the value placed in address
# 1 is called the noun, and the value placed in address 2 is called the verb. Each of
# the two input values will be between 0 and 99, inclusive.


def determine_inputs_for_computer(input: list, value: int):
    # brute force...
    for i in range(0, 100):
        for j in range(0, 100):
            new_inputs = list(input)  # reinit every time
            new_inputs[1] = i
            new_inputs[2] = j

            print(f'attempting with noun:{i} and verb:{j}...')
            result = run_int_code(new_inputs)[0]
            if result == value:
                return (i, j)

# Find the input noun and verb that cause the program to produce the output
# 19690720. What is 100 * noun + verb? (For example, if noun=12 and verb=2,
# the answer would be 1202.)


noun, verb = determine_inputs_for_computer(input, 19690720)

print(100 * noun + verb)
