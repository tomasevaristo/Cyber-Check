import argparse
import json
import os
import subprocess
import sys

# List of common antivirus vendors for detection in application names
AV_VENDORS = [
    "bitdefender", "norton", "kaspersky", "avast", "avg",
    "sophos", "malwarebytes", "intego", "clamxav"
]


def check_antivirus():
    """
    Checks if a known antivirus application is installed under /Applications,
    or if macOS XProtect definitions exist.

    Returns: (status: bool, info: str)
    """
    # 1. Scan /Applications for known AV vendor names
    try:
        apps = os.listdir('/Applications')
        for app in apps:
            name_lower = app.lower()
            for vendor in AV_VENDORS:
                if vendor in name_lower:
                    return True, f'{app} detected'
    except Exception:
        pass

    # 2. Check macOS built-in XProtect definitions as fallback
    xprotect_paths = [
        '/System/Library/CoreServices/XProtect.bundle',
        '/var/db/xprotect'
    ]
    for path in xprotect_paths:
        if os.path.exists(path):
            return True, f'XProtect detected at {path}'

    # No antivirus found
    return False, 'No antivirus detected'


def check_firewall():
    """
    Checks if the macOS Application Firewall is enabled using socketfilterfw.

    Returns: (status: bool, info: str)
    """
    cmd = ['/usr/libexec/ApplicationFirewall/socketfilterfw', '--getglobalstate']
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        output = result.stdout.strip().lower()
        if 'state = 1' in output or 'enabled' in output:
            return True, 'Application Firewall is enabled'
        if 'state = 0' in output or 'disabled' in output:
            return False, 'Application Firewall is disabled'
        return None, f'Unexpected output: {output}'
    except FileNotFoundError:
        return None, 'socketfilterfw not found'
    except Exception as e:
        return None, f'Error detecting firewall: {e}'


def check_updates():
    """
    Checks if automatic software update schedule is enabled via softwareupdate.

    Returns: (status: bool, info: str)
    """
    cmd = ['softwareupdate', '--schedule']
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        output = result.stdout.strip().lower()
        # Detect 'disabled' explicitly
        if 'disabled' in output:
            return False, 'Automatic updates are disabled'
        # Look for 'enabled', 'turned on', or standalone 'on'
        if 'enabled' in output or 'turned on' in output or ' on' in output:
            return True, 'Automatic updates are enabled'
        return None, f'Unexpected output: {output}'
    except FileNotFoundError:
        return None, 'softwareupdate tool not found'
    except Exception as e:
        return None, f'Error detecting updates: {e}'


# List of checks: each tuple is (description, check_function)
CHECKS = [
    ('Antivirus', check_antivirus),
    ('Application Firewall', check_firewall),
    ('Automatic Software Updates', check_updates),
]


def run_checks():
    """
    Executes all checks and returns a list of results.
    """
    results = []
    for description, func in CHECKS:
        status, info = func()
        results.append({
            'description': description,
            'status': status,
            'info': info
        })
    return results


def print_results(results):
    """
    Displays results in the terminal with icons.
    """
    for result in results:
        status = result['status']
        icon = '✔️' if status else ('⚠️' if status is False else '❓')
        print(f"[{icon}] {result['description']} — {result['info']}")


def save_results(results, filename, fmt):
    """
    Saves results to a file (text or JSON).
    """
    with open(filename, 'w', encoding='utf-8') as f:
        if fmt == 'json':
            json.dump(results, f, ensure_ascii=False, indent=2)
        else:
            for r in results:
                status_str = 'OK' if r['status'] else ('WARN' if r['status'] is False else 'UNKNOWN')
                f.write(f"{status_str}: {r['description']} — {r['info']}\n")


def parse_args():
    parser = argparse.ArgumentParser(
        description='Cyber Hygiene Checklist CLI Tool'
    )
    parser.add_argument(
        '-o', '--output',
        help='Path to output file (optional)',
        default=None
    )
    parser.add_argument(
        '-f', '--format',
        help='Output format: text or json',
        choices=['text', 'json'],
        default='text'
    )
    return parser.parse_args()


def main():
    args = parse_args()
    results = run_checks()
    print_results(results)
    if args.output:
        save_results(results, args.output, args.format)
        print(f"Results saved to {args.output} (format: {args.format})")


if __name__ == '__main__':
    main()
