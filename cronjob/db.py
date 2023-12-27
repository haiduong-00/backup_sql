import subprocess

def backup_postgresql(host, port, username, password, database, backup_path):
    # Format the command string
    command = f'pg_dump -h {host} -p {port} -U {username} -W -Fc -f {backup_path} {database}'
    
    # Execute the command
    subprocess.run(command, shell=True)
    
# Example usage
backup_postgresql('localhost', '5432', 'postgres', 'password', 'postgres', '/home/duong/Documents/backup51.bak')