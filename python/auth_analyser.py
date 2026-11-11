
# Lab 07 - Authentication Log Analyser

failures = 0

with open("auth-failures-sample.log", "r") as file:
    for line in file:
        if "pam_unix(su-l:auth): authentication failure" in line:
            failures += 1

print("Authentication failures:", failures)

