# SIEM

# Table of Contents
* [Overview](#overview)
* [Architecture](#architecture)
* [Phase 1](#phase-1)
* [Phase 2](#phase-2)
* [Phase 3](#phase-3)
* [Phase 4](#phase-4)
* [Potential Improvement](#potential-improvement)
* [Key Takeaways](#key-takeaways)

## Overview

This project involved the design, deployment, and configuration of a fully functional Security Information and Event Management (SIEM) system using Microsoft Sentinel in a hybrid Azure environment. The goal was to create a live security monitoring lab to gain hands-on experience with enterprise-grade security tools, log ingestion, threat detection, and incident response workflows.

The lab simulates a corporate environment with both cloud and on-premises components, integrating various log sources to provide a unified security view. Custom detection rules were developed to identify suspicious activity, and a live attack simulation was conducted to validate the SIEM.

Disclaimer: This project was conducted in a personal lab environment with no connection to any production or corporate network. All activities were performed for educational purposes only.

## Architecture

1. Cloud Environment (Microsoft Azure):
   - Resource Group: Contains all project resources.
   - Microsoft Sentinel Workspace: The central brain of the SIEM, deployed on a Log Analytics workspace.
   - Azure Virtual Network (VNet): A segmented network to host cloud resources.
   - Windows Server 2022 Virtual Machine (VM): A cloud-based server acting as a critical asset.
2. Simulated "On-Premises" Environment:
   - A Windows 10 Virtual Machine running locally (e.g., on VMware/VirtualBox) treated as a corporate user's workstation.

3. Log Sources Integrated:
   - Azure Activity Logs: Monitoring administrative activity on the Azure subscription.
   - Microsoft Defender for Cloud: Providing threat detection for the Azure VM.
   - Windows Security Events: Collected from both VMs using the Azure Monitor Agent.
   - Sysmon (System Monitor): Installed on both VMs for advanced process and network activity visibility.
   - Simulated Firewall Logs (Custom Table): Ingested via the Log Analytics Custom Logs API to demonstrate parsing custom data formats.

### Phase 1

1. Created a new Azure subscription to isolate the lab and control costs.
2. Deployed a Resource Group, Log Analytics Workspace, and a Windows Server 2022 Virtual Machine within a new VNet.
3. Enabled Microsoft Sentinel on the created Log Analytics workspace.

### Phase 2

4. Enabled the built-in data connectors for Azure Activity and Microsoft Defender for Cloud with one click.

5. Onboard Windows Security Events:
   - Installed the Azure Monitor Agent (AMA) on both the Azure VM and the local Win10 VM.
   - Created a Data Collection Rule (DCR) in Azure to define exactly which events to collect (e.g., Security Event Codes 4625 (failed logons))
   - Linked the DCR to the VMs.

6. Advanced Logging with Sysmon:
   - Downloaded and configured Sysmon with a popular SwiftOnSecurity configuration file on both VMs for deep visibility into process trees, network connections, and file changes.
   - Created a second DCR to collect the Sysmon logs from the Event Log and route them to the Sentinel workspace.

7. Custom Log Ingestion:
   - Used the HTTP Data Collector API for Log Analytics to ingest a sample of custom firewall logs in CSV format.

### Phase 3

8. Custom Analytics Rules:
```kql
// KQL Query for RDP Brute Force Detection
SecurityEvent
| where EventID == 4625
| where Account !contains "$" // Filter out machine accounts
| summarize FailedAttempts = count(), FailedAccounts = makeset(Account) by SourceIPAddress, bin(TimeGenerated, 15m)
| where FailedAttempts > 10
| project TimeGenerated, SourceIPAddress, FailedAttempts, FailedAccounts
```

9. A rule to alert on the execution of known hacking tools like Mimikatz or PsExec (based on process name or path).
10. A rule to alert on successful logins from locations inconsistent with the user's typical pattern (using the ipgeo() function in KQL).

### Phase 4

11. Manually executed attack sequences on the local Win10 VM to generate malicious telemetry:
12. Performed a brute-force RDP attack using Hydra from a Kali Linux VM.
13. Attempted to run payloads with names mimicking common malware.
14. Generated a high volume of network requests to simulate scanning.
15. Monitored the Incidents blade in Sentinel, clicked into the generated incidents, and used the Investigation Graph to trace the attack chain and identify compromised entities.

### Potential Improvement

Create an automated playbook that would trigger when a high-severity incident was generated.

### Key Takeaways

1. Hands-on SIEM Experience
2. Log Integration & Normalization
3. Threat Detection Engineering
4. Incient Response Simulation
