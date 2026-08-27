from FeatureDriftDetector import FDD
import pandas as pd
import warnings
from river.drift import ADWIN

warnings.filterwarnings("ignore", category=FutureWarning)

data = pd.read_csv("../dataset/NSL-KDD.csv")


# FDD(
#     config = "simple",
#     dataset = data,
#     features = ['tcp.ack', 'tcp.ack_raw', 'tcp.checksum', 'tcp.connection.fin',
#        'tcp.connection.rst', 'tcp.connection.syn', 'tcp.connection.synack',
#        'tcp.dstport', 'tcp.flags', 'tcp.flags.ack', 'tcp.len', 'tcp.seq',
#        'Attack_label', 'Attack_type_encoded'],
#     mode = ["univariate", 0.01]
# )



FDD(
    config = "simple",
    dataset = data,
    features = ['duration', 'protocol_type', 'service', 'flag',
       'src_bytes', 'dst_bytes', 'urgent'],
    mode = ["univariate", 0.01]
)


# FDD(
#     config = ["weight", 6],
#     dataset = data,
#     features = {"feature1" : 2 , "feature2": 5, "feature3" : 4, "feature4" : 2},
#     mode = ["covariate-online", 0.01]
# )