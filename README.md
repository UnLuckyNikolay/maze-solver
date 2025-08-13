# Maze Generator and Solver

Tool that generates and solves randomized mazes built as a Boot.dev project.

Includes a config file `constants.py` and graphical enhancements.

## Install and Run

1. Install [Python](https://www.python.org/downloads) 3.10 or higher.

2. Clone the repository:

    ```bash
	git clone https://github.com/UnLuckyNikolay/maze-solver
    cd maze-solver
	```

3.  Edit the settings in `constants.py` if needed

4. Run:

	```bash 
	python3 main.py
	```

## Features

* Depth-first algorithms for creating and solving randomized mazes on a loop
* 3D-styled vector graphics for the maze
* Configuration file `constants.py` that includes screen resolution, maze size, animation speed, color variables and debug features

## Project Progression

* **Project completed!**

	The basic version of the project.

	![Project Phase 1 Showcase](https://imgur.com/b886dgI.png)

* **General refinement**

	First round of polishes. Tweaked the algorithm to ignore certain obvious dead-ends. Changed all the colors, added corners and thickness to the walls. Made the path go through the entrance and exit.

	![Project Phase 2 Showcase](https://imgur.com/UqQGwlO.png)

* **3D style**

	Fully rewritten how the walls work. Previous walls were just simple lines and were deleted by painting them over. New walls are classes that store IDs of the polygons which allows to delete them on the go.

	![Project Phase 3 Showcase](https://imgur.com/d4JhPXa.png)