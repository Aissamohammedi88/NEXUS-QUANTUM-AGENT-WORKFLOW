#!/usr/bin/env python3
import os, json, hashlib
from datetime import datetime, timezone

VERSION = "4.0.0"
AUTEUR = "Aissa Mohammedi (DGK)"
BASE = os.path.expanduser("~/Documents/nexus_ai_compress")
RAPTOR_DIR = os.path.join(BASE, "raptor")
os.makedirs(RAPTOR_DIR, exist_ok=True)


def main():
tree = {
"version": VERSION,
"auteur": AUTEUR,
"date": datetime.now(timezone.utc).isoformat(),
"niveaux": [
{"niveau": 1, "nom": "Tokens", "description": "Mots bruts"},
{"niveau": 2, "nom": "Phrases", "description": "Groupes de tokens"},
{"niveau": 3, "nom": "Paragraphes", "description": "Groupes de phrases"},
{"niveau": 4, "nom": "Sections", "description": "Groupes de paragraphes"},
{"niveau": 5, "nom": "Documents", "description": "Groupes de sections"}
]
}
tree["hash_sha256"] = hashlib.sha256(
json.dumps(tree, sort_keys=True).encode()
).hexdigest()

path = os.path.join(RAPTOR_DIR, "tree.json")
with open(path, "w", encoding="utf-8") as f:
json.dump(tree, f, indent=2, ensure_ascii=False)
print("RAPTOR : {} niveaux indexes".format(len(tree["niveaux"])))
print("Rapport : {}".format(path))


if __name__ == "__main__":
main()
