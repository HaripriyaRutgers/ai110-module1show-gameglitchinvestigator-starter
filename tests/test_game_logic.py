from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == ("Win", "🎉 Correct!")

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High" with correct message
    result = check_guess(60, 50)
    assert result == ("Too High", "📉 Go LOWER!")

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low" with correct message
    result = check_guess(40, 50)
    assert result == ("Too Low", "📈 Go HIGHER!")

def test_check_guess_with_string_secret_positive():
    # Test that string secrets are handled correctly (converted to int)
    result = check_guess(60, "50")
    assert result == ("Too High", "📉 Go LOWER!")

    result = check_guess(40, "50")
    assert result == ("Too Low", "📈 Go HIGHER!")

def test_check_guess_with_string_secret_negative():
    # Test the bug fix: negative string secrets should give correct hints
    # This was the "negative numbers being the secret number bug"
    result = check_guess(10, "-35")
    assert result == ("Too High", "📉 Go LOWER!")  # 10 > -35, so too high

    result = check_guess(-40, "-35")
    assert result == ("Too Low", "📈 Go HIGHER!")  # -40 < -35, so too low

    result = check_guess(-35, "-35")
    assert result == ("Win", "🎉 Correct!")

def test_check_guess_fallback_string_comparison():
    # If secret can't be converted to int, fall back to string comparison
    result = check_guess(2, "abc")
    # '2' vs 'abc': '2' < 'a' (ascii), so "Too Low"? Wait, '2' ascii 50, 'a' 97, 50 < 97, so guess < secret, "Too Low"
    # But '2' > 'a'? No, 50 < 97, so "Too Low"
    assert result == ("Too Low", "📈 Go HIGHER!")

    result = check_guess(100, "50")
    # '100' > '50' lexicographically? '1' vs '5', '1' < '5', so "Too Low"? No.
    # Since int("50") works, it uses numeric: 100 > 50, "Too High"
    assert result == ("Too High", "📉 Go LOWER!")
