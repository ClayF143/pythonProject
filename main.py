# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import chess


def heuristic_piece_vals(my_board):
    if my_board.is_game_over():
        outcome = my_board.outcome()
        if outcome.winner is None:
            return 0
        if outcome.winner == chess.WHITE:
            return 100
        if outcome.winner == chess.BLACK:
            return -100

    result = 0
    for char in my_board.fen().split()[0]:
        if char == 'R':
            result += 5
        elif char == 'N' or char == 'B':
            result += 3
        elif char == 'Q':
            result += 10
        elif char == 'P':
            result += 1
        elif char == 'r':
            result -= 5
        elif char == 'n' or char == 'b':
            result -= 3
        elif char == 'q':
            result -= 10
        elif char == 'p':
            result -= 1
    return result


def min_max(my_board, curr_depth, max_depth):
    if my_board.is_game_over():
        return None, heuristic_piece_vals(my_board)
    for m in my_board.legal_moves:
        temp_board = chess.Board(my_board.fen())
        temp_board.push(m)
        if curr_depth == max_depth:
            temp_val = heuristic_piece_vals(temp_board)
        else:
            temp_val = min_max(temp_board, curr_depth + 1, max_depth)[1]
            old_val = heuristic_piece_vals(my_board)

        if 'best_board' not in locals():
            best_board = temp_board
            best_val = temp_val
            best_move = m
        elif (my_board.turn and temp_val > best_val) or \
             (not my_board.turn and temp_val < best_val):
            best_board = temp_board
            best_val = temp_val
            best_move = m
    return best_move, best_val


if __name__ == '__main__':
    board = chess.Board('Q7/p1p1q1pk/3p2rp/4n3/3bP3/7b/PP3PPK/R1B2R2 b - - 0 1')
    i = 3
    while not board.is_game_over():
        print(board)
        move = min_max(board, 0, i)[0]
        board.push(move)
        print(move)
        print()
    print(board)
    print(move)
