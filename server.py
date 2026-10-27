import http.server
import socketserver
import time
import json
import random

PORT = 9003
WORK_DIR = "."

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
            return super().do_GET()
        
        if self.path == '/stream':
            self.send_response(200)
            self.send_header('Content-Type', 'text/event-stream')
            self.send_header('Cache-Control', 'no-cache')
            self.send_header('Connection', 'keep-alive')
            self.end_headers()

            # Simulation du Swarm
            scenarios = [
                {"agent": "Planner", "message": "Analyse de la requête : 'Crée un serveur web'..."},
                {"agent": "Planner", "message": "Plan : 1. Importer http.server 2. Créer un Handler 3. Lancer le serveur."},
                {"agent": "Coder", "message": "Génération du code Python..."},
                {"agent": "Coder", "message": "Code généré (15 lignes). Envoi au Sandbox."},
                {"agent": "Executor", "message": "Exécution sécurisée (timeout=30s)..."},
                {"agent": "Executor", "message": "❌ ERROR: Address already in use (Port 8080)"},
                {"agent": "Reflector", "message": "Échec détecté. Erreur d'architecture. Retry 1/3."},
                {"agent": "Reflector", "message": "Injection de l'erreur dans le contexte."},
                {"agent": "Coder", "message": "Correction du code (changement de port vers 8081)."},
                {"agent": "Executor", "message": "Exécution sécurisée (timeout=30s)..."},
                {"agent": "Executor", "message": "✅ SUCCESS. Serveur en écoute sur le port 8081."},
                {"agent": "Reflector", "message": "Analyse de la sortie : OK."},
                {"agent": "Reflector", "message": "💾 Mémorisation de la tâche réussie dans ChromaDB."},
                {"agent": "Reflector", "message": "🏁 Tâche accomplie. Statut: DONE."},
            ]

            try:
                for step in scenarios:
                    time.sleep(2) # Pause pour l'effet visuel
                    data = json.dumps(step)
                    self.wfile.write(f"data: {data}\n\n".encode())
                    self.wfile.flush()
            except Exception:
                pass
            return

        self.send_error(404)

print(f"🚀 Serveur de simulation Swarm actif sur http://localhost:{PORT}")
print("Ouvre ton navigateur et regarde les agents travailler.\n")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
