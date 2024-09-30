import pytest
from martian_robots import MartianRobots
from main import process_input


# Unit Tests

def test_turn_left():
    """Test turning left in all directions."""
    robot = MartianRobots(5, 5)
    x, y, orientation = robot.turn_left(0, 0, 'N')
    assert orientation == 'W'

    x, y, orientation = robot.turn_left(0, 0, 'W')
    assert orientation == 'S'

    x, y, orientation = robot.turn_left(0, 0, 'S')
    assert orientation == 'E'

    x, y, orientation = robot.turn_left(0, 0, 'E')
    assert orientation == 'N'


def test_turn_right():
    """Test turning right in all directions."""
    robot = MartianRobots(5, 5)
    x, y, orientation = robot.turn_right(0, 0, 'N')
    assert orientation == 'E'

    x, y, orientation = robot.turn_right(0, 0, 'E')
    assert orientation == 'S'

    x, y, orientation = robot.turn_right(0, 0, 'S')
    assert orientation == 'W'

    x, y, orientation = robot.turn_right(0, 0, 'W')
    assert orientation == 'N'


def test_move_forward():
    """Test moving forward in all directions within grid bounds."""
    robot = MartianRobots(5, 5)
    x, y, orientation, lost = robot.move_forward(1, 1, 'N')
    assert (x, y, orientation, lost) == (1, 2, 'N', False)

    x, y, orientation, lost = robot.move_forward(1, 1, 'E')
    assert (x, y, orientation, lost) == (2, 1, 'E', False)

    x, y, orientation, lost = robot.move_forward(1, 1, 'S')
    assert (x, y, orientation, lost) == (1, 0, 'S', False)

    x, y, orientation, lost = robot.move_forward(1, 1, 'W')
    assert (x, y, orientation, lost) == (0, 1, 'W', False)


def test_move_out_of_bounds():
    """Test moving the robot out of bounds and getting lost."""

    # First test: Moving north out of bounds
    robot1 = MartianRobots(5, 5)
    x, y, orientation, lost = robot1.move_forward(5, 5, 'N')
    assert (x, y, orientation, lost) == (5, 5, 'N', True), "Robot should be lost moving north out of bounds"

    # Second test: Moving east out of bounds from a fresh robot instance
    robot2 = MartianRobots(5, 5)
    x, y, orientation, lost = robot2.move_forward(5, 5, 'E')
    assert (x, y, orientation, lost) == (5, 5, 'E', True), "Robot should be lost moving east out of bounds"


# Integration Tests


def test_invalid_grid_size():
    """Test invalid grid size input."""
    with pytest.raises(ValueError):
        input_data = "-1 5\n3 2 N\nFRRFLLFFRRFLL"
        result = process_input(input_data)  # Negative grid size is invalid
    with pytest.raises(ValueError):
        input_data = "5 0\n3 2 N\nFRRFLLFFRRFLL"
        result = process_input(input_data)  # Negative grid size is invalid   # Zero grid height is invalid


def test_robot_lost():
    """Test robot getting lost when moving out of bounds."""
    input_data = "5 3\n3 2 N\nFRRFLLFFRRFLL"
    result = process_input(input_data)
    assert result[0] == "3 3 N LOST", "Robot should be lost"


def test_scent_prevents_loss():
    """Test the scenario where the scent prevents another robot from getting lost."""
    input_data = (
        "5 3\n"
        "3 2 N\nFRRFLLFFRRFLL\n"  # First robot gets lost
        "3 2 N\nFRRFLLFFRF\n"           # Second robot should move and check scent
    )
    result = process_input(input_data)
    assert result[0] == "3 3 N LOST", "First robot should get lost"
    assert result[1] == "4 3 E", "Second robot should move east to (4, 3) without getting lost"


def test_robot_moves():
    """Test robot moves normally within grid bounds."""
    input_data = "5 3\n1 1 E\nRFRFRFRF"
    result = process_input(input_data)
    assert result[0] == "1 1 E", "Robot should remain at (1, 1) facing East"


