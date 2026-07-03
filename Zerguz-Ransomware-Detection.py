#!/usr/bin/env python3

import os
import sys
import time
import platform
import subprocess
import logging
from datetime import datetime

try:
    from colorama import init as colorama_init, Fore, Back, Style
except ImportError:
    print("colorama not found. Install with: pip install colorama")
    sys.exit(1)

try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
except ImportError:
    print("watchdog not found. Install with: pip install watchdog")
    sys.exit(1)

colorama_init(autoreset=True)

CANARY_DIR = "Important-Files"
LOG_FILE = "zerguz_events.log"
SUSPICIOUS_EXTENSIONS = {
    ".enc", ".locked", ".crypt", ".crypted", ".encrypted",
    ".ransom", ".locky", ".cerber", ".wcry", ".wncry", ".zzz",
    ".xyz", ".crypto", ".ezz", ".exx", ".r5a", ".vault",
}
ENABLE_REAL_NETWORK_KILL = True

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def banner():
    art = f"""{Fore.RED}{Style.BRIGHT}
     ███████╗███████╗██████╗  ██████╗ ██╗   ██╗███████╗
     ╚══███╔╝██╔════╝██╔══██╗██╔════╝ ██║   ██║╚══███╔╝
       ███╔╝ █████╗  ██████╔╝██║  ███╗██║   ██║  ███╔╝
      ███╔╝  ██╔══╝  ██╔══██╗██║   ██║██║   ██║ ███╔╝
     ███████╗███████╗██║  ██║╚██████╔╝╚██████╔╝███████╗
     ╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝
    {Style.RESET_ALL}{Fore.YELLOW}{Style.BRIGHT}
          >> Ransomware Defender - Canary Token EDR <<
    {Style.RESET_ALL}{Fore.CYAN}
     -----------------------------------------------------
      Canary Folder : {Style.RESET_ALL}{Fore.WHITE}{CANARY_DIR}{Style.RESET_ALL}{Fore.CYAN}
      Log File      : {Style.RESET_ALL}{Fore.WHITE}{LOG_FILE}{Style.RESET_ALL}{Fore.CYAN}
      Operating Sys.: {Style.RESET_ALL}{Fore.WHITE}{platform.system()}{Style.RESET_ALL}{Fore.CYAN}
      Net Isolation : {Style.RESET_ALL}{Fore.WHITE}{"ACTIVE" if ENABLE_REAL_NETWORK_KILL else "SIMULATION (disabled)"}{Style.RESET_ALL}{Fore.CYAN}
     -----------------------------------------------------
    {Style.RESET_ALL}
    """
    print(art)


def ensure_canary_dir():
    if not os.path.exists(CANARY_DIR):
        os.makedirs(CANARY_DIR)
        decoy_files = [
            "Accounting_2024_Report.xlsx",
            "Employee_Salary_Info.docx",
            "Backup_Passwords.txt",
            "Project_Contract.pdf",
        ]
        for fname in decoy_files:
            with open(os.path.join(CANARY_DIR, fname), "w", encoding="utf-8") as f:
                f.write("You little moron :)\n")
        print(f"{Fore.GREEN}[+] Canary folder created and populated with decoy files: "
              f"{CANARY_DIR}{Style.RESET_ALL}")
    else:
        print(f"{Fore.YELLOW}[i] Canary folder already exists: {CANARY_DIR}{Style.RESET_ALL}")


def print_alarm(reason: str):
    msg = "ALERT: ZERGUZ DETECTED RANSOMWARE - NETWORK CONNECTION SEVERED!"
    bar = "!" * len(msg)
    print(f"\n{Back.RED}{Fore.WHITE}{Style.BRIGHT}{bar}{Style.RESET_ALL}")
    print(f"{Back.RED}{Fore.WHITE}{Style.BRIGHT}{msg}{Style.RESET_ALL}")
    print(f"{Back.RED}{Fore.WHITE}{Style.BRIGHT}{bar}{Style.RESET_ALL}")
    print(f"{Fore.RED}[REASON] {reason}{Style.RESET_ALL}")
    print(f"{Fore.RED}[TIME] {datetime.now().isoformat()}{Style.RESET_ALL}\n")
    logging.warning(f"RANSOMWARE ALERT - Reason: {reason}")


