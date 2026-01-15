# Gemini CLI Test Project - Tic-Tac-Toe

## Project Overview
This project is a simple, interactive Command Line Interface (CLI) implementation of the classic Tic-Tac-Toe game. It is written in Python and allows two players to play against each other on the same terminal.

### Key Features
- **Language:** Python 3
- **Interface:** Text-based CLI
- **Gameplay:** 2-player hotseat (Player X vs Player O)
- **Input:** Accepts row and column numbers (1-based index)

## Architecture
The project consists of a single Python script:
- `tictactoe.py`: Contains the game logic, board rendering, input handling, and the main game loop.

## Getting Started

### Prerequisites
- Python 3.x installed on your system.

### Running the Game
To start the game, navigate to the project directory and run:

```bash
python3 tictactoe.py
```

### How to Play
1. The game displays a 3x3 grid.
2. Players take turns placing their mark ('X' or 'O').
3. When prompted, enter the **row** and **column** numbers separated by a space (e.g., `1 2` for row 1, column 2).
   - Rows and columns are numbered **1, 2, and 3**.
4. The first player to align 3 marks horizontally, vertically, or diagonally wins.
5. If the board fills up without a winner, the game declares a draw.

## Development Conventions

### File Structure
- `tictactoe.py`: Main source code.
- `.gitignore`: Standard Python ignore patterns (pycache, venvs).

### Coding Style
- **Input Handling:** User input is 1-based for friendliness but converted to 0-based for internal array logic.
- **Error Handling:** `try-except` blocks catch `ValueError` (non-integer input) and `IndexError` (out of bounds) to prevent crashes and prompt for retry.
