# Setup and Deployment Guide

## 📋 Prerequisites

- Docker and Docker Compose installed
- Python 3.8+ (for challenge development)
- Git

## 🚀 Quick Start

### Clone the Repository
```bash
git clone https://github.com/bgctubitclub/BGCTUB_Central_IT_Fest.git
cd BGCTUB_Central_IT_Fest
```

## 📦 Challenge Deployment

### Static Challenges (Crypto, OSINT, RE, Forensics)

Static challenges only require file distribution. Participants download files from the `challenge_files/` of each challanges directory.

### Web Challenges (Docker-based)

Each web challenge includes a Dockerfile and web files.

#### Deploy Individual Challenge
```bash
cd "Web Exploitation/Robots/challenge_files/"
docker build -t robots-chall .
docker run -d -p 9001:9001 robots-chall
```

#### Deploy All Web Challenges
```bash
# From repository root
cd "Web Exploitation/Robots/challenge_files/"
docker build -t robots-chall .
docker run -d -p 9001:9001 robots-chall

cd "Web Exploitation/Too Trusting/challenge_files/"
docker build -t too_trusting-chall .
docker run -d -p 9002:9002 too_trusting-chall

cd "Web Exploitation/Employee Portal/challenge_files/"
docker build -t employee_portal-chall .
docker run -d -p 9003:9003 employee_portal-chall
```

#### Stop Challenges
```bash
docker stop robots-chall
docker stop too_trusting-chall
docker stop employee_portal-chall
```

## 🔧 Challenge Configuration

### Port Mappings

| Challenge | Internal Port | External Port |
|-----------|--------------|---------------|
| Robots | 9001 | 9001 |
| Too Trusting | 9002 | 9002 |
| Employee Portal | 9003 | 9003 |


### Manual Testing

1. Deploy challenge
2. Verify accessibility
3. Test intended solution
4. Test unintended solutions (if any)
5. Verify flag submission

## 📊 Monitoring

### Docker Stats
```bash
docker stats
```

## 🐛 Troubleshooting

### Port Already in Use?
```bash
# Find process using port
lsof -i :9001

# Kill process
kill -9 <PID>
```

### Docker Permission Issues
```bash
# Add user to docker group
sudo usermod -aG docker $USER
newgrp docker
```


### Clean Up
```bash
# Remove all stopped containers
docker container prune

# Remove unused images
docker image prune

# Remove unused volumes
docker volume prune
```
