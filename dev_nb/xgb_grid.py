import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from xgboost import XGBClassifier
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import GridSearchCV
from sklearn.utils import shuffle

data_a05 = pd.read_csv('../../data_z02_001_0001_a05.csv')
data_a1 = pd.read_csv('../../data_z02_001_0001_a1.csv')
data_a5 = pd.read_csv('../../data_z02_001_0001_a5.csv')

data_tot = pd.concat([data_a05, data_a1, data_a5])


NI = shuffle(data_tot[data_tot['type']=='NI']).head(430242)
MT = shuffle(data_tot[data_tot['type']=='MT']).head(430242)
CE = shuffle(data_tot[data_tot['type']=='CE'])
balanced_data = pd.concat([NI, MT,CE])

shuffle_data = shuffle(balanced_data)

# Load the dataset
data = shuffle_data

# Separate the features and labels
X = data[['Mass_BH', 'Mass_1', 'logP']]
y = data['type']

selected_columns = ['Mass_BH', 'Mass_1', 'logP']
scaler = StandardScaler()
X[selected_columns] = scaler.fit_transform(X[selected_columns])

# Perform label encoding on the labels
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Grid search for learning_rate
learning_rate_grid = {
    'learning_rate': [1, 2, 5]
}

xgb_classifier = XGBClassifier(n_jobs=10)
learning_rate_search = GridSearchCV(xgb_classifier, learning_rate_grid, scoring='accuracy', cv=3)
learning_rate_search.fit(X_train, y_train)
best_learning_rate = learning_rate_search.best_params_['learning_rate']

print('best learning rate', best_learning_rate)
# Grid search for max_depth
max_depth_grid = {
    'max_depth': [7]
}

xgb_classifier = XGBClassifier(n_jobs=10, learning_rate=best_learning_rate)
max_depth_search = GridSearchCV(xgb_classifier, max_depth_grid, scoring='accuracy', cv=3)
max_depth_search.fit(X_train, y_train)
best_max_depth = max_depth_search.best_params_['max_depth']

print('best max depth', best_max_depth)

# Grid search for n_estimators
n_estimators_grid = {
    'n_estimators': [300]
}

xgb_classifier = XGBClassifier(n_jobs=10, learning_rate=best_learning_rate, max_depth=best_max_depth)
n_estimators_search = GridSearchCV(xgb_classifier, n_estimators_grid, scoring='accuracy', cv=3)
n_estimators_search.fit(X_train, y_train)
best_n_estimators = n_estimators_search.best_params_['n_estimators']

print('best n estimators', best_n_estimators)

# Train the classifier with the best hyperparameters
best_classifier = XGBClassifier(n_jobs=10, learning_rate=best_learning_rate, max_depth=best_max_depth, n_estimators=best_n_estimators)
best_classifier.fit(X_train, y_train)

# Predict on the validation set using the best classifier
y_pred = best_classifier.predict(X_test)

# Calculate and print the evaluation scores
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

print(best_classifier)


