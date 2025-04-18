# Random Forest
An algorithm used for both **classification** and **regression** tasks. It consists of multiple decision trees. This is why it called 'Forest'. Compare to decision tree, Random Forest has more accurate and stable since it ensemble of trees outputs and give the best choice.
## Instance
Suppose there is a dataset that composes of 1000 houses data, which contains various features such as quare footage, location and age of the house.
To create a Random Forest, you need to generate multiple bootstrap samples from the original dataset, Let's say you decide to create 100 decision trees in your Random Forest.
    
    'D1​={(x1​,y1​),(x2​,y2​),(x3​,y3​),…,(x1000​,y1000​)}'

x<sub>i</sub> represents the features of the i-th house, and y<sub>i</sub> represents the house price.

For Regression:

    'y^​=1001​i=1∑100​Ti​(x)'

For Classification:

    'y^​=mode(T1​(x),T2​(x),…,T100​(x))'

## Code
'''python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

data = load_iris()
X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

print(Classification Report:")
print(classification_report(y_test, y_pred))

importances = clf.feature_importances_
feature_names = data.feature_names

print("Feature Importances:")
for feature, importance in zip(feature_names, importances):
    print(f"{feature}: {importance:.4f}")
