# bitbar-plugins

Some random plugins for [BitBar](https://github.com/matryer/bitbar). If you have homebrew, and easy way to install bitbar is `brew cask install bitbar`.

## HelpScout

Shows active conversations across your mailboxes.

To set it up, you need to create an "App". Just to go "your profile" > "my apps" and create a new one (may as well call it "BitBar").

```sh
# Securely store the credentials on your Mac keychain
security add-generic-password -a $USER -s bitbar_helpscout_credentials -w "your_client_id:your_client_secret"

# Install the plugin
open bitbar://openPlugin?src=https://raw.githubusercontent.com/dropseed/bitbar-plugins/master/helpscout.1h.py
```

## ZenDesk

Shows unsolved tickets.

[Create an API token](https://flinthillsdesign.zendesk.com/agent/admin/api/settings/tokens) for your account.

```sh
# Add your email address + created token to your Mac keychain
security add-generic-password -a $USER -s bitbar_zendesk_credentials -w "your_email_address:your_token"

# Install the plugin
open bitbar://openPlugin?src=https://raw.githubusercontent.com/dropseed/bitbar-plugins/master/zendesk.1h.py
```

## Time

Shows UTC time in the menu bar, and a few timezones when you click on it. Makes it a little easier to translate UTC time if you spend a lot of time looking at logs and things where dates are printed in UTC.

```sh
# Install the plugin
open bitbar://openPlugin?src=https://raw.githubusercontent.com/dropseed/bitbar-plugins/master/time.30s.sh
```

## Week number

Shows the current week number in the menu bar (ex. "Week 11"). That's it.

```sh
# Install the plugin
open bitbar://openPlugin?src=https://raw.githubusercontent.com/dropseed/bitbar-plugins/master/week.6h.sh
```

## Docker

Shows the number of running docker containers and gives quick menu links to kill them.

```sh
# Install the plugin
open bitbar://openPlugin?src=https://raw.githubusercontent.com/dropseed/bitbar-plugins/master/docker.10m.py
```
