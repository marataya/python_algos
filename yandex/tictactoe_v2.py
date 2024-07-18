def check_win(count):
  """
  Checks if a player has a winning streak of 5 with consecutive elements.

  Args:
      count: A dictionary containing player moves and their counts.

  Returns:
      True if a player has a winning streak with consecutive elements, False otherwise.
  """
  for player in count:
    rows = count["rows"]
    columns = count["columns"]
    diagonals = count["diagonals"]

    # Check rows
    current_count = 0
    for row, row_count in rows.items():
      current_count = max(current_count, row_count)  # Track consecutive count
      if current_count >= 5:
        return True
      if row_count == 0:  # Reset count if a cell is empty
        current_count = 0

    # Check columns (similar logic as rows)
    current_count = 0
    for col, col_count in columns.items():
      current_count = max(current_count, col_count)
      if current_count >= 5:
        return True
      if col_count == 0:
        current_count = 0

    # Check diagonals (considering absolute values for summing and tracking consecutive count)
    current_count = 0
    for diag, diag_count in diagonals.items():
      current_count = max(current_count, abs(diag_count))
      if current_count >= 5:
        return True
      if diag_count == 0:
        current_count = 0

  return False

def check_winner(moves):
    count = {}
    players = ["First", "Second"]
    inattention = False
    for i, (r, c) in enumerate(moves):
        player = players[i % 2]
        count[player] = count.get(player, {})
        count[player]["rows"] = count[player].get("rows", {})
        count[player]["columns"] = count[player].get("columns", {})
        count[player]["diagonals"] = count[player].get("diagonals", {})

        count[player]["rows"][r] = count[player]["rows"].get(r, 0) + 1
        count[player]["columns"][c] = count[player]["columns"].get(c, 0) + 1
        count[player]["diagonals"][r - c] = count[player]["diagonals"].get(r - c, 0) + 1
        count[player]["diagonals"][r + c] = count[player]["diagonals"].get(r + c, 0) + 1

        if check_win(count[player]):
            winner = player
            if i < len(moves)-1:
                return "Inattention"
            else:
                return player

    return "Draw"


# n = int(input())
# moves = []
# for _ in range(n):
#     r, c = map(int, input().split())
#     moves.append((r, c))

moves = [
    (5, 0),
    (1, 1),
    (4, 0),
    (2, 1),
    (3, 0),
    (3, 1),
    (2, 0),
    (4, 1),
    (1, 0),
    (5, 1)
]

moves1 = [
    (4, 4),
    (4, 5),
    (2, 2),
    (2, 3),
    (3, 3),
    (3, 4),
    (1, 1),
    (1, 2),
    (5, 5)
]

result = check_winner(moves)
print(result)