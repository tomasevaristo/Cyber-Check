# Cyber-Check
A simple command-line tool to perform basic cyber hygiene checks on macOS (with support for antivirus detection, firewall status, and automatic updates). This project aims to help users quickly assess the security posture of their system.
Features

Antivirus Detection: Scans /Applications for known AV vendors and checks for macOS XProtect definitions.

Firewall Status: Queries the built-in Application Firewall via socketfilterfw.

Automatic Updates: Reads the software update schedule using softwareupdate --schedule.

Flexible Output: Print results to the console with icons or export to JSON/text file.

Quick Start

Clone the repository

git clone https://github.com/yourusername/cyber-hygiene-checklist.git
cd cyber-hygiene-checklist/cli

Install requirements (if any external libraries are added)

pip install -r ../requirements.txt

Run the script

python3 cyber_check.py

Export results

python3 cyber_check.py --output result.json --format json

Usage

usage: cyber_check.py [-h] [-o OUTPUT] [-f {text,json}]

Cyber Hygiene Checklist CLI Tool

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Path to output file (optional)
  -f {text,json}, --format {text,json}
                        Output format: text or json

Extending Checks

Add new checks: In cyber_check.py, add a function that returns (bool, str) and register it in CHECKS.

Linux/Windows support: Implement OS-specific detection in new functions and conditionally include them.

Contributing

See CONTRIBUTING.md for guidelines on submitting issues and pull requests.

License

This project is licensed under the MIT License — see the LICENSE file for details.

Badges


