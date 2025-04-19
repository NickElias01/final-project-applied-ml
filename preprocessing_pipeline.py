import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder

# Define the mapping for MSSubClass
mssubclass_mapping = {
    20: "1-STORY 1946 & NEWER",
    30: "1-STORY 1945 & OLDER",
    40: "1-STORY W/FINISHED ATTIC",
    45: "1-1/2 STORY - UNFINISHED",
    50: "1-1/2 STORY FINISHED",
    60: "2-STORY 1946 & NEWER",
    70: "2-STORY 1945 & OLDER",
    75: "2-1/2 STORY ALL AGES",
    80: "SPLIT OR MULTI-LEVEL",
    85: "SPLIT FOYER",
    90: "DUPLEX - ALL STYLES",
    120: "1-STORY PUD 1946 & NEWER",
    150: "1-1/2 STORY PUD",
    160: "2-STORY PUD 1946 & NEWER",
    180: "PUD - MULTILEVEL",
    190: "2 FAMILY CONVERSION"
}

# Custom preprocessing function
def preprocess_data(data):
    # Map MSSubClass to create MSSubClassMapped
    data['MSSubClassMapped'] = data['MSSubClass'].map(mssubclass_mapping)
    
    # Create HouseAge
    data['HouseAge'] = 2025 - data['YearBuilt']
    
    return data

# Define numerical and categorical features
numerical_features = ['GrLivArea', 'HouseAge']
categorical_features_onehot = ['Neighborhood']
categorical_features_ordinal = ['OverallQual', 'MSSubClassMapped']

# Define transformers
numerical_transformer = StandardScaler()
categorical_transformer_onehot = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
categorical_transformer_ordinal = OrdinalEncoder()

# Combine transformations using ColumnTransformer
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_features),  # Scale numerical features
        ('onehot', categorical_transformer_onehot, categorical_features_onehot),  # OneHotEncode Neighborhood
        ('ordinal', categorical_transformer_ordinal, categorical_features_ordinal)  # OrdinalEncode OverallQual and MSSubClassMapped
    ]
)

# Create the pipeline
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor)  # Preprocessing step
])