def isolate_network():
    system = os.name

    if not ENABLE_REAL_NETWORK_KILL:
        print(f"{Fore.YELLOW}[SIMULATION] Real network kill is disabled "
              f"(ENABLE_REAL_NETWORK_KILL=False). Commands will only be logged.{Style.RESET_ALL}")
        logging.info("SIMULATION MODE: Network isolation triggered but no real command executed.")
        return

    try:
        if system == "nt":
            print(f"{Fore.CYAN}[*] Windows detected. Disabling network adapters...{Style.RESET_ALL}")
            subprocess.run(["ipconfig", "/release"], shell=True,
                            capture_output=True, timeout=15)
            result = subprocess.run(
                ["netsh", "interface", "show", "interface"],
                shell=True, capture_output=True, text=True, timeout=15
            )
            logging.info(f"Current interfaces:\n{result.stdout}")

            for line in result.stdout.splitlines():
                parts = line.split()
                if len(parts) >= 4 and parts[0] in ("Enabled", "Etkin"):
                    iface_name = " ".join(parts[3:])
                    subprocess.run(
                        ["netsh", "interface", "set", "interface", iface_name, "admin=disable"],
                        shell=True, capture_output=True, timeout=15
                    )
                    logging.info(f"Interface disabled: {iface_name}")

        elif system == "posix":
            print(f"{Fore.CYAN}[*] Linux/Unix detected. Bringing down network interfaces...{Style.RESET_ALL}")
            result = subprocess.run(
                ["ip", "-o", "link", "show"],
                capture_output=True, text=True, timeout=15
            )
            logging.info(f"Current interfaces:\n{result.stdout}")

            for line in result.stdout.splitlines():
                iface = line.split(":")[1].strip().split("@")[0]
                if iface and iface != "lo":
                    subprocess.run(
                        ["sudo", "ip", "link", "set", iface, "down"],
                        capture_output=True, timeout=15
                    )
                    logging.info(f"Interface brought down: {iface}")
        else:
            print(f"{Fore.RED}[!] Unsupported operating system: {system}{Style.RESET_ALL}")
            logging.error(f"Isolation attempted on unsupported OS: {system}")

        print(f"{Fore.GREEN}[✓] Network isolation commands executed.{Style.RESET_ALL}")
        logging.info("Network isolation procedure completed.")

    except Exception as e:
        print(f"{Fore.RED}[ERROR] Error during network isolation: {e}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[HINT] This operation usually requires Administrator/root privileges.{Style.RESET_ALL}")
        logging.error(f"Network isolation error: {e}")


class CanaryHandler(FileSystemEventHandler):
    def __init__(self):
        super().__init__()
        self.triggered = False

    def _trigger(self, reason: str):
        if self.triggered:
            return
        self.triggered = True
        print_alarm(reason)
        isolate_network()

    def on_modified(self, event):
        if event.is_directory:
            return
        self._trigger(f"File modified (possible encryption): {event.src_path}")

    def on_deleted(self, event):
        if event.is_directory:
            return
        self._trigger(f"File deleted (possible wipe behavior): {event.src_path}")

    def on_moved(self, event):
        dest = getattr(event, "dest_path", "")
        _, ext = os.path.splitext(dest)
        ext = ext.lower()

        if ext in SUSPICIOUS_EXTENSIONS:
            self._trigger(
                f"SUSPICIOUS EXTENSION DETECTED! '{event.src_path}' -> '{dest}' "
                f"(extension: {ext})"
            )
        else:
            self._trigger(f"File renamed/moved: {event.src_path} -> {dest}")

    def on_created(self, event):
        if event.is_directory:
            return
        _, ext = os.path.splitext(event.src_path)
        if ext.lower() in SUSPICIOUS_EXTENSIONS:
            self._trigger(
                f"SUSPICIOUS NEW FILE CREATED: {event.src_path} (extension: {ext})"
            )


def main():
    banner()
    ensure_canary_dir()

    event_handler = CanaryHandler()
    observer = Observer()
    observer.schedule(event_handler, path=CANARY_DIR, recursive=True)
    observer.start()

    print(f"{Fore.GREEN}[+] Zerguz is now in monitoring mode. Watching canary folder...{Style.RESET_ALL}")
    print(f"{Fore.CYAN}    Press CTRL+C to exit.{Style.RESET_ALL}\n")
    logging.info("Zerguz started, monitoring began.")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print(f"\n{Fore.YELLOW}[!] Shutting down Zerguz...{Style.RESET_ALL}")
        logging.info("Zerguz stopped by user.")
    observer.join()


if __name__ == "__main__":
    main()
