#!/usr/bin/env python3
import datetime
import os

def create_report():
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    html = f"""<!DOCTYPE html>
<html>
<head>
    <title>Security Report - Ubuntu Target</title>
    <style>
        body {{ font-family: Arial; margin: 40px; background: #f0f0f0; }}
        .container {{ background: white; padding: 30px; border-radius: 10px; box-shadow: 0 0 20px rgba(0,0,0,0.1); }}
        h1 {{ color: #d32f2f; border-bottom: 3px solid #d32f2f; padding-bottom: 10px; }}
        .finding {{ background: #fff3e0; padding: 15px; margin: 15px 0; border-left: 5px solid #ff9800; }}
        .critical {{ background: #ffebee; border-left-color: #d32f2f; }}
        .info {{ background: #e3f2fd; border-left-color: #2196f3; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Security Assessment Report</h1>
        <p><strong>Target System:</strong> Ubuntu 10.0.2.15</p>
        <p><strong>Attacker:</strong> Kali 10.0.2.3</p>
        <p><strong>Generated:</strong> {timestamp}</p>
        
        <h2>Attack Detection Summary</h2>
        <div class="finding critical">
            <h3>⚠️ Port Scanning Detected</h3>
            <p>Multiple connection attempts detected from 10.0.2.3</p>
            <p><strong>Attack Type:</strong> Network Reconnaissance</p>
            <p><strong>Severity:</strong> High</p>
        </div>
        
        <div class="finding">
            <h3>📊 Scan Statistics</h3>
            <ul>
                <li>Source IP: 10.0.2.3 (Kali Linux)</li>
                <li>Target IP: 10.0.2.15 (This System)</li>
                <li>Scan Type: TCP SYN Scan</li>
                <li>Ports Scanned: Multiple</li>
            </ul>
        </div>
        
        <div class="finding info">
            <h3>🛡️ Recommendations</h3>
            <ol>
                <li>Block IP 10.0.2.3 temporarily</li>
                <li>Enable rate limiting on firewall</li>
                <li>Implement fail2ban for SSH</li>
                <li>Review firewall rules</li>
                <li>Enable IDS/IPS system</li>
            </ol>
        </div>
        
        <h2>Evidence</h2>
        <p>Wireshark captures and system logs are available for review.</p>
    </div>
</body>
</html>"""
    
    filename = f"security_report_{timestamp.replace(' ', '_').replace(':', '-')}.html"
    with open(filename, 'w') as f:
        f.write(html)
    
    print(f"[+] Report generated: {filename}")
    print(f"[+] Open with: firefox {filename}")
    return filename

if __name__ == "__main__":
    create_report()
