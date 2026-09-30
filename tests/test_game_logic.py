from logic_utils import check_guess, parse_guess
from streamlit.testing.v1 import AppTest

def test_winning_guess():
    result = check_guess(50, 50)
    assert result == ("Win", "🎉 Correct!")

def test_guess_too_high():
    result = check_guess(60, 50)
    assert result == ("Too High", "📉 Go LOWER!")

def test_guess_too_low():
    result = check_guess(40, 50)
    assert result == ("Too Low", "📈 Go HIGHER!")

def test_guess_handles_string_secret():
    assert check_guess(57, "58") == ("Too Low", "📈 Go HIGHER!")

def test_parse_guess_rejects_out_of_range_values():
    assert parse_guess("-1", 1, 100) == (
        False,
        None,
        "Guess must be between 1 and 100.",
    )
    assert parse_guess("101", 1, 100) == (
        False,
        None,
        "Guess must be between 1 and 100.",
    )

def test_new_game_allows_guess_after_win():
    app = AppTest.from_file("app.py").run()
    app.session_state["status"] = "won"
    app.session_state["attempts"] = 3
    app.session_state["score"] = 70
    app.session_state["history"] = [72]
    app.session_state["guess_input_Normal"] = "94"

    app.button[1].click().run()

    assert app.session_state["status"] == "playing"
    assert app.session_state["attempts"] == 0
    assert app.session_state["score"] == 0
    assert app.session_state["history"] == []
    assert app.session_state["guess_input_Normal"] == ""

    app.session_state["secret"] = 50
    app.text_input[0].set_value("49")
    app.button[0].click().run()

    assert app.session_state["status"] == "playing"
    assert app.session_state["history"] == [49]
    assert not app.exception
