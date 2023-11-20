import socket
import struct

def extract_ipv4_addresses(ip_header):
    version_and_ihl = ip_header[0]
    ihl = (version_and_ihl & 0xF) * 4
    src_ip = socket.inet_ntoa(ip_header[12:16])
    dest_ip = socket.inet_ntoa(ip_header[16:20])
    return src_ip, dest_ip

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    sock.bind(("127.0.0.1", 0))

    sock.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    sock.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

    print(socket.if_nameindex())

    try:
        while True:
            data, addr = sock.recvfrom(65535)
            dest_mac, src_mac, eth_proto = struct.unpack('! 6s 6s H', data[:14])
            version_and_ihl = data[14]  # Extract IP version and header length
            version = version_and_ihl >> 4  # The higher 4 bits represent the version
            ihl = (version_and_ihl & 0xF) * 4  # Header length in bytes

            sender_ip, dest_ip = extract_ipv4_addresses(data[14:])

            print(f"Version: {version} | IHL: {version_and_ihl & 0xF} | Ether Type: {eth_proto}, {socket.htons(eth_proto)}, {addr}")
            print(f"Header Length: {ihl} bytes")
            print(f"Sender IP: {sender_ip} | Destination IP: {dest_ip}")

            print(f"Source MAC: {src_mac.hex()} | Destination MAC: {dest_mac.hex()} | Ether Type: {eth_proto}")
    except KeyboardInterrupt:
        print("Capture stopped by user.")
    except Exception as e:
        print(e)
    finally:
        sock.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)

if __name__ == "__main__":
    main()
