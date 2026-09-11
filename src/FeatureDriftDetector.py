from scipy.stats import ks_2samp
import numpy as np
from river.drift import ADWIN
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
from scipy.spatial.distance import squareform
from scipy.cluster import hierarchy


def GreaterWeight(cluster):
    weightest = -1
    representative = ''

    for feature, weight in cluster.items():
        if weight >= weightest:
            weightest = weight
            representative = feature
    
    servants = list(cluster.keys())
    servants.remove(representative)
    
    return representative, servants

def CreateClusters(matrix):
    distance = 1 - np.abs(matrix)
    distance_format = squareform(distance, checks=False)
    
    #arvore de linkage
    linkage = hierarchy.linkage(distance_format, method='complete')

    threshold = 0.25 #correlação >= 0.75
    labels = hierarchy.fcluster(linkage, t=threshold, criterion='distance')

    df_clusters = pd.DataFrame({'feature': matrix.columns, 'cluster': labels})
    clusters = df_clusters.groupby('cluster')['feature'].apply(list).to_dict()

    return clusters

def FDD2(dataset, features, threshold , sensi):
    
    print("Starting concept drift detection")
    peso_limite = threshold
    peso_atual = 0

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


    #Formar matrix de correlação com as primeiras 500 instâncias
    window = pd.DataFrame(instances)
    correlation = window.corr(method="spearman")
    correlation = abs(correlation) >= 0.75

    #criar clusters usando a matrix e atrelar pesos
    clusters = CreateClusters(correlation)

    clusters = {
        cluster_id: {feature: features[feature] for feature in feature_list}
        for cluster_id, feature_list in clusters.items()
    }


    # 5: {'flag': 8, 'src_bytes': 1, 'same_srv_rate': 3}
    # A cada instância, itero de cluster em cluster, verifico a coluna de maior peso no cluster(representante)
    #Localizo o detector do representante, atualizo ele para aquela instância, atrelo as outra colunas do cluster,
    #pulo para próximo cluster

    #rodar detectores para o restante
    for i, instance in data.iloc[500:].iterrows():
        features_with_drift = []

        for cluster in clusters.values():
                representative, servants = GreaterWeight(cluster)
                val = instance[representative]
                detectors[representative].update(val)

                if detectors[representative].drift_detected:
                    peso_atual += features[representative]
                    features_with_drift.append(representative)
                    for servant in servants:
                        peso_atual += features[servant]
                        features_with_drift.append(servant)            


        if features_with_drift:
            print(f"Instância {i}: Drift detectado nas colunas {features_with_drift}")

    print("Total drift weight: {}".format(peso_atual))
    if(peso_atual > peso_limite):
        print("Drift threshold has been exceeded")

    print("-" * 25)
    print("")