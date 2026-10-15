import numpy as np
from river.drift import ADWIN
import pandas as pd
from scipy.spatial.distance import squareform
from scipy.cluster import hierarchy

def CreateClusters(matrix):
    distance = 1 - np.abs(matrix)
    distance_format = squareform(distance, checks=False)
    
    #linkage tree
    linkage = hierarchy.linkage(distance_format, method='complete')

    threshold = 0.25 #correlation >= 0.75
    labels = hierarchy.fcluster(linkage, t=threshold, criterion='distance')

    df_clusters = pd.DataFrame({'feature': matrix.columns, 'cluster': labels})
    clusters = df_clusters.groupby('cluster')['feature'].apply(list).to_dict()

    return clusters

def FeatureCorrelator(instances, features):
    window = pd.DataFrame(instances)
    correlation = window.corr(method="spearman")
    correlation = abs(correlation) >= 0.55

    #criar clusters usando a matrix e atrelar pesos
    clusters = CreateClusters(correlation)

    clusters = {
        cluster_id: {feature: features[feature] for feature in feature_list}
        for cluster_id, feature_list in clusters.items()
    }

    return clusters
