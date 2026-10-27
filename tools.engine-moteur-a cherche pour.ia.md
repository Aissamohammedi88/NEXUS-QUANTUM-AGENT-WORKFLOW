#!/usr/bin/env python3# -*- coding: utf-8 -*-
"""
NEXUS FERTECH WEB — Agent de recherche local
Utilise l'API publique DuckDuckGo (Instant Answer).
Port : 9400 · Zéro dépendance externe.
"""

import os
import json
import urllib.request
import urllib.parse
import http.server
import socketserver
from datetime import datetime

VERSION = "1.0.0"
PORT = int(os.environ.get("PORT", 9400))
HOST = "127.0.0.1"

# ═══════════════════════════════════════════════════════════════════
# HTML / CSS / JS (Interface Fertech)
# ═══════════════════════════════════════════════════════════════════
HTML_PAGE = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>NEXUS FERTECH — Agent DDG</title>
<style>
:root {
--bg: #0a0a0f;
--panel: #12121a;
--border: #2a2a3a;
--text: #e0e0e0;
--dim: #6b7280;
--green: #00ff9d;
--cyan: #00d4ff;
--red: #ff2d55;
}
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
font-family: 'SF Mono', 'Monaco', 'Courier New', monospace;
background: var(--bg);
color: var(--text);
padding: 20px;
min-height: 100vh;
background-image:
radial-gradient(ellipse at top, rgba(0, 255, 157, 0.05), transparent 60%),
linear-gradient(rgba(42, 42, 58, 0.1) 1px, transparent 1px),
linear-gradient(90deg, rgba(42, 42, 58, 0.1) 1px, transparent 1px);
background-size: 100% 100%, 30px 30px, 30px 30px;
}
.container { max-width: 900px; margin: 0 auto; }
.header {
border: 1px solid var(--border);
background: var(--panel);
padding: 20px;
border-radius: 8px;
margin-bottom: 20px;
position: relative;
overflow: hidden;
}
.header::before {
content: "";
position: absolute;
top: 0; left: 0; right: 0;
height: 2px;
background: linear-gradient(90deg, transparent, var(--green), transparent);
animation: scan 3s linear infinite;
}
@keyframes scan {
0% { transform: translateX(-100%); }
100% { transform: translateX(100%); }
}
h1 {
color: var(--green);
font-size: 20px;
margin-bottom: 6px;
text-shadow: 0 0 10px rgba(0, 255, 157, 0.5);
}
.subtitle { color: var(--dim); font-size: 11px; letter-spacing: 1px; }
.status-bar {
display: flex;
gap: 15px;
margin-top: 10px;
font-size: 10px;
color: var(--cyan);
}
.status-dot {
display: inline-block;
width: 8px; height: 8px;
background: var(--green);
border-radius: 50%;
margin-right: 5px;
box-shadow: 0 0 10px var(--green);
animation: pulse 2s infinite;
}
@keyframes pulse { 0%, 100% { opacity: 1; } 50% { opacity: 0.3; } }

.search-box {
display: flex;
gap: 10px;
margin-bottom: 20px;
}
input[type="text"] {
flex: 1;
background: var(--panel);
border: 1px solid var(--border);
color: var(--green);
padding: 15px;
font-family: inherit;
font-size: 14px;
border-radius: 8px;
outline: none;
transition: border 0.2s;
}
input[type="text"]:focus {
border-color: var(--green);
box-shadow: 0 0 15px rgba(0, 255, 157, 0.2);
}
button {
background: var(--green);
color: #000;
border: none;
padding: 15px 30px;
font-family: inherit;
font-weight: bold;
font-size: 13px;
border-radius: 8px;
cursor: pointer;
letter-spacing: 1px;
transition: transform 0.1s;
}
button:active { transform: scale(0.98); }

#results { display: flex; flex-direction: column; gap: 12px; }

.result-card {
background: var(--panel);
border: 1px solid var(--border);
border-left: 3px solid var(--cyan);
padding: 16px;
border-radius: 6px;
transition: border-color 0.2s;
}
.result-card:hover { border-left-color: var(--green); }
.result-type {
display: inline-block;
font-size: 9px;
text-transform: uppercase;
letter-spacing: 1px;
color: var(--cyan);
background: rgba(0, 212, 255, 0.1);
padding: 3px 8px;
border-radius: 4px;
margin-bottom: 8px;
}
.result-title {
font-size: 15px;
font-weight: bold;
color: #fff;
margin-bottom: 6px;
}
.result-text {
font-size: 12px;
color: var(--dim);
line-height: 1.5;
}
.result-url {
display: block;
margin-top: 8px;
font-size: 11px;
color: var(--green);
text-decoration: none;
word-break: break-all;
}
.result-url:hover { text-decoration: underline; }

.loader {
text-align: center;
padding: 40px;
color: var(--green);
font-size: 12px;
letter-spacing: 2px;
}
.spinner {
width: 30px; height: 30px;
border: 2px solid var(--border);
border-top-color: var(--green);
border-radius: 50%;
animation: spin 0.8s linear infinite;
margin: 0 auto 15px;
}
@keyframes spin { to { transform: rotate(360deg); } }

.error {
background: rgba(255, 45, 85, 0.1);
border: 1px solid var(--red);
color: var(--red);
padding: 15px;
border-radius: 6px;
font-size: 12px;
}
</style>
</head>
<body>
<div class="container">
<div class="header">
<h1>NEXUS FERTECH</h1>
<div class="subtitle">AGENT DE RECHERCHE LOCAL · DUCKDUCKGO API</div>
<div class="status-bar">
<span><span class="status-dot"></span>SYSTEM ONLINE</span>
<span>PORT: 9400</span>
<span id="time">--:--:--</span>
</div>
</div>

