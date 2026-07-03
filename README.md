# 🛡️ Zerguz Ransomware Detection

```{=html}

```
Behavior-Based Ransomware Detection • Canary Token Strategy • Automatic
Network Isolation • Cross Platform
```{=html}

```

------------------------------------------------------------------------

## 📌 Overview

**Zerguz Ransomware Detection** is a lightweight Behavior-Based
Detection tool written in Python.

Instead of relying on malware signatures, Zerguz monitors a dedicated
**Canary Folder** filled with decoy files. If ransomware attempts to
encrypt, rename, modify or delete these files, Zerguz immediately
detects the behavior, records the event, displays an alert and can
automatically isolate the system from the network.

The project demonstrates core Blue Team and SOC concepts including:

-   Behavior-Based Detection
-   Canary Token Strategy
-   Early Ransomware Detection
-   Incident Response
-   Automatic Host Isolation
-   Event Logging

------------------------------------------------------------------------

# ✨ Features

  -----------------------------------------------------------------------
  Feature                       Description
  ----------------------------- -----------------------------------------
  🔍 Real-Time Monitoring       Watches the canary folder continuously

  🎯 Canary Files               Creates fake sensitive files
                                automatically

  🚨 Behavioral Detection       Detects modification, deletion, move and
                                encryption attempts

  🌐 Network Isolation          Disables network interfaces after
                                detection

  📝 Logging                    Stores every alert inside
                                **zerguz_events.log**

  💻 Cross Platform             Windows and Linux supported

  🎨 Colored Console            Clean terminal interface using Colorama
  -----------------------------------------------------------------------

------------------------------------------------------------------------

# ⚙️ Detection Workflow

``` text
Start
 │
 ▼
Create Canary Folder
 │
 ▼
Generate Decoy Files
 │
 ▼
Monitor File Events
 │
 ▼
Suspicious Activity?
 │
 ├── No → Continue Monitoring
 │
 └── Yes
        │
        ▼
     Raise Alert
        │
        ▼
    Save Security Log
        │
        ▼
 Automatic Network Isolation
```

------------------------------------------------------------------------

# 📂 Canary Folder

When started, Zerguz creates:

``` text
Important-Files/
```

Example decoy documents:

``` text
Accounting_2024_Report.xlsx
Employee_Salary_Info.docx
Backup_Passwords.txt
Project_Contract.pdf
```

These files are intentionally attractive to ransomware.

------------------------------------------------------------------------

# 🚨 Detection Events

The application detects:

-   File Modification
-   File Deletion
-   File Rename
-   File Move
-   Creation of suspicious files
-   Known ransomware extensions

Supported extensions include:

``` text
.enc
.locked
.crypt
.crypted
.encrypted
.ransom
.locky
.cerber
.wcry
.wncry
.zzz
.xyz
.crypto
.ezz
.exx
.r5a
.vault
```

------------------------------------------------------------------------

# 🌐 Automatic Network Isolation

After detection:

### Windows

-   Releases IP configuration
-   Lists interfaces
-   Disables active adapters

### Linux

-   Enumerates interfaces
-   Brings every interface except loopback down

> Administrator/root privileges are recommended.

------------------------------------------------------------------------

# 📜 Logging

Every security event is written to:

``` text
zerguz_events.log
```

Including:

-   Timestamp
-   Detection reason
-   Warning messages
-   Isolation status
-   Errors

------------------------------------------------------------------------

# 📦 Installation

``` bash
https://github.com/Malikejder/Zerguz-Ransomware-Detection.git

cd Zerguz-Ransomware-Detection

pip install watchdog colorama
```

------------------------------------------------------------------------

# ▶️ Usage

``` bash
python Zerguz-Ransomware-Detection.py
```

------------------------------------------------------------------------

# 🏗️ Project Structure

``` text
.
├── Zerguz-Ransomware-Detection.py
├── zerguz_events.log
└── Important-Files/
    ├── Accounting_2024_Report.xlsx
    ├── Employee_Salary_Info.docx
    ├── Backup_Passwords.txt
    └── Project_Contract.pdf
```
------------------------------------------------------------------------

# ⚠️ Disclaimer

This project is intended for educational, research and defensive
cybersecurity purposes only.

------------------------------------------------------------------------

# 👨‍💻 Author

**Malikejder Durgun**

SOC Analyst • Blue Team • Python Developer • Cybersecurity
