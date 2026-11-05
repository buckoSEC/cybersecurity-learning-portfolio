# Snort — Intrusion Detection System Lab

**Environment:** Kali Linux (WSL2)  
**Tool:** Snort  
**Status:** Initial setup completed; practical detection testing pending

## Objective

Gain practical experience with network intrusion detection systems (IDS), including installation, configuration, and the fundamentals of identifying suspicious network activity.

## 1. Installation & Setup

- Installed Snort within a Kali Linux environment.
- Explored Snort's command-line interface and configuration requirements.
- Investigated configuration file locations and differences between Snort versions.
- Successfully validated a Snort configuration with zero warnings.

## 2. Intrusion Detection Concepts

Developed an introductory understanding of:

- Network-based intrusion detection systems (NIDS).
- The distinction between IDS and IPS.
- Signature-based detection.
- Traffic monitoring and packet inspection.
- Detection rules, alerts, and network security monitoring.

## 3. Configuration Validation

Successfully performed a Snort configuration validation test.

**Observed result:**

```text
Snort successfully validated the configuration (with 0 warnings).
Snort exiting
```

This confirmed that the tested configuration passed Snort's validation checks. It did not establish that intrusion detection rules were successfully generating alerts.

## 4. Troubleshooting & Learning

During setup, I encountered configuration-file location issues when attempting to access:

```bash
sudo cat /etc/snort/snort.conf
```

The file was not found at that location.

This highlighted the importance of identifying the installed Snort version and locating its configuration files rather than assuming a particular file structure.

## 5. Skills Developed

- Introduction to IDS installation and configuration.
- Linux-based security tool administration.
- Command-line troubleshooting.
- Configuration validation.
- Understanding network monitoring technologies.

## 6. Next Steps

- [ ] Identify and document the installed Snort version.
- [ ] Locate and examine the active configuration file.
- [ ] Create a simple custom detection rule.
- [ ] Generate controlled traffic in an isolated lab.
- [ ] Verify that Snort generates an alert.
- [ ] Capture and document the resulting alerts.

## Summary

This exercise provided initial hands-on experience with Snort and reinforced Linux troubleshooting skills.

The next phase will focus on progressing from configuration validation to practical network traffic detection and alert analysis.
