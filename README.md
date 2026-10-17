<svg viewBox="0 0 1200 800" xmlns="http://www.w3.org/2000/svg">
  <!-- Background -->
  <defs>
    <linearGradient id="bg-gradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#0d1117;stop-opacity:1"/>
      <stop offset="100%" style="stop-color:#161b22;stop-opacity:1"/>
    </linearGradient>
    
    <filter id="glow">
      <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    
    <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#6d4aff"/>
    </marker>
  </defs>
  
  <rect width="1200" height="800" fill="url(#bg-gradient)"/>
  
  <!-- Title -->
  <text x="600" y="60" text-anchor="middle" fill="#fff" font-family="Inter, Segoe UI, sans-serif" font-size="32" font-weight="bold">
    NEXUS ARCHON WORKFLOW
  </text>
  <text x="600" y="90" text-anchor="middle" fill="#8b949e" font-size="16">
    Agent Autonome de Validation et Correction de Code
  </text>
  
  <!-- Stage 1: DETECTION -->
  <rect x="50" y="130" width="300" height="280" rx="12" fill="#21262d" stroke="#30363d" stroke-width="2"/>
  <text x="200" y="165" text-anchor="middle" fill="#6d4aff" font-size="18" font-weight="bold">1. DÉTECTION</text>
  
  <rect x="80" y="190" width="240" height="60" rx="8" fill="#0d1117" stroke="#30363d"/>
  <text x="200" y="225" text-anchor="middle" fill="#c9d1d9" font-size="14">CodeQL + AST</text>
  
  <rect x="80" y="270" width="240" height="60" rx="8" fill="#0d1117" stroke="#30363d"/>
  <text x="200" y="305" text-anchor="middle" fill="#c9d1d9" font-size="14">Semgrep + Regex</text>
  
  <rect x="80" y="350" width="240" height="60" rx="8" fill="#0d1117" stroke="#30363d"/>
  <text x="200" y="385" text-anchor="middle" fill="#c9d1d9" font-size="14">Dependabot + Snyk</text>
  
  <!-- Arrow 1→2 -->
  <line x1="350" y1="270" x2="410" y2="270" stroke="#6d4aff" stroke-width="3" marker-end="url(#arrowhead)"/>
  <text x="380" y="265" text-anchor="middle" fill="#8b949e" font-size="12">Flux</text>
  
  <!-- Stage 2: VÉRIFICATION QUANTIQUE -->
  <rect x="450" y="130" width="300" height="280" rx="12" fill="#21262d" stroke="#30363d" stroke-width="2"/>
  <text x="600" y="165" text-anchor="middle" fill="#6d4aff" font-size="18" font-weight="bold">2. VÉRIFICATION</text>
  
  <rect x="480" y="190" width="240" height="70" rx="8" fill="#1f6feb20" stroke="#1f6feb" stroke-dasharray="5,3">
    <animate attributeName="stroke-opacity" values="0.6;0.9;0.6" dur="3s" repeatCount="indefinite"/>
  </rect>
  <text x="600" y="225" text-anchor="middle" fill="#58a6ff" font-size="14" font-weight="bold">Qiskit Simulator</text>
  <text x="600" y="245" text-anchor="middle" fill="#8b949e" font-size="11">(Simulation quantique)</text>
  
  <rect x="480" y="280" width="240" height="70" rx="8" fill="#0d1117" stroke="#30363d"/>
  <text x="600" y="315" text-anchor="middle" fill="#c9d1d9" font-size="14">Vérification Bayésienne</text>
  
  <!-- Arrow 2→3 -->
  <line x1="750" y1="270" x2="810" y2="270" stroke="#6d4aff" stroke-width="3" marker-end="url(#arrowhead)"/>
  
  <!-- Stage 3: ACTION -->
  <rect x="850" y="130" width="300" height="280" rx="12" fill="#21262d" stroke="#30363d" stroke-width="2"/>
  <text x="1000" y="165" text-anchor="middle" fill="#6d4aff" font-size="18" font-weight="bold">3. ACTION</text>
  
  <rect x="880" y="190" width="240" height="80" rx="8" fill="#0d1117" stroke="#30363d"/>
  <text x="1000" y="225" text-anchor="middle" fill="#c9d1d9" font-size="14">Autofix PR</text>
  <text x="1000" y="245" text-anchor="middle" fill="#8b949e" font-size="11">Correction automatique</text>
  
  <rect x="880" y="290" width="240" height="60" rx="8" fill="#0d1117" stroke="#30363d"/>
  <text x="1000" y="325" text-anchor="middle" fill="#c9d1d9" font-size="14">Rapport Détaillé</text>
  
  <!-- Stage 4: DÉCISION -->
  <rect x="50" y="480" width="1100" height="280" rx="12" fill="#161b22" stroke="#30363d" stroke-width="2"/>
  <text x="600" y="515" text-anchor="middle" fill="#6d4aff" font-size="18" font-weight="bold">4. DÉCISION AUTONOME</text>
  
  <text x="600" y="545" text-anchor="middle" fill="#8b949e" font-size="14">Score global calculé à partir de 12 métriques</text>
  
  <!-- Score meter -->
  <rect x="300" y="570" width="600" height="40" rx="8" fill="#21262d"/>
  <rect x="310" y="580" width="480" height="20" rx="4" fill="url(#score-gradient)">
    <defs>
      <linearGradient id="score-gradient" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" style="stop-color:#da3610"/>
        <stop offset="50%" style="stop-color:#d29922"/>
        <stop offset="100%" style="stop-color:#238636"/>
      </linearGradient>
    </defs>
  </rect>
  
  <!-- Threshold markers -->
  <line x1="450" y1="560" x2="450" y2="620" stroke="#da3610" stroke-dasharray="4,4"/>
  <text x="450" y="635" text-anchor="middle" fill="#da3610" font-size="12">&lt; 50 ❌ REJET</text>
  
  <line x1="600" y1="560" x2="600" y2="620" stroke="#d29922" stroke-dasharray="4,4"/>
  <text x="600" y="635" text-anchor="middle" fill="#d29922" font-size="12">= 50-80 ⚠️ MANUEL</text>
  
  <line x1="750" y1="560" x2="750" y2="620" stroke="#238636" stroke-dasharray="4,4"/>
  <text x="750" y="635" text-anchor="middle" fill="#238636" font-size="12">&gt; 80 ✅ AUTORISÉ</text>
  
  <!-- Footer -->
  <text x="600" y="780" text-anchor="middle" fill="#8b949e" font-size="12">
    © 2026 NEXUS ARCHON — Licence MIT • Déployez dans .github/workflows/
  </text>
