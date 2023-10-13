# Bowling Class

This Python class, `Bowling`, is designed to help you calculate and keep track of scores for a game of ten-pin bowling. 
It provides methods to add points for each frame and calculate the total score. 

This README will explain the usage and features of the class.

## Table of Contents

- [Usage](#usage)
- [Methods](#methods)
- [Example](#example)
- [Contributing](#contributing)


## Usage

You can use the `Bowling` class in your Python projects to keep track of bowling scores. Follow these steps to get started:

1. Import the `Bowling` class in your Python script:
   ```python
   from bowling import Bowling

2. Create an instance of the class:
   ```python
   game = Bowling()
   ```
3. Add points for each frame using the add_points method:
   ATENTION: Do NOT use X or /, use the real number os points for each ball.
   ```python
   game.add_points(10)  # Strike in the first frame
   game.add_points(7, 3)  # Spare in the second frame
   ```
4. Calculate the total score using the calculate_points method:
   ```python
     game.calculate_points(True)
   ```
6. Show Total Points using the game.show_total_score method:
   ```python
   game.show_total_score()
   ```

## Methods

* add_points(self, first_ball, second_ball=0, extra_ball_frame10=0):
  > Add points for each frame. The extra_ball_frame10 parameter is optional and used for the 10th frame.

* calculate_points(self, full=False):
  > Use this method for calculate the points. It handles strikes, spares, and normal frames.
  > For DEFAULT it calculates the score for the last frame. If pass the parameter True, it recalculates the entire score;

* show_frame_table(self):
  > Display the frame table.

* show_score_table(self):
  > Display the score table.

* show_total_score(self):
  > Display the total score for the game.

## Example
```python 
   from bowling import Bowling
   
   # Create a new game
   game = Bowling()
   
   # Add points for each frame
   game.add_points(10)  # Strike in the first frame
   game.add_points(7, 3)  # Spare in the second frame
   # Add points for subsequent frames
   
   # Calculate the total score
   game.calculate_points(True)
   
   # Display frame table, score table, and the total score
   game.show_frame_table()
   game.show_score_table()
   game.show_total_score()
```

## Contributing
If you would like to contribute to the development of this class, feel free to fork the repository, make your changes, and submit a pull request.
