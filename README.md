## 📁 Project Structure

```
CipherApp/
├── README.md                           # Main documentation
├── .github/
│   ├── workflows/
│   │   ├── python-ci.yml              # CI/CD pipeline
│   │   ├── codeql-analysis.yml        # Security scanning
│   │   ├── dependency-review.yml      # Dependency checks
│   │   ├── auto-merge.yml             # Auto-merge Dependabot
│   │   └── stale.yml                  # Issue management
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug-report.yml             # Bug report template
│   │   └── feature-request.yml        # Feature request template
│   ├── PULL_REQUEST_TEMPLATE.md       # PR template
│   └── dependabot.yml                 # Auto-updates
├── src/
│   ├── cipher_decoder.py              # Main application
│   ├── embed_wordlist.py              # Wordlist utility
│   └── words.txt                      # Data file
├── docs/
│   └── notes.md                       # Development notes
├── assets/
│   └── Classical Encryption Suite Banner Gothic Font.png
└── DevAssets/
    ├── cipher_decoder.py              # Development copy
    └── embed_wordlist.py              # Development copy
