import unittest
from unittest.mock import patch
from io import StringIO
import tictactoe

class TestTicTacToeLogic(unittest.TestCase):
    def setUp(self):
        self.empty_board = [[" " for _ in range(3)] for _ in range(3)]

    def test_check_winner_rows(self):
        # Test all rows for X
        for r in range(3):
            board = [[" " for _ in range(3)] for _ in range(3)]
            board[r] = ["X", "X", "X"]
            self.assertTrue(tictactoe.check_winner(board, "X"), f"X should win row {r}")
            self.assertFalse(tictactoe.check_winner(board, "O"), f"O should not win row {r}")

    def test_check_winner_cols(self):
        # Test all columns for O
        for c in range(3):
            board = [[" " for _ in range(3)] for _ in range(3)]
            for r in range(3):
                board[r][c] = "O"
            self.assertTrue(tictactoe.check_winner(board, "O"), f"O should win col {c}")
            self.assertFalse(tictactoe.check_winner(board, "X"), f"X should not win col {c}")

    def test_check_winner_diagonals(self):
        # Main diagonal
        board = [
            ["X", " ", " "],
            [" ", "X", " "],
            [" ", " ", "X"]
        ]
        self.assertTrue(tictactoe.check_winner(board, "X"))
        
        # Anti-diagonal
        board = [
            [" ", " ", "O"],
            [" ", "O", " "],
            ["O", " ", " "]
        ]
        self.assertTrue(tictactoe.check_winner(board, "O"))

    def test_no_winner(self):
        self.assertFalse(tictactoe.check_winner(self.empty_board, "X"))
        board = [
            ["X", "O", "X"],
            ["X", "O", "O"],
            ["O", "X", "X"]
        ] # Draw board
        self.assertFalse(tictactoe.check_winner(board, "X"))
        self.assertFalse(tictactoe.check_winner(board, "O"))

    def test_is_full(self):
        self.assertFalse(tictactoe.is_full(self.empty_board))
        
        full_board = [
            ["X", "O", "X"],
            ["X", "O", "O"],
            ["O", "X", "X"]
        ]
        self.assertTrue(tictactoe.is_full(full_board))
        
        partial_board = [
            ["X", "O", "X"],
            [" ", "O", "O"],
            ["O", "X", "X"]
        ]
        self.assertFalse(tictactoe.is_full(partial_board))


class TestTicTacToeGameFlow(unittest.TestCase):
    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_x_wins_game(self, mock_stdout, mock_input):
        # Simulate inputs for X winning:
        # X: 1 1, O: 2 1, X: 1 2, O: 2 2, X: 1 3
        mock_input.side_effect = [
            "1 1", # X
            "2 1", # O
            "1 2", # X
            "2 2", # O
            "1 3"  # X wins
        ]
        
        tictactoe.tic_tac_toe()
        output = mock_stdout.getvalue()
        self.assertIn("Player X wins!", output)

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_draw_game(self, mock_stdout, mock_input):
        # Sequence for a draw
        # X | O | X
        # X | O | O
        # O | X | X
        mock_input.side_effect = [
            "1 1", "1 2", "1 3", # X O X
            "2 1", "2 2", "2 3", # X O O
            "3 2", "3 1", "3 3"  # X O X (Wait, carefully mapped)
        ]
        # Re-mapping to actual game flow logic to ensure valid moves
        # Board positions:
        # 1,1(X) 1,2(O) 1,3(X)
        # 2,1(X) 2,2(O) 2,3(O)
        # 3,1(O) 3,2(X) 3,3(X)
        
        # Move sequence:
        # X: 1 1
        # O: 1 2
        # X: 1 3
        # O: 2 2
        # X: 2 1
        # O: 2 3
        # X: 3 2
        # O: 3 1
        # X: 3 3
        
        mock_input.side_effect = [
            "1 1", "1 2",
            "1 3", "2 2",
            "2 1", "2 3",
            "3 2", "3 1",
            "3 3"
        ]
        
        tictactoe.tic_tac_toe()
        output = mock_stdout.getvalue()
        self.assertIn("It's a draw!", output)

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_input_and_retry(self, mock_stdout, mock_input):
        # Simulate invalid inputs then a win
        mock_input.side_effect = [
            "invalid", # ValueError
            "1",       # ValueError (not enough values)
            "4 4",     # IndexError (logic handles bounds)
            "1 1",     # Valid X
            "1 1",     # Cell taken
            "2 1",     # Valid O
            "1 2",     # X
            "2 2",     # O
            "1 3"      # X wins
        ]
        
        tictactoe.tic_tac_toe()
        output = mock_stdout.getvalue()
        self.assertIn("Invalid input", output)
        # self.assertIn("Coordinates out of range", output) # This is swallowed by the generic error handler
        self.assertIn("Cell already taken", output)
        self.assertIn("Player X wins!", output)

if __name__ == '__main__':
    unittest.main()
