import os

os.system("python3 preprocess_enron.py train enron.vocab /home/hadoop/EE542")
print
os.system("python3 nblearn.py TrainingFile ModelFile")
print
os.system("python3 preprocess_enron.py test enron.vocab /home/hadoop/EE542")
print
os.system("python3 nbclassify.py ModelFile TestFile")

