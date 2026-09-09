from FeatureDriftDetector import FDD
import pandas as pd
import warnings
from river.drift import ADWIN

warnings.filterwarnings("ignore", category=FutureWarning)

data = pd.read_csv("../dataset/NSL-KDD.csv")


#print(data.columns)

# FDD(
#     config = "simple",
#     dataset = data,
#     features = ['tcp.ack', 'tcp.ack_raw', 'tcp.checksum', 'tcp.connection.fin',
#        'tcp.connection.rst', 'tcp.connection.syn', 'tcp.connection.synack',
#        'tcp.dstport', 'tcp.flags', 'tcp.flags.ack', 'tcp.len', 'tcp.seq',
#        'Attack_label', 'Attack_type_encoded'],
#     mode = ["univariate", 0.01]
# )


# FDD(
#     config = ["weight", 10],
#     dataset = data,
#     features = {'duration' : 2, 'protocol_type' : 1, 'service': 3, 'flag' : 3,
#        'src_bytes' : 2, 'dst_bytes' : 5, 'urgent': 4},
#     mode = ["univariate", 0.01]
# )



# FDD(
#     config = "simple",
#     dataset = data,
#     features = ['duration', 'protocol_type', 'service', 'flag',
#        'src_bytes', 'dst_bytes', 'urgent', 'hot', 'num_failed_logins',
#        'logged_in', 'num_compromised', 'root_shell', 'su_attempted',
#        'num_root', 'num_file_creations', 'num_shells', 'num_access_files',
#        'is_guest_login', 'count', 'srv_count', 'serror_rate',
#        'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate', 'same_srv_rate',
#        'diff_srv_rate', 'srv_diff_host_rate', 'dst_host_count',
#        'dst_host_srv_count', 'dst_host_same_srv_rate',
#        'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate',
#        'dst_host_srv_diff_host_rate', 'dst_host_serror_rate',
#        'dst_host_srv_serror_rate', 'dst_host_rerror_rate',
#        'dst_host_srv_rerror_rate'],
#     mode = ["univariate", 0.01]
# )

FDD(
    dataset = data,
    features = {"duration" : 2, "protocol_type" : 5, "service" : 7, "flag" : 8,
       "src_bytes" : 1, "dst_bytes" : 2, "urgent" : 1, "hot" : 4, "num_failed_logins" : 7,
       "logged_in" : 3, "num_compromised" : 4, "root_shell" : 2, "su_attempted" : 2,
       "num_root" : 1, "num_file_creations" : 1, "num_shells" : 6, "num_access_files" : 8,
       "is_guest_login" : 2, "count" : 2, "srv_count" : 1, "serror_rate" : 3,
       "srv_serror_rate" : 3, "rerror_rate" : 3, "srv_rerror_rate" : 3, "same_srv_rate" : 3,
       "diff_srv_rate" : 2, "srv_diff_host_rate" : 1, "dst_host_count" : 1,
       "dst_host_srv_count" : 7, "dst_host_same_srv_rate" : 1,
       "dst_host_diff_srv_rate" : 1, "dst_host_same_src_port_rate" : 1,
       "dst_host_srv_diff_host_rate" : 2, "dst_host_serror_rate" : 4,
       "dst_host_srv_serror_rate" : 2, "dst_host_rerror_rate" : 5,
       "dst_host_srv_rerror_rate": 2},
    threshold = 60,
    sensi = 0.01
)

# FDD(
#     config = ["weight", 6],
#     dataset = data,
#     features = {"feature1" : 2 , "feature2": 5, "feature3" : 4, "feature4" : 2},
#     mode = ["covariate-online", 0.01]
# )