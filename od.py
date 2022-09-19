import config
#import onedrivesdk

import db

"""
def connectod():
    redirect_uri = config.redirect_url
    client_secret = config.client_secret
    client_id = config.client_id
    api_base_url = 'https://api.onedrive.com/v1.0/'
    scopes = ['wl.signin', 'wl.offline_access', 'onedrive.readwrite']

    http_provider = onedrivesdk.HttpProvider()
    auth_provider = onedrivesdk.AuthProvider(
        http_provider=http_provider,
        client_id=client_id,
        scopes=scopes)

    client = onedrivesdk.OneDriveClient(api_base_url, auth_provider, http_provider)
    auth_url = client.auth_provider.get_auth_url(redirect_uri)
    # Ask for the code
    print('Paste this URL into your browser, approve the app\'s access.')
    print('Copy everything in the address bar after "code=", and paste it below.')
    print(auth_url)
    code = input('Paste code here: ')

    client.auth_provider.authenticate(code, redirect_uri, client_secret)
    """

def refreshdb():
    return 0


def refresh():
    p = db.verifyRefreshDate()
    if p == False:
        print("date Error: you can't refresh the database toooo many times!")
        return 1
    else:
        code = refreshdb()
        if code == 0:
            print("successfully refreshed the database!")
            db.updateRefreshDate()
            return 0
        else:
            return 2


#connectod()