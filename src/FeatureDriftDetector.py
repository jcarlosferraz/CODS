from scipy.stats import ks_2samp
import numpy as np
from river.drift import ADWIN
from sklearn.preprocessing import MinMaxScaler
import pandas as pd


def FDD(dataset, features, threshold , sensi):
    
    print("Starting concept drift detection")
    peso_limite = threshold
    peso_atual = 0


    for feature in dataset:
        if feature in features:

            #preparar stream
            coluna = dataset[[feature]]

            #normalizar dados antes
            scaler = MinMaxScaler()
            coluna = pd.DataFrame(scaler.fit_transform(coluna), columns=coluna.columns)

            adwin = ADWIN(sensi)
            stream = coluna[feature]
            
            #loop do adwin

            for i, x in enumerate(stream, start=1):
                
                adwin.update(x)

                if adwin.drift_detected:
                    print("DRIFT🚨: Feature {} -> drift around instance {}".format(feature, i))
                    peso_atual += features[feature]
                            

    print("Total drift weight: {}".format(peso_atual))
    if(peso_atual > peso_limite):
        print("Drift threshold has been exceeded")

    print("-" * 25)
    print("")