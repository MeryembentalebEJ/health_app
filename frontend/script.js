const API_URL = "http://127.0.0.1:5000"; // Change si besoin

// Fonction pour calculer le BMI
function calculateBMI() {
    const height = document.getElementById("height").value;
    const weight = document.getElementById("weight").value;

    fetch(`${API_URL}/bmi`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ height: parseFloat(height), weight: parseFloat(weight) })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("bmi-result").innerText = `Votre BMI est : ${data.bmi}`;
    })
    .catch(error => {
        document.getElementById("bmi-result").innerText = "Erreur lors du calcul du BMI.";
        console.error("Erreur:", error);
    });
}

// Fonction pour calculer le BMR
function calculateBMR() {
    const height = document.getElementById("bmr-height").value;
    const weight = document.getElementById("bmr-weight").value;
    const age = document.getElementById("bmr-age").value;
    const gender = document.getElementById("bmr-gender").value;

    fetch(`${API_URL}/bmr`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ height: parseInt(height), weight: parseFloat(weight), age: parseInt(age), gender: gender })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("bmr-result").innerText = `Votre BMR est : ${data.bmr}`;
    })
    .catch(error => {
        document.getElementById("bmr-result").innerText = "Erreur lors du calcul du BMR.";
        console.error("Erreur:", error);
    });
}
