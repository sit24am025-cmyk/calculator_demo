from dataclasses import dataclass, field
from numbers import Real


def _ensure_real(value, name):
    if isinstance(value, bool) or not isinstance(value, Real):
        raise TypeError(f"{name} must be a real number")
    return value


@dataclass
class Calculator:
    history: list[str] = field(default_factory=list)

    def _record(self, operation, a, b, result):
        self.history.append(f"{operation}({a}, {b}) = {result}")
        return result

    def add(self, a, b):
        a = _ensure_real(a, "a")
        b = _ensure_real(b, "b")
        return self._record("add", a, b, a + b)

    def subtract(self, a, b):
        a = _ensure_real(a, "a")
        b = _ensure_real(b, "b")
        return self._record("subtract", a, b, a - b)

    def multiply(self, a, b):
        a = _ensure_real(a, "a")
        b = _ensure_real(b, "b")
        return self._record("multiply", a, b, a * b)

    def divide(self, a, b):
        a = _ensure_real(a, "a")
        b = _ensure_real(b, "b")
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return self._record("divide", a, b, a / b)

    def get_history(self):
        return list(self.history)

    def clear_history(self):
        self.history.clear()


calculator = Calculator()


def add(a, b):
    return calculator.add(a, b)


def subtract(a, b):
    return calculator.subtract(a, b)


def multiply(a, b):
    return calculator.multiply(a, b)


def divide(a, b):
    return calculator.divide(a, b)


def get_history():
    return calculator.get_history()


def clear_history():
    return calculator.clear_history()
