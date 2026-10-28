import urllib.request

# ---- GitHub repo details ----
GITHUB_USER = "PV-Sudarsan"
GITHUB_REPO = "script"
BRANCH = "main"

BASE_URL = f"https://raw.githubusercontent.com/{GITHUB_USER}/{GITHUB_REPO}/{BRANCH}/"

# Experiment number -> (name, folder, files)
EXPERIMENTS = {
    "1":  ("Network Commands",         "Ex01_Network_Commands",    ["ex1_commands.py"]),
    "2":  ("HTTP Web Client",          "Ex02_HTTP_Web_Client",     ["ex2_http_client.py"]),
    "3a": ("Echo Client/Server (TCP)", "Ex03a_Echo_TCP",           ["ex3a_echo_server.py", "ex3a_echo_client.py"]),
    "3b": ("Chat (TCP)",               "Ex03b_Chat_TCP",           ["ex3b_chat_server.py", "ex3b_chat_client.py"]),
    "4":  ("DNS using UDP",            "Ex04_DNS_UDP",             ["ex4_dns_server.py", "ex4_dns_client.py"]),
    "5":  ("Packet Capture",           "Ex05_Packet_Capture",      ["ex5_capture.py"]),
    "6a": ("ARP using UDP",            "Ex06a_ARP_UDP",            ["ex6a_arp_server.py", "ex6a_arp_client.py"]),
    "6b": ("RARP using UDP",           "Ex06b_RARP_UDP",           ["ex6b_rarp_server.py", "ex6b_rarp_client.py"]),
    "7":  ("Congestion Control",       "Ex07_Congestion_Control",  ["ex7_congestion.py"]),
    "8":  ("TCP/UDP Performance",      "Ex08_TCP_UDP_Performance", ["ex8_tcp_udp.py"]),
    "9a": ("Distance Vector Routing",  "Ex09a_Distance_Vector",    ["ex9a_distance_vector.py"]),
    "9b": ("Link State Routing",       "Ex09b_Link_State",         ["ex9b_link_state.py"]),
    "10": ("CRC Error Detection",      "Ex10_CRC",                 ["ex10_crc.py"]),
}

# Show menu
print("===== CN LAB EXPERIMENTS =====")
for num, (name, folder, files) in EXPERIMENTS.items():
    print(f"{num:>3}. {name}")

choice = input("\nEnter experiment number: ").strip().lower()
if choice not in EXPERIMENTS:
    print("Invalid choice")
    exit()

name, folder, files = EXPERIMENTS[choice]

# If the experiment has server and client, ask which one to run
if len(files) == 2:
    print("\n1. Server   (run this first)")
    print("2. Client   (run in a second terminal)")
    part = input("Choose 1 or 2: ").strip()
    file = files[0] if part == "1" else files[1]
else:
    file = files[0]

# Download the code from GitHub (kept in memory, not saved)
url = BASE_URL + folder + "/" + file
print("\nFetching", url)
try:
    code = urllib.request.urlopen(url).read().decode()
except Exception as e:
    print("Could not download the code:", e)
    exit()

show = input("Show the code before running? (y/n): ").strip().lower()
if show == "y":
    print("\n" + "-" * 50)
    print(code)
    print("-" * 50)

# Run the downloaded code
print(f"\nRunning {file} ...\n")
exec(code, {"__name__": "__main__"})
