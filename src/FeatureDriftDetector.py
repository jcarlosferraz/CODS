from scipy.stats import ks_2samp
import numpy as np
from river.drift import ADWIN
from sklearn.preprocessing import MinMaxScaler
import pandas as pd


def FDD(config, dataset, features, mode):
    print("-" * 25)
    if(config == "simple"):
        print("Simple config selected")


        if(mode[0] == "univariate"):

            for feature in dataset:
                if feature in features:

                    #preparar stream e normalizar, eu transformo coluna em dataset e depois em series
                    coluna = dataset[[feature]]

                    scaler = MinMaxScaler()
                    coluna = pd.DataFrame(scaler.fit_transform(coluna), columns=coluna.columns)
                    
                    adwin = ADWIN(mode[1])
                    stream = coluna[feature]
                    
                    #loop do adwin

                    for i, x in enumerate(stream, start=1):

                        adwin.update(x)

                        if adwin.drift_detected:
                            print("DRIFT🚨: Feature {} -> drift around instance {}".format(feature, i))
            print("Execution completed!")
                    

        else:
            print("Error: select a valid mode -> univariate")
            

    elif(config[0] == "weight"):
        print("Weight config selected")
        peso_limite = config[1]
        peso_atual = 0


        if(mode[0] == "univariate"):

            for feature in dataset:
                if feature in features:

                    #preparar stream
                    coluna = dataset[[feature]]

                    #normalizar dados antes
                    scaler = MinMaxScaler()
                    coluna = pd.DataFrame(scaler.fit_transform(coluna), columns=coluna.columns)

                    adwin = ADWIN(mode[1])
                    stream = coluna[feature]
                    
                    #loop do adwin

                    for i, x in enumerate(stream, start=1):

                        adwin.update(x)

                        if adwin.drift_detected:
                            print("DRIFT🚨: Feature {} -> drift around instance {}".format(feature, i))
                            peso_atual += features[feature]
                            
        
        else:
            print("Error: select a valid mode -> univariate")

        print("Total drift weight: {}".format(peso_atual))
        if(peso_atual > peso_limite):
            print("Drift threshold has been exceeded")

    else:
        print("Error: select a valid config -> simple, weight")

    print("-" * 25)
    print("")