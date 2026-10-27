#!/usr/bin/env python3
import os, json, hashlib, secrets
from datetime import datetime, timezone

VERSION = "4.0.0"
AUTEUR = "Aissa Mohammedi (DGK)"
BASE = os.path.expanduser("~/Documents/nexus_ai_compress")
KEYS_DIR = os.path.join(BASE, "keys")
os.makedirs(KEYS_DIR, exist_ok=True)


def main():
seed = secrets.token_hex(32)
master = hashlib.sha256(seed.encode()).hexdigest()

keys = {
"version": VERSION,
"auteur": AUTEUR,
"date": datetime.now(timezone.utc).isoformat(),
"master_key": master,
"seed_hash": hashlib.sha256(seed.encode()).hexdigest(),
"sous_cles": {
"compression": hashlib.sha256((master + "compress").encode()).hexdigest()[:32],
"kv_cache": hashlib.sha256((master + "kv").encode()).hexdigest()[:32],
"ternary": hashlib.sha256((master + "ternary").encode()).hexdigest()[:32],
"raptor": hashlib.sha256((master + "raptor").encode()).hexdigest()[:32]
}
}
keys["hash_sha256"] = hashlib.sha256(
json.dumps(keys, sort_keys=True).encode()
).hexdigest()

path = os.path.join(KEYS_DIR, "keys.json")
with open(path, "w", encoding="utf-8") as f:
json.dump(keys, f, indent=2, ensure_ascii=False)
os.chmod(path, 0o600)
print("Cle maitre : {}".format(master[:32] + "..."))
print("Rapport : {}".format(path))


if __name__ == "__main__":
main()
