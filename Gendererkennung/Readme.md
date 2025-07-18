Gender Classification with Decision Tree
Dieses Projekt demonstriert die Anwendung eines Entscheidungsbaum-Klassifikators (DecisionTreeClassifier) aus der scikit-learn-Bibliothek, um das Geschlecht einer Person basierend auf gegebenen Merkmalen vorherzusagen. Die Daten stammen aus einer CSV-Datei mit verschiedenen Attributen.

Voraussetzungen
Stelle sicher, dass du Python und die folgenden Bibliotheken installiert hast:

bash
Kopieren
Bearbeiten
pip install pandas scikit-learn
Daten
Die CSV-Datei gender_classification.csv sollte sich im folgenden Verzeichnis befinden:

Erwartete Struktur der CSV-Datei:
Die Datei sollte eine Spalte gender enthalten, die das Zielmerkmal (Label) darstellt, sowie weitere Spalten mit Merkmalen (Features), z. B.:

height,weight,shoe_size,gender
170,65,40,male
160,55,38,female
...
Codebeschreibung
Daten laden
Die CSV-Datei wird mit pandas.read_csv() eingelesen.

Features und Labels trennen
Die Spalte gender wird als Label verwendet. Alle anderen Spalten gelten als Eingabemerkmale.

Train-Test-Split
Die Daten werden im Verhältnis 80:20 in Trainings- und Testdaten aufgeteilt.

Modellerstellung und Training
Ein Entscheidungsbaum-Klassifikator wird erstellt und mit den Trainingsdaten trainiert.

Vorhersage und Genauigkeit
Das Modell trifft Vorhersagen auf den Testdaten, und die Genauigkeit wird mit accuracy_score berechnet.

Ausgabe
Nach dem Ausführen des Skripts wird die Klassifikationsgenauigkeit ausgegeben:
Accuracy: 0.8750
(Dieser Wert hängt von den Daten und der Modellkonfiguration ab.)

Modell
Modelltyp: DecisionTreeClassifier

Bibliothek: scikit-learn

Parameter: random_state=42

Hinweis
Achte darauf, dass die CSV-Datei korrekt formatiert ist und die Spalte gender vorhanden ist. Falls die Datei einen anderen Namen oder Pfad hat, passe die read_csv()-Zeile entsprechend an.

Lizenz
Dieses Projekt ist zu Lern- und Demonstrationszwecken gedacht. Keine kommerzielle Nutzung ohne Rücksprache.

