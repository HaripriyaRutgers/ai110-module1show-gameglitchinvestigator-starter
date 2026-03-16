def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"

    This function ensures hints are correct (higher/lower) even when the
    secret is stored as a string.
    """

    if guess == secret:
        return "Win", "🎉 Correct!"

    # Prefer numeric comparison when possible.
    try:
        secret_int = int(secret)
    except (TypeError, ValueError):
        secret_int = None

    if secret_int is not None:
        if guess > secret_int:
            return "Too High", "📉 Go LOWER!"
        if guess < secret_int:
            return "Too Low", "📈 Go HIGHER!"

    # Fall back to string comparison for non-numeric secrets.
    g = str(guess)
    s = str(secret)
    if g == s:
        return "Win", "🎉 Correct!"
    if g > s:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"

#FIX: Refactored logic into logic_utils.py using Copilot Agent mod
def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number.

    Prevents score from going negative.
    """
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return max(0, current_score - 5)  # Prevent negative

    if outcome == "Too Low":
        return max(0, current_score - 5)  # Prevent negative

    return current_score
