from FeatureDriftDetector import FDD2
import pandas as pd
import warnings
from river.drift import ADWIN

warnings.filterwarnings("ignore", category=FutureWarning)

data = pd.read_csv("../dataset/NSL-KDD.csv")


#print(data.columns)


FDD2(
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

# FDD2(
#     dataset = data,
#     features = {"duration" : 2, "protocol_type" : 5, "service" : 7, "flag" : 8,
#        "src_bytes" : 1, "dst_bytes" : 2, "urgent" : 1, "hot" : 4},
#     threshold = 10,
#     sensi = 0.01
# )

