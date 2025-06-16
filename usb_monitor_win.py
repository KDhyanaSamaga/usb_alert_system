
import win32file
import win32con
import time
from notifier import notify

def get_usb_drives():
    drives = []
    bitmask = win32file.GetLogicalDrives()
    for letter in range(26):
        if bitmask & (1 << letter):
            drive = f"{chr(65 + letter)}:\\"
            drive_type = win32file.GetDriveType(drive)
            if drive_type == win32con.DRIVE_REMOVABLE:
                drives.append(drive)
    return set(drives)

def monitor_usb():
    print("[*] Monitoring USB drives. Press Ctrl+C to stop.")
    previous = get_usb_drives()

    try:
        while True:
            time.sleep(2)
            current = get_usb_drives()
            inserted = current - previous
            removed = previous - current
            if inserted:
                message = f"USB Inserted: {', '.join(inserted)}"
                print(f"[ALERT] {message}")
                notify("USB Inserted", message)
            if removed:
                message = f"USB Removed: {', '.join(removed)}"
                print(f"[ALERT] {message}")
                notify("USB Removed", message)
            previous = current
    except KeyboardInterrupt:
        print("\n[*] Monitoring stopped.")

if __name__ == "__main__":
    monitor_usb()