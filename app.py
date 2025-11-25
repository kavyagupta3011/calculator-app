from flask import Flask, jsonify, request

app = Flask(__name__)

# --- Calculator Core Logic ---
def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# --- Flask Routes ---
@app.get("/")
def home():
    return jsonify({"message": "Calculator API is running!"})

@app.get("/calc")
def calculate():
    try:
        a = float(request.args.get("a"))
        b = float(request.args.get("b"))
        op = request.args.get("op")

        if op == "add": result = add(a, b)
        elif op == "sub": result = sub(a, b)
        elif op == "mul": result = mul(a, b)
        elif op == "div": result = div(a, b)
        else:
            return jsonify({"error": "Invalid operation"}), 400

        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
