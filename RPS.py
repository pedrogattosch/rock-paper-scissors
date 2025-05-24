def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    pattern_length = 3
    guess = "R"

    if len(opponent_history) > pattern_length:
        recent_pattern = opponent_history[-pattern_length:]

        pattern_counts = {}

        for i in range(len(opponent_history) - pattern_length):
            pattern = tuple(opponent_history[i:i + pattern_length])
            next_play = opponent_history[i + pattern_length]

            if pattern == tuple(recent_pattern):
                if next_play in pattern_counts:
                    pattern_counts[next_play] += 1
                else:
                    pattern_counts[next_play] = 1

        if pattern_counts:
            predicted_play = max(pattern_counts, key=pattern_counts.get)

            if predicted_play == "R":
                guess = "P"
            elif predicted_play == "P":
                guess = "S"
            elif predicted_play == "S":
                guess = "R"

    return guess
