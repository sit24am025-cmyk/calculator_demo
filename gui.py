import tkinter as tk
from tkinter import ttk, messagebox
from calculator import add, subtract, multiply, divide, get_history, clear_history


class CalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator Demo")
        self.geometry("420x420")
        self.resizable(False, False)

        self.a_var = tk.StringVar()
        self.b_var = tk.StringVar()
        self.op_var = tk.StringVar(value="add")
        self.result_var = tk.StringVar(value="Result will appear here.")

        self._build_ui()
        self._refresh_history()

    def _build_ui(self):
        ttk.Label(self, text="First number").pack(pady=(12, 2))
        ttk.Entry(self, textvariable=self.a_var).pack(fill="x", padx=16)

        ttk.Label(self, text="Operation").pack(pady=(12, 2))
        ttk.Combobox(
            self,
            textvariable=self.op_var,
            values=["add", "subtract", "multiply", "divide"],
            state="readonly",
        ).pack(fill="x", padx=16)

        ttk.Label(self, text="Second number").pack(pady=(12, 2))
        ttk.Entry(self, textvariable=self.b_var).pack(fill="x", padx=16)

        ttk.Button(self, text="Calculate", command=self.calculate).pack(pady=14)
        ttk.Button(self, text="Clear history", command=self.clear_history_ui).pack()

        ttk.Label(self, textvariable=self.result_var, font=("Arial", 12, "bold")).pack(pady=12)

        ttk.Label(self, text="History").pack(pady=(10, 2))
        self.history_box = tk.Listbox(self, height=10)
        self.history_box.pack(fill="both", expand=True, padx=16, pady=(0, 16))

    def calculate(self):
        try:
            a = float(self.a_var.get())
            b = float(self.b_var.get())
        except ValueError:
            messagebox.showerror("Input error", "Please enter valid numbers.")
            return

        ops = {
            "add": add,
            "subtract": subtract,
            "multiply": multiply,
            "divide": divide,
        }

        try:
            result = ops[self.op_var.get()](a, b)
            self.result_var.set(f"Result: {result}")
            self._refresh_history()
        except (TypeError, ValueError, KeyError) as exc:
            messagebox.showerror("Calculation error", str(exc))

    def clear_history_ui(self):
        clear_history()
        self._refresh_history()
        self.result_var.set("Result will appear here.")

    def _refresh_history(self):
        self.history_box.delete(0, tk.END)
        history = get_history()
        if not history:
            self.history_box.insert(tk.END, "No history yet.")
            return
        for item in history:
            self.history_box.insert(tk.END, item)


if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()
