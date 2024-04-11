import os
import time
import psutil

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    memory = psutil.virtual_memory()
    return memory.percent

def get_network_throughput():
    net_io = psutil.net_io_counters()
    return net_io.bytes_sent, net_io.bytes_recv

def get_disk_usage():
    disk_usage = psutil.disk_usage('/')
    return disk_usage.percent

def get_disk_io():
    disk_io = psutil.disk_io_counters()
    return disk_io.read_bytes, disk_io.write_bytes

def get_network_packets():
    net_io = psutil.net_io_counters()
    return net_io.packets_sent, net_io.packets_recv

def get_system_uptime():
    uptime_seconds = time.time() - psutil.boot_time()
    uptime_time = time.strftime("%H:%M:%S", time.gmtime(uptime_seconds))
    return uptime_time

def get_load_average():
    # Note: load average might not be meaningful on Windows
    try:
        return os.getloadavg()
    except AttributeError:
        return (0, 0, 0)  # Placeholder if not available

def get_running_processes():
    return len(psutil.pids())

def get_cpu_temperature():
    try:
        temps = psutil.sensors_temperatures()
        cpu_temp = temps['coretemp'][0].current  # This key might vary
        return cpu_temp
    except (KeyError, AttributeError):
        return "N/A"

def main():
    try:
        while True:
            # Fetch all metrics
            cpu_usage = get_cpu_usage()
            memory_usage = get_memory_usage()
            sent, received = get_network_throughput()
            disk_usage = get_disk_usage()
            disk_read, disk_write = get_disk_io()
            packets_sent, packets_recv = get_network_packets()
            system_uptime = get_system_uptime()
            load_avg_1, load_avg_5, load_avg_15 = get_load_average()
            num_processes = get_running_processes()
            cpu_temp = get_cpu_temperature()

            # Clear the screen
            os.system('cls' if os.name == 'nt' else 'clear')

            # Print the updated information
            print("----------------------------------------------", flush=True)
            print("CPU Usage: {}%".format(cpu_usage))
            print("Memory Usage: {}%".format(memory_usage))
            print("Network Throughput - Sent: {} bytes, Received: {} bytes".format(sent, received))
            print("Disk Usage: {}%".format(disk_usage))
            print("Disk IO - Read: {} bytes, Write: {} bytes".format(disk_read, disk_write))
            print("Network Packets - Sent: {}, Received: {}".format(packets_sent, packets_recv))
            print("System Uptime: {}".format(system_uptime))
            print("Load Average (1m, 5m, 15m): {:.2f}, {:.2f}, {:.2f}".format(load_avg_1, load_avg_5, load_avg_15))
            print("Running Processes: {}".format(num_processes))
            print("CPU Temperature: {}".format(cpu_temp))
            print("---------------------------------------------- (CTRL + C to exit)", end="", flush=True)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

if __name__ == "__main__":
    main()
#cas de ridder