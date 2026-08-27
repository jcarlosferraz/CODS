import pandas as pd
from nfstream import NFStreamer


def Collector(arquivo_pcap, nome_saida):

    # agrupar automaticamente por IP Origem/Destino, Porta Origem/Destino e Protocolo)
    streamer = NFStreamer(source=arquivo_pcap)

    print("Processando o arquivo PCAP e extraindo os fluxos...")

    #Converte os fluxos capturados para DataFrame
    df_fluxos = streamer.to_pandas()

    # 5. Salva o resultado em um arquivo CSV
    df_fluxos.to_csv(nome_saida, index=False)

    print(f"Sucesso! Os fluxos foram salvos em: {nome_saida}")

    return df_fluxos