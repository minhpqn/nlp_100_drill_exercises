"""
DESCRIPTION

    Build a classification model for sentiment analysis task with 
    logistic regression model on the data with simple
    bag-of-words features

    Perform cross-validation on the dataset 
    http://www.cs.cornell.edu/people/pabo/movie-review-data/rt-polaritydata.tar.gz  
    Output mean of accuracy, precision, recall, and F1 score for 
    5-fold cross validation

    Use more efficient way for loading text data and extracting features
"""
# -*- coding: utf-8 -*-
#!/usr/bin/env python

# Author: Pham Quang Nhat Minh

import sys
import codecs
import numpy as np
import scipy.sparse as sp
from nltk.stem.snowball import SnowballStemmer
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn import metrics
from sklearn import cross_validation
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

# read sentiment.txt file
# Return a list of strings and list of labels
def load_data(filename):
	stemmer = SnowballStemmer(u'english')
	labels = []
	sentences = []
	f = codecs.open(data_file, 'rU')
	for line in f:
		line = line.rstrip()
		if line == '': continue
		fields = line.split()
		lb = fields[0]		
		labels.append(lb)

		words = []
		for i in xrange(1, len(fields)):
			w = stemmer.stem(fields[i].decode('utf-8', errors='ignore'))
			words.append(w)

		sentences.append( ' '.join( words ) )

	f.close()

	y = np.array(labels)

	return (sentences, y)

if __name__ == '__main__':
	data_file = '../data/sentiment.txt'

	sentences, y = load_data(data_file)
	# use binary features
	# Reference: http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html
	count_vect = CountVectorizer( stop_words='english', binary=True )

	X_binary = count_vect.fit_transform( sentences )

	clf = LogisticRegression(C=100.0, random_state=0)
	scores = cross_validation.cross_val_score(clf, X_binary, y, cv=5)
	print scores

	predicted = cross_validation.cross_val_predict(clf, X_binary, y, cv=5)
	print metrics.classification_report(y, predicted)

	acc  = metrics.accuracy_score(y, predicted)
	prec = metrics.precision_score(y, predicted, average='macro', pos_label=None) 	     
	recall = metrics.recall_score(y, predicted, average='macro', pos_label=None)
	f1 = metrics.f1_score(y, predicted, average='macro', pos_label=None)

	print "Accuracy, precision, recall, f1: %0.4f %0.4f %0.4f %0.4f" % (acc, prec, recall, f1)

	print 
	print '== Use TfIdf weighting =='
	count_vect = CountVectorizer( stop_words='english' )
	X_count = count_vect.fit_transform( sentences )

	tfidf_transformer = TfidfTransformer()
	X_tfidf = tfidf_transformer.fit_transform( X_count )
	scores = cross_validation.cross_val_score(clf, X_tfidf, y, cv=5)
	print scores

	predicted = cross_validation.cross_val_predict(clf, X_tfidf, y, cv=5)
	print metrics.classification_report(y, predicted)

	print
	print '== Use SVM method =='
	sen_clf = LinearSVC()
	scores = cross_validation.cross_val_score(sen_clf, X_tfidf, y, cv=5)
	print scores
	predicted = cross_validation.cross_val_predict(sen_clf, X_tfidf, y, cv=5)
	print metrics.classification_report(y, predicted)

    







