"""
Internet speed test with two backends:
1) Python speedtest-cli (HTTPS enabled)
2) Fallback to Ookla's 'speedtest' CLI if installed

Usage:
    python internet_speed_test.py
"""

import json
import shutil
import subprocess
import sys

def run_with_speedtest_cli():
    # Requires: pip install speedtest-cli
    import speedtest
    print("🚀 Running speed test via Python speedtest-cli (HTTPS)...")
    try:
        st = speedtest.Speedtest(secure=True)  # <-- important for 403 issues
        st.get_best_server()
        download = st.download(threads=None) / 1_000_000  # bits/s -> Mbps
        upload = st.upload(threads=None) / 1_000_000      # bits/s -> Mbps
        res = st.results.dict()
        ping = res.get("ping")
        server = res.get("server", {})
        sponsor = server.get("sponsor", "")
        name = server.get("name", "")

        print(f"📡 Server: {sponsor} ({name})")
        print(f"📍 Ping: {ping:.2f} ms")
        print(f"⬇️  Download: {download:.2f} Mbps")
        print(f"⬆️  Upload:   {upload:.2f} Mbps")
        return True
    except speedtest.ConfigRetrievalError as e:
        print("⚠️  speedtest-cli couldn’t fetch config (often a 403/blocked issue).")
        return False
    except Exception as e:
        print(f"⚠️  speedtest-cli failed: {e}")
        return False

def run_with_ookla_cli():
    # Requires Ookla CLI installed and available as 'speedtest'
    # Windows install (one-time):
    #   winget install --id Ookla.Speedtest.CLI -e
    # or (if you use Chocolatey): choco install speedtest
    if not shutil.which("speedtest"):
        print("❌ Ookla CLI not found on PATH.")
        print("   Install it with: winget install --id Ookla.Speedtest.CLI -e")
        return False

    print("🚀 Running speed test via Ookla CLI...")
    try:
        cp = subprocess.run(
            ["speedtest", "-f", "json"],
            capture_output=True,
            text=True,
            check=True
        )
        data = json.loads(cp.stdout)

        # Ookla returns bandwidth in bytes/sec; convert to Mbps
        down_mbps = (data["download"]["bandwidth"] * 8) / 1_000_000
        up_mbps   = (data["upload"]["bandwidth"] * 8) / 1_000_000
        ping_ms   = data["ping"]["latency"]
        server    = data.get("server", {})
        name      = server.get("name", "")
        location  = f'{server.get("location","")}, {server.get("country","")}'.strip(", ")

        print(f"📡 Server: {name} ({location})")
        print(f"📍 Ping: {ping_ms:.2f} ms")
        print(f"⬇️  Download: {down_mbps:.2f} Mbps")
        print(f"⬆️  Upload:   {up_mbps:.2f} Mbps")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Ookla CLI error:\n{e.stderr or e.stdout}")
        return False
    except Exception as e:
        print(f"❌ Unexpected Ookla CLI error: {e}")
        return False

def main():
    # First try Python library with HTTPS; if that fails, try Ookla CLI
    if run_with_speedtest_cli():
        return
    print("\n🔁 Falling back to Ookla CLI...\n")
    if not run_with_ookla_cli():
        sys.exit(1)

if __name__ == "__main__":
    main()
