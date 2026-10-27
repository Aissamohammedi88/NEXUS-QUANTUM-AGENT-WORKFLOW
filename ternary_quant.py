#!/usr/bin/env python3
import os, json, hashlib
from datetime import datetime, timezone

VERSION = "4.0.0"
AUTEUR = "Aissa Mohammedi (DGK)"
BASE = os.path.expanduser("~/Documents/nexus_ai_compress")
TERNARY_DIR = os.path.join(BASE, "ternary")
os.makedirs(TERNARY_DIR, exist_ok=True)


class TernaryCodec:
TRITS_PER_BYTE = 5

@classmethod
def float_to_trit(cls, value):
if value < -0.5:
return -1
elif value > 0.5:
return 1
return 0

@classmethod
def pack_trits(cls, trits):
result = bytearray()
for i in range(0, len(trits), cls.TRITS_PER_BYTE):
bloc = trits[i:i + cls.TRITS_PER_BYTE]
while len(bloc) < cls.TRITS_PER_BYTE:
bloc.append(0)
code = 0
for j, t in enumerate(bloc):
code += (t + 1) * (3 ** j)
if code > 255:
code = 255
result.append(code)
return bytes(result)


def taille_ternaire(num_params):
return (num_params * 1.58) / 8


def main():
print("=" * 60)
print("NEXUS TERNARY QUANTIZATION — 1.58 bit")
print("Auteur : {}".format(AUTEUR))
print("=" * 60)

test = [0.8, -0.3, 0.0, -0.9, 0.5, 0.2, -1.0, 1.0, -0.1, 0.7]
trits = [TernaryCodec.float_to_trit(v) for v in test]
packed = TernaryCodec.pack_trits(trits)
print("Original : {}".format(test))
print("Trits : {}".format(trits))
print("Octets : {} (pour {} valeurs)".format(len(packed), len(test)))

print("")
print("Tailles pour differents modeles :")
modeles = [
("DeepSeek V3 (671B)", 671_000_000_000),
("DeepSeek 7B", 7_000_000_000),
("Mistral 7B", 7_000_000_000),
]

resultats = {}
for nom, params in modeles:
fp16 = params * 16 / 8 / (1024**3)
q4 = params * 4.5 / 8 / (1024**3)
q2 = params * 2.6 / 8 / (1024**3)
tern = taille_ternaire(params) / (1024**3)
resultats[nom] = {
"params": params, "fp16_go": round(fp16, 2),
"q4_go": round(q4, 2), "q2_go": round(q2, 2),
"ternaire_go": round(tern, 2)
}
print("")
print(" {} :".format(nom))
print(" FP16 : {} Go".format(round(fp16, 2)))
print(" Q4_K_M : {} Go".format(round(q4, 2)))
print(" Q2_K : {} Go".format(round(q2, 2)))
print(" Ternaire: {} Go".format(round(tern, 2)))

report = {
"version": VERSION,
"auteur": AUTEUR,
"date": datetime.now(timezone.utc).isoformat(),
"bits_par_param": 1.58,
"modeles": resultats,
"conclusion": "DeepSeek V3 minimum 130 Go. DeepSeek 7B 2.8 Go en Q2_K."
}
report["hash_sha256"] = hashlib.sha256(
json.dumps(report, sort_keys=True).encode()
).hexdigest()

path = os.path.join(TERNARY_DIR, "ternary_report.json")
with open(path, "w", encoding="utf-8") as f:
json.dump(report, f, indent=2, ensure_ascii=False)
print("")
print("Rapport : {}".format(path))


if __name__ == "__main__":
main()
