import numpy as np
from river.drift import ADWIN
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
from AutonomousFeatureCorrelator import AutonomousFeatureCorrelator

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


def FDD2(dataset, features, threshold , sensi):
    
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

    clusters = AutonomousFeatureCorrelator(instances, features)
    num_clusters = len(clusters)
    num_created_matrix += 1

    #rodar detectores para o restante
    for i, instance in data.iloc[500:].iterrows():

        features_with_drift = []

        for cluster in clusters.values():
                representative, followers = GreaterWeight(cluster)
                val = instance[representative]
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