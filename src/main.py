from FeatureDriftDetector import FDD2
import pandas as pd
import warnings
from river.drift import ADWIN
import time

warnings.filterwarnings("ignore", category=FutureWarning)

data = pd.read_csv("../dataset/NSL-KDD.csv")
inicio = time.time()


# FDD2(
#     dataset = data,
#     features = {"duration" : 1, "protocol_type" : 1, "service" : 1, "flag" : 3,
#        "src_bytes" : 3, "dst_bytes" : 3, "urgent" : 1, "hot" : 1, "num_failed_logins" : 1,
#        "logged_in" : 3, "num_compromised" : 1, "root_shell" : 1, "su_attempted" : 1,
#        "num_root" : 1, "num_file_creations" : 1, "num_shells" : 1, "num_access_files" : 1,
#        "is_guest_login" : 1, "count" : 10, "srv_count" : 10, "serror_rate" : 7,
#        "srv_serror_rate" : 7, "rerror_rate" : 7, "srv_rerror_rate" : 1, "same_srv_rate" : 10,
#        "diff_srv_rate" : 1, "srv_diff_host_rate" : 1, "dst_host_count" : 1,
#        "dst_host_srv_count" : 5, "dst_host_same_srv_rate" : 5,
#        "dst_host_diff_srv_rate" : 1, "dst_host_same_src_port_rate" : 5,
#        "dst_host_srv_diff_host_rate" : 1, "dst_host_serror_rate" : 7,
#        "dst_host_srv_serror_rate" : 7, "dst_host_rerror_rate" : 7,
#        "dst_host_srv_rerror_rate": 1},
#     threshold = 60,
#     sensi = 0.01
# )

FDD2( data, 
    {"duration" : 1, "protocol_type" : 1, "service" : 1, "flag" : 3,
    "src_bytes" : 3, "dst_bytes" : 3, "urgent" : 1, "hot" : 1, "num_failed_logins" : 1,
    "logged_in" : 3, "num_compromised" : 1, "root_shell" : 1, "su_attempted" : 1,
    "num_root" : 1, "num_file_creations" : 1, "num_shells" : 1, "num_access_files" : 1,
    "is_guest_login" : 1, "count" : 10, "srv_count" : 10, "serror_rate" : 7,
    "srv_serror_rate" : 7, "rerror_rate" : 7, "srv_rerror_rate" : 1, "same_srv_rate" : 10,
    "diff_srv_rate" : 1, "srv_diff_host_rate" : 1, "dst_host_count" : 1,
    "dst_host_srv_count" : 5, "dst_host_same_srv_rate" : 5,
    "dst_host_diff_srv_rate" : 1, "dst_host_same_src_port_rate" : 5,
    "dst_host_srv_diff_host_rate" : 1, "dst_host_serror_rate" : 7,
    "dst_host_srv_serror_rate" : 7, "dst_host_rerror_rate" : 7,
    "dst_host_srv_rerror_rate": 1},
    60,
    0.01
)

    
# FDD2( 
#     data, 
#     {'http.content_length' : 1 , 'http.response' : 1 , 'tcp.ack' : 1 , 'tcp.ack_raw' : 1 ,
#        'tcp.checksum' : 1 , 'tcp.connection.fin' : 1 , 'tcp.connection.rst' : 1 ,
#        'tcp.connection.syn' : 1 , 'tcp.connection.synack' : 1 , 'tcp.dstport' : 1 ,
#        'tcp.flags' : 1 , 'tcp.flags.ack' : 1 , 'tcp.len' : 1 , 'tcp.seq' : 1 , 'udp.time_delta' : 1 ,
#        'mqtt.len' : 1 , 'mqtt.topic_len' : 1 , 'mbtcp.len' : 1 , 'mbtcp.unit_id' : 1 ,
#        'Attack_label' : 1 , 'Attack_type_encoded' : 1},
#     60,
#     0.01
# )



fim = time.time()
print(f"Tempo de execução: {fim - inicio:.4f} segundos")

