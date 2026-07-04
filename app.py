from flask import Flask, request, render_template_string
from calculator import add, subtract, multiply, divide, get_history, clear_history

app = Flask(__name__)

HTML = """
<!doctype html>
<title>Calculator Demo</title>
<h1>Calculator Demo</h1>

<form method="post" action="/calculate">
  <input name="a" value="{{ a }}" placeholder="First number">
  <select name="operation">
    <option value="add" {% if operation == "add" %}selected{% endif %}>Add</option>
    <option value="subtract" {% if operation == "subtract" %}selected{% endif %}>Subtract</option>
    <option value="multiply" {% if operation == "multiply" %}selected{% endif %}>Multiply</option>
    <option value="divide" {% if operation == "divide" %}selected{% endif %}>Divide</option>
  </select>
  <input name="b" value="{{ b }}" placeholder="Second number">
  <button type="submit">Calculate</button>
</form>

{% if error %}
<p style="color:red;">{{ error }}</p>
{% endif %}

{% if result is not none %}
<p><strong>Result:</strong> {{ result }}</p>
{% endif %}

<form method="post" action="/clear-history">
  <button type="submit">Clear history</button>
</form>

<h2>History</h2>
<ul>
  {% for item in history %}
    <li>{{ item }}</li>
  {% else %}
    <li>No history yet.</li>
  {% endfor %}
</ul>
"""

OPS = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
}


@app.route("/", methods=["GET"])
def home():
    return render_template_string(
        HTML,
        result=None,
        error=None,
        history=get_history(),
        a="",
        b="",
        operation="add",
    )


@app.route("/calculate", methods=["POST"])
def calculate():
    a_raw = request.form.get("a", "")
    b_raw = request.form.get("b", "")
    operation = request.form.get("operation", "add")

    try:
        a = float(a_raw)
        b = float(b_raw)
    except ValueError:
        return render_template_string(
            HTML,
            result=None,
            error="Please enter valid numbers.",
            history=get_history(),
            a=a_raw,
            b=b_raw,
            operation=operation,
        ), 400

    try:
        result = OPS[operation](a, b)
    except KeyError:
        return render_template_string(
            HTML,
            result=None,
            error="Unknown operation.",
            history=get_history(),
            a=a_raw,
            b=b_raw,
            operation=operation,
        ), 400
    except (TypeError, ValueError) as exc:
        return render_template_string(
            HTML,
            result=None,
            error=str(exc),
            history=get_history(),
            a=a_raw,
            b=b_raw,
            operation=operation,
        ), 400

    return render_template_string(
        HTML,
        result=result,
        error=None,
        history=get_history(),
        a=a_raw,
        b=b_raw,
        operation=operation,
    )


@app.route("/clear-history", methods=["POST"])
def clear_history_route():
    clear_history()
    return render_template_string(
        HTML,
        result=None,
        error=None,
        history=get_history(),
        a="",
        b="",
        operation="add",
    )


if __name__ == "__main__":
    app.run(debug=True)
