from ftplib import FTP

class FTPClient:
    def __init__(self, host, username, password):
        self.ftp = FTP(host)
        self.ftp.login(username, password)
        self.processed_files = set()
        print("Connected successfully")

    def list_files(self):
        files = self.ftp.nlst()
        print("Files on server:", files)
        return files

    def download_file(self, filename, local_path):
        with open(local_path, 'wb') as f:
            self.ftp.retrbinary(f'RETR {filename}', f.write)
        print(f"File downloaded successfully: {filename}")


# --- RUN THE CLIENT ---
client = FTPClient("ftp.example.com", "user", "pass")

files = client.list_files()

client.download_file("test.txt", "test_local.txt")





