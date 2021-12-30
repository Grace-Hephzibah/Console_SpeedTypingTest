def penalty_code(current_text, target_text, val):
    # Penalty calculation code
    penalty = 0
    for i, char in enumerate(current_text):
        if char != target_text[i]:
            penalty += 1
    tot_len = max(len(current_text), 1)
    penalty_rate = round(penalty / tot_len, 2)  # Let the answer vary between 0 and 1 for simplicity
    actual_wpm = round(val * (1 - penalty_rate))  # Let the number be whole number here

    return penalty_rate, actual_wpm
