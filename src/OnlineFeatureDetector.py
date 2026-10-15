import numpy as np
from river.drift import ADWIN
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
from OnlineFeatureCorrelator import FeatureCorrelator

def InstanceCollect(data, current_instance):
    instances = []

    for i, instance in data.iloc[current_instance: current_instance + 500].iterrows():
        instances.append(instance)
    
    return instances

def GreaterWeight(cluster):
    weightest = -1
    representative = ''

    for feature, weight in cluster.items():
        if weight >= weightest:
            weightest = weight
            representative = feature
    
    followers = list(cluster.keys())
    followers.remove(representative)
    
    return representative, followers


def CODS(dataset, features, threshold , sensi):
    
    print("Starting concept drift detection")
    peso_limite = threshold
    peso_atual = 0
    num_clusters = 0
    num_created_matrix = 0


    #Features filtradas pelo operador
    data = dataset[list(features.keys())]

    #criar detectores, dict no formato --> {nomeColuna : objetoADWIN}
    detectors = {col: ADWIN(sensi) for col in data}

    #Rodar detectores para primeiras 500 instâncias
    instances = []

    for i, instance in data.iloc[:500].iterrows():
        instances.append(instance)
        features_with_drift = []

        for col in data:
            val = instance[col]
            detectors[col].update(val)

            if detectors[col].drift_detected:
                peso_atual += data[col]
                features_with_drift.append(col)

        if features_with_drift:
            print(f"Instância {i}: Drift detectado nas colunas {features_with_drift}")

    clusters = FeatureCorrelator(instances, features)
    num_clusters = len(clusters)
    num_created_matrix += 1 

    #mapear o nome de cada coluna para seu index
    col_to_idx = {col: idx for idx, col in enumerate(data.columns)}

    #Localizar ID do representante de cada cluster
    processed_clusters = []
    for cluster in clusters.values():
        representative, followers = GreaterWeight(cluster)
        rep_idx = col_to_idx[representative] # Pega o índice numérico da coluna
        processed_clusters.append((representative, rep_idx, followers))

    #dataframe --> numpy matriz
    X = data.to_numpy(dtype=float)

    for i in range(len(X)):
        row = X[i]
        features_with_drift = []

        # Iterar apenas sobre os clusters já processados
        for representative, rep_idx, followers in processed_clusters:

            val = row[rep_idx]            
            detectors[representative].update(val)

            if detectors[representative].drift_detected:
                peso_atual += features[representative]
                features_with_drift.append(representative)
                
                for follower in followers:
                    peso_atual += features[follower]
                    features_with_drift.append(follower)           

        if features_with_drift:
            print(f"Instância {i}: Drift detectado nas colunas {features_with_drift}")

    print("Total drift weight: {}".format(peso_atual))
    if(peso_atual > peso_limite):
        print("Drift threshold has been exceeded")

    media_detectors = num_clusters / num_created_matrix
    print("Média de detectores usados: {}".format(media_detectors))
    print("-" * 25)
    print("")