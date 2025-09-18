# Honeypot

## Table of Contents

* [Overview](#overview)
* [Objectives](#key-objectives)
* [Architecture](#architecture)
* [Phase 1](#phase-1)
* [Phase 2](#phase-2)

### Overview

This project involved the deployment and analysis of a modern, multi-service honeypot platform to actively monitor and study malicious activity on the internet. The primary goal was to gain firsthand experience with attacker Tactics, Techniques, and Procedures (TTPs), collect Indicators of Compromise (IOCs), and understand the value of threat intelligence in a defensive security strategy.

The honeypot suite was deployed on a cloud server, presenting a vulnerable attack surface to the internet. All inbound connection attempts were logged, analyzed, and visualized to provide insights into the current threat landscape.

### Key Objectives

- Gain Practical Security Experience: Move from theoretical security concepts to hands-on interaction with live attacker traffic.
- Threat Intelligence Gathering: Collect real-world data on attacker IPs, tools, and methodologies.
- Data Analysis & Visualization: Correlate and visualize attack data to identify patterns and trends.
- Understand Attack Motivations: Analyze what services attackers are most interested in and why.

### Architecture

The project leverages T-Pot, a popular all-in-one honeypot platform based on Docker. T-Pot combines multiple excellent honeypot projects into a single, manageable system, complete with the Elastic Stack (ELK) for logging and visualization.

#### Phase 1

1. I chose a low-cost cloud Virtual Private Server (VPS) provider. A cloud server is ideal as it is isolated from my personal network and has a public IP address.
2. I spun up a new Ubuntu 22.04 LTS server with at least 4GB RAM and 2 CPU cores to ensure smooth operation of the resource-intensive ELK stack.
3. Before deploying the honeypot, I performed basic server hardening:
   - Created a non-root user with sudo privileges.
   - Configured a firewall (UFW) to allow only SSH access from my personal IP address and allowed all other inbound traffic to the honeypot ports.
   - Installed and configured fail2ban for the SSH service to protect the management port.

#### Phase 2




