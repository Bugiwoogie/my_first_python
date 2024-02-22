import requests
import ftplib
import pprint
from credentials import NEXUS_USERNAME, NEXUS_PASSWORD, FTP_SERVER_URL, FTP_USERNAME, FTP_PASSWORD

# Connect to Nexus Mods
login_url = 'https://users.nexusmods.com/auth/sign_in'
session = requests.session()

# Authenticate
login_data = {
    'login': NEXUS_USERNAME,
    'password': NEXUS_PASSWORD,
    'loginform': 'loginform',
    'stayloggedin': 'false'
}
print(session.post(login_url, data=login_data))
pprint.pprint(session)

# now i need to know the version of the installed mod and then i check for the version on the modding page.
# when version on modding page is higher, download the new files and place them on the server
# also making a backup before manipulating the servers files
# i need a text file, with the url for the mod and the installed version on the server
# when the patcher downloads a newer version, the textfile is being edited by this script to change the version number

# Get mod information
mod_url = 'https://www.nexusmods.com/mods'
response = session.get(mod_url)

# Parse mod information and check for updates

# Download updates if available

# Upload files via FTP to gaming server
# ftp = ftplib.FTP(FTP_SERVER_URL, FTP_USERNAME, FTP_PASSWORD)
# Perform FTP operations here

# Close FTP connection
# ftp.quit()