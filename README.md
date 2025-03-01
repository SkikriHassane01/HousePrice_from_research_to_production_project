# House Price Prediction: From Research to Production

## Project Overview

This project demonstrates a complete machine learning workflow for predicting house prices, from initial research and exploration to a production-ready deployment package. Using the [Kaggle House Prices dataset](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data), the model predicts sale prices based on various housing attributes.

## Key Features

- **End-to-end ML pipeline** from research to production
- **Feature selection** from 81 original features to optimal predictive subset
- **Production-ready package** with proper versioning and installation
- **Comprehensive testing suite** to ensure model reliability
- **Detailed documentation** of both research and production phases

## Project Structure

```
├── Research_Environment/     # Exploratory work and analysis
│   ├── Notebooks/            # Sequential analysis and modeling
│   ├── Data/                 # Training and testing datasets
│   ├── Model/                # Saved model files
│   └── processing/           # Feature processing scripts
│
├── Production_Environment/   # Deployable package
│   ├── regression_model/     # Core model package
│   │   ├── config/           # Model configuration 
│   │   ├── datasets/         # Dataset versioning
│   │   └── pipeline.py       # Production pipeline
│   ├── tests/                # Test suite
│   └── requirements/         # Environment dependencies
│
└── Diagram/                  # Project architecture diagrams
```

## Installation & Usage

### For Development

```bash
# Clone the repository
git clone https://github.com/SkikriHassane01/HousePrice_from_research_to_production_project.git
cd HousePrice_from_research_to_production_project

# Research environment setup
cd Research_Environment
pip install -r research_requirements.txt

# Production environment setup
cd ../Production_Environment
pip install -e .
```

### For Production Use

```bash
pip install HousePrice-regression-model
```

### Making Predictions

```python
from regression_model.predict import make_prediction

# Load data as DataFrame
input_data = pd.DataFrame(...)

# Generate predictions
results = make_prediction(input_data=input_data)
predictions = results["predictions"]
```

## Model Features

The model uses 40 carefully selected features including:
- Property characteristics (MSSubClass, MSZoning, LotArea)
- Location attributes
- Building information (GrLivArea, TotRmsAbvGrd)
- Quality indicators (KitchenQual)
- Amenities (Fireplaces, GarageCars, WoodDeckSF)

## Project Development Steps

1. **Research Phase**
   - Data exploration and cleaning
   - Feature engineering to create new predictors
   - Feature selection to identify most important variables
   - Model experimentation and hyperparameter tuning
   - Pipeline development for reproducibility

2. **Production Phase**
   - Package structure design following best practices
   - Configuration management for model parameters
   - Version control for both code and datasets
   - Testing suite implementation
   - Deployment preparation and documentation

## Requirements

- Python 3.6+
- Core packages: scikit-learn, pandas, numpy
- See requirements files for complete dependencies

## License

This project is licensed under Apache License - see the LICENSE file for details.

## Author

Hassane Skikri - [Email](mailto:hassaneskikri@gmail.com) - [GitHub](https://github.com/SkikriHassane01)

---

# How to Create This Project: Step-by-Step Guide

## 1. Project Setup and Planning

1. **Define project scope and objectives**
   - Identify problem: house price prediction
   - Determine success metrics: RMSE, R²

2. **Set up project structure**
   - Create separate environments for research and production
   - Initialize git repository
   - Create initial README and documentation

## 2. Research Phase

1. **Data exploration (01. Data Analysis.ipynb)**
   - Load and examine the dataset
   - Analyze features and target variable
   - Identify missing values and outliers
   - Visualize relationships and distributions

2. **Feature engineering (02. FeatureSelection.ipynb)**
   - Create derived features
   - Handle categorical variables
   - Address missing values
   - Apply transformations

3. **Feature selection (03. model Training.ipynb)**
   - Identify most predictive features
   - Remove redundant variables
   - Apply dimensionality reduction if needed
   - Save selected feature list

4. **Model training and evaluation**
   - Split data into training and validation sets
   - Train multiple model types
   - Tune hyperparameters
   - Evaluate performance

5. **Pipeline development (05. finalPipeline.ipynb)**
   - Create reproducible preprocessing pipeline
   - Integrate model into pipeline
   - Test pipeline on validation data
   - Document pipeline steps

## 3. Production Phase

1. **Package structure setup**
   - Create `regression_model` package
   - Set up `setup.py` and `pyproject.toml`
   - Define package metadata and dependencies

2. **Model serialization and configuration**
   - Create config management system
   - Define model parameters in YAML files
   - Implement dataset versioning
   - Create prediction API

3. **Testing infrastructure**
   - Write unit tests for components
   - Create integration tests for pipeline
   - Test packaging and installation
   - Implement differential testing

4. **Documentation and deployment**
   - Complete API documentation
   - Update README with installation and usage instructions
   - Create example notebooks
   - Prepare for distribution

5. **Continuous integration**
   - Set up CI pipeline
   - Automate testing and linting
   - Configure deployment workflows

This comprehensive approach ensures a reliable and maintainable machine learning solution that transitions smoothly from research to production.