# Nitz Ultimate Cipher Tool - Development Notes

## Project Overview
This is a classical encryption suite built with Python, featuring multiple cipher algorithms and a user-friendly GUI interface.

## Features Implemented
- Caesar Cipher
- Vigenere Cipher
- Other classical encryption methods
- Graphical User Interface (GUI)
- Wordlist integration for enhanced functionality
- Standalone executable distribution

## Technical Details
- **Language**: Python
- **GUI Framework**: Tkinter
- **Build Tool**: PyInstaller
- **Version Control**: Git
- **Hosting**: GitHub

## File Structure
- `cipher_decoder.py` - Main application code
- `embed_wordlist.py` - Wordlist embedding utility
- `words.txt` - Dictionary file
- `dist/` - Built executables
- `build/` - PyInstaller build files
- `*.spec` - PyInstaller specifications

## Build Instructions
1. Install dependencies: `pip install pyinstaller`
2. Run PyInstaller: `pyinstaller --onefile cipher_decoder.py`
3. Executable will be in `dist/` folder

## Distribution
- Source code available on GitHub
- Executable available via GitHub Releases
- Code signed for security

## Developer
- Nitesh Raja Nagalu
- GitHub: @niteshrajanagalu
- Instagram: @nitesh_ig
- Email: niteshrajanaglu@gmail.com

## Future Enhancements
- Additional cipher algorithms
- Cross-platform support
- Advanced encryption modes
- User authentication
- Cloud sync capabilities

## Known Issues
- Windows security warnings (normal for self-signed apps)
- Requires unblocking executable on first run

## License
This project is open source. Please check repository for license details.