</svg>
# NEXUS ARCHON

**Agent autonome de validation, correction et rapport de code**

> *"Votre équipe QA qui ne dort jamais, ne fait pas de pause café, et apprend de chaque PR."*

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![NEXUS](https://img.shields.io/badge/NEXUS-ARCHON-purple)](https://github.com/nexus/archon)
[![Actions](https://github.com/nexus/archon/workflows/NEXUS%20ARCHON/badge.svg)](#)

---

## 📖 Sommaire

1. [Concept](#-concept)
2. [Architecture](#-architecture)
3. [Installation](#-installation)
4. [Configuration](#-configuration)
5. [Workflow GitHub Actions](#-workflow-github-actions)
6. [Scores & Décisions](#-scores--décisions)
7. [Limites & Transparence](#-limites--transparence)
8. [Roadmap](#-roadmap)
9. [Contribuer](#-contribuer)

---

## 🎯 Concept

NEXUS ARCHON est un **agent autonome** qui s'intègre directement dans votre flux GitHub. Il ne se contente pas de détecter des problèmes — il les comprend, les priorise, propose des correctifs, et **prend des décisions** selon des règles configurables.

**Ce que NEXUS ARCHON n'est PAS :**
- ❌ Un simple linter supplémentaire
- ❌ Un bot qui spamme des commentaires
- ❌ Une boîte noire magique

**Ce que NEXUS ARCHON EST :**
- ✅ Un **orchestrateur** qui combine CodeQL, Semgrep, Dependabot, Snyk + vérifications personnalisées
- ✅ Un **correcteur autonome** capable de soumettre des PR de fix automatiques
- ✅ Un **rapporteur transparent** qui explique ses décisions avec des scores chiffrés
- ✅ Un **agent bayésien** qui affine ses critères à chaque PR traitée

---

## 🏗 Architecture

### Flux de traitement

┌─────────────────────────────────────────────────────────────────────┐ │ NEXUS ARCHON │ ├─────────────────────────────────────────────────────────────────────┤ │ │ │ [PR Open] → [DÉTECTION] → [VÉRIFICATION] → [ACTION] → [DECISION] │ │ ↓ ↓ ↓ ↓ │ │ CodeQL Qiskit Autofix Score ≥ 80 │ │ Semgrep Bayesian Rapport Merge ✅ │ │ Snyk+Deps ↓ │ │ └──────────→ Score < 50│ │ Reject ❌ │ │ │ └─────────────────────────────────────────────────────────────────────┘

### Composants

| Module | Rôle | Technologie |
|--------|------|-------------|
| **Détection** | Analyse statique + dépendances | CodeQL, Semgrep, Dependabot, Snyk |
| **Vérification** | Validation probabiliste | Qiskit (simulation), Bayes Net |
| **Action** | Correction auto + rapport | Python scripts + Templates |
| **Décision** | Score global + règles | Scoring engine configurable |

---

## 📥 Installation

### Option 1 : Déploiement rapide (recommandé)

```bash
# Clonez le dépôt
git clone https://github.com/your-org/nexus-archon.git
cd nexus-archon

# Copiez le workflow
cp .github/workflows/nexus-archon.yml .github/workflows/

# Personnalisez la configuration
cp config/default.yaml config/project.yaml
nano config/project.yaml

# Activer dans votre repo
git add .github/config/
git commit -m "feat: configure NEXUS ARCHON"
git push origin main
Option 2 : Via Marketplace GitHub

    Allez dans Settings → Actions → Workflow Marketplace
    Cherchez "NEXUS ARCHON"
    Cliquez sur Configure
    Validez le workflow

⚙️ Configuration
Fichier config/project.yaml
# Configuration NEXUS ARCHON

name: Nexus Archon
version: 1.0.0

# --- Détection ---
detection:
  codeql:
    enabled: true
    languages: [python, javascript, typescript]
    queries: [security-and-quality]
  
  semgrep:
    enabled: true
    configs:
      - p/python
      - p/security-audit
  
  dependabot:
    enabled: true
    schedule: daily
    open-pull-requests-limit: 10
  
  snyk:
    enabled: true
    severity-threshold: HIGH

# --- Vérification ---
verification:
  quantum_simulator:
    enabled: false  # True pour simulation Qiskit (nécessite accès quantique)
    qubits: 12
    shots: 1000
  
  bayesian:
    enabled: true
    priors:
      security: 0.85
      quality: 0.80
      performance: 0.75

# --- Action ---
action:
  autofix:
    enabled: true
    max-auto-prs-per-day: 5
    requires-review: false  # Set true si vous voulez validation humaine
    
  reporting:
    format: markdown
    include-recommendations: true
    include-fix-suggestions: true

# --- Décision ---
decision:
  thresholds:
    auto-merge: 80
    manual-review: 50
    auto-reject: 50
  
  weights:
    security: 0.35
    code-quality: 0.30
    dependencies: 0.20
    performance: 0.15
