# Aufgabe Machine Learning
#             0. Installation von pandas und scikit-learn
#             1. Importiere die Daten als Dataframe in dein Python Skript
#             2. Teile die Daten in features und labels auf
#             3. Teile die Daten in Trainings- und Testdaten auf 80-20
#             4. Trainiere einen DecisionTreeClassifier mit den Trainingsdaten
#             5. Treffe eine Vorhersage für die Testdaten
#             6. Bestimme die Accuracy des trainierten Modells

import pandas,sklearn 
import sklearn.metrics
import sklearn.model_selection
import sklearn.tree


df = pandas.read_csv('gender_classification.csv')

# Daten auf features und labels aufteilen
X = df.drop(columns='gender') #column gender existiert nicht in features 
y = df['gender'] 

#teilen die Daten in trainings- und testdaten
X_train,X_test,y_train,y_test = sklearn.model_selection.train_test_split(X,y,test_size= 0.2,random_state=42)

# classifier erzeugen und mit daten trainieren
clf = sklearn.tree.DecisionTreeClassifier(random_state=42)
clf.fit(X_train,y_train)

# eine Vorhersage und ganauhigkeit berechnen
prediction = clf.predict(X_test)
accur = sklearn.metrics.accuracy_score(y_test,prediction)
print(f"Accuracy: {accur:.4f}")
