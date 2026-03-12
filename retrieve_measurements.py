# -*- coding: utf-8 -*-
"""
Created on Thu Jul 17 12:29:27 2025

@author: vriesen
"""

from ftplib import FTP
from datetime import datetime
import os

# Configuratie
ftp_host = 'dataservices.koenders-instruments.com'
ftp_user = 'HMVT'
ftp_pass = '193yhbk#U'
remote_path = r'/upload data/S9081 HMVT CR1000X_measurements.dat'
local_path = r'C:\Users\vriesen\OneDrive - KWR Water\GitHub\SWAP_analysis\S9081 HMVT CR1000X_measurements.dat'

def get_remote_mod_time(ftp, filename):
    """Haalt de laatste wijzigingsdatum van een bestand op via MDTM"""
    response = ftp.sendcmd(f'MDTM {filename}')
    remote_time_str = response[4:].strip()
    return datetime.strptime(remote_time_str, '%Y%m%d%H%M%S')

def get_local_mod_time(filepath):
    """Geeft de lokale bestandstijd terug als datetime object"""
    if not os.path.exists(filepath):
        return None
    timestamp = os.path.getmtime(filepath)
    return datetime.fromtimestamp(timestamp)

def show_tail_of_file(filepath, num_lines=1):
    """Toont de laatste N regels van het bestand."""
    with open(filepath, 'rb') as f:
        # Lees de laatste ~10 kB van het bestand
        f.seek(0, os.SEEK_END)
        filesize = f.tell()
        seek_offset = min(filesize, 10240)
        f.seek(-seek_offset, os.SEEK_END)
        lines = f.readlines()[-num_lines:]
    
    print(f"\nLast line of new file:")
    for line in lines:
        try:
            data = line.decode('utf-8').strip()
            values = data.split(',')
            print(f'date: {values[0]}, redox (CW2S1-4) = {float(values[22])+200} mV, and voltage of battery = {float(values[2])}')
        except UnicodeDecodeError:
            print("[Niet leesbare regel]")


def download_file():
    with FTP(ftp_host) as ftp:
        ftp.login(ftp_user, ftp_pass)

        remote_dir, remote_file = os.path.split(remote_path)
        ftp.cwd(remote_dir)

        remote_time = get_remote_mod_time(ftp, remote_file)
        local_time = get_local_mod_time(local_path)

        print(f"Remote: {remote_time}, Local: {local_time}")

        if not local_time or remote_time > local_time:
            print("Nieuw bestand gevonden. Downloaden...")
            with open(local_path, 'wb') as f:
                ftp.retrbinary(f'RETR {remote_file}', f.write)
            print("Download voltooid.")
            show_tail_of_file(local_path)  # ⬅️ Toegevoegd
        else:
            raise Exception(f"Geen nieuw bestand gevonden op de FTP-server. Remote: {remote_time}, Local: {local_time}")
            


if __name__ == "__main__":
    download_file()
