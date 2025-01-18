# 🧩 Sudoku Solver Visualization

## 🌟 Overview
This project is a **Sudoku Solver Visualization** built using Python and Pygame. It showcases how a Sudoku puzzle is solved step-by-step, visually highlighting the progress. The project is modular, with each component separated into logical files for better maintainability and readability.

---

## 📂 File Structure
```
sudoku_solver/
|
├── main.py                # Entry point of the program
├── constants.py           # Constants like colors, grid size, and cell size
├── visualization.py       # Functions for drawing the grid and Pygame setup
├── board.py               # Functions related to board handling
├── solver.py              # Sudoku solving logic
└── __init__.py            # To make the directory a package (optional for Python 3.3+)
```

---

## 🛠️ How It Works

### 1. **Main Script (`main.py`)**
- 🏁 This is the entry point of the application.
- Initializes the Sudoku board and starts the visualization loop.
- Handles user input such as quitting the program.

### 2. **Constants (`constants.py`)**
- 📋 Contains global constants such as:
  - 🧮 Grid size, cell size, and padding.
  - 🎨 Color definitions for the UI (e.g., `WHITE`, `GRAY`, etc.).

### 3. **Visualization (`visualization.py`)**
- 🖼️ Manages Pygame initialization and drawing of the grid.
- Handles the visual representation of the Sudoku board, including:
  - 🔢 Number placement.
  - ✨ Highlighting cells during the solving process.
  - 📏 Drawing the grid lines.

### 4. **Board Handling (`board.py`)**
- 🧮 Contains helper functions for board setup and manipulation:
  - `string_to_board(sudoku_string)`: Converts a string representation of the Sudoku puzzle into a 2D list.

### 5. **Solver (`solver.py`)**
- 🤖 Implements the logic to solve the Sudoku puzzle using:
  - **Backtracking Algorithm**: A recursive method to try numbers in empty cells while ensuring validity.
  - **Validation Function**: Ensures a number can be placed in a specific cell based on Sudoku rules.
- Calls visualization functions to update the grid in real-time as it solves the puzzle.

---

## ⚙️ How to Install
1. Ensure you have Python (>=3.7) installed on your system.
2. Install Pygame by running the following command:
   ```bash
   pip install pygame
   ```
3. Clone or download the project files to your local system.

---

## ▶️ How to Run
1. Navigate to the project directory:
   ```bash
   cd sudoku_solver
   ```
2. Run the program:
   ```bash
   python main.py
   ```

---

## 📌 Where to Define the Sudoku Puzzle
- The Sudoku puzzle you want to solve is defined as a string in `main.py`:
  ```python
  sudoku_string = "070000300040053900900008000006000004300049000005000060000100200050000700000070051"
  ```
- Replace the `sudoku_string` with your own puzzle string. The string must contain exactly 81 characters where:
  - Digits `1-9` represent pre-filled cells.
  - `0` represents empty cells.

---

## ✨ Features
- **Dynamic Visualization**: Watch the Sudoku puzzle being solved step-by-step.
- **Customizable**: Update the Sudoku string in `main.py` to solve different puzzles.
- **User Interaction**:
  - 🛑 Press `ESC` to quit the program.
  - 🚀 Automatically starts solving upon launch.

---

## 🔍 Example
The default Sudoku puzzle is defined in `main.py` as:
```python
sudoku_string = "070000300040053900900008000006000004300049000005000060000100200050000700000070051"
```
You can replace this string with any valid Sudoku puzzle (81 characters, 0 for empty cells).

---

## 🤝 Contributing
Feel free to modify or extend the project. Some potential improvements:
- Adding a GUI for users to input their puzzles.
- Implementing advanced solving techniques.

---

## 📜 License
This project is open-source and free to use.

---

