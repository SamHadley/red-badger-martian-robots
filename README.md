# Martian Robots Simulation

## Project Structure
- ```main.py```: The entry point for the application. It reads input data, processes the robot movements, and writes the results to an output file.

- ```martian_robots.py```: Contains the core MartianRobots class, which defines the behavior of the robots and their movements within the grid.

- ```test_martian_robots.py```: Contains unit tests and integration tests for validating the correctness of the robot movement and grid boundary behaviors.


## Instructions for Running the Code

### Prerequisites
- Python 3
- Pytest

### Installation
1. Git clone the repo to local enviroment
2. Ensure all prerequisites are installed (pip install package), will install them

### Running the simulation
1. Update ```test_input.txt``` to contain your input instructions
2. Run the simulation by executing the following command in the terminal:
``` python main.py test_input.txt ```
3. After running the simulation, the results will be written to robot_positions_data.txt in the same directory.


## Testing 
To ensure the correctness of the robot movements and behavior, unit tests and integration tests are provided. These can be run using pytest.

### Running tests
1. Install pytest if you haven't already:
``` pip install pytest ```
2. Run the tests by executing the following command in the terminal:
``` pytest test_martian_robots.py ```

## Design Choices

### 1. Modular Design
The code is split into three main components:

- main.py: Handles input/output and orchestrates the core logic by calling the MartianRobots class. It focuses on processing the input data, feeding it to the core logic, and writing results to an output file.
- martian_robots.py: Contains the main logic of the robot simulation through the MartianRobots class. This class encapsulates the grid, robot movements, and boundary checks. It keeps the logic clean and separated from input handling.
- test_martian_robots.py: Contains unit and integration tests to ensure that the simulation behaves as expected. Tests are separated to focus on individual methods (unit tests) and end-to-end scenarios (integration tests).

### 2. Robot Movements
Each robot moves based on a set of instructions:

- Turning (L and R): These commands rotate the robot 90 degrees left or right without changing its position.
- Moving Forward (F): This command moves the robot one unit forward in the direction it is facing. The movement is bounded by the grid, and if a robot tries to move off the grid, it will be marked as "lost."
This movement logic is encapsulated in the MartianRobots class, which has dedicated methods (turn_left(), turn_right(), move_forward()) for each command. By separating these concerns, the logic remains clean, testable, and maintainable.

### 3. Scenting Mechanism
When a robot is lost by moving out of bounds, a "scent" is left at its last known position. This prevents future robots from becoming lost if they try to move off the grid at the same location. The choice to use a set (self.scented_positions) allows for fast lookups of previously scented positions, ensuring efficient checking for each robot's movements.

This feature ensures that robots can behave more intelligently by recognizing dangerous positions on the grid and avoiding repeated losses.

### 4. Grid Boundary Constraints
The grid dimensions are provided as input, with the assumption that they are non-negative integers. If the grid dimensions are zero or negative, the program raises a ValueError, preventing the simulation from running with invalid grid sizes. This design choice ensures that the grid is always a valid, playable space.

### 5. Command Flexibility
While the simulation currently supports three commands (L, R, F), the architecture of the MartianRobots class is future-proofed to allow easy extension. The self.commands dictionary maps each command to its corresponding method, making it simple to add new commands in the future.

### 6. Error Handling
The code includes basic error handling for invalid input and file handling:

- Invalid Grid Size: The program raises a ValueError if the grid size is invalid.
- Invalid Commands: If an unknown command is encountered, the program prints a warning and ignores the invalid command, allowing the simulation to continue.
- File Not Found: If the input file cannot be found, the program prints an error message and exits gracefully.
These design choices aim to make the program robust to user error and ensure a smooth experience.

### 7. Testing Strategy
The project includes a comprehensive suite of unit tests and integration tests:

- Unit Tests: These tests validate the correctness of individual methods, such as turning left, turning right, and moving forward.
- Integration Tests: These tests simulate real-world scenarios by testing the entire sequence of robot movements across different grid configurations and checking the final output.
Using pytest ensures that the code is thoroughly validated with a simple and powerful testing framework.

