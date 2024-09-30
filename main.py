import sys
from martian_robots import MartianRobots


def process_input(input_data):
    lines = [line for line in input_data.splitlines() if line.strip()]
    max_x, max_y = map(int, lines[0].split())

    # Create an instance of MartianRobots with the grid size
    if max_x > 0 and max_y > 0:
        mars_robots = MartianRobots(max_x, max_y)
    else:
        raise ValueError('Grid size outside of constraints.')

    result = []
    for i in range(1, len(lines), 2):
        x, y, orientation = lines[i].split()
        x, y = int(x), int(y)
        instructions = lines[i + 1]

        print(f"Robot '{i}' is starting move with the following initial details:")

        final_x, final_y, final_orientation, lost = mars_robots.move_robot(x, y, orientation, instructions)
        if lost:
            result.append(f"{final_x} {final_y} {final_orientation} LOST")
        else:
            result.append(f"{final_x} {final_y} {final_orientation}")

    return result


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    # Read input data from the file
    try:
        with open(input_file, 'r') as file:
            input_data = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
        sys.exit(1)

    # Process the input and get the result
    result = process_input(input_data)

    # Write the result to output_data.txt
    with open("robot_positions_data.txt", 'w') as output_file:
        for res in result:
            output_file.write(res + "\n")

    print("Results have been written to robot_positions_data.txt")


if __name__ == "__main__":
    main()
