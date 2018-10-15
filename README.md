# bitbar-plugins

Some random plugins for [BitBar](https://github.com/matryer/bitbar).

## HelpScout

Shows active conversations across your mailboxes.

To set it up, you need to create an "App". Just to go "your profile" > "my apps" and create a new one (may as well call it "BitBar").

```sh
# Securely store the credentials on your Mac keychain
security add-generic-password -a $USER -s bitbar_helpscout_credentials -w "client_id:client_secret"

# To install the plugin
open bitbar://openPlugin?src=https://raw.githubusercontent.com/dropseed/bitbar-plugins/master/helpscout.1h.py
```

## ZenDesk

Shows unsolved tickets.

[Create an API token](https://flinthillsdesign.zendesk.com/agent/admin/api/settings/tokens) for your account.

```sh
# Add your email address + created token to your Mac keychain
security add-generic-password -a $USER -s bitbar_zendesk_credentials -w "email_address:token"

# To install the plugin
open bitbar://openPlugin?src=https://raw.githubusercontent.com/dropseed/bitbar-plugins/master/zendesk.1h.py
```
