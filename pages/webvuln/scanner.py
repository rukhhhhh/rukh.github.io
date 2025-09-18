import argparse
import requests
import urllib.parse
from urllib.parse import urlparse, urlencode, parse_qs
import re
from colorama import Fore, Style, init

# Initialize colorama for cross-platform colored text
init(autoreset=True)

# Banner
def print_banner():
    banner = f"""
    {Fore.RED}╦ ╦╔═╗╦╔═╔═╗╔╦╗╔═╗  ╔╗╔╔═╗╔╦╗╔═╗╦  ╦╔═╗╦╔╗╔╔═╗
    {Fore.RED}║ ║╠═╝╠╩╗║╣ ║║║║╣   ║║║║╣ ║║║╠═╝║  ║╠═╝║║║║║ ╦
    {Fore.RED}╚═╝╩  ╩ ╩╚═╝╩ ╩╚═╝  ╝╚╝╚═╝╩ ╩╩  ╩═╝╩╩  ╩╝╚╝╚═╝
    {Style.BRIGHT}{Fore.CYAN}        OWASP Top 10 - SQLi & XSS Fuzzer
    """
    print(banner)

# Load payloads from a file
def load_payloads(file_path):
    # Reads payloads from a given file and returns a list.
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            payloads = [line.strip() for line in file if line.strip()]
        return payloads
    except FileNotFoundError:
        print(f"{Fore.RED}[ERROR] Payload file not found: {file_path}")
        return []

# Check responses for SQL Injection clues
def check_sql_injection(response, payload):
    # Analyzes the HTTP response for indications of a SQL injection vulnerability.
    # Common SQL error messages patterns
    error_patterns = [
        r"you have an error in your sql syntax",
        r"warning: mysql",
        r"unclosed quotation mark",
        r"quoted string not properly terminated",
        r"sqlcommand",
        r"unknown column",
        r"union.*select"
    ]

    # Check if the payload is reflected in the response (basic check for UNION-based)
    if payload in response.text:
        # Simple check for a common UNION-based injection pattern
        if "NULLNULL" in response.text:
            return True

    # Check for any of the error patterns
    for pattern in error_patterns:
        if re.search(pattern, response.text, re.IGNORECASE):
            return True

    return False

# Check responses for XSS clues
def check_xss(response, payload):
    # Analyzes the HTTP response for indications of a successful XSS injection.
    # Check if the payload is reflected unsanitized in the HTML
    # This is a basic check and can produce false positives
    if payload in response.text:
        # Look for the payload outside of script tags (indicating it might be executed)
        if re.search(rf"<script[^>]*>{re.escape(payload)}", response.text, re.IGNORECASE):
            return True
        # Look for common XSS vectors like onerror, src, etc.
        if re.search(rf"(onerror|onload|src)=[^>]*{re.escape(payload)}", response.text, re.IGNORECASE):
            return True
    return False

# The core fuzzing function
def fuzz_url(url, sql_payloads, xss_payloads):
    print(f"\n{Fore.YELLOW}[INFO] Fuzzing URL: {url}")

    # Parse the URL to get its components
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)

    # If the URL has no parameters, skip it.
    if not query_params:
        print(f"{Fore.CYAN}[INFO] No parameters to fuzz in URL: {url}")
        return

    # Test each parameter individually
    for param in query_params:
        print(f"{Fore.MAGENTA}[TESTING] Parameter: {param}")

        # Test SQLi payloads
        for payload in sql_payloads:
            # Create a new set of parameters with the fuzzed value
            fuzzed_params = query_params.copy()
            fuzzed_params[param] = [payload] # Override the parameter with the payload

            # Reconstruct the full URL with the fuzzed parameters
            new_query = urlencode(fuzzed_params, doseq=True)
            fuzzed_url = urllib.parse.urlunparse((
                parsed_url.scheme,
                parsed_url.netloc,
                parsed_url.path,
                parsed_url.params,
                new_query,
                parsed_url.fragment
            ))

            try:
                # Send the HTTP request
                response = requests.get(fuzzed_url, timeout=5)
                if check_sql_injection(response, payload):
                    print(f"{Fore.GREEN}[VULNERABLE - SQLi] {fuzzed_url}")
                    print(f"   Payload: {payload}")
            except requests.exceptions.RequestException as e:
                print(f"{Fore.RED}[ERROR] Request failed for {fuzzed_url}: {e}")
                continue

        # Test XSS payloads
        for payload in xss_payloads:
            fuzzed_params = query_params.copy()
            fuzzed_params[param] = [payload]

            new_query = urlencode(fuzzed_params, doseq=True)
            fuzzed_url = urllib.parse.urlunparse((
                parsed_url.scheme,
                parsed_url.netloc,
                parsed_url.path,
                parsed_url.params,
                new_query,
                parsed_url.fragment
            ))

            try:
                response = requests.get(fuzzed_url, timeout=5)
                if check_xss(response, payload):
                    print(f"{Fore.GREEN}[VULNERABLE - XSS] {fuzzed_url}")
                    print(f"   Payload: {payload}")
            except requests.exceptions.RequestException as e:
                print(f"{Fore.RED}[ERROR] Request failed for {fuzzed_url}: {e}")
                continue

def main():
    print_banner()

    parser = argparse.ArgumentParser(description="Web Vulnerability Scanner for SQLi and XSS")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-u", "--url", help="Single URL to scan")
    group.add_argument("-l", "--list", help="File containing a list of URLs to scan")

    args = parser.parse_args()

    # Load the payloads
    sql_payloads = load_payloads("sql_payloads.txt")
    xss_payloads = load_payloads("xss_payloads.txt")

    if not sql_payloads or not xss_payloads:
        print(f"{Fore.RED}[ERROR] Could not load payloads. Exiting.")
        return

    targets = []

    # Get the list of target URLs
    if args.url:
        targets = [args.url]
    elif args.list:
        try:
            with open(args.list, 'r') as f:
                targets = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            print(f"{Fore.RED}[ERROR] File not found: {args.list}")
            return

    # Fuzz each target URL
    for target_url in targets:
        fuzz_url(target_url, sql_payloads, xss_payloads)

if __name__ == "__main__":
    main()
