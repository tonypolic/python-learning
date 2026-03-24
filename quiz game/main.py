def get_next_question():
    """Return the next quiz question."""
    return "What is 2 + 2? "

while not game_over:
    # Ask the user a question
    question = get_next_question()
    user_answer = input(question)

    # Check if the answer is correct
    if check_answer(user_answer):
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

    # Check if the game is over
    game_over = check_game_over()