import datetime
import os
import shutil
import configparser

# Tạo đối tượng ConfigParser
config = configparser.ConfigParser()
data  = configparser.ConfigParser()

# Mở file settings.ini
config.read("settings.ini")
data.read("data.ini")

# Lấy giá trị của biến database_host
config_file = config['Default']["path_dir"]
data_file = config['DEFAULT']

print("???", config['DEFAULT']['username'])
# config_file = 'path/to/config/file.ini'  # Replace with the path to your config file

# backup_dir = 'path/to/backup/folder'  # Replace with the path to your backup folder
# os.makedirs(backup_dir, exist_ok=True)

now = datetime.datetime.now()

year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
# backup_filename = f"{data_file['username']}_{data_file['database']}_{year}-{month:02d}-{day:02d}_{hour:02d}-{minute:02d}.bak"
# shutil.copy(config_file, backup_filename)

# print(f"Config file backed up to: {backup_file}")

print(config_file)
