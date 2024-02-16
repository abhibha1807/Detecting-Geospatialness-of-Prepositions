# Disambiguating spatial prepositions: the case of geo-spatial sense detection


Spatial relations in natural language are frequently expressed through prepositions. Thus, in the locative expressions “New York in the United States” and “the house on the 
river” the prepositions “in” and “on” respectively serve to communicate the relationships in space between the subject and object of the preposition. Automatic detection of 
the use of prepositions in a spatial and in particular a geo-spatial sense that refers to geographic context is of interest in supporting automated methods for determining the 
actual geographic location referred to by locative expressions. This work focuses on disambiguation of prepositions in natural language, with the goal of distinguishing whether a 
preposition is used in a specifically geo-spatial sense. We conduct machine learning experiments that demonstrate the clear bene- fit for geo-spatial sense detection of using 
transformer model deep learning methods when compared with a variety of methods, that include Naive Bayes, Support Vector Machine (SVM) and Random Forest classifiers with hand 
crafted linguistic features, and a bag of words approach with a meta-classifier that adds geo-spatial features. The best performance was obtained with the BERT-based XLNet 
transfomer model, with a best precision of 0.96 and and an F1 score of 0.94 when evaluated on a corpus of natural language expressions that were annotated for this task. 
We also conducted experiments to detect generic spatial sense, in which the best the best F1 score, of 0.95, was again obtained with XLNet.

## KEYWORDS:
Preposition disambiguation, geo-spatial sense, generic spatial sense, transfer learning, BERT-based mod- els, geo-spatial corpus, geo-referencing, locative expressions


## Recommended Citation

@article{https://doi.org/10.1111/tgis.12976,
author = {Radke, Mansi A. and Gupta, Abhibha and Stock, Kristin and Jones, Christopher B.},
title = {Disambiguating spatial prepositions: The case of geo-spatial sense detection},
journal = {Transactions in GIS},
volume = {26},
number = {6},
pages = {2621-2650},
doi = {https://doi.org/10.1111/tgis.12976},
url = {https://onlinelibrary.wiley.com/doi/abs/10.1111/tgis.12976},
eprint = {https://onlinelibrary.wiley.com/doi/pdf/10.1111/tgis.12976},
abstract = {Abstract Spatial relations in natural language are frequently expressed through prepositions. Thus, in the locative expressions “New York in the United States” and “the house on the river” the prepositions “in” and “on,” respectively, serve to communicate the relationships in space between the subject and object of the preposition. Automatic detection of the use of prepositions in a spatial and in particular a geo-spatial sense that refers to geographic context is of interest in supporting automated methods for determining the actual geographic location referred to by locative expressions. This work focuses on disambiguation of prepositions in natural language, with the goal of distinguishing whether a preposition is used in a specifically geo-spatial sense. We conduct machine learning experiments that demonstrate the clear benefit for geo-spatial sense detection of using transformer model deep learning methods when compared with a variety of methods, that include Naive Bayes, support vector machine, and random forest classifiers with handcrafted linguistic features, and a bag of words approach with a meta-classifier that adds geo-spatial features. The best performance was obtained with the Bidirectional Encoder Representation from Transformer-based XLNet transformer model, with a best precision of 0.96 and an F1 score of 0.94 when evaluated on a corpus of natural language expressions that were annotated for this task. We also conducted experiments to detect generic spatial sense, in which the best F1 score, of 0.95, was again obtained with XLNet.},
year = {2022}
}

