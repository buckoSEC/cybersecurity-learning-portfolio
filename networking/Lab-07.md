# Lab 07 — Linux Log Analysis & Security Monitoring

**Project:** Small Business Network Security Assessment  
**Status:** Completed — manual investigation and a basic Python matching counter

## Objective

Investigate Linux authentication logs, generate controlled failed authentication events, distinguish genuine event records from search artefacts, and build a small Python script that counts matching authentication failure lines.

## Environment

- Kali Linux running under WSL2 with systemd.
- Available log sources: `/var/log/auth.log`, `/var/log/syslog`, and the systemd journal through `journalctl`.
- Local authentication test: `su - alice`, with failures recorded by PAM.
- Tools: `grep`, `wc`, a text editor, and Python 3.
- Analysis files: `auth_analyser.py` and `auth-failures-sample.log`.

## Procedure

The commands below are brief, representative commands for the documented workflow. They are not a complete terminal transcript.

### 1. Inspect available logs

Reviewed the available text logs and journal to locate authentication activity.

```bash
sudo tail /var/log/auth.log
sudo tail /var/log/syslog
sudo journalctl -n 50
```

The relevant evidence for this exercise came from PAM authentication failure records in `auth.log`. Availability of other log sources does not imply that every source contained the same events.

### 2. Generate and identify failed authentication events

Used a local account-switch attempt with an incorrect password to generate real failed authentication activity:

```bash
su - alice
```

The matching PAM message contained:

```text
pam_unix(su-l:auth): authentication failure
```

The account fields observed in the conversation included:

```text
ruser=kali rhost= user=alice
```

Here, `kali` initiated the attempt and `alice` was the target account. These are representative fragments from the recorded results, not reconstructed full log lines; timestamps, hostnames and process IDs are omitted.

### 3. Remove a search false positive and save the sample

A text search also matched a sudo audit record containing the search command itself. Because the command text included the authentication failure phrase, that record could be mistaken for another failed authentication event.

Filtered out `COMMAND=` records before counting and exporting the matching events:

```bash
sudo grep -F 'pam_unix(su-l:auth): authentication failure' /var/log/auth.log \
  | grep -v 'COMMAND=' | wc -l
```

**Observed result:** `3` matching authentication failure records.

```bash
sudo grep -F 'pam_unix(su-l:auth): authentication failure' /var/log/auth.log \
  | grep -v 'COMMAND=' > auth-failures-sample.log
cat auth-failures-sample.log
wc -l auth-failures-sample.log
```

The initial sample contained three matching failure lines. Excluding `COMMAND=` addressed the false positive encountered in this lab; it is a simple filter, not a general log parser.

### 4. Count matching lines with Python

The first version counted every line in the sample. It returned `3` while the file contained only the three failure records, but this alone did not demonstrate that it recognised authentication failures.

Added a condition so the counter increased only when the PAM failure phrase appeared. The following reflects the verified matching logic:

```python
# Lab 07 - Authentication Log Analyser

failures = 0

with open("auth-failures-sample.log", "r") as file:
    for line in file:
        if "pam_unix(su-l:auth): authentication failure" in line:
            failures += 1

print("Authentication failures:", failures)
```

Run the script from the directory containing the sample:

```bash
python3 auth_analyser.py
```

### 5. Test with an unrelated line

Deliberately added a normal line to the sample:

```bash
echo "Normal system activity" >> auth-failures-sample.log
python3 auth_analyser.py
```

The file then contained **four lines: three matching failures and one unrelated line**. After the code adjustment, the user confirmed that the count went back from `4` to `3`.

The reported result corresponds to:

```text
Authentication failures: 3
```

This verified that the counter excluded the deliberately added normal line.

## Observations and Evidence

| Check | Actual observation | What it establishes |
| --- | --- | --- |
| Local authentication test | Failed `su - alice` activity produced PAM failure records | Real local authentication failures were available for analysis |
| Filtered manual search | Three records matched the PAM failure phrase | Three matching failure lines were identified after excluding command records |
| Search false positive | A sudo record contained the search phrase in its command text | A matching string alone does not establish the record's meaning |
| Initial Python counter | Counted all sample lines | A line counter can appear correct when every input line is relevant |
| Mixed-input test | Four total lines; corrected script returned three matches | The condition excluded the added unrelated line |

This write-up records the results confirmed in the conversation. It does not attach original screenshots or raw log files, and the code shown above documents the verified logic rather than claiming a separately inspected script export.

## Findings

- Linux authentication logs provided evidence of controlled, local failed account-switch attempts.
- Inspecting record context was necessary to distinguish PAM events from sudo records that merely repeated the search phrase.
- Adding an unrelated line exposed the difference between counting input lines and counting matching events.
- The completed Python script is a basic foundation for log analysis: it reads a saved file and reports matching lines.

## Limitations

- The script performs a simple substring match. It does not parse structured events or validate the source of each matching line.
- It counts matching lines, not unique incidents, and does not deduplicate records.
- Username extraction and grouping were proposed but were **not completed or verified** in this lab.
- Timestamp parsing, time-window detection and alert thresholds were **not implemented**. Three total failures do not establish three failures within one minute or demonstrate a brute-force attack.
- The script reads a saved sample using a relative filename; it does not monitor logs continuously or generate alerts.
- The test demonstrated exclusion of one deliberately added unrelated line. Other authentication formats and false-positive cases were not validated.

## Next Steps

1. Extract the target `user=` field without confusing it with `ruser=`.
2. Group matching failures by target username.
3. Parse timestamps and count failures within a defined time window.
4. Test multiple users, different message formats, missing fields and command-text false positives.
5. Add a clearly defined alert threshold once grouping and time-window logic have been validated.

## Suggested Repository Layout

Keep this write-up beside the existing Labs 04–06 write-up:

```text
networking/small-business-security-assessment/
├── Lab07.md
└── labs/
    └── lab-07-log-analysis/
        ├── README.md
        ├── auth_analyser.py
        └── evidence/
            └── auth-failures-sample.log
```

This is a suggested layout; the script and evidence file are not supplied by this document. If the sample is stored under `evidence/`, adjust the script's input path accordingly. Review raw logs before publishing and retain the fields needed to explain the result when sanitising them.

[Back to project](README.md)
