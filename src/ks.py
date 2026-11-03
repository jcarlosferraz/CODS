import pandas as pd
from scipy.stats import ks_2samp
import time

inicio = time.time()

DRIFT_POINT = 12597  #Instance where abrupt drift occurs

WINDOW_SIZE = 1000

# Mesmas features usadas no adwin.py
FEATURES = [
    "duration", "protocol_type", "service", "flag",
    "src_bytes", "dst_bytes", "urgent", "hot", "num_failed_logins",
    "logged_in", "num_compromised", "root_shell", "su_attempted",
    "num_root", "num_file_creations", "num_shells", "num_access_files",
    "is_guest_login", "count", "srv_count", "serror_rate",
    "srv_serror_rate", "rerror_rate", "srv_rerror_rate", "same_srv_rate",
    "diff_srv_rate", "srv_diff_host_rate", "dst_host_count",
    "dst_host_srv_count", "dst_host_same_srv_rate",
    "dst_host_diff_srv_rate", "dst_host_same_src_port_rate",
    "dst_host_srv_diff_host_rate", "dst_host_serror_rate",
    "dst_host_srv_serror_rate", "dst_host_rerror_rate",
    "dst_host_srv_rerror_rate",
]

# FEATURES = ['http.content_length' , 'http.response' , 'tcp.ack' , 'tcp.ack_raw' ,
#        'tcp.checksum' , 'tcp.connection.fin' , 'tcp.connection.rst' ,
#        'tcp.connection.syn' , 'tcp.connection.synack' , 'tcp.dstport' ,
#        'tcp.flags' , 'tcp.flags.ack' , 'tcp.len' , 'tcp.seq' , 'udp.time_delta' ,
#        'mqtt.len' , 'mqtt.topic_len' , 'mbtcp.len' , 'mbtcp.unit_id' ,
#        'arp.opcode_1.0' , 'arp.opcode_2.0']

# FEATURES = ['bidirectional_ack_packets', 'bidirectional_bytes',
#        'bidirectional_cwr_packets', 'bidirectional_duration_ms',
#        'bidirectional_ece_packets', 'bidirectional_fin_packets',
#        'bidirectional_first_seen_ms', 'bidirectional_last_seen_ms',
#        'bidirectional_max_piat_ms', 'bidirectional_max_ps',
#        'bidirectional_mean_piat_ms', 'bidirectional_mean_ps',
#        'bidirectional_min_piat_ms', 'bidirectional_min_ps',
#        'bidirectional_packets', 'bidirectional_psh_packets',
#        'bidirectional_rst_packets', 'bidirectional_stddev_piat_ms',
#        'bidirectional_stddev_ps', 'bidirectional_syn_packets',
#        'dst2src_ack_packets', 'dst2src_bytes', 'dst2src_duration_ms',
#        'dst2src_ece_packets', 'dst2src_fin_packets', 'dst2src_first_seen_ms',
#        'dst2src_last_seen_ms', 'dst2src_max_piat_ms', 'dst2src_max_ps',
#        'dst2src_mean_piat_ms', 'dst2src_mean_ps', 'dst2src_min_piat_ms',
#        'dst2src_min_ps', 'dst2src_packets', 'dst2src_psh_packets',
#        'dst2src_rst_packets', 'dst2src_stddev_piat_ms', 'dst2src_stddev_ps',
#        'dst2src_syn_packets', 'dst_port', 'expiration_id',
#        'protocol', 'src2dst_ack_packets', 'src2dst_bytes',
#        'src2dst_cwr_packets', 'src2dst_duration_ms', 'src2dst_ece_packets',
#        'src2dst_fin_packets', 'src2dst_first_seen_ms', 'src2dst_last_seen_ms',
#        'src2dst_max_piat_ms', 'src2dst_max_ps', 'src2dst_mean_piat_ms',
#        'src2dst_mean_ps', 'src2dst_min_piat_ms', 'src2dst_min_ps',
#        'src2dst_packets', 'src2dst_psh_packets', 'src2dst_rst_packets',
#        'src2dst_stddev_piat_ms', 'src2dst_stddev_ps', 'src2dst_syn_packets',
#        'src_port']

ALPHA = 0.001

# Read dataset
data = pd.read_csv("dataset/NSL-KDD.csv")

print(f"Dataset Loaded: {data.shape[0]} instances, {data.shape[1]} columns\n")

# Define windows
start_a = DRIFT_POINT - WINDOW_SIZE  
end_a = DRIFT_POINT                  
start_b = DRIFT_POINT                
end_b = DRIFT_POINT + WINDOW_SIZE  

window_a = data.iloc[start_a:end_a]
window_b = data.iloc[start_b:end_b]

print(f"Ponto de drift suspeito: instância {DRIFT_POINT}")
print(f"α = {ALPHA}")
print("-" * 80)

# KS 2-sample
results = []

for feat in FEATURES:
    if feat not in data.columns:
        print(f"⚠ Feature '{feat}' não encontrada no dataset, pulando...")
        continue

    sample_a = window_a[feat].values
    sample_b = window_b[feat].values

    stat, pvalue = ks_2samp(sample_a, sample_b)
    drift = pvalue < ALPHA

    results.append({
        "feature": feat,
        "ks_statistic": stat,
        "p_value": pvalue,
        "drift": drift,
    })

# Ordenar por p-valor
results.sort(key=lambda r: r["p_value"])

# Exibir resultados
print(f"\n{'Feature':<35} {'KS Stat':>10} {'P-value':>14} {'Drift?':>8}")
print("=" * 70)

drift_count = 0
for r in results:
    marker = "YES" if r["drift"] else "  NO"
    pval_str = f"{r['p_value']:.2e}" if r["p_value"] < 0.001 else f"{r['p_value']:.6f}"
    print(f"{r['feature']:<35} {r['ks_statistic']:>10.6f} {pval_str:>14} {marker:>8}")
    if r["drift"]:
        drift_count += 1

print("=" * 70)
print(f"\nResults: {drift_count}/{len(results)} features with concept drift detected (p < {ALPHA})")

fim = time.time()
print(f"Tempo de execução: {fim - inicio:.4f} segundos")
