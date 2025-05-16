# Cyber-Check
A simple command-line tool to perform basic cyber hygiene checks on macOS (with support for antivirus detection, firewall status, and automatic updates). This project aims to help users quickly assess the security posture of their system.
# Features

**Antivirus Detection:** Scans /Applications for known AV vendors and checks for macOS XProtect definitions.

**Firewall Status:** Queries the built-in Application Firewall via socketfilterfw.

**Automatic Updates:** Reads the software update schedule using softwareupdate --schedule.

**Flexible Output:** Print results to the console with icons or export to JSON/text file.

# Quick Start

1. **Clone the repository**

   ```bash
   git clone https://github.com/tomasevaristo/Cyber-Check.git
   cd Cyber-Check

2. **Install requirements (if any external libraries are added)**

     ```bash
    pip install -r ../requirements.txt

3. **Run the script**

     ```bash
    python3 CyberCheckScript.py

 4. **Export results (If you want)**

     ```bash
    python3 CyberCheckScript.py --output result.json --format json


