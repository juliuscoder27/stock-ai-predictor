# Stock‑AI‑Predictor
Didn't really know anything about coding before
getting into it atm - have a math/physics background
o3 came out tdy and I thought this would be a nice way to learn a bit about coding and test its capabilities - almost everything in this project will be ai generated - if you want to recreate it I suggest going the same rout as I did and build it with o3 and o4-mini-high

With the following prompt you should be on your way of learning all this in no time (I literally started coding yesterday, had to set up vs code, github, anaconda, etc., all of which is hella annoying on apple silikon but with the new models its crazy easy) 

Please read through and understand the prompt before just copy pasting it so that you can adjust it based on what you need (I told it to use a lot of MATLAB analogies because thats what I know, with models as powerful as o3 the only limit is your imagination, be specific in your prompts!)

Alright so heres the prompt:

"
I want to build an AI model in Python that predicts stock prices. Please provide a comprehensive, step-by-step guide that clearly explains all the necessary steps, decisions, and components involved in this project.

Please make this guide as high level as possible while retaining appliability. Focus on ensuring my understanding of the concepts and reasons behind decisions. I will work through this guide with o4-mini-high. Because of this please deeply explain the pros and cons of each descision in the path and the reasons behind them and let me decide what path I take. 
Please include prompts with the goal of generating a detailed step-by-step guide for the implementation side of each possible step in your highlevel guide. This way your guide can focus on only understanding and big ideas/concepts, you deligate the choices to me, and the implementation to o4-mini-high and me.

Here is my current knowledge and background:

Python: I have Python 3.13 installed but have no prior coding experience with Python specifically. I have, however, previously completed a large project using MATLAB, so I am familiar with concepts like arrays and matrices.

Machine Learning: I understand the basic concepts of machine learning and have a foundational understanding of common neural network architectures such as CNNs and RNNs.

Stocks & Technical Analysis: My understanding of stock market concepts and technical analysis is very basic.

Please ensure your guide ensures understanding and evaluation of (while facilitating implementation with a smaller model):

Environment Setup: Clear instructions on setting up a suitable environment, including any IDE recommendations, and necessary libraries/packages.

Data Collection & Preprocessing: How and from where to collect stock price data, and how to preprocess this data for input into a neural network (handling missing values, scaling, normalization).

Feature Engineering: Explanation of potential useful features and how to implement them.

Model Selection & Architecture: Suggestions on selecting and designing appropriate neural network architectures specifically tailored to stock price prediction, with explanations of choices (e.g., LSTM vs. GRU vs. Transformer-based architectures).

Training & Validation: How to train the model effectively, including setting up a validation strategy (cross-validation, train-test splits, metrics to measure accuracy).

Testing & Deployment: How to test the model's predictive performance rigorously, including evaluation metrics suitable for stock price prediction, and basic deployment strategies for practical usage.

Given my background, please keep explanations clear but thorough, bridging concepts from MATLAB to Python wherever possible.
"
Its probably best for you to leave the first paragraphs unchanged - feel free to drastically adjust the current knowledge and background part. 

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
