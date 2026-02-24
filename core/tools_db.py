import os
from .system import get_os, run_command

CATEGORIES = {
    "1": {
        "name": "Information Gathering",
        "description": "Tools for reconnaissance and OSINT",
        "tools": [
            {
                "name": "Nmap",
                "desc": "Network exploration tool and security / port scanner",
                "install": {
                    "Linux": "sudo apt install -y nmap",
                    "Termux": "pkg install -y nmap",
                    "Windows": "echo Please install Nmap manually from nmap.org"
                },
                "run": "nmap"
            },
            {
                "name": "Sherlock",
                "desc": "Hunt down social media accounts by username",
                "install": {
                    "Linux": "git clone https://github.com/sherlock-project/sherlock.git && cd sherlock && python3 -m pip install -r requirements.txt",
                    "Termux": "git clone https://github.com/sherlock-project/sherlock.git && cd sherlock && python -m pip install -r requirements.txt",
                    "Windows": "git clone https://github.com/sherlock-project/sherlock.git && cd sherlock && pip install -r requirements.txt"
                },
                "run": "python sherlock/sherlock"
            },
            {
                "name": "RedHawk",
                "desc": "All in one tool for Information Gathering and Vulnerability Scanning",
                "install": {
                    "Linux": "git clone https://github.com/Tuhinshubhra/RED_HAWK.git",
                    "Termux": "git clone https://github.com/Tuhinshubhra/RED_HAWK.git",
                    "Windows": "git clone https://github.com/Tuhinshubhra/RED_HAWK.git"
                },
                "run": "php RED_HAWK/rhawk.php"
            }
        ]
    },
    "2": {
        "name": "Exploitation Tools",
        "description": "Exploit vulnerabilities",
        "tools": [
            {
                "name": "Metasploit",
                "desc": "Advanced open-source platform for developing, testing, and using exploit code",
                "install": {
                    "Linux": "curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && chmod 755 msfinstall && ./msfinstall",
                    "Termux": "wget https://raw.githubusercontent.com/gushmazuko/metasploit_in_termux/master/metasploit.sh && chmod +x metasploit.sh && ./metasploit.sh",
                    "Windows": "echo Please download Metasploit installer from rapid7.com"
                },
                "run": "msfconsole"
            },
            {
                "name": "SQLMap",
                "desc": "Automatic SQL injection and database takeover tool",
                "install": {
                    "Linux": "sudo apt install -y sqlmap || git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev",
                    "Termux": "git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev",
                    "Windows": "git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev"
                },
                "run": "python sqlmap-dev/sqlmap.py"
            }
        ]
    },
    "3": {
        "name": "Web Attack Tools",
        "description": "Tools for testing web applications",
        "tools": [
            {
                "name": "Nikto",
                "desc": "Web server scanner",
                "install": {
                    "Linux": "sudo apt install -y nikto || git clone https://github.com/sullo/nikto",
                    "Termux": "git clone https://github.com/sullo/nikto",
                    "Windows": "git clone https://github.com/sullo/nikto"
                },
                "run": "perl nikto/program/nikto.pl"
            },
            {
                "name": "Dirb",
                "desc": "Web Content Scanner",
                "install": {
                    "Linux": "sudo apt install -y dirb",
                    "Termux": "echo Dirb needs compiling. Consider using dirb source.",
                    "Windows": "echo Dirb not fully supported on Windows natively."
                },
                "run": "dirb"
            }
        ]
    },
    "4": {
        "name": "Password Cracking",
        "description": "Tools for cracking passwords and hashes",
        "tools": [
            {
                "name": "Hydra",
                "desc": "Network logon cracker",
                "install": {
                    "Linux": "sudo apt install -y hydra",
                    "Termux": "pkg install -y hydra",
                    "Windows": "echo Install Kali WSL or use pre-compiled binaries."
                },
                "run": "hydra"
            },
            {
                "name": "John the Ripper",
                "desc": "Advanced password cracker",
                "install": {
                    "Linux": "sudo apt install -y john",
                    "Termux": "pkg install -y john",
                    "Windows": "echo Please install John the Ripper manually for Windows."
                },
                "run": "john"
            },
            {
                "name": "CuPP",
                "desc": "Common User Passwords Profiler",
                "install": {
                    "Linux": "git clone https://github.com/Mebus/cupp.git",
                    "Termux": "git clone https://github.com/Mebus/cupp.git",
                    "Windows": "git clone https://github.com/Mebus/cupp.git"
                },
                "run": "python cupp/cupp.py"
            }
        ]
    },
    "5": {
        "name": "Phishing & Social Eng.",
        "description": "Tools for phishing attacks",
        "tools": [
            {
                "name": "Zphisher",
                "desc": "Automated Phishing Tool",
                "install": {
                    "Linux": "git clone https://github.com/htr-tech/zphisher.git",
                    "Termux": "git clone https://github.com/htr-tech/zphisher.git",
                    "Windows": "echo Zphisher is a bash script. Use WSL or Git Bash."
                },
                "run": "cd zphisher && bash zphisher.sh"
            },
            {
                "name": "HiddenEye",
                "desc": "Modern Phishing Tool",
                "install": {
                    "Linux": "git clone https://github.com/DarkSecDevelopers/HiddenEye.git && cd HiddenEye && pip3 install -r requirements.txt",
                    "Termux": "git clone https://github.com/DarkSecDevelopers/HiddenEye.git && cd HiddenEye && pip install -r requirements.txt",
                    "Windows": "git clone https://github.com/DarkSecDevelopers/HiddenEye.git && cd HiddenEye && pip install -r requirements.txt"
                },
                "run": "python HiddenEye/HiddenEye.py"
            }
        ]
    },
    "6": {
        "name": "WiFi & Wireless",
        "description": "WiFi hacking and auditing tools",
        "tools": [
            {
                "name": "Aircrack-ng",
                "desc": "WiFi security auditing tools suite",
                "install": {
                    "Linux": "sudo apt install -y aircrack-ng",
                    "Termux": "pkg install -y root-repo && pkg install -y aircrack-ng",
                    "Windows": "echo Aircrack-ng is not fully supported natively on Windows for capturing."
                },
                "run": "aircrack-ng"
            },
            {
                "name": "Wifite",
                "desc": "Automated wireless auditor",
                "install": {
                    "Linux": "sudo apt install -y wifite",
                    "Termux": "echo Wifite requires root on Termux and special WiFi cards.",
                    "Windows": "echo Not supported natively."
                },
                "run": "wifite"
            }
        ]
    },
    "7": {
        "name": "DDoS Attacks",
        "description": "Stress testing tools",
        "tools": [
            {
                "name": "Hammer",
                "desc": "DDoS Script",
                "install": {
                    "Linux": "git clone https://github.com/cyweb/hammer.git",
                    "Termux": "git clone https://github.com/cyweb/hammer.git",
                    "Windows": "git clone https://github.com/cyweb/hammer.git"
                },
                "run": "python hammer/hammer.py"
            },
            {
                "name": "Xerxes",
                "desc": "Most powerful DoS tool",
                "install": {
                    "Linux": "git clone https://github.com/XCHG90/xerxes.git && cd xerxes && gcc xerxes.c -o xerxes",
                    "Termux": "pkg install -y clang && git clone https://github.com/XCHG90/xerxes.git && cd xerxes && clang xerxes.c -o xerxes",
                    "Windows": "echo Xerxes requires a C compiler. Install GCC via MinGW."
                },
                "run": "./xerxes/xerxes"
            }
        ]
    }
}
