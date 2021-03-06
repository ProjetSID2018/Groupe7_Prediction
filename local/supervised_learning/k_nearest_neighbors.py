# -*- coding: utf-8 -*-
# group 7

import numpy as np
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn import metrics


###########                 FINAL MODEL ASSESSMENT                  ###########

# Import data for final model assessment (with train/test where test sample was
# not used during grid search)
xtrain, xtest, ytrain, ytest = pickle.load(open('../../../train_test_data_group7', 'rb'))


def model_assessment(model, model_name):
    """
    Take a model and it's name in parameters, train a classifier and print the
    classification report and the confusion matrix.
    """
    labels = ['international', 'france', 'economie', 'sciences_high_tech',
              'arts_et_culture', 'sports', 'sante']
    clf = model.fit(xtrain, ytrain)
    predicted = clf.predict(xtest)
    print('--- %s results ---\n' % model_name)
    print(metrics.classification_report(ytest, predicted, target_names=labels))
    print('Confusion matrix:\n%s' % metrics.confusion_matrix(ytest, predicted))
    print('\nAccuracy score : %s' % metrics.accuracy_score(ytest, predicted))


model_assessment(KNeighborsClassifier(n_neighbors=20), 'K Nearest Neighbors')


###########                     GRID SEARCH CV                      ###########

## Import data
#df = pickle.load(open('../../../recoded_filtered_data_group7', 'rb'))
#
## Delete duplicates and unrecoded labels
#df.drop_duplicates(['title'], keep='last', inplace=True)
#df = df[df['theme_recoded'] != 'delete']
#
## Fix random seed for reproducibility
#np.random.seed(10)
#
## Split our df for train/test with a stratify strategy
#xtrain, xtest, ytrain, ytest = train_test_split(df, df['theme_recoded'], test_size=0.2,
#                                                stratify=df['theme_recoded'])
#
## Build a pipeline to behave like a compound classifier
#text_clf = Pipeline([('tfidf', TfidfVectorizer()), ('clf', KNeighborsClassifier())])
#
## Define a grid of possible values
#parameters = {
#        'tfidf__ngram_range': [(1, 1)],
#        'tfidf__max_df': [0.80],
#        'tfidf__min_df': [2],
#        'tfidf__max_features': [10000],
#        'clf__n_neighbors': [20]
#        }
#
## Run an exhaustive search of the best parameters from the grid
#gs_clf = GridSearchCV(text_clf, parameters, scoring='f1_weighted', cv=3, verbose=2,
#                      n_jobs=-1)
#gs_clf = gs_clf.fit(xtrain['content'], ytrain)
#print(gs_clf.best_score_)
#print(gs_clf.best_params_)
