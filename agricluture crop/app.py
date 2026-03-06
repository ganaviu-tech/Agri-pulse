import os
from flask import Flask, render_template, request
import processor
from agripulse_logic import calculate_agripulse_score

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():

    results = None

    if request.method == "POST":

        crop = request.form.get("crop")
        file = request.files.get("file")

        if file and crop:
            results = processor.process_csv(file, crop)
            return render_template("results.html", results=results)

    return render_template("index.html")


@app.route('/analyze_manual', methods=['POST'])
def analyze_manual():

    crop = request.form.get('crop')

    try:

        n = float(request.form.get('N'))
        p = float(request.form.get('P'))
        k = float(request.form.get('K'))
        ph = float(request.form.get('pH'))

        score, health, deficiencies, fertilizer = calculate_agripulse_score(crop, n, p, k, ph)

        results = [{
            "soil_id": "MANUAL_ENTRY",
            "target_crop": crop,
            "health_metrics": {
                "overall_health": health,
                "critical_deficiencies": deficiencies
            },
            "recommendation": {
                "suitability_score": score,
                "fertilizer_plan": fertilizer
            },
            "ai_explanation": f"Soil analysis completed. The soil health for {crop} is {health}. Apply recommended fertilizers to improve yield."
        }]

        return render_template("results.html", results=results)

    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)