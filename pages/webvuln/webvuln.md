# Web Vulnerability Scanner

## Table of Contents

* [Overview](#overview)

### Overview

A Python-based automated security testing tool designed to identify common web application vulnerabilities from the **OWASP Top 10**. This scanner demonstrates core penetration testing methodologies, including fuzzing, payload injection, and response analysis.

## 🚀 Features

- **SQL Injection (SQLi) Detection:** Tests for both error-based and union-based SQL injection vulnerabilities in GET parameters.
- **Cross-Site Scripting (XSS) Detection:** Fuzzes parameters with a suite of payloads designed to bypass simple filters.
- **Custom Payload Support:** Easily extensible payload lists for SQLi and XSS in separate `.txt` files.
- **Configurable Target Scanning:** Specify a single URL or provide a file with a list of URLs for batch scanning.
- **Response Analysis:** Uses regex patterns and string matching to identify potential vulnerabilities in server responses.
- **Reporting:** Outputs clear, color-coded findings to the console for immediate analysis.

## 🛠️ Installation & Usage

### Prerequisites
- **Python 3.8 or higher**
- The `requests` library.

Install the required dependency using pip:
```bash
pip install requests
```

### Project Implementation

#### Phase 1: Research & Design

1. Studied how popular tools like sqlmap and Burp Suite Intruder operate to inform my design choices.
2. Designed the script flow: Parse Input -> Load Payloads -> Fuzz Parameters -> Analyze Response -> Report Findings.

#### Phase 2: Core Development

1. Initialized a Python project and installed the requests library for robust HTTP handling.
2. Implemented the argparse module to handle user input for single URLs (-u) or wordlists (-l).
3. Created two foundational payload files:
   - sql_payloads.txt: Contains classic test strings like ', ' OR '1'='1, and UNION SELECT NULL--.
   - xss_payloads.txt: Contains simple and polyglot payloads like <script>alert(1)</script> and "><img src=x onerror=alert(1)>.

4. Built the fuzz_url function which:
   - Parses a URL to isolate its parameters.
   - Iterates over each parameter, injecting every payload from the lists.
   - Sends a HTTP GET request for each fuzzed parameter and captures the response.

5. Developed the check_sql_injection and check_xss functions. These functions use a combination of:
   - To find common SQL error messages (e.g., You have an error in your SQL syntax) or successful XSS execution.
   - To detect successful UNION-based SQL injections (NULLNULL) or the presence of our XSS payload in the response.

Code Snippet from scanner.py: 
```python
#!/usr/bin/env python3
"""
Web Vulnerability Scanner
Author: Sharukh Khan
Description: A simple scanner to detect SQL Injection and XSS vulnerabilities.
"""
```
