import pandas as pd
from nfstream import NFStreamer


def Collector(arquivo_pcap, nome_saida):

    # agrupar IP Origem/Destino, Porta Origem/Destino e Protocolo)
    streamer = NFStreamer(source=arquivo_pcap)

    print("Processando o arquivo PCAP e extraindo os fluxos...")

    df_fluxos = streamer.to_pandas()


    df_fluxos.to_csv(nome_saida, index=False)

    print(f"Sucesso! Os fluxos foram salvos em: {nome_saida}")

    return df_fluxos