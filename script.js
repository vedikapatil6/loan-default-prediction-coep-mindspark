document.getElementById('loanForm').addEventListener('submit', async function (event) {
    event.preventDefault();

    const formData = new FormData(this);
    const formObj = Object.fromEntries(formData.entries());

    const response = await fetch('/predict', {
        method: 'POST',
        body: new URLSearchParams(formObj)
    });

    const result = await response.json();
    if (result.error) {
        document.getElementById('result').innerHTML = `<p style="color: red;">Error: ${result.error}</p>`;
    } else {
        document.getElementById('result').innerHTML = `
            <p>Random Forest Prediction: ${result.random_forest === 1 ? 'Defaulter' : 'Non-Defaulter'}</p>
            <p>XGBoost Prediction: ${result.xgboost === 1 ? 'Defaulter' : 'Non-Defaulter'}</p>
        `;
    }
});
