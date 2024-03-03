"""

"""


def climbingLeaderboard(ranked, player):
    set = {x for x in ranked}
    ranks_desc = sorted(list(set), reverse=True)
    player_desc = sorted(player, reverse=True)

    player_rank = 0

    result = []
    for i in range(len(player_desc)):
        while player_rank < len(ranks_desc) and player_desc[i] < ranks_desc[player_rank]:
            player_rank += 1

        result.append(player_rank + 1)

    return result[::-1]


if __name__ == '__main__':
    # Example usage:
    ranked = [100, 90, 90, 80, 75, 60]
    player = [50, 65, 77, 90, 102]
    print(climbingLeaderboard(ranked, player))  # Output: [6, 5, 4, 2, 1]
