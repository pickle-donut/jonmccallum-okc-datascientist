# Set Global Variables
RANDOM_STATE=42

# Modules
from sklearn.linear_model import ElasticNet, HuberRegressor, Ridge

# Model Definitions
modelDefinitions=[
    
    # Start of Elastic Net Model Definition
    ('elastic_net', {
        'estimator': ElasticNet(random_state=RANDOM_STATE),
        'modelParams':{
             'max_iter': [100, 250, 500, 750, 1000, 5000, 10000],
             'alpha': [0.005, 0.01, 0.025, 0.05, 0.075, 0.1, 0.25, 0.5],
             'l1_ratio': [0.001, 0.005, 0.0075, 0.01, 0.025, 0.1, 0.2, 0.25, 0.30, 0.5, 0.75, 0.85, 0.9, 0.95]
        }
     }),
    
    # Start of Huber-Regressor Model Definition
    ('huber-regressor', {
        'estimator': HuberRegressor(),
        'modelParams':{
             'max_iter': [100, 250, 500, 750, 1000, 5000, 10000],
             'alpha': [0.005, 0.01, 0.025, 0.05, 0.075, 0.1, 0.25, 0.5],
        }

     }),
    
    # Start of Ridge Regressor Model Definition
    ('ridge-regressor', {
        'estimator': Ridge(),
        'modelParams':{
             'max_iter': [100, 250, 500, 750, 1000, 5000, 10000],
             'alpha': [0.005, 0.01, 0.025, 0.05, 0.075, 0.1, 0.25, 0.5],
             'alpha': ['auto', 'svd', 'cholesky', 'lsqr', 'sparse_cg', 'sag', 'saga', 'lbfgs'],
        }

     })
    
]


