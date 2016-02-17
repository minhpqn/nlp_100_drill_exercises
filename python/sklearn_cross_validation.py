"""
DESCRIPTION

    Build a classification model for sentiment analysis task with 
    logistic regression model on the data with simple
    bag-of-words features

    Perform cross-validation on the dataset 
    http://www.cs.cornell.edu/people/pabo/movie-review-data/rt-polaritydata.tar.gz  
    Output mean of accuracy, precision, recall, and F1 score for 
    5-fold cross validation
"""
# -*- coding: utf-8 -*-
#!/usr/bin/env python

# Author: Pham Quang Nhat Minh

import sys
import codecs
import numpy as np
import scipy.sparse as sp
from nltk.stem.snowball import SnowballStemmer
from sklearn import metrics
from sklearn import cross_validation
from sklearn.linear_model import LogisticRegression

# Read sentences in data_file, one sentence per lines with the format
# +1 effective but too-tepid biopic
# Return
#   X: scipy.sparse matrix of shape (n_samples, n_features)
#   y: ndarray of shape (n_samples)
#   n_samples, n_features
def load_data(data_file):
	# TASK: Read stopwords into a dictionary
	stopdict = {}
	f = codecs.open('../data/stopword.txt', 'rU', 'utf-8')
	for line in f:
		w = line.strip()
		if w == '': continue
		stopdict[w] = 1
	f.close()

	# TASK: create a Stemmer object for stemming
	stemmer = SnowballStemmer(u'english')

	# TASK: Open file to read, and get n_samples, n_features
	# Get list of dictionaries for each sentence
	# Get a vocabulary dictionary mapping from word to id
	# (index starts from 0)
	# Get array of labels (n_samples)
	labels = []
	sentences = []
	vocab  = {}
	n_samples  = 0
	n_features = 0
	f = codecs.open(data_file, 'rU')
	prev_line = ''
	for line in f:
		line = line.rstrip()
		if line == '': continue
		fields = line.split()
		lb = fields[0]		
		labels.append(lb)
		n_samples += 1		

		sen_vec = {}
		for i in xrange(1, len(fields)):
			w = stemmer.stem(fields[i].decode('utf-8', errors='ignore'))
			if stopdict.has_key(w):	continue

			if sen_vec.has_key(w):
				sen_vec[w] += 1
			else:
				sen_vec[w] = 0			

			if not vocab.has_key(w):
				vocab[w] = n_features
				n_features += 1

		sentences.append(sen_vec)

	f.close()

	# TASK: Create a sparse matrix of shape (n_samples, n_features)
	X = sp.lil_matrix( (n_samples, n_features) )

	# TASK: create ndarray from array of labels
	y = np.array(labels)

	# TASK: Add binary values for elements of dictionaries into
	# the sparse matrix
	for i in xrange(0, len(sentences)):
		sen_vec = sentences[i]
		for w in sen_vec.keys():
			fid = vocab[w]
			X[i, fid] = 1

	# TASK: return X, y, n_samples, n_features
	# return (X, y, n_samples, n_features)
	return (X, y, n_samples, n_features)


if __name__ == '__main__':
	data_file = '../data/sentiment.txt'

	# TASK: Read data from file sentiment.txt into X, y
	# X: scipy.sparse matrix of shape (n_samples, n_features)
	# y: ndarray of shape (n_samples)
	X, y, n_samples, n_features = load_data(data_file)

	# TASK: Computing cross-validated metrics
	# average accuracy, precision, recall, and F1 score for 
	# 5-fold cross validation
	clf = LogisticRegression(C=100.0, random_state=0)
	scores = cross_validation.cross_val_score(clf, X, y, cv=5)
	print scores

	predicted = cross_validation.cross_val_predict(clf, X, y, cv=5)
	print metrics.classification_report(y, predicted)

	acc  = metrics.accuracy_score(y, predicted)
	prec = metrics.precision_score(y, predicted, average='macro', pos_label=None) 	     
	recall = metrics.recall_score(y, predicted, average='macro', pos_label=None)
	f1 = metrics.f1_score(y, predicted, average='macro', pos_label=None)

	# TASK: Report results average accuracy, precision, recall, and F1 score
	print "Accuracy, precision, recall, f1: %0.2f %0.2f %0.2f %0.2f" % (acc, prec, recall, f1)