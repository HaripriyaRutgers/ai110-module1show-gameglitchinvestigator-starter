# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  - The instructions say that the guess is between 1 to 100 but when i played the game the actuall answer was -35 which is a negative number so it kept saying go lower
  - Does not let me hit new game, even if i did, it did not start a new game, i had to reload the website again to start a new game.
  - The secret number was 21 but when i typed my first guess which was 50, it said to go higher.
  - Attenpts left and Score keeps going to negative numbers
  - No of attempts aloowed for easy mode is 6 meanwhile it is 8 for normal. It should be the other way around

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
 I used Copilot for this project
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

Copilor suggested fixing the check_guess function in logic_utils.py by correcting the inverted hint messages ("Go LOWER!" for guesses that are too high and "Go HIGHER!" for guesses that are too low) and ensuring proper handling of string secrets. This was correct because the original code had the hints the otherway around. I verified it by running the updated function with test inputs like check_guess(60, 50) returning ("Too High", "Go LOWER!"), and by creating and running pytest tests that passed, confirming the hints are now valid.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

The AI initially suggested that the secret number could be negative because the game's range was set to 1-100, saying the bug was in the random generation allowing negatives. This was misleading because the random.randint(1, 100) always produces positive numbers, and the real issue was the inverted hints making it look like the secret was negative. I verified by checking the code: the range function returns positive bounds, and testing showed that even with correct ranges, the hints were wrong (eg guessing 50 for secret 21 said "go higher" instead of "go lower"). The AI later corrected this by focusing on the hint logic.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I reran the app and tried playing the game to make sure that the the intended bugs were fixed. I also asked copilot to genertae pytests to make sure that the fixes that it suggested and I approves were really working.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

  I ran pytest on the test_game_logic.py file, which had check_guess function with various inputs, including string secrets representing negative numbers. The tests passed, showing that the hint messages were accurate ("Go LOWER!" for too high, "Go HIGHER!" for too low) This confirmed the fix for the inverted hints and negative secret bug worked as expected.

- Did AI help you design or understand any tests? How?

  Yes Copilot helped design the pytest by generating the test cases, including specific scenarios like testing with negative string secrets (check_guess(10, "-35")). It also explained how the tests verified the fixes, such as maing sure that the numeric comparison is done over string comparison when possible, which helped me understand why the original code failed and how the new version succeeded.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.

  The secret number kept changing because Streamlit reruns the entire script everytime the user inputs their guess into the game, instead of it staying the same for each game session
   

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

  Streamlit "reruns" mean the app re-executes the whole Python script from top to bottom every time you click a button or change something.

- What change did you make that finally gave the game a stable secret number?

  I ensured the secret is only set once in st.session_state when the app starts, and properly reset it when clicking "New Game" to random.randint(1, 100), preventing it from changing in the middle of the game due to reruns.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

  Using pytest to write automated tests for functions after fixing bugs, to ensure changes work. I did not know you could use AI to write test cases for you

- What is one thing you would do differently next time you work with AI on a coding task?

  Ask the AI to generate tests earlier in the debugging process, and also give specific instrctions so that it is not out of context for the AI to understand.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

  This project showed me that AI-generated code can have subtle bugs like inverted logic or poor error handling, so I now approach it with more skepticism and always test thoroughly. It also highlighted how AI can be a great teammate for quick fixes and test generation, but human verification is essential.
