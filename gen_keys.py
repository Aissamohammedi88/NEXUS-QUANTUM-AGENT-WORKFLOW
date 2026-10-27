#!/usr/bin/env python3
import os, json, secrets, uuid
from datetime import datetime, timezone

BASE = os.path.expanduser("~/Documents/nexus_ai_compress")
KEYS_DIR = os.path.join(BASE, "keys")
CERTS_DIR = os.path.join(BASE, "certificats")
os.makedirs(KEYS_DIR, exist_ok=True)
os.makedirs(CERTS_DIR, exist_ok=True)

def key(prefix):
return "{}_{}".format(prefix, secrets.token_urlsafe(48))

keys = {
"generated_at": datetime.now(timezone.utc).isoformat(),
"dock_key": key("dock"),
"ai_key": key("ai"),
"agent_key": key("agent"),
"compress_key": key("compress"),
"raptor_key": key("raptor"),
"ultraconnect_key": secrets.token_hex(64),
"session_id": str(uuid.uuid4()),
"fingerprint": secrets.token_hex(16)
}

keys_path = os.path.join(KEYS_DIR, "keys.json")
with open(keys_path, "w") as f:
json.dump(keys, f, indent=2)
os.chmod(keys_path, 0o600)

cert_path = os.path.join(CERTS_DIR, "certificate.txt")
with open(cert_path, "w") as f:
f.write("NEXUS AI COMPRESSION CERTIFICATE\n")
f.write("=" * 50 + "\n")
f.write("Date : {}\n".format(keys["generated_at"]))
f.write("Session : {}\n".format(keys["session_id"]))
f.write("Fingerprint: {}\n".format(keys["fingerprint"]))
f.write("=" * 50 + "\n")
os.chmod(cert_path, 0o600)

print("Clés : {}".format(keys_path))
print("Cert : {}".format(cert_path))
