#!/usr/bin/env python3
import os, json, time, hashlib, subprocess
from datetime import datetime, timezone

VERSION = "4.0.0"
AUTEUR = "Aissa Mohammedi (DGK)"
BASE = os.path.expanduser("~/Documents/nexus_ai_compress")
BENCH_DIR = os.path.join(BASE, "benchmarks")
os.makedirs(BENCH_DIR, exist_ok=True)


def run_ollama(model):
try:
start = time.time()
result = subprocess.run(
["ollama", "run", model, "Test de generation"],
capture_output=True, text=True, timeout=30
)
duree = time.time() - start
return {
"modele": model,
"duree_s": round(duree, 2),
"succes": result.returncode == 0,
"extrait": result.stdout[:200] if result.stdout else ""
}
except Exception as e:
return {"modele": model, "erreur": str(e), "succes": False}


def main():
print("=" * 60)
print("NEXUS BENCHMARK")
print("=" * 60)

modeles = ["deepseek-r1:1.5b"]
resultats = []
for m in modeles:
print("Test : {}".format(m))
r = run_ollama(m)
resultats.append(r)
print(" Duree : {}s".format(r.get("duree_s", "?")))
print(" Succes : {}".format(r.get("succes", False)))

report = {
"version": VERSION,
"auteur": AUTEUR,
"date": datetime.now(timezone.utc).isoformat(),
"resultats": resultats
}
report["hash_sha256"] = hashlib.sha256(
json.dumps(report, sort_keys=True).encode()
).hexdigest()

path = os.path.join(BENCH_DIR, "benchmark_report.json")
with open(path, "w", encoding="utf-8") as f:
json.dump(report, f, indent=2, ensure_ascii=False)
print("")
print("Rapport : {}".format(path))


if __name__ == "__main__":
main()
