# Stock‑AI‑Predictor

End‑to‑end AI pipeline for stock price forecasting:

- `data/`    – raw & cached market data  
- `notebooks/` – EDA and model exploration  
- `src/`     – code modules  
- `experiments/` – trained models, logs  

## Setup

1. `conda env create -f environment.yml`  
2. `conda activate stockai`  
3. `code .` to open in VS Code

## Usage

- Run `python src/train.py` to train.  
- Inspect results under `experiments/`.
