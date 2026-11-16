
# PAWPOINTS🐾
Welcome to PawPoints, a wildlife-based quiz game.

## Why this exists?
In my first year-2022, my friend losh and I were sitting around, trying to pick a project idea that wouldn't melt our brains but would still look good enough to not fail. Thanks to this random project suggestion from our professor, and my friend/teammate losh who tolerated me during a all-nighter to pull this off!
And thus, **PawPoints** was developed! yes, but with *a LOT of changes* (thank you again, staff). We coded, debugged, redesigned, and probably broke the script once!
Anyway, it was the first project! and yes from us, *due tomorrow, do tomorrow* fellas (why do you think our staff suggested the idea, if not for the due date? hahaha, jk)
-This project was done mostly with friendship, late-night logic errors, and a bunch of "oops, forgot to strip() that input"

## What is it?
Pawpoints is a **command-line Python quiz game** with 3 difficulty levels:
Run the program with command: `python pawpoints.py`
- Easy –- for normal students 
- Intermediate -– for students who still remember their bio class  
- Difficult -– for that one zoologist student who knows what a *tardigrade* is
  
You get 2 attempts per question; Answers are not case-sensitive, but spelling must be correct! And the scoring works like this:
- First try correct -> 10 points
- Second try correct -> 5 points
- Both wrong -> 0 points

## Project Structure
Store everything within a folder like below:
/pawpoints/
├── pawpoints.py
├── easy.txt 
├── intermediate.txt 
└── difficult.txt 
You can add additional q&a's in .txt files if you want(but add them in alternating lines!)

## Requirements
- Python 3.x 
- No external libraries required

## What did we learn from this?
- File handling: Reading questions from external .txt files
- Functions: Separating check_guess() and scores()
- Input validation: Handling invalid difficulty selections and non-integer inputs
- Exception handling: Using try/except for missing files
- Global variables: Tracking scores across functions
- Conditional logic: like different feedback depending on the player's performance.
