# Kali Linux — Security Lab Progress

**Status:** Ongoing hands-on learning  
**Environment:** Kali Linux on WSL2 with systemd

After starting with Ubuntu as my first Linux distribution, I’m using Kali to develop my Linux and cybersecurity skills through practical labs. My focus is on understanding the commands I run, interpreting their output, and documenting what the results actually show.

## Progress So Far

Through my Linux security labs, I’ve practised:

- **Service auditing:** Using Nmap and `ss` to investigate listening services and compare results before and after stopping a local test server.
- **Traffic analysis:** Capturing local traffic with `tcpdump` and examining TCP and HTTP behaviour in Wireshark.
- **Permissions and access control:** Working with `chmod`, `chown`, users, and groups to test who can access files.
- **Log analysis:** Exploring `/var/log/auth.log`, `/var/log/syslog`, and the systemd journal with `journalctl`.
- **Basic Python automation:** Reading a saved log sample and counting lines that match an authentication failure message.

## Latest Lab — Authentication Log Analysis

I generated real failed authentication events using `su - alice` and identified **three matching PAM authentication failure records**.

During the investigation, a search also matched a sudo record containing the search command itself. Filtering out those command records helped distinguish the actual authentication events from the search false positive.

I then built `auth_analyser.py` to read `auth-failures-sample.log`. After adding a normal line, the file contained **four lines**, but the corrected script still counted **three authentication failures**. This confirmed that it counted matching lines rather than every line in the file.

The script is currently a simple matching counter. Username grouping, time-window detection, and alerting are future improvements.

## What I’m Learning

These exercises are helping me connect Linux administration with security investigation: checking access permissions, understanding exposed services, and reading logs in context. I’m also learning to test my assumptions—a matching string or a plausible count needs further checking before I draw a conclusion.

## Next Steps

- Continue building confidence with Linux commands and troubleshooting.
- Extend the log analyser to group failures by username and examine timestamps.
- Keep recording commands, observations, and limitations from each lab.

## Related Write-ups

- [Labs 04–06 — Service auditing, traffic analysis, and Linux hardening](../../networking/small-business-security-assessment/Labs04-06.md)
- [Lab 07 — Linux Log Analysis & Security Monitoring](../../networking/small-business-security-assessment/Lab07.md)

[Back to distributions](README.md) · [Linux goals and progress](../README.md)
