# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] **Purpose:** Guess the secret number using the game's higher/lower hints before the attempt limit runs out.
- [x] **Bugs found:** The higher/lower hints were reversed, guesses outside the selected range were accepted, and the completed-game status prevented New Game from accepting another guess. The debug panel can also display the previous score during the same run that calculates the final score.
- [x] **Fixes applied:** Moved game rules into `logic_utils.py`, corrected hint directions, validated guesses against the selected difficulty, and reset the game state and input when New Game is clicked. The debug-score display issue remains marked with a `FIXME` in `app.py`.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Start the app with `python -m streamlit run app.py`, select a difficulty, and expand **Developer Debug Info** to see the secret number and allowed range.
2. Enter a valid guess below the secret. The game reports **Too Low** and, when **Show hint** is enabled, prompts you to go higher.
3. Enter a valid guess above the secret. The game reports **Too High** and prompts you to go lower.
4. Enter a number outside the selected difficulty's range, such as `101` in Normal mode. The game rejects it with a range-validation message.
5. Enter the secret number to win. Then select **New Game**; the score, attempts, history, and input reset, and another guess can be submitted without refreshing the page.

## 🧪 Test Results

```text
$ ./.venv/bin/python -m pytest -q
......                                                                   [100%]
6 passed in 1.07s
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
