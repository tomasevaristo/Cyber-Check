# Cyber Hygiene Checklist CLI Tool

A simple command-line tool to perform basic cyber hygiene checks on macOS (with support for antivirus detection, firewall status, and automatic updates). This project helps you quickly assess your system’s security posture.

## Features

- **Antivirus Detection**: Scans `/Applications` for known AV vendors and checks for macOS XProtect definitions.
- **Firewall Status**: Queries the built-in Application Firewall via `socketfilterfw`.
- **Automatic Updates**: Reads the software update schedule using `softwareupdate --schedule`.
- **Flexible Output**: Print results to the console with icons or export to JSON/text file.

## Installation

### From PyPI (future)

```bash
pip install cyber-hygiene
```

*(Note: available after publishing on PyPI)*

### Directly from GitHub

```bash
git clone git@github.com:tomasevaristo/Cyber-Check.git
cd Cyber-Check
pip install .
```
## Quick Start

After installation, the `cyber-hygiene` command becomes available:

```bash
# Show help and options
cyber-hygiene --help

# Run default checks
cyber-hygiene

# Export results to JSON
cyber-hygiene --output result.json --format json
```

## Usage

```bash
usage: cyber-hygiene [-h] [-o OUTPUT] [-f {text,json}]

Cyber Hygiene Checklist CLI Tool

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        path to output file (optional)
  -f {text,json}, --format {text,json}
                        output format: text or json
```

## Configuration & Extensibility

- **Add new checks**: In `CyberCheckScript.py`, define a function returning `(bool, str)` and register it in `CHECKS`.
- **Multi-platform**: Implement OS-specific checks under `if sys.platform == ...`
- **Verbose/Quiet modes**: Add flags and use Python’s `logging` module.

## Print Screens 
<img width="682" alt="Screenshot 2025-05-16 at 14 23 35" src="https://github.com/user-attachments/assets/db11e384-5e77-4ac9-b085-99f5888b7f21" />
<img width="682" alt="Screenshot 2025-05-16 at 14 24 30" src="https://github.com/user-attachments/assets/d3c30267-fe29-484f-a046-06f7facbb5ca" />

## License

This project is licensed under the MIT License. See the [LICENSE](/LICENSE) file for details.
