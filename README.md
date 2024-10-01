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
