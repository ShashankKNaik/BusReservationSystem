"""
Created on Thu Feb 11 18:45:40 2021

@author: shashank
"""
#first ML program
#Loan approval classification based on applicants status and previous data

from sklearn import tree
import numpy as np
import matplotlib.pyplot as plt

#status=["age{y=0/m=1/o=2}","has_job{0/1}","own_house{0/1}","credit_rating{f=0/g=1/e=2}"]

status=np.array([[0,0,0,0],[0,0,0,1],[0,1,0,1],[0,1,1,0],[0,0,0,0],
                 [1,0,0,0],[1,0,0,1],[1,1,1,1],[1,0,1,2],[1,0,1,2],
                 [2,0,1,2],[2,0,1,1],[2,1,0,1],[2,1,0,2],[2,0,0,0]])

#class{approved=1/not=0}

clas=np.array([0,0,1,1,0,0,0,1,1,1,1,1,1,1,0])

classifier=tree.DecisionTreeClassifier().fit(status,clas)

print (classifier.predict([[0,0,1,0]]))

fig = plt.figure(figsize=(50,40))
_ = tree.plot_tree(classifier)
