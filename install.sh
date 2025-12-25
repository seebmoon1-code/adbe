
#!/bin/bash

# ADBE Engine Auto-Installer v2.0
# Designed for Sovereign Android Environments (Termux)

echo -e "\e[1;36m[+] Starting ADBE Engine Installation...\e[0m"

# Update package database
echo -e "\e[1;32m[*] Updating repositories...\e[0m"
pkg update -y && pkg upgrade -y

# Installing Core Dependencies
echo -e "\e[1;32m[*] Installing Python and Termux-API...\e[0m"
pkg install -y python termux-api

# Installing Python libraries from requirements.txt
if [ -f "requirements.txt" ]; then
    echo -e "\e[1;32m[*] Installing Python requirements...\e[0m"
    pip install -r requirements.txt
else
    echo -e "\e[1;33m[!] requirements.txt not found. Skipping pip install.\e[0m"
fi

echo -e "\e[1;34m"
echo "=========================================="
echo "   ADBE ENGINE INSTALLED SUCCESSFULLY     "
echo "   Run it using: python adbe1.py          "
echo "=========================================="
echo -e "\e[0m"
