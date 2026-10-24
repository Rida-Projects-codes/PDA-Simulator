# PDA Simulator

## Project Description
The PDA Simulator is a Python application developed using Tkinter. It recognizes balanced parentheses and palindrome strings using stack operations. It displays the input symbol, current state, stack contents, transition performed, and final acceptance or rejection status.

## Technologies Used
- Python 3
- Tkinter GUI
- Stack Data Structure

## Features
- Recognizes balanced parentheses.
- Recognizes palindrome strings.
- Displays step-by-step stack operations.
- Shows current state and transitions.
- Displays ACCEPTED or REJECTED status.
- Provides a simple graphical user interface.

## Project Structure

```text
PDA-Simulator/
├── pda_simulator.py
└── README.md
```

## Requirements
- Python 3 installed.
- Tkinter library available with Python.

No external packages are required.

## How to Run in VS Code

1. Open the project folder in VS Code.
2. Open the terminal using **Terminal → New Terminal**.
3. Run the following command:

```bash
python pda_simulator.py
```

4. Select the recognition type:
   - Balanced Parentheses
   - Palindrome
5. Enter the input string.
6. Click **Simulate PDA** to view the processing steps and result.

## Sample Test Cases

| Type | Input | Expected Output |
|---|---|---|
| Balanced Parentheses | `()` | ACCEPTED |
| Balanced Parentheses | `(()())` | ACCEPTED |
| Balanced Parentheses | `(()` | REJECTED |
| Palindrome | `madam` | ACCEPTED |
| Palindrome | `abba` | ACCEPTED |
| Palindrome | `hello` | REJECTED |

## Working Principle

### Balanced Parentheses
- Push each opening parenthesis onto the stack.
- Pop an opening parenthesis when a matching closing parenthesis is encountered.
- Accept the string if all parentheses match and only the bottom stack marker remains.

### Palindrome
- Guess the midpoint of the input string.
- Push the first half onto the stack.
- Compare the remaining half with the stack by popping matching symbols.
- Accept if all symbols match and only the bottom marker remains.

## Output
The application displays:
- Input symbol
- Current state
- Stack contents
- Transition performed
- Final acceptance or rejection status

## Conclusion
This project demonstrates the working of a Pushdown Automaton using stack operations. It provides a simple way to understand string recognition and automata theory through a graphical interface.
