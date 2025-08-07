import socket
import os
import time
import requests
from colorama import Fore, Style, init

# Inisialisasi colorama
init(autoreset=True)

# Daftar port umum
COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    8080: "HTTP-Alt",
}

# Clear screen
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Banner tampilan
def banner():
    clear()
    print(Fore.CYAN + "="*60)
    print(Fore.MAGENTA + Style.BRIGHT + "     █▀▄▀█ ▄▀█ █▀▄ █▀█ █▀█ █░░ █▀▀")
    print(Fore.MAGENTA + Style.BRIGHT + "     █░▀░█ █▀█ █▄▀ █▀▀ █▀▄ █▄▄ ██▄")
    print(Fore.YELLOW + Style.BRIGHT + "          DOMAIN ➤ IP ➤ PORT ➤ INFO")
    print(Fore.GREEN + "              Developer AnsXploit")
    print(Fore.CYAN + "="*60)

# Ambil IP dari domain
def get_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except socket.gaierror:
        return None

# Scan port umum
def scan_ports(ip):
    open_ports = []
    for port, service in COMMON_PORTS.items():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((ip, port))
        if result == 0:
            open_ports.append((port, service))
        s.close()
    return open_ports

# Dapatkan Server Header dari HTTPS
def get_server_header_https(domain):
    try:
        url = f"https://{domain}"
        r = requests.get(url, timeout=3)
        return r.headers.get("Server")
    except:
        return None

# Program utama
def main():
    while True:
        banner()
        print(Fore.LIGHTBLUE_EX + "Contoh domain: google.com, github.com, openai.com")
        domain = input(Fore.LIGHTGREEN_EX + "\nMasukkan domain: " + Fore.WHITE).strip()

        if not domain:
            print(Fore.RED + "\n❌ Domain tidak boleh kosong!")
            time.sleep(2)
            continue

        print(Fore.YELLOW + "\n🔍 Mendapatkan IP...")
        ip = get_ip(domain)
        time.sleep(1)

        if not ip:
            print(Fore.RED + "❌ Gagal mendapatkan IP. Pastikan domain valid.")
            time.sleep(2)
            continue

        print(Fore.GREEN + f"\n✅ IP dari {domain}: {Fore.WHITE + Style.BRIGHT}{ip}")

        print(Fore.YELLOW + "\n🌐 Mendeteksi server domain (HTTPS)...")
        server = get_server_header_https(domain)
        if server:
            print(Fore.CYAN + f"🔧 Server Header: {Fore.WHITE + server}")
        else:
            print(Fore.RED + "⚠️  Tidak bisa mendeteksi server header (HTTPS).")

        print(Fore.YELLOW + "\n🔐 Scanning port penting...")
        open_ports = scan_ports(ip)
        if open_ports:
            print(Fore.GREEN + "\n✅ Port terbuka:")
            for port, service in open_ports:
                print(Fore.LIGHTCYAN_EX + f" - Port {port} ({service})")
        else:
            print(Fore.RED + "❌ Tidak ada port umum yang terbuka.")

        again = input(Fore.CYAN + "\nCek domain lain? (y/n): ").lower()
        if again != "y":
            print(Fore.LIGHTYELLOW_EX + "\n👋 Terima kasih sudah pakai tools dari " +
                  Fore.LIGHTGREEN_EX + "Developer AnsXploit!\n")
            break
        else:
            time.sleep(1)

# Jalankan
if __name__ == '__main__':
    main()