
import tkinter as tk
from tkinter import ttk, messagebox


def balanced_parentheses(string):
    stack = ["Z0"]
    steps = [("Start", "q0", "Z0", "Initialize stack")]
    valid = True

    for ch in string:
        if ch == "(":
            stack.append("(")
            steps.append((ch, "q0", " ".join(stack),
                          "Push ( onto stack"))

        elif ch == ")":
            if stack[-1] == "(":
                stack.pop()
                steps.append((ch, "q0", " ".join(stack),
                              "Pop ( from stack"))
            else:
                steps.append((ch, "qReject", " ".join(stack),
                              "No matching opening parenthesis"))
                valid = False
                break
        else:
            steps.append((ch, "qReject", " ".join(stack),
                          "Invalid input symbol"))
            valid = False
            break

    if valid and stack == ["Z0"]:
        steps.append(("End", "qAccept", "Z0",
                      "All parentheses matched"))
        return True, steps

    if valid:
        steps.append(("End", "qReject", " ".join(stack),
                      "Unmatched opening parenthesis"))

    return False, steps


def palindrome(string):
    steps = []
    n = len(string)

    # Try possible midpoints of the string.
    for odd in (False, True):
        for mid in range(n + 1):
            if odd and mid == n:
                continue

            left = mid
            right = n - mid - int(odd)

            if left != right or right < 0:
                continue

            stack = ["Z0"]
            trace = [("Start", "qPush", "Z0",
                      "Initialize stack")]

            for ch in string[:mid]:
                stack.append(ch)
                trace.append((ch, "qPush", " ".join(stack),
                              "Push " + ch))

            trace.append(("ε", "qMatch", " ".join(stack),
                          "Guess midpoint"))

            if odd:
                trace.append((string[mid], "qMatch",
                              " ".join(stack),
                              "Skip middle symbol"))

            valid = True

            for ch in string[mid + int(odd):]:
                if len(stack) > 1 and stack[-1] == ch:
                    stack.pop()
                    trace.append((ch, "qMatch", " ".join(stack),
                                  "Match and pop " + ch))
                else:
                    trace.append((ch, "qReject", " ".join(stack),
                                  "Symbol mismatch"))
                    valid = False
                    break

            if valid and stack == ["Z0"]:
                trace.append(("End", "qAccept", "Z0",
                              "All symbols matched"))
                return True, trace

            steps = trace

    if not steps:
        steps = [("Start", "qReject", "Z0",
                  "No valid midpoint found")]

    return False, steps


def simulate():
    string = input_entry.get()
    mode = choice.get()

    if mode == "Balanced Parentheses":
        accepted, steps = balanced_parentheses(string)
    else:
        accepted, steps = palindrome(string)

    for item in table.get_children():
        table.delete(item)

    for symbol, state, stack, transition in steps:
        table.insert("", "end",
                     values=(symbol, state, stack, transition))

    if accepted:
        result.config(text="ACCEPTED", foreground="green")
    else:
        result.config(text="REJECTED", foreground="red")


def load_example():
    choice.set("Balanced Parentheses")
    input_entry.delete(0, "end")
    input_entry.insert(0, "()()")
    simulate()


# Main window
root = tk.Tk()
root.title("PDA Simulator")
root.geometry("950x600")

tk.Label(root, text="PDA Simulator",
         font=("Arial", 20, "bold")).pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Select Language:").grid(row=0, column=0,
                                              padx=5, pady=5)

choice = ttk.Combobox(
    frame,
    values=["Balanced Parentheses", "Palindrome"],
    state="readonly",
    width=25
)
choice.grid(row=0, column=1, padx=5)
choice.set("Balanced Parentheses")

tk.Label(frame, text="Input String:").grid(row=1, column=0,
                                            padx=5, pady=5)

input_entry = tk.Entry(frame, width=30)
input_entry.grid(row=1, column=1, padx=5)
input_entry.insert(0, "()()")

tk.Button(frame, text="Simulate PDA",
          command=simulate).grid(row=2, column=1, pady=8)

tk.Button(frame, text="Load Example",
          command=load_example).grid(row=2, column=0, pady=8)

result = tk.Label(root, text="Result appears here",
                  font=("Arial", 15, "bold"))
result.pack(pady=5)

columns = ("Symbol", "State", "Stack", "Transition")

table = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    table.heading(col, text=col)
    table.column(col, width=210, anchor="center")

table.pack(fill="both", expand=True, padx=10, pady=10)

scroll = ttk.Scrollbar(root, orient="vertical",
                       command=table.yview)
table.configure(yscrollcommand=scroll.set)
scroll.place(relx=0.99, rely=0.48, relheight=0.43, anchor="ne")

root.mainloop()
