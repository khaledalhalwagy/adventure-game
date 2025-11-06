# adventure-game
I built a fully playable Python text adventure that combines creative storytelling with programmatic game mechanics. The game uses a list of diverse mythological and folkloric creatures picked at random each run, and composes encounter narration on the fly using template strings — producing varied and surprising outputs for the same encounter. Players make branching choices (e.g., knock on a door, explore a cave, stab or run), pick up a unique weapon (the “dagger of Ogoroth”), and see combat outcomes determined by a mixture of state variables and randomized logic. A scoring system tracks player progress and leads to an end-game puzzle when certain conditions are met.

On the engineering side I focused on modularity and player experience: functions isolate gameplay segments (choice handling, fight sequences, scoring, replay flow), deliberate pauses (time.sleep) create readable pacing, and input validation ensures robust user interaction. The development process was iterative — I rewrote the code multiple times to integrate new mechanics (randomized monster pool, narrative victory variants, alternative defeat/escape mechanics), refine branching logic, and improve the overall play loop.

Key features & highlights (bullet list you can paste into the Skills / Highlights area)

Procedural enemy generation from a curated list of mythological/encyclopedic creatures.

Dynamic narrative generation using string templates for varied victory/defeat messages.

Branching gameplay with choice-driven state changes (different houses/caves, fight/flight decisions).

Points-based progression and conditional end-game riddle that rewards reaching a score threshold.

Item mechanics (weapon upgrade: replace rusty dagger with magical dagger) that change combat outcomes.

Robust input handling and replayability loop (play again / exit).

User experience improvements with paced output (timed print delays).

Iterative development — rewrote and refactored the project twice to add creative features and harden logic.

Technologies & skills demonstrated

Language: Python (core language features, control flow, functions)

Libraries: random, time, sys, unicodedata (text handling and UX pacing)

Software practices: modular design, input validation, iterative refactoring, narrative design, procedural content generation, state management

What I learned / personal takeaways (good to include in “What I did / Learned”)

How to design engaging text-based mechanics with minimal UI by focusing on pacing, choice impact, and varied narrative output.

Practical experience with procedural content generation and how small template systems can create the illusion of depth.

The importance of modular functions to keep branching stories maintainable and easy to extend.

How to balance randomness and deterministic state (score, item possession) to create meaningful player decisions.

Iterative development: rewriting and refactoring are crucial to introduce new ideas without increasing technical debt.
