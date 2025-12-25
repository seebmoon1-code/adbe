import subprocess
import json
import os
import sys
import shutil
import time

class ADBE:
    """
    ADBE (Android Direct Bridge Engine) v2.0
    A professional framework for independent Android system management.
    Designed to bypass ADB dependencies by interfacing directly with OS/Kernel.
    """

    def __init__(self):
        self.VERSION = "2.0"
        self.REQUIRED_TOOLS = ['termux-battery-status', 'termux-vibrate', 'termux-notification']
        self._check_env()

    def _execute(self, cmd_list):
        """Secure internal executor for system commands."""
        try:
            process = subprocess.Popen(
                cmd_list, 
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE,
                text=True
            )
            stdout, _ = process.communicate(timeout=5)
            return stdout.strip() if process.returncode == 0 else None
        except Exception:
            return None

    def _check_env(self):
        """Validates the engineering environment."""
        missing = [tool for tool in self.REQUIRED_TOOLS if shutil.which(tool) is None]
        if missing:
            print(f"\033[91m[!] Environment Breach: {', '.join(missing)} missing.\033[0m")
            print("[*] Fix: Run 'sh install.sh' to repair the castle.")
            sys.exit(1)

    def get_system_resources(self):
        """Analyzes CPU & RAM with Fallback Strategies for Restricted Kernels."""
        # RAM Extraction
        ram_usage = "N/A"
        try:
            with open('/proc/meminfo', 'r') as f:
                lines = f.readlines()
                m = {l.split(':')[0]: int(l.split()[1]) for l in lines[:5]}
                total = m.get('MemTotal')
                avail = m.get('MemAvailable') or m.get('MemFree')
                if total and avail:
                    ram_usage = f"{round(((total - avail) / total) * 100, 1)}%"
        except:
            ram_usage = "Secured"

        # CPU Load Extraction
        cpu_load = "N/A"
        try:
            with open('/proc/loadavg', 'r') as f:
                cpu_load = f.read().split()[0]
        except:
            cpu_load = "Hidden"

        return {"cpu": cpu_load, "ram": ram_usage}

    def get_battery(self):
        raw = self._execute(['termux-battery-status'])
        return json.loads(raw) if raw else {}

    def get_network(self):
        raw = self._execute(['termux-telephony-deviceinfo'])
        if not raw or "error" in raw:
            return {"operator": "Restricted", "type": "N/A"}
        data = json.loads(raw)
        return {
            "operator": data.get("network_operator_name", "Unknown"),
            "type": data.get("network_type", "N/A")
        }

    def dashboard(self):
        """Professional CLI Dashboard for Engineers."""
        os.system('clear')
        res = self.get_system_resources()
        batt = self.get_battery()
        net = self.get_network()

        print("\033[1;36m") # Cyan
        print("    █████╗ ██████╗ ██████╗ ███████╗")
        print("    ██╔══██╗██╔══██╗██╔══██╗██╔════╝")
        print("    ███████║██║  ██║██████╔╝█████╗  ")
        print("    ██╔══██║██║  ██║██╔══██╗██╔══╝  ")
        print("    ██║  ██║██████╔╝██████╔╝███████╗")
        print(f"    [ ADBE Engine v{self.VERSION} - Independent ]\033[0m")
        print("="*50)
        print(f"\033[1;32m[+]\033[0m CPU Load: {res['cpu']}  |  RAM Usage: {res['ram']}")
        print(f"\033[1;32m[+]\033[0m Battery:  {batt.get('percentage', '??')}% ({batt.get('status', '??')})")
        print(f"\033[1;32m[+]\033[0m Network:  {net['operator']} [{net['type']}]")
        print("="*50)
        print("\033[90m[*] Monitoring system... Press Ctrl+C to terminate.\033[0m")

if __name__ == "__main__":
    adbe = ADBE()
    try:
        # Physical Alert: Start-up vibration
        subprocess.run(['termux-vibrate', '-d', '150'], stderr=subprocess.DEVNULL)
        while True:
            adbe.dashboard()
            time.sleep(3)
    except KeyboardInterrupt:
        print("\n\033[91m[!] Sovereign Engine Terminated.\033[0m")
