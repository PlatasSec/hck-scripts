def hex_to_ip_port(hex_address):
    # Split the hex address into parts
    ip_part, port_part = hex_address.split(':')

    # Convert IP address from hex to decimal
    ip_parts = [ip_part[i:i + 2] for i in range(0, len(ip_part), 2)][::-1]
    ip_decimal = ".".join(str(int(part, 16)) for part in ip_parts)

    # Convert port from hex to decimal
    port_decimal = str(int(port_part, 16))

    return ip_decimal, port_decimal

def decode_proc_net_tcp_info(data):
    decoded_info = []
    lines = data.strip().split("\n")

    for line in lines:
        parts = line.strip().split()
        connection = {}

        connection['sl'] = parts[0][:-1]
        local_ip, local_port = hex_to_ip_port(parts[1])
        rem_ip, rem_port = hex_to_ip_port(parts[2])

        connection['local_address'] = f"{local_ip}:{local_port}"
        connection['rem_address'] = f"{rem_ip}:{rem_port}"

        connection['st'] = parts[3]
        connection['tx_queue'] = parts[4]
        connection['rx_queue'] = parts[5]
        connection['tr'] = parts[6]
        connection['tm->when'] = parts[7]
        connection['retrnsmt'] = parts[8]
        connection['uid'] = parts[9]
        connection['timeout'] = parts[10]
        connection['inode'] = parts[11]

        decoded_info.append(connection)

    return decoded_info

data = """
0: 00000000:0016 00000000:0000 0A 00000000:00000000 00:00000000 00000000 0 0 916869924 1 0000000000000000 100 0 0 10 0
1: 0100007F:22B8 00000000:0000 0A 00000000:00000000 00:00000000 00000000 0 0 916871144 1 0000000000000000 100 0 0 10 0
2: 0B00007F:92BB 00000000:0000 0A 00000000:00000000 00:00000000 00000000 65534 0 916899881 1 0000000000000000 100 0 0 10 0
3: 00000000:1F40 00000000:0000 0A 00000000:00000000 00:00000000 00000000 0 0 916898925 1 0000000000000000 100 0 0 10 0
4: 037DB9C0:1F40 027DB9C0:8998 01 00000000:00000000 00:00000000 00000000 0 0 916989497 1 0000000000000000 20 4 30 10 -1
5: 037DB9C0:1F40 027DB9C0:8994 06 00000000:00000000 03:0000176E 00000000 0 0 0 3 0000000000000000
"""

decoded = decode_proc_net_tcp_info(data)

for connection in decoded:
    print(f"Connection Serial Number: {connection['sl']}")
    print(f"Local Address: {connection['local_address']}")
    print(f"Remote Address: {connection['rem_address']}")
    print(f"State: {connection['st']}")
    print(f"TX Queue: {connection['tx_queue']}")
    print(f"RX Queue: {connection['rx_queue']}")
    print(f"Traffic: {connection['tr']}")
    print(f"Time When: {connection['tm->when']}")
    print(f"Retransmit: {connection['retrnsmt']}")
    print(f"UID: {connection['uid']}")
    print(f"Timeout: {connection['timeout']}")
    print(f"INode: {connection['inode']}")
    print("-----------------------------")
