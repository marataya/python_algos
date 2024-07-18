def check_winner(moves):
    count = {}
    players = ["First", "Second"]
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

        if count[player]["rows"][r] == 5 or count[player]["columns"][c] == 5 or count[player]["diagonals"][
            r - c] == 5 or count[player]["diagonals"][r + c] == 5:
            return "Inattention"

        if i > 0:
            prev_player = players[(i - 1) % 2]
            if prev_player in count and (
                    count[prev_player]["rows"] or count[prev_player]["columns"] or count[prev_player]["diagonals"]):
                return "Inattention"

    if len(moves) % 2 == 0:
        last_player = "Second"
    else:
        last_player = "First"

    if last_player in count and (
            count[last_player]["rows"] or count[last_player]["columns"] or count[last_player]["diagonals"]):
        return "Inattention"
    else:
        return "Draw"


n = int(input())
moves = []
for _ in range(n):
    r, c = map(int, input().split())
    moves.append((r, c))

result = check_winner(moves)
print(result)