# Nitz Ultimate Cipher Tool 🔐

A comprehensive classical encryption suite built with Python, featuring multiple cipher algorithms and a user-friendly GUI interface.

![Cipher Tool Banner](src/Classical%20Encryption%20Suite%20Banner%20Gothic%20Font.png)

## ✨ Features

- **Multiple Ciphers**: Supports Caesar, Vigenere, and other classical encryption methods
- **GUI Interface**: Easy-to-use graphical interface for encryption/decryption
- **Wordlist Integration**: Embedded wordlist for enhanced functionality
- **Standalone Executable**: No installation required - just download and run
- **AI-Enhanced UI**: Interface designed with Kilo Code AI assistance
- **Code Signed**: Professional code signing through Codegic

## 🚀 Quick Start

### Download the App
1. Go to [Releases](https://github.com/niteshrajanagalu/CipherApp/releases)
2. Download `Nitz Ultimate Cipher Tool.exe`
3. Run the executable directly

### For Developers
```bash
# Clone the repository
git clone https://github.com/niteshrajanagalu/CipherApp.git

# Install dependencies
pip install pyinstaller

# Build executable
pyinstaller --onefile src/cipher_decoder.py
```

## 📋 System Requirements

- **Operating System**: Windows 10/11
- **No additional dependencies** for the executable version

## 🛠️ Usage

1. Launch the application
2. Select your desired cipher algorithm
3. Enter your message and key
4. Choose encrypt or decrypt
5. View the result

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
```

## 🏆 CI/CD Pipeline

This project features a comprehensive CI/CD pipeline:

- ✅ **Python CI**: Multi-version testing (3.8-3.11)
- ✅ **CodeQL Security**: Automated vulnerability scanning
- ✅ **Dependency Review**: Security checks for dependencies
- ✅ **Auto-merge**: Automated Dependabot PR merging
- ✅ **Stale Management**: Automated issue/PR cleanup

## 🔧 Technical Details

- **Language**: Python 3.x
- **GUI Framework**: Tkinter
- **Build Tool**: PyInstaller
- **Version Control**: Git
- **Hosting**: GitHub
- **AI Assistance**: Kilo Code AI for UI design
- **Code Signing**: Codegic professional certification

## 👨‍💻 Developer

**Nitesh Raja Nagalu**
- GitHub: [@niteshrajanagalu](https://github.com/niteshrajanagalu)
- Instagram: [@nitesh_ig](https://www.instagram.com/nitesh_ig/)
- Email: niteshrajanaglu@gmail.com

## 🤝 Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## 📜 Security Note

This executable is code-signed by Codegic for trusted distribution. If Windows shows a security warning:
1. Right-click the downloaded file
2. Select "Properties"
3. Check "Unblock" in the General tab
4. Click "Apply" then "OK"

## 📄 License

This project is open source. Please check the repository for license details.

## ⭐ Support

For questions, bug reports, or feature requests:
- Create an [issue](https://github.com/niteshrajanagalu/CipherApp/issues) on GitHub
- Contact the developer directly

---

⭐ **Star this repository** if you find it useful!
