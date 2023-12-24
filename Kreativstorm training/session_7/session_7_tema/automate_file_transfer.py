import ftplib
import os

HOSTNAME = 'ftp.dlptest.com'
port = 21
USERNAME = 'dlpuser'
PASSWORD = 'rNrKYTX9g7z3RgJRmxWuGHbeu'
file_1 = 'test_ftp.txt'
file_2 = 'test_2_ftp.txt'

remote_dir = ''
local_dir = ''

# connect the ftp server
ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)
# ftp_server.dir()
# store files_to_upload on the server
# with open(file_2, 'rb') as file:
#     ftp_server.storbinary(f"STOR {file_2}", file)
#
#     ftp_server.dir()

# download the files
# with open(file_1, "wb") as file:
#     ftp_server.retrbinary(f"RETR {file_1}", file.write)


# close the FTP connection
# ftp_server.quit()