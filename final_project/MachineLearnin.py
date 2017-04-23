# General libraries.
import re
import numpy as np
#import matplotlib.pyplot as plt
import pandas as pd

# SK-learn libraries for learning.
from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.grid_search import GridSearchCV

# SK-learn libraries for evaluation.
from sklearn.metrics import confusion_matrix
from sklearn import metrics
from sklearn.metrics import classification_report
 
# SK-learn libraries for feature extraction from text.
from sklearn.feature_extraction.text import *

#to ignore warnings
import warnings
warnings.filterwarnings('ignore')

#for postgres connections
import psycopg2 
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT



print("Importing data from postgres database....")
# Connect to the database
conn = psycopg2.connect(database="projectdatabase", user="postgres", password="pass", host="localhost", port="5432")
conn.set_client_encoding('utf-8')
#initializing  cursor
cur = conn.cursor()

#cur.execute('SHOW client_encoding;')
#records = cur.fetchall()
#print("Client encoding is:", records)



#sql = 'SELECT Consumer_complaint_narrative,  timely_response from ccdata'
try:
	cur.execute('select consumer_complaint_narrative, timely_response from ccdata')
	records = cur.fetchall()
except UnicodeError:
	print ("Unicode error")



print("Data loaded in records object... ")
#print(records[1:5])
#print(len(records))

column_names = ['consumer_complaint_narrative','timely_response']


df = pd.DataFrame.from_records(records, columns=column_names)
print("Data successfully imported to pandas dataframe!")
print("Imported Dataframe shape is:",df.shape)


All_Complaints = df.shape[0]
print("Number of total complaints:", All_Complaints)

df['consumer_complaint_narrative'].replace('', np.nan, inplace=True)
print("Getting rid of complaints with no narrative from the imported data...")
df.dropna(subset=['consumer_complaint_narrative'], inplace=True)
print("Number of complaints with narrative:", df.shape[0])
print("% with Narrative:", round(df.shape[0]/All_Complaints , 2)*100 , "%")


print("Splitting imported data into training and development data...")

train_data = df['consumer_complaint_narrative'][:130000]
train_labels = df['timely_response'][:130000]
#print(train_data.shape, train_labels.shape)

dev_data = df['consumer_complaint_narrative'][130001:]
dev_labels =df['timely_response'][130001:]
print("Dev_Data shape:",dev_data.shape, "Dev label shape:", dev_labels.shape)


def P2():
     
    #using min_df argument to prune ffeatures
    print("Creating a dictionary of consumer narrative words by applying CountVectorizer method on training data...")
    cv = CountVectorizer(input= u'content',   analyzer='word',   min_df=10    ) 
    
    print("Creating vocabulary using training data...")
    td_matrix = cv.fit_transform(train_data)
    print("The size of the vocabulary excluding words that appear in fewer than 10 documents is: ", td_matrix.shape[1])
    #print(cv.get_feature_names())
    print("\n")
     
    print("Creating a sparse matrix for dev data using the vocabulary created by training data...")
    dd_matrix = cv.transform(dev_data)
    #feature_names_d = cv.get_feature_names()
    print("The size of the vocabulary for dev data is: ", dd_matrix.shape[1])
    
    
    print("Using logistic regression to predict if complaint will be resolved on time...")
    clf = LogisticRegression(penalty = 'l1', C = 1.00,tol=.01  )
    #clf.fit(td_matrix , train_labels)  
    #print("Score for training data with penalty = L1 for logistic regression is", clf.score(td_matrix , train_labels)   )
    print("Training the logistic regression model using training data...")
    clf.fit(td_matrix , train_labels)  
    print("Predicting the outcome for dev data....") 
    print("Score(accuracy) for dev data with penalty = L1 for logistic regression is", 
          np.round(clf.score(dd_matrix , dev_labels) * 100, 2), "%"   )

    predicted_dev_labels = clf.predict(dd_matrix)

    return predicted_dev_labels


#print("ANSWER:")    
predicted_dev_labels = P2()
#print("Predicted dev labels shape: ",predicted_dev_labels.shape)

#print("Printing some incorrectly predicted complaints for review:")

#counter = 0
#i = 130005 

#while i in range(130001,dev_labels.shape[0]) and counter < 6:
 #   if dev_labels[i] != predicted_dev_labels[i]:
  #      print()
   #     print("Actual resoultion:", dev_labels[i])
    #    print("Predict resoultion:", predicted_dev_labels[i])
     #   print("Complaint Narrative:", dev_data[i])
      #  counter += 1
   # i += 1

