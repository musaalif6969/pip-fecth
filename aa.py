import subprocess
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import urllib.request
import sys

# Check and install required modules if not found
try:
    import Pillow
except ImportError:
    subprocess.run([sys.executable, "-m", "pip", "install", "Pillow"])

try:
    import tkinter
except ImportError:
    subprocess.run([sys.executable, "-m", "pip", "install", "tkinter"])

def restart_pc():
    subprocess.run(["shutdown.exe", "/r", "/t", "00"])

def activate():
    subprocess.run(["taskkill", "/f", "/im", "explorer.exe"])  # Kill Explorer
    activation_keys = [
        "TX9XD-98N7V-6WMQ6-BX7FG-H8Q99",
        "3KHY7-WNT83-DGQKR-F7HPR-844BM",
        "7HNRX-D7KGG-3K4RQ-4WPJ4-YTDFH",
        "PVMJN-6DFY6-9CCP6-7BKTT-D3WVR",
        "W269N-WFGWX-YVC9B-4J6C9-T83GX",
        "MH37W-N47XK-V7XM9-C7227-GCQG9",
        "NW6C2-QMPVW-D7KKK-3GKT6-VCFB2",
        "2WH4N-8QGBV-H22JP-CT43Q-MDWWJ",
        "NPPR9-FWDCX-D2C8J-H872K-2YT43",
        "DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4",
        "WNMTR-4C88C-JK8YV-HQ7T2-76DF9",
        "2F77B-TNFGY-69QQF-B8YKP-D69TJ"
    ]

    for key in activation_keys:
        subprocess.run(["cscript", "//nologo", "c:\\windows\\system32\\slmgr.vbs", "/ipk", key], stdout=subprocess.DEVNULL)

    kms_servers = [
        "kms.chinancce.com",
        "NextLevel.uk.to",
        "GuangPeng.uk.to",
        "AlwaysSmile.uk.to",
        "kms.shuax.com"
    ]

    for i, server in enumerate(kms_servers):
        print("************************************\n")
        print(f"Trying KMS Server {i + 1}/{len(kms_servers)}: {server}")
        subprocess.run(["cscript", "//nologo", "c:\\windows\\system32\\slmgr.vbs", "/skms", server], stdout=subprocess.DEVNULL)
        
        activation_result = subprocess.run(["cscript", "//nologo", "c:\\windows\\system32\\slmgr.vbs", "/ato"], stdout=subprocess.PIPE, text=True)
        
        if "successfully" in activation_result.stdout.lower():
            print("\nActivation successful!")
            choice = messagebox.askyesno("Activation Successful", "Do you want to restart your PC now?")
            if choice:
                restart_pc()
            subprocess.run(["explorer.exe"])  # Start Explorer again
            break
        else:
            print("\nThe connection to the server failed! Trying to connect to another one...\nPlease wait...\n")

root = tk.Tk()
root.title("Midnight Co")
root.geometry("400x220")  # Wider GUI

# Download the image and display it
image_url = "https://raw.githubusercontent.com/musaalif6969/krunker/main/logo.png"
with urllib.request.urlopen(image_url) as url:
    image_data = url.read()
    with open("logo.png", "wb") as f:
        f.write(image_data)

image = Image.open("logo.png")
photo = ImageTk.PhotoImage(image)
logo_label = tk.Label(root, image=photo)
logo_label.pack(pady=10)

activation_button = tk.Button(root, text="Activate Windows", command=activate)
activation_button.pack(pady=10)

root.mainloop()
