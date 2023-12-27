import configparser
import datetime as dt
import os

# Tạo đối tượng ConfigParser
config = configparser.ConfigParser()

# Mở file settings.ini
config.read("settings.ini")

# Lấy giá trị của biến database_host

def delete_old_backups():
    backup_folder = config["Default"]["path_dir"]
    
    # Số ngày quy định để giữ lại backup
    days_to_keep = config["Default"]["DAYS_TO_KEEP"]
    days_to_keep = int(days_to_keep)

    current_date = dt.datetime.now()

    for filename in os.listdir(backup_folder):
        file_path = os.path.join(backup_folder, filename)

        if os.path.isfile(file_path) and filename.endswith(".bak"):
            # Lấy thông tin thời gian tạo của tệp
            creation_time = dt.datetime.fromtimestamp(os.path.getctime(file_path))

            days_difference = (current_date - creation_time).days
            print("days_difference", days_difference)

            # Nếu tệp cũ hơn số ngày quy định, thì xóa nó
            if days_difference > days_to_keep:
                os.remove(file_path)
                print(f"Deleted old backup: {filename}")

    print("Old backups deleted successfully.")

# Gọi hàm để thực hiện xóa các tệp backup cũ
delete_old_backups()