<div class="search-box">
<input type="text" id="query" placeholder="Entrez votre requête..." onkeydown="if(event.key==='Enter') search()">
<button onclick="search()">SCAN</button>
</div>

<div id="results"></div>
</div>

<script>
function updateTime() {
const now = new Date();
document.getElementById('time').textContent = now.toLocaleTimeString('fr-FR');
}
setInterval(updateTime, 1000);
updateTime();

async function search() {
const query = document.getElementById('query').value.trim();
if (!query) return;

const resultsDiv = document.getElementById('results');
resultsDiv.innerHTML = '<div class="loader"><div class="spinner"></div>ANALYSE EN COURS...</div>';

try {
const response = await fetch('/api/search?q=' + encodeURIComponent(query));
const data = await response.json();

if (data.error) {
resultsDiv.innerHTML = '<div class="error">ERREUR : ' + data.error + '</div>';
return;
}

if (!data.results || data.results.length === 0) {
resultsDiv.innerHTML = '<div class="error">AUCUN RÉSULTAT TROUVÉ POUR : ' + query + '</div>';
return;
}

let html = '';
data.results.forEach(r => {
html += '<div class="result-card">';
html += '<div class="result-type">' + r.type + '</div>';
html += '<div class="result-title">' + escapeHtml(r.title) + '</div>';
html += '<div class="result-text">' + escapeHtml(r.text) + '</div>';
if (r.url) html += '<a class="result-url" href="' + r.url + '" target="_blank">' + r.url + '</a>';
html += '</div>';
});
resultsDiv.innerHTML = html;

} catch (e) {
resultsDiv.innerHTML = '<div class="error">ERREUR RÉSEAU : ' + e.message + '</div>';
}
}

function escapeHtml(s) {
return String(s || '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
}
</script>
</body>
</html>
"""

# ═══════════════════════════════════════════════════════════════════
# MOTEUR API DUCKDUCKGO
# ═══════════════════════════════════════════════════════════════════

def search_duckduckgo(query):
"""Interroge l'API publique DuckDuckGo."""
url = f"https://api.duckduckgo.com/?q={urllib.parse.quote(query)}&format=json&no_html=1&skip_disambig=1"

req = urllib.request.Request(url)
req.add_header("User-Agent", "NexusFertech/1.0")

try:
with urllib.request.urlopen(req, timeout=10) as response:
data = json.loads(response.read().decode("utf-8"))
except Exception as e:
return {"error": str(e)}

results = []

# 1. Réponse directe (Abstract)
if data.get("AbstractText"):
results.append({
"type": "Réponse Directe",
"title": data.get("Heading", query),
"text": data["AbstractText"],
"url": data.get("AbstractURL", "")
})

# 2. Sujets connexes (Related Topics)
if data.get("RelatedTopics"):
for topic in data["RelatedTopics"][:10]:
if "Text" in topic:
results.append({
"type": "Sujet Connexe",
"title": topic.get("Name", "Info"),
"text": topic.get("Text", ""),
"url": topic.get("FirstURL", "")
})
elif "Topics" in topic:
for sub in topic["Topics"][:3]:
results.append({
"type": "Sous-Sujet",
"title": sub.get("Name", "Info"),
"text": sub.get("Text", ""),
"url": sub.get("FirstURL", "")
})

# 3. Résultats (Results)
if data.get("Results"):
for r in data["Results"][:5]:
results.append({
"type": "Résultat",
"title": r.get("Text", "")[:60],
"text": r.get("Text", ""),
"url": r.get("FirstURL", "")
})

return {"query": query, "results": results}

# ═══════════════════════════════════════════════════════════════════
# SERVEUR HTTP
# ═══════════════════════════════════════════════════════════════════

class Handler(http.server.BaseHTTPRequestHandler):
def log_message(self, *args):
pass

def _send_json(self, data, code=200):
try:
body = json.dumps(data, ensure_ascii=False).encode("utf-8")
self.send_response(code)
self.send_header("Content-Type", "application/json; charset=utf-8")
self.send_header("Access-Control-Allow-Origin", "*")
self.end_headers()
self.wfile.write(body)
except Exception:
pass

def _send_html(self, html):
try:
body = html.encode("utf-8")
self.send_response(200)
self.send_header("Content-Type", "text/html; charset=utf-8")
self.end_headers()
self.wfile.write(body)
except Exception:
pass

def do_GET(self):
parsed = urllib.parse.urlparse(self.path)
path = parsed.path
qs = urllib.parse.parse_qs(parsed.query)

if path == "/" or path == "/index.html":
self._send_html(HTML_PAGE)

elif path == "/api/search":
query = qs.get("q", [""])[0]
if not query:
self._send_json({"error": "Requête vide"}, 400)
return

print(f"[{datetime.now().strftime('%H:%M:%S')}] 🔍 Scan : {query}")
result = search_duckduckgo(query)
self._send_json(result)

elif path == "/api/health":
self._send_json({"status": "ok", "version": VERSION, "port": PORT})

else:
self._send_json({"error": "Not found"}, 404)

class Server(socketserver.ThreadingMixIn, http.server.HTTPServer):
daemon_threads = True
allow_reuse_address = True

def main():
print("\n" + "="*60)
print(" 🛰️ NEXUS FERTECH — AGENT DDG")
print("="*60)
print(f" URL : http://{HOST}:{PORT}/")
print(f" Status : En écoute...")
print("="*60 + "\n")

try:
with Server((HOST, PORT), Handler) as httpd:
httpd.serve_forever()
except KeyboardInterrupt:
print("\n👋 Agent arrêté.")

if __name__ == "__main__":
main()
