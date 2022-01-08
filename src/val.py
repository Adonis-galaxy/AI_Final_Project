from sklearn.neural_network import MLPRegressor
import numpy as np
from sklearn import svm
from sklearn.svm import SVC
import sklearn
from sklearn.neighbors import KNeighborsClassifier
def validation(model,val_data,val_labels,num_val):
    if type(model) == MLPRegressor:
        true_val=0
        predict_val = model.predict(val_data.T).argmax(1)
        for i in range(num_val):
            if predict_val[i] == val_labels[i]:
                true_val += 1
        print("val acc:", true_val/num_val)
        return true_val/num_val
    elif type(model) == KNeighborsClassifier:
        true_val=0
        predict_val = model.predict(val_data.T)
        for i in range(num_val):
            if predict_val[i] == val_labels[i]:
                true_val += 1
        print("val acc:", true_val/num_val)
        return true_val/num_val
    elif type(model) == svm.LinearSVC: # svm 
        true_val=0
        predict_val = model.predict(val_data.T)
        for i in range(num_val):
            if predict_val[i] == val_labels[i]:
                true_val += 1
        print("val acc:", true_val/num_val)
        return true_val/num_val
    elif type(model) == svm.SVC: # svm 
        true_val=0
        predict_val = model.predict(val_data.T)
        for i in range(num_val):
            if predict_val[i] == val_labels[i]:
                true_val += 1
        print("val acc:", true_val/num_val)
        return true_val/num_val
    elif type(model) == sklearn.naive_bayes.BernoulliNB: # svm 
        true_val=0
        predict_val = model.predict(val_data.T)
        for i in range(num_val):
            if predict_val[i] == val_labels[i]:
                true_val += 1
        print("val acc:", true_val/num_val)
        return true_val/num_val
    elif type(model) == sklearn.naive_bayes.GaussianNB: # svm 
        true_val=0
        predict_val = model.predict(val_data.T)
        for i in range(num_val):
            if predict_val[i] == val_labels[i]:
                true_val += 1
        print("val acc:", true_val/num_val)
        return true_val/num_val
    elif type(model) == sklearn.naive_bayes.ComplementNB: # svm 
        true_val=0
        predict_val = model.predict(val_data.T)
        for i in range(num_val):
            if predict_val[i] == val_labels[i]:
                true_val += 1
        print("val acc:", true_val/num_val)
        return true_val/num_val
    else:
        print(type(model))
        raise RuntimeError("What model? Write your model val function here")
