# Nibbles Write-Up

## Table of Contents

* [Overview](#overview)
* [Enumeration](#enumeration)

### Overview

This is write-up on Nibbles, there are 2 identifiable methods of exploitation. 1 with metasploit and 1 without. This serves as an experience and knowledge bank for me!
The vulnerability to be exploited is **CVE-2015-6967: Nibbleblog 4.0.3 - Arbitrary File Upload (Metasploit)**<br>
It allows an authenticated attacker to exploit an arbitrary file upload flaw, enabling the execution of malicious PHP code on the server. 
This vulnerability is particularly dangerous as it can lead to remote code execution which will be demonstrated below.

### Enumeration

The first step is to get an idea of the available open ports and the services running. <br>
We run a basic nmap scan to see if we get any hits. <br>


