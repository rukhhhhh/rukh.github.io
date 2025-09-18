# Honeypot

## Table of Contents

* [Overview](#overview)
* [Objectives](#key-objectives)
* [Architecture](#architecture)
* [Phase 1](#phase-1)
* [Phase 2](#phase-2)
* [Phase 3](#phase-3)
* [Phase 4](#phase-4)
* [Security Considerations](#security-considerations)
* [Key Takeaways](#key-takeaways)

### Overview

This project involved the deployment and analysis of a modern, multi-service honeypot platform to actively monitor and study malicious activity on the internet. The primary goal was to gain firsthand experience with attacker Tactics, Techniques, and Procedures (TTPs), collect Indicators of Compromise (IOCs), and understand the value of threat intelligence in a defensive security strategy.

The honeypot suite was deployed on a cloud server, presenting a vulnerable attack surface to the internet. All inbound connection attempts were logged, analyzed, and visualized to provide insights into the current threat landscape.

Disclaimer: This project was conducted for educational purposes only. All activities were contained within a personally owned and controlled lab environment.

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

Downloading T-Pot & Installation

```bash
git clone https://github.com/telekom-security/tpotce
cd tpotce/iso/installer/
./install.sh
```

- Installed Docker and Docker-Compose.
- Pulled all necessary honeypot and ELK container images from Docker Hub.
- Configured the system to run T-Pot on startup.

#### Phase 3

1. Once installed, the Kibana dashboard was accessible via HTTPS on port 64294. I connected to it securely from my local machine.
2. For the first 48 hours, I let the system run without interaction to collect a baseline of data.
3. I regularly reviewed the dashboard to watch attacks happen in near real-time. The dashboard provided maps of attacker locations, lists of targeted services, and samples of captured malware.

#### Phase 4

I used Kibana's built-in dashboards to filter and analyze data:
1. Identified the most persistent sources of malicious traffic.
2. Saw that SSH, Telnet, and SMB were the most frequently probed services.
3. Visualized the global origin of attacks.
Bonus: The Dionaea honeypot successfully lured attackers into uploading malware samples.
I compiled a list of IOCs, including malicious IP addresses, known-bad usernames/passwords used in brute-force attempts.

Top Targeted Service: SSH (22/TCP)
Common Usernames: admin, root, user

### Security Considerations

1. The honeypot was deployed on an isolated cloud VPS with no connections to my personal or corporate networks.
2. The server was explicitly set up to be probed and attacked. All activities were monitored and logged for research purposes only.
3. No retaliatory action was taken against source IPs. The gathered IOCs can be used for defensive blocking but not for offensive countermeasures.
4. Captured malware samples are stored in encrypted containers and are only analyzed in isolated, disposable virtual environments to prevent accidental infection.

### Key Takeaways

1. Automated attacks are continuous and pervasive. Security through obscurity is not a viable strategy.
2. The sheer volume of SSH brute-force attacks underscores the critical need for key-based authentication and strong passwords.
3. Honeypots are a powerful tool for early warning and intelligence gathering, revealing TTPs without exposing real assets.
4. Visualizing attack data makes the scale and nature of threats immediately apparent, which is crucial for communicating risk to stakeholders.
