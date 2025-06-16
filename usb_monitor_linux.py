
import pyudev
from notifier import notify

def monitor_usb():
    context = pyudev.Context()
    monitor = pyudev.Monitor.from_netlink(context)
    monitor.filter_by(subsystem='usb')
    print("[*] Monitoring USB devices. Press Ctrl+C to stop.")
    for device in iter(monitor.poll, None):
        if device.action == 'add':
            message = f"USB Inserted: {device}"
            print(f"[ALERT] {message}")
            notify("USB Inserted", message)
        elif device.action == 'remove':
            message = f"USB Removed: {device}"
            print(f"[ALERT] {message}")
            notify("USB Removed", message)

if __name__ == "__main__":
    monitor_usb()