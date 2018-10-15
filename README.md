# bitbar-plugins

Some random plugins for [BitBar](https://github.com/matryer/bitbar).

## HelpScout

Shows active conversations across your mailboxes.

To set it up, you need to create an "App". Just to go "your profile" > "my apps" and create a new one (may as well call it "BitBar"). Then, securely store the credentials on your Mac keychain by running: `security add-generic-password -a $USER -s bitbar_helpscout_credentials -w "client_id:client_secret"`

[Install to bitbar](bitbar://openPlugin?src=https://raw.githubusercontent.com/dropseed/bitbar-plugins/master/helpscout.1h.py)
