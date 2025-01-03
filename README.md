# Python Wordle Clone

A Python implementation of Wordle focusing on efficient data structures and clean object-oriented design. Uses sets for O(1) word validation, dictionaries for letter tracking, and colored terminal output.

## Running the Game
1. Ensure you have Python installed.
2. Place `answerlist.txt` and `valid-wordle-words.txt` in the same directory as `Game.py`.
3. Run `python Game.py`.

Game displays colored feedback in the terminal:
- **Blue**: Correct letter, correct position.
- **Yellow**: Correct letter, wrong position.

## Compatibility with Windows Command Prompt
If you are running the program in the Windows Command Prompt and encounter issues with colored output, follow these steps to enable ANSI escape code support:

1. Open `cmd` as an administrator.
2. Enable Virtual Terminal Processing by running the following command:
   ```cmd
   reg add HKCU\Console /f /v VirtualTerminalLevel /t REG_DWORD /d 1
   ```
3. Restart the Command Prompt and rerun the game.

Alternatively, you can use a terminal that natively supports ANSI escape codes, such as **Windows Terminal**, **PowerShell**, or **Git Bash**.

