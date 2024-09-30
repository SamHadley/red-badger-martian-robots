DIRECTIONS = ['N', 'E', 'S', 'W']  # Clockwise: North, East, South, West
MOVES = {
    'N': (0, 1),
    'E': (1, 0),
    'S': (0, -1),
    'W': (-1, 0)
}

class MartianRobots:
    def __init__(self, max_x, max_y):
        self.max_x = max_x
        self.max_y = max_y
        self.scented_positions = set()  # Set to store scent coordinates

        # Dictionary to hold available commands and their respective methods
        self.commands = {
            'L': self.turn_left,
            'R': self.turn_right,
            'F': self.move_forward
        }

    def turn_left(self, x, y, orientation):
        """Turn left by 90 degrees"""
        new_orientation = DIRECTIONS[(DIRECTIONS.index(orientation) - 1) % 4]
        return x, y, new_orientation

    def turn_right(self, x, y, orientation):
        """Turn right by 90 degrees"""
        new_orientation = DIRECTIONS[(DIRECTIONS.index(orientation) + 1) % 4]
        return x, y, new_orientation

    def move_forward(self, x, y, orientation):
        """Move forward in the current direction"""
        new_x = x + MOVES[orientation][0]
        new_y = y + MOVES[orientation][1]

        # If the robot moves within the bounds of the grid
        if 0 <= new_x <= self.max_x and 0 <= new_y <= self.max_y:
            return new_x, new_y, orientation, False
        # If moving off the grid, check if a scent is present
        elif (x, y) not in self.scented_positions:
            self.scented_positions.add((x, y))  # Mark the position as scented
            return x, y, orientation, True  # Robot is lost

        print(f"Warning: Robot cannot move off the edge of grid, as previous robot has already been lost from this position.")
        return x, y, orientation, False  # Ignore the move but don't get lost

    def move_robot(self, x, y, orientation, instructions):
        """Execute all instructions for a robot"""
        lost = False

        print(f"Initial position: ({x}, {y}), Orientation: {orientation}, Lost: {lost}")

        for instruction in instructions:
            if instruction in self.commands:
                # Execute the command and update the robot's state
                if instruction == 'F':
                    x, y, orientation, lost = self.commands[instruction](x, y, orientation)
                else:
                    x, y, orientation = self.commands[instruction](x, y, orientation)

                # Print out the robot's state after each instruction
                print(f"After instruction '{instruction}': Position: ({x}, {y}), Orientation: {orientation}, Lost: {lost}")
            else:
                # Future-proofing: if an unknown command is encountered, just ignore
                print(f"Warning: Command '{instruction}' is not recognized. Ignoring.")

            if lost:
                print(f"Robot lost at: ({x}, {y}), Orientation: {orientation}")
                break  # Stop execution if the robot is lost

        print(f"Final position: ({x}, {y}), Orientation: {orientation}, Lost: {lost}")

        return x, y, orientation, lost
