# BGCTUB-ITC Breach

**Category:** Digital Forensics  
**Difficulty:** Hard  
**Points:** 2250 (15 flags - [3 x 50pts, 3 x 100pts, 3 x 150pts, 3 x 200pts, 3 x 250pts])  
**Author:** BGCTUB IT Club

## 📖 Description

During the BGCTUB IT Fest, the Central System of the BGCTUB IT Club was compromised by an unknown attacker. The adversary gained an initial foothold and then proceeded to move laterally across the infrastructure. Fortunately, network defenders managed to capture a traffic dump/logs of the attacker's activity.

As a member of the Security Operations Center (SOC) team, your task is to analyze this capture and answer a series of questions to uncover the full attack chain.

## 📥 Files

- `capture.pcapng` - Complete network traffic capture

## 🚩 15 Questions to Answer

### Q1. What are the IP addresses of the attacker and the victim?
**Example:** `BGCTUB_ITC{192.168.1.10_192.168.1.20}`
### Q2. How many ports did the attacker enumerate on the victim system?
**Example:** `BGCTUB_ITC{5}`
### Q3. What is the name and version of the FTP service running?
**Example:** `BGCTUB_ITC{ProFTPd_1.3.6}`
### Q4. What credentials did the attacker use to access the FTP server?
**Example:** `BGCTUB_ITC{username_password}`
### Q5. What is the fully qualified domain name (FQDN) of the web server?
**Example:** `BGCTUB_ITC{test.localdomain}`
### Q6. Which tool did the attacker use to enumerate the web application, and what version?
**Example:** `BGCTUB_ITC{toolname_10.0.0}`
### Q7. What is the disallowed path found for internet crawlers?
**Example:** `BGCTUB_ITC{/secret/}`
### Q8. What credentials did the attacker use to log in to the web application's admin dashboard?
**Example:** `BGCTUB_ITC{username_password}`
### Q9. Which directory stores the uploaded files?
**Example:** `BGCTUB_ITC{/directory/}`
### Q10. What is the name of the malicious shell the attacker uploaded to gain RCE?
**Example:** `BGCTUB_ITC{filename.ext}`
### Q11. Which port did the attacker use to gain remote code execution (RCE)?
**Example:** `BGCTUB_ITC{55555}`
### Q12. What is the password of the user Manager?
**Example:** `BGCTUB_ITC{password}`
### Q13. What is the full name of the user who handles the FTP service?
**Example:** `BGCTUB_ITC{full_name}`
### Q14. What is the misconfigured binary that the attacker used for Privilege Escalation?
**Example:** `BGCTUB_ITC{tar}`
### Q15. Who was the attacker?
**Example:** `BGCTUB_ITC{redteam123}`

## 💡 Hints

1. Start by identifying the attack and victim IPs
2. Use Wireshark display filters to isolate specific protocols
3. Follow TCP streams to see complete conversations
4. Look for FTP-DATA for file transfers
5. HTTP traffic will reveal web enumeration and exploitation
6. Track the reverse shell connection
7. Look for privilege escalation commands in the shell session

## 🛠️ Recommended Tools

- Wireshark / tshark
- NetworkMiner
- tcpdump
- strings

## 🎥 Video Walkthrough

🎥 [Watch on YouTube](https://youtu.be/jFSo8OmqZ1k)

## 🏷️ Tags

`pcap-analysis` `network-forensics` `wireshark` `attack-chain`
