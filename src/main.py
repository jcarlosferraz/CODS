from OnlineFeatureDetector import CODS
import pandas as pd
import warnings
import time

warnings.filterwarnings("ignore", category=FutureWarning)

data = pd.read_csv("../dataset/iot23.csv")
start = time.time()



## Example case for NSL-KDD

# CODS( data, 
#     {
#     "duration": 1, "protocol_type": 1, "service": 1, "flag": 1,
#     "src_bytes": 1, "dst_bytes": 1, "urgent": 1, "hot": 1, "num_failed_logins": 1,
#     "logged_in": 1, "num_compromised": 1, "root_shell": 1, "su_attempted": 1,
#     "num_root": 1, "num_file_creations": 1, "num_shells": 1, "num_access_files": 1, 
#     "is_guest_login": 1, "count": 1, "srv_count": 1, "serror_rate": 1, 
#     "srv_serror_rate": 1, "rerror_rate": 1, "srv_rerror_rate": 1, "same_srv_rate": 1, 
#     "diff_srv_rate": 1,  "srv_diff_host_rate": 1, "dst_host_count": 1,
#     "dst_host_srv_count": 1, "dst_host_same_srv_rate": 1,
#     "dst_host_diff_srv_rate": 1, "dst_host_same_src_port_rate": 1,
#     "dst_host_srv_diff_host_rate": 1, "dst_host_serror_rate": 1,
#     "dst_host_srv_serror_rate": 1, "dst_host_rerror_rate": 1,
#     "dst_host_srv_rerror_rate": 1
# },
#     60,
#     0.01
# )

##Example case for Edge-IIoT

# CODS( 
#     data, 
#     {'http.content_length' : 3 , 'http.response' : 3 , 'tcp.ack' : 1 , 'tcp.ack_raw' : 1 ,
#        'tcp.checksum' : 1 , 'tcp.connection.fin' : 2 , 'tcp.connection.rst' : 2 ,
#        'tcp.connection.syn' : 2 , 'tcp.connection.synack' : 2 , 'tcp.dstport' : 3 ,
#        'tcp.flags' : 2 , 'tcp.flags.ack' : 2 , 'tcp.len' : 3 , 'tcp.seq' : 1 , 'udp.time_delta' : 1 ,
#        'mqtt.len' : 1 , 'mqtt.topic_len' : 1 , 'mbtcp.len' : 1 , 'mbtcp.unit_id' : 1},
#     60,
#     0.01
# )

##Example case for IoT-23, set of assignments cited in section 4

CODS(
    data,
    {
    # Flags SYN
    'bidirectional_syn_packets': 3, 'src2dst_syn_packets': 3,
    'dst2src_syn_packets': 3,

    # Flags ACK
    'bidirectional_ack_packets': 2, 'src2dst_ack_packets': 3,
    'dst2src_ack_packets': 2,

    # Volume
    'bidirectional_packets': 3, 'src2dst_packets': 3, 'dst2src_packets': 3,
    'bidirectional_bytes': 2, 'src2dst_bytes': 2, 'dst2src_bytes': 2,

    #Packet size
    'bidirectional_mean_ps': 2, 'src2dst_mean_ps': 3, 'dst2src_mean_ps': 2,
    'bidirectional_min_ps': 2, 'src2dst_min_ps': 2, 'dst2src_min_ps': 2,
    'bidirectional_max_ps': 2, 'src2dst_max_ps': 2, 'dst2src_max_ps': 2,
    'bidirectional_stddev_ps': 2, 'src2dst_stddev_ps': 3, 'dst2src_stddev_ps': 2,

    # Time between packets
    'bidirectional_mean_piat_ms': 2, 'src2dst_mean_piat_ms': 3, 'dst2src_mean_piat_ms': 2,
    'bidirectional_min_piat_ms': 2, 'src2dst_min_piat_ms': 2, 'dst2src_min_piat_ms': 1,
    'bidirectional_max_piat_ms': 2, 'src2dst_max_piat_ms': 2, 'dst2src_max_piat_ms': 1,
    'bidirectional_stddev_piat_ms': 2, 'src2dst_stddev_piat_ms': 2, 'dst2src_stddev_piat_ms': 1,

    #Flow duration
    'bidirectional_duration_ms': 2, 'src2dst_duration_ms': 2, 'dst2src_duration_ms': 2,


    'bidirectional_rst_packets': 2, 'src2dst_rst_packets': 2, 'dst2src_rst_packets': 2,
    'bidirectional_fin_packets': 2, 'src2dst_fin_packets': 2, 'dst2src_fin_packets': 2,
    'bidirectional_psh_packets': 2, 'src2dst_psh_packets': 2, 'dst2src_psh_packets': 1,
    'bidirectional_cwr_packets': 1, 'src2dst_cwr_packets': 1,
    'bidirectional_ece_packets': 1, 'src2dst_ece_packets': 1, 'dst2src_ece_packets': 1,

    'protocol': 2,      # SYN flood uses TCP protocol
    'dst_port': 2,    
    'src_port': 1,  

    'expiration_id': 1},
    60,
    0.01)

end = time.time()
print(f"Run Time: {end - start:.4f} seconds")
