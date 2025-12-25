# ADBE (Android Direct Bridge Engine)
> **Slogan:** A sovereign castle doesn't need a second one.

ADBE is a professional-grade framework designed for independent Android system management. It interfaces directly with the Linux Kernel and OS layers via Termux, bypassing traditional ADB dependencies.

## Key Features
- **Kernel Interfacing:** Direct extraction of telemetry from `/proc`.
- **Zero Dependency:** Designed to run natively on Android devices.
- **Real-time Monitoring:** High-performance CLI dashboard for CPU, RAM, and Power.

## Installation
1. Install Termux.
2. Install dependencies:
   ```bash
   pkg install termux-api python
