#!/usr/bin/env python3
import subprocess
import time
from datetime import datetime

def monitor_connections():
    print("[*] Starting Port Scan Detection...")
    print("[*] Monitoring on Ubuntu 10.0.2.15")
    print("-" * 50)
    
    connection_count = {}
    
    while True:
        result = subprocess.run(['ss', '-tn'], capture_output=True, text=True)
        
        for line in result.stdout.split('\n'):
            if '10.0.2.3' in line:  # Detect connections from Kali
                if '10.0.2.3' not in connection_count:
                    connection_count['10.0.2.3'] = 0
                connection_count['10.0.2.3'] += 1
                
                if connection_count['10.0.2.3'] > 5:
                    print(f"[!] ALERT: Port scan detected from Kali (10.0.2.3)")
                    print(f"    Time: {datetime.now()}")
                    print(f"    Connections: {connection_count['10.0.2.3']}")
                    print("-" * 50)
        
        time.sleep(3)
        connection_count.clear()

if __name__ == "__main__":
    monitor_connections()
