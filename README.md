✅ 1. Automated ML Pipeline (main.py)
Data ingestion from MySQL
Data validation
Data transformation (scaling + encoding)
Model training (Linear Regression + Random Forest)
Model evaluation (RMSE, MAE, R²)
Model registry / deployment
Artifact versioning
✅ 2. Streamlit App (app.py)
Dropdown-based input form
Batch prediction (CSV upload)
Downloadable output
✅ 3. Model Versioning
Saved inside:

prediction/models/current_model.joblib
prediction/models/best_model_<timestamp>.joblib
✅ 4. Batch Testing
Using:

python check_model.py
📁 Project Structure
📦 root
│
├── app.py
├── main.py
├── check_model.py
├── requirements.txt
├── README.md
├── .gitignore
├── Dockerfile
├── .env (ignored)
│
├── laptop_price/
│   ├── components/
│   ├── pipeline/
│   ├── utils/
│   ├── entity/
│   ├── exception.py
│   ├── logger.py
│   └── config.py
│
├── artifacts/
│   ├── raw/
│   ├── transformed/
│   └── model/
│
└── prediction/
    └── models/