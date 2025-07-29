# Iris Flask ML App
This is a Flask web application that predicts the Iris flower species using a Machine Learning model trained on the Iris dataset.

## Features
- Input Sepal & Petal dimensions
- Predict Iris species (Setosa, Versicolor, Virginica)
- Built with Python, Flask, and scikit-learn

## How to Run
1. Create a virtual environment
   \`\`\`bash
   python -m venv venv
   source venv/Scripts/activate  # On Windows
   \`\`\`

2. Install dependencies
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

3. Train the model
   \`\`\`bash
   python train_model.py
   \`\`\`

4. Run the Flask app
   \`\`\`bash
   python app.py
   \`\`\`

5. Open in browser
   \`\`\`
   http://127.0.0.1:5000
   \`\`\`

## Project Structure
\`\`\`
iris_flask_app/
├── app.py
├── train_model.py
├── Iris.csv
├── templates/
│   └── index.html
├── requirements.txt
└── README.md
\`\`\`

## Deployment
Can be deployed on Render or Heroku." > README.md
https://iris-flower-prediction-fs8f.onrender.com
