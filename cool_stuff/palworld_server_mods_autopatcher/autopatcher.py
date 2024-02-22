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