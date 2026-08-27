import pandas as pd
import warnings
from StreamCollector import Collector
from FeatureDriftDetector import FDD
import time


inicio = time.perf_counter()

honey = Collector("../pcap/honey5.pcap", "../honey.csv")
hakai = Collector("../pcap/cap8.pcap", "../hakai.csv")

data = pd.concat([honey, hakai] , ignore_index=True)
data.to_csv("../fluxo-final.csv")

FDD(
    config = "simple",
    dataset = data,
    features = ["bidirectional_packets",
    "bidirectional_bytes",
    "src2dst_packets",
    "src2dst_bytes",
    "dst2src_packets",
    "dst2src_bytes",
    "bidirectional_duration_ms",
    "src2dst_duration_ms",
    "dst2src_duration_ms"],
    mode = ["covariate-split", 8]
)

# FDD(
#     config = "simple",
#     dataset = data,
#     features = ["bidirectional_packets",
#     "bidirectional_bytes",
#     "src2dst_packets",
#     "src2dst_bytes",
#     "dst2src_packets",
#     "dst2src_bytes",
#     "bidirectional_duration_ms",
#     "src2dst_duration_ms",
#     "dst2src_duration_ms"],
#     mode = ["covariate-online", 0.1]
# )

fim = time.perf_counter()
tempo_gasto = fim - inicio  # Medido em segundos
print(tempo_gasto)

# 1166  +     2967     =  4132
#honey   +    hakai     =   

#delay = T_detection - T_real = 
#T_real = 12597
#139 139 171 171 683 747 875 139 --> 383 