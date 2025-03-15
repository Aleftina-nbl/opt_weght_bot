from flask import Flask, request, jsonify

app = Flask(__name__)

def calculate_weight(gender, age, height, chest, child):
    children = int(child) if child else 0
    if gender.lower() == "чоловік":
        weight = (height - 100 + chest / 10 + (age / 10)) * (1 + 0.05 * child)
    else:
        weight = (height - 110 + chest / 10 + (age / 15)) * (1 + 0.04 * child)
    return round(weight, 2)

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.json
    weight = calculate_weight(
        data.get("gender"),
        int(data.get("age")),
        int(data.get("height")),
        int(data.get("chest")),
        int(data.get("child", 0))
    )
    return jsonify({"ideal_weight": weight})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
