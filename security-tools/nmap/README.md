# Nmap

**Status:** Ongoing learning

Nmap is a network discovery and security auditing tool used to identify hosts, open ports, and services. This section will document my learning and practical lab work with Nmap.

## Learning Focus

- Discovering hosts on a network.
- Scanning TCP ports and understanding open, closed, and filtered results.
- Identifying services and their versions.
- Understanding different scan types and when to use them.
- Saving and interpreting scan results.

## Example Lab Commands

Use these only against systems I own or have explicit permission to test. Replace `TARGET_IP` with an authorised lab target.

```bash
# Discover hosts on an authorised lab subnet
nmap -sn 192.168.56.0/24

# Scan common TCP ports
nmap TARGET_IP

# Identify service versions
nmap -sV TARGET_IP

# Scan specific ports and save the results
nmap -p 22,80,443 -oN scan-results.txt TARGET_IP
```

## Next Steps

Add practical lab examples, scan output, and explanations of findings as my learning progresses.
