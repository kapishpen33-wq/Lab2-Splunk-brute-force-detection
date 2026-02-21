# Lab2-Splunk-brute-force-detection
End-to-end SIEM lab: Built a Python script to generate a 10,000-event log dataset and utilized Splunk SPL/Regex to detect simulated Brute Force attacks (MITRE T1110).
# SIEM Lab: Brute Force Detection with Splunk and Python

## Objective
The objective of this lab is to simulate a brute force attack, ingest the resulting logs into a SIEM (Splunk), normalize the data, and write a custom detection query to identify the attacker. 

## Tools Used
* **Python 3:** For generating custom, time-stamped application logs containing randomized benign traffic and concentrated malicious traffic.
* **Splunk Enterprise:** For data ingestion, field extraction (Regex), and security alerting (SPL).

## MITRE ATT&CK Mapping
* **Tactic:** Credential Access
* **Technique:** Brute Force (T1110)

## Lab Steps
### 1. Data Generation
Wrote a Python script (`log_generator.py`) to generate an `app_server.log` file. The script utilizes the `datetime` and `random` libraries to simulate realistic log flow, inserting a concentrated burst of `WARN` events from a single IP address (`10.10.10.5`) among normal `INFO` traffic.

### 2. Data Ingestion & Normalization
* Ingested the raw logs into Splunk Enterprise.
* Created a custom sourcetype: `custom_app_secure`.
* Utilized **Regular Expressions (Regex)** to extract the custom field `src_ip` from the unstructured log data to allow for mathematical analysis.

### 3. Threat Detection (SPL)
Developed the following Search Processing Language (SPL) query to isolate the attack and visualize the spike in failed login attempts over time:

`index=* OR index=* sourcetype=custom_app_secure WARN | timechart count by src_ip`

## Results
*Successfully mapped the simulated attack, identifying a distinct spike in failed authentication attempts from IP 10.10.10.5.*

<img width="1440" height="900" alt="Screenshot 2026-02-21 at 11 54 56 AM" src="https://github.com/user-attachments/assets/af5516d2-c2af-4900-9ba8-2a05ce28086e" />

