## Log analyzer-Brute Force Detection tool

# overview
This project is a simple Python-based log analyzer that dectects suspicious login activity in authentication logs.

The program scans a log file containing login attempts and identifies:
- IP addresses with multiple failed login attempts
- Suspicious IPs based on a failure threshold
- The IP address with the highest number of failed attemps
- Possible brute-force attacks occuring within a short time window

This tool demonstrates basic security log analysis techniques commonly used in cybersecurity and Security Operations  Centers (SOC).

## Features
. Counts failed login attempts per IP
. Identifies suspicious IP addresses
. Finds the top attacking IP
. Detects possible brute-force login attacks

## Technologies
. Python
. File parsing
. Dictionaris
. Datetime module

## How to Run
code :
Run the program:
python log_analyzer.py
Then enter the log file name:
auth_log_sample.txt

## Purpose
This project was created  as a learning exercise to practice Pyhthon programming and basic cybersecurity log analysis techniques.

## Example input:
2026-03-11 10:15:01 - 192.168.1.10 - login failed
2026-03-11 10:15:10 - 192.168.1.10 - login failed
2026-03-11 10:15:20 - 192.168.1.10 - login failed
2026-03-11 10:15:35 - 192.168.1.10 - login failed
2026-03-11 10:16:00 - 192.168.1.22 - login success
2026-03-11 10:17:05 - 192.168.1.55 - login failed
2026-03-11 10:18:10 - 192.168.1.55 - login failed
2026-03-11 10:18:40 - 192.168.1.55 - login failed
2026-03-11 10:20:10 - 10.0.0.8 - login failed
2026-03-11 10:20:30 - 10.0.0.8 - login failed
2026-03-11 10:20:50 - 10.0.0.8 - login failed 
2026-03-11 10:21:05 - 10.0.0.8 - login failed
2026-03-11 10:21:20 - 192.168.1.10 - login failed
2026-03-11 10:25:00 - 172.16.0.2 - login failed

## Example output:
Failed login counts:
192.168.1.10: 5
192.168.1.55: 3
10.0.0.8: 4
172.16.0.2: 1


Suspicious IPs:
192.168.1.10 -> 5 failed attempts
192.168.1.55 -> 3 failed attempts
10.0.0.8 -> 4 failed attempts
Top attacking IP:
192.168.1.10 -> 5 failed attempts

Brute-force analysis:
Possible brute-force attack detected
IP: 192.168.1.10
Failures: 3
Within seconds: 19

Possible brute-force attack detected 
IP: 10.0.0.8
Failures: 3
Within seconds: 40
