# calculator_demo

A simple calculator project with:
- addition
- subtraction
- multiplication
- division
- divide-by-zero protection
- operation history
- Flask web app
- Tkinter GUI app

## Install

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e .[dev]
```

## Run the web app

```bash
flask --app app run
```

## Run the GUI app

```bash
python gui.py
```

## Run tests

```bash
pytest
```

## Behavior

- `add(a, b)` returns the sum
- `subtract(a, b)` returns the difference
- `multiply(a, b)` returns the product
- `divide(a, b)` returns the quotient
- `divide(a, b)` raises `ValueError("Cannot divide by zero")` when `b == 0`
- invalid inputs raise `TypeError`
