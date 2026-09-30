# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Logs**

Document at least 3 bugs you found. Add rows as needed.

| Input Used | Expected Behavior | Actual Behavior | Console Error / Output | Suspected Code Location |
|------------|-------------------|-----------------|------------------------|-------------------------|
| Enter the displayed secret number and submit it; compare the win-message score with the score in Developer Debug Info. | The final score in the win message should match the score shown in the debug panel. | In my run, the finalized score did not match the score shown in the debug panel. | None observed. | `app.py`: `update_score()` and the win-message score display. |

| Win the game, then select **New Game**. | The game should reset its completed status and let the player make another guess without reloading the page. | The completed-game state remains active, so the new game cannot be played; refreshing the page is required to start over. | None observed. | `app.py`: the `new_game` handler and `st.session_state.status` reset. |

| Set the secret to 58, then submit 57 and `-1`. | For 57, the hint should say “Go HIGHER!” For `-1`, the app should reject the guess as outside the 1–100 range. | The hint says “Go LOWER!” for 57, and `-1` is accepted instead of triggering range validation. | None observed. | `app.py`: `parse_guess()` range validation and `check_guess()` hint comparison/message. |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

I used GitHub Copilot in VS Code. Copilot correctly identified that the New Game handler left the old `won` status in session state, so the status guard stopped later guesses; I used a button callback to reset the game before Streamlit reruns. An early Copilot response only added a `FIXME` marker, which documented the problem but did not restore play, so I followed up with a callback that also resets the score, history, attempts, and old input. An AppTest that starts from a won game, clicks New Game, and submits another guess verified the fix.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I considered the bug fixed only after testing the full interaction: a completed game resets, the old guess is cleared, and a new guess is accepted. The new pytest case verifies those state changes and the existing logic tests cover the hint directions and input range; all six tests passed. Copilot helped translate the UI failure into explicit state assertions that can catch a regression without relying on a manual browser check.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

When someone interacts with a Streamlit widget, Streamlit runs the app script again from top to bottom. Ordinary variables are recreated during that rerun, while values in `st.session_state` persist for that user's session. That is why a button callback can reset session state before the next run, and why leaving the old `won` status in state kept the game locked.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

I want to keep writing a focused regression test for the exact bug I am fixing. The AppTest for this game reproduced a completed round, clicked New Game, and verified that another guess could be submitted. That gave me a repeatable check of the state transition instead of relying only on what I saw in the browser.

- What is one thing you would do differently next time you work with AI on a coding task?

Next time, I would give the assistant the reproduction steps, expected behavior, and relevant tests in the first prompt. I would ask for one scoped change at a time, review the diff, and run the focused test before moving to the next issue. That should make it easier to catch incomplete fixes while the change is still small.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

I now treat AI-generated code as a draft to verify, not as proof that a bug is fixed. In this project, tests and diff review exposed state-flow details that a plausible-looking code change could miss.
