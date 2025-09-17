# Simple Port Scanner — Joshua-hub-tech

**A small, beginner-friendly TCP port scanner written in Python.**
Use this tool only on systems you own or have explicit permission to test.

## Features
- Scans a list or range of TCP ports.
- Uses threads for faster scanning.
- Saves results to `example_output.txt`.

## Files
- `scanner.py` — the scanner script.
- `example_output.txt` — sample output from a local scan.
- `README.md` — this file.
- `LICENSE` — MIT license.
- `.gitignore` — ignores __pycache__.

## Usage (quick)
1. Make sure you have Python 3.8+ installed.
2. From a terminal, run:
   ```bash
   python3 scanner.py --host example.com --start 1 --end 1024 --threads 100
   ```
   Or scan specific ports:
   ```bash
   python3 scanner.py --host 192.168.1.10 --ports 22,80,443
   ```

## Notes & Responsible Use
**Only** scan systems you own or have written permission to test. Unauthorized scanning can be illegal and unethical.
Include this repository's URL in any reports and always follow a responsible disclosure policy.

## Want this as a GitHub repo?
1. Download the ZIP included with this project.
2. Create a new repository on GitHub and upload the files (or push using git — see below).
3. Pin the repo to your profile.

### Git push example (if you want to use command-line git)
```bash
git init
git add .
git commit -m "Initial commit — simple port scanner"
git branch -M main
git remote add origin git@github.com:Joshua-hub-tech/port-scanner.git
git push -u origin main
```

If you prefer, I can generate the full repo with README and commits for you to copy-paste. Tell me which option you want next.
