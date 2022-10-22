#!/usr/bin/env python3.6.7
# -*- coding: UTF-8 -*-
"""
Author: Patrick

Date: 2021/6/21 20:05

Docs: 
    
"""
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA

data = pd.read_csv('data/pca.csv')
X = data.to_numpy()

pca = PCA(n_components=3)
newX = pca.fit(X)
ratio = pca.explained_variance_ratio_
cov = pca.get_covariance()
comp = pca.components_
print(ratio)
print(cov)
print(comp)
