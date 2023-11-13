import unittest
from io import StringIO
from unittest.mock import patch
from battling_knights import Arena, parse_moves, update_board_with_moves, output_final_state

class TestKnightArena(unittest.TestCase):
    def setUp(self):
        self.arena = Arena()

    def test_single_move_red_knight(self):
        moves = parse_moves(StringIO("red:S\n"))  # Use 'red' instead of 'R'
        update_board_with_moves(self.arena, moves)
        output_file = "output_single_move_red_knight.json"  # Specify the file path
        output_final_state(self.arena, output_file)
        # Add assertions to check the output, e.g., assert os.path.isfile(output_file)

    def test_multiple_moves(self):
        moves = parse_moves(StringIO("red:S\nblue:E\ngreen:N\nyellow:N\n"))  # Specify knight names
        update_board_with_moves(self.arena, moves)
        output_file = "output_multiple_moves.json"  # Specify the file path
        output_final_state(self.arena, output_file)
        # Add assertions to check the output

    def test_knight_battle(self):
        moves = parse_moves(StringIO("red:S\nblue:S\ngreen:N\nyellow:N\n"))  # Specify knight names
        update_board_with_moves(self.arena, moves)
        output_file = "output_knight_battle.json"  # Specify the file path
        output_final_state(self.arena, output_file)
        # Add assertions to check the output

    def test_invalid_moves(self):
        moves = parse_moves(StringIO("GAME-START\nINVALID\nGAME-END\n"))
        update_board_with_moves(self.arena, moves)
        output_file = "output_invalid_moves.json"  # Specify the file path
        output_final_state(self.arena, output_file)
        # Add assertions to check the output

if __name__ == "__main__":
    unittest.main()
