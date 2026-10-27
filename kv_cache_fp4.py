#!/usr/bin/env python3
import os, json, hashlib
from datetime import datetime, timezone
from dataclasses import dataclass, asdict

VERSION = "4.0.0"
AUTEUR = "Aissa Mohammedi (DGK)"
BASE = os.path.expanduser("~/Documents/nexus_ai_compress")
KV_DIR = os.path.join(BASE, "kv_cache")
os.makedirs(KV_DIR, exist_ok=True)


class FP4Codec:
FP4_VALUES = [0.0, 0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 6.0,
-0.0, -0.5, -1.0, -1.5, -2.0, -3.0, -4.0, -6.0]

@classmethod
def float_to_fp4(cls, value):
best_idx = 0
best_diff = float("inf")
for i, v in enumerate(cls.FP4_VALUES):
diff = abs(v - value)
if diff < best_diff:
best_diff = diff
best_idx = i
return best_idx

@classmethod
def fp4_to_float(cls, code):
return cls.FP4_VALUES[code] if 0 <= code < 16 else 0.0

@classmethod
def compress_array(cls, values):
result = bytearray()
for i in range(0, len(values), 2):
v1 = cls.float_to_fp4(values[i])
v2 = cls.float_to_fp4(values[i + 1]) if i + 1 < len(values) else 0
result.append((v1 << 4) | v2)
return bytes(result)


@dataclass
class KVCacheStats:
num_layers: int = 32
num_heads: int = 32
head_dim: int = 128
seq_len: int = 8192
fp16_size_bytes: int = 0
fp4_size_bytes: int = 0
ratio: float = 0.0
reduction_percent: float = 0.0


class MlaKvCache:
def __init__(self, num_layers=32, num_heads=32, head_dim=128, latent_dim=512):
self.num_layers = num_layers
self.num_heads = num_heads
self.head_dim = head_dim
self.latent_dim = latent_dim

def calculer_taille_fp16(self, seq_len):
return 2 * self.num_layers * self.num_heads * self.head_dim * seq_len * 2

def calculer_taille_fp4(self, seq_len):
return int(self.num_layers * self.latent_dim * seq_len * 0.5)

def statistiques(self, seq_len=8192):
fp16 = self.calculer_taille_fp16(seq_len)
fp4 = self.calculer_taille_fp4(seq_len)
ratio = fp4 / fp16 if fp16 > 0 else 1.0
return KVCacheStats(
num_layers=self.num_layers, num_heads=self.num_heads,
head_dim=self.head_dim, seq_len=seq_len,
fp16_size_bytes=fp16, fp4_size_bytes=fp4,
ratio=round(ratio, 4), reduction_percent=round((1 - ratio) * 100, 2))


def main():
print("=" * 60)
print("NEXUS FP4 KV CACHE")
print("Auteur : {}".format(AUTEUR))
print("=" * 60)

test_values = [0.0, 0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 6.0, -2.0, -4.0]
compressed = FP4Codec.compress_array(test_values)
print("Test codec : {} valeurs -> {} octets".format(len(test_values), len(compressed)))

mla = MlaKvCache()
stats = mla.statistiques(seq_len=8192)

print("FP16 baseline : {} Go".format(round(stats.fp16_size_bytes / (1024**3), 3)))
print("FP4+MLA : {} Mo".format(round(stats.fp4_size_bytes / (1024**2), 2)))
print("Reduction : {} %".format(stats.reduction_percent))

report = {
"version": VERSION,
"auteur": AUTEUR,
"date": datetime.now(timezone.utc).isoformat(),
"stats": asdict(stats)
}
report["hash_sha256"] = hashlib.sha256(
json.dumps(report, sort_keys=True).encode()
).hexdigest()

path = os.path.join(KV_DIR, "kv_cache_fp4_report.json")
with open(path, "w", encoding="utf-8") as f:
json.dump(report, f, indent=2, ensure_ascii=False)
print("Rapport : {}".format(path))


if __name__ == "__main__":
main()
