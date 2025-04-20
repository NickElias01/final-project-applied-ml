![Row of Houses with For Sale Signs](images/ReadmeImage_ForSaleSign_ChatGPT_Image.png)

## Table of Contents
- [Housing Price Predictor](#housing-price-predictor)
  - [Author](#author)
      - [Link to Notebook file in GitHub](#link-to-notebook-file-in-github)
      - [Link to Peer Review in GitHub](#link-to-peer-review-in-github)
  - [Project Overview](#project-overview)
    - [Key Features of the Project](#key-features-of-the-project)
  - [Repository Structure](#repository-structure)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Clone the Repository](#clone-the-repository)
    - [Set Up the Virtual Environment](#set-up-the-virtual-environment)
  - [How to Use](#how-to-use)
  - [Results](#results)
  - [Conclusions](#conclusions)
  - [Technologies Used](#technologies-used)
  - [Future Work](#future-work)
  - [License](#license)

---

# Housing Price Predictor
## Author  
**Nick Elias, Elias Analytics**  
**Institution**: Northwest Missouri State University  
*CSIS 44688-80 Applied Machine Learning*  
#### [Link to Notebook file in GitHub](https://github.com/NickElias01/final-project-applied-ml/blob/main/regression_nickelias.ipynb)
#### [Link to Peer Review in GitHub](https://github.com/NickElias01/final-project-applied-ml/blob/main/peer_review.md)

---

## Project Overview  
This project focuses on predicting housing prices using machine learning techniques applied to a real estate dataset. The analysis involves data preprocessing, feature engineering, and model evaluation to build accurate regression models. The dataset, sourced from the [Kaggle Housing Prices Competition](https://www.kaggle.com/c/house-prices-advanced-regression-techniques), includes various features such as living area, house age, and overall quality, which are used to predict the target variable, `SalePrice`.

### Key Features of the Project  
- **Three Machine Learning Pipelines**:
  1. **Baseline Pipeline**: Standard scaling with linear regression.  
  2. **Pipeline with Imputation**: Adds missing value imputation for robustness.  
  3. **Advanced Polynomial Pipeline**: Incorporates polynomial features to capture non-linear relationships.  
- **Evaluation Metrics**: RMSE, R², cross-validation, and learning curves.  
- **Feature Engineering**: Creation of `HouseAge` and encoding of categorical variables.  
- **Outlier Handling**: Removal of extreme values to improve model performance.  

The **Advanced Polynomial Pipeline** achieved the best results, demonstrating the importance of scaling and feature engineering in improving predictive accuracy.

---

## Repository Structure  
```plaintext
final-project-applied-ml/
├── data/
|   ├── data_description.txt
|   ├── sample_submission.csv
|   ├── test.csv                        # Competition testing dataset for predicting SalePrice
|   ├── train.csv                       # Dataset used in analysis for training and testing
├── .gitignore
├── feature_combinations_results.csv    # Results of initial pipeline variable combinations
├── regression_nickelias.ipynb          # Full Analysis
├── preprocessing_pipeline.py           # Helper functions for preprocessing pipeline
├── README.md
├── requirements.txt
└── peer_review.md                      # Review of classmate project
```

## Getting Started  

### Prerequisites  
Before running this project, ensure you have the following installed:  
- **Python 3.8 or higher**  
- **Git**  
- **Jupyter Notebook**  

### Clone the Repository  
To get a copy of the project on your local machine, follow these steps:  
1. Open your terminal or command prompt.  
2. Run the following commands:  
   ```bash
   git clone https://github.com/NickElias01/final-project-applied-ml.git
   cd final-project-applied-ml
    ```

### Set Up the Virtual Environment  
To ensure a clean and isolated environment for running the project, follow these steps:

1. **Create a virtual environment**:  
   Run the following command to create a virtual environment named `venv`:  
   ```bash
   python -m venv venv
    ```

2. **Activate the virtual environment**:
    - On Windows:
    ```powershell
    .venv\Scripts\activate
    ```

    -On macOS/Linux:
    ```bash
    source venv/bin/activate
    ```

3. **Install the required dependencies**:
    - Use the requirements.txt file to install all necessary Python packages:
    ```python
    pip install -r requirements.txt
    ```

4. **Verify the installation**:
    - Ensure all dependencies are installed correctly by running:
    ```python
    pip list
    ```

5. **Open the Jupyter Notebook regression_nickelias.ipynb**
    - Follow the structured analysis in the notebook to explore the project.


## How to Use

1. Data Preprocessing: The notebook includes steps for handling missing values, encoding categorical variables, and scaling numerical features.
2. Model Training: Train and evaluate three pipelines to predict housing prices.
3. Customization: Modify the preprocessing pipeline or experiment with additional features/models.


## Results
* Baseline Pipeline: **RMSE = 33,146.29, R² = 0.78**
* Pipeline with Imputation: Similar performance to the baseline.
* Advanced Polynomial Pipeline: **RMSE = 31,613.86, R² = 0.80**

The advanced pipeline outperformed others by capturing non-linear relationships through polynomial features.

## Conclusions
This Regression analysis attempted to predict housing prices from the train.csv dataset by utilizing three specific attributes: GrLivArea ( Above ground living area sqft), HouseAge (current year 2025 - yearbuilt), and OverallQual (Rating of the overall material and finish of the house).

These attributes were chosen because they seemed to have strong potential for correlation with SalePrice, had no Null values in the dataset, and did not overlap significantly based on a correlation matrix.

I tried applying the linear regression model with various combinations of the three attributes using a for loop method to iterate through all possible combinations (GrLivArea only, GrLivArea + HouseAge, all 3, etc.). I found that the combination with the highest R^2 score used all 3 attributes as the input features to predict the target variable SalePrice. This method yielded R^2 = 0.78 and RMSE = 33146, which means my model explained about 78% of the variablity in SalePrice based on the test data.

Then I updated the pipeline to impute missing values with the mean for numerical features and the most common value for categorical features (although this yielded no changes since my train and test samples had 0 missing values).

Finally, I added polynomial features with degree 3, which helped capture some of the non-linear relationships within the data. This strengthened the model to R^2 = 0.80 and RMSE = 31614. This can be considered a very good predicting model in the context of housing market analysis.


## Technologies Used

* Python 3.x
* Jupyter Notebook
* scikit-learn
* pandas
* matplotlib
* seaborn


## Future Work
- Experiment with classification models (e.g., Decision Trees, Random Forests) for categorical features.
- Explore neural networks to incorporate all 81 features for enhanced predictions.
- Fine-tune hyperparameters and test additional advanced models like Gradient Boosting.


## License

This project is licensed under the MIT License. See the LICENSE file for details.