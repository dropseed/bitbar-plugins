#!/usr/bin/env PYTHONIOENCODING=UTF-8 /usr/local/bin/python3
import requests
from subprocess import check_output


CLIENT_ID, CLIENT_SECRET = (
    check_output(
        [
            "security",
            "find-generic-password",
            "-s",
            "bitbar_helpscout_credentials",
            "-w",
        ]
    )
    .decode("utf-8")
    .strip()
    .split(":")
)

response = requests.post(
    "https://api.helpscout.net/v2/oauth2/token",
    data={
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
    },
)
response.raise_for_status()
access_token = response.json()["access_token"]

session = requests.Session()
session.headers.update({"Authorization": f"Bearer {access_token}"})

response = session.get("https://api.helpscout.net/v2/conversations?status=active")
response.raise_for_status()
try:
    conversations = response.json()["_embedded"]["conversations"]
except KeyError:
    conversations = []

response = session.get("https://api.helpscout.net/v2/mailboxes")
response.raise_for_status()
mailboxes = response.json()["_embedded"]["mailboxes"]

print(
    f"{len(conversations)} | templateImage=iVBORw0KGgoAAAANSUhEUgAAADAAAABICAYAAACwc3YrAAAACXBIWXMAABYlAAAWJQFJUiTwAAAB0klEQVRoBe2ajW2DQAxGP3eBZoSMkBEyQjdoR8gIGYER6CaMwAh0g3YCV24PqaL8+cD4IvmTrCjJBd673AFHQsyMR87TQ9OHQAEJAe+EgHdCwDsh4J0Q8E4IeCcEvBMC3jETIKKzZfs+JgJEVANoiOi0sv0FQEtEN/XO5K7EngVA4DnVfWnbAAT+M7WXx5OGxxJeqlPA93VzERiB598vWAUvVR8uMAU/JTADL9Vo9r15EqcJ+6poL/ANgOeJJo0KwKrnx3pzoef7ejlkCK2Al7oq4Vs1hyF8rYSX9y/mAgCqUuDVAgDOJcHnCNxKgs8RmBv7m+DT0DxbCzRG8H3HqE5iOQJ3Q/h/h14LgasxPK+5gs0WGAwjC3j1MMoRkENpZQTPh16NGsDzYesBI3jWHkpLg6/ULAXBq8b+FoFWCT889O4GrxaQxYYGnufP3pvhcwTGzsST8OkzZvA5AlO9OXlVaQnPGYv6buS1r3T90iq2887Mb8p9j0YrMIRcA/8xeL4b/E+UQ+g0uA24uBgZzJtdhk32HPgDtHollaQ7C3iprL+cya1wZh6bD7u0V7HkCJSU+IXGOyHgnRDwTgh4JwS8EwLeCQHvhIB3QsA7jy0A4BvjGNgHmHpDqAAAAABJRU5ErkJggg=="
)
print("---")

for mailbox in mailboxes:
    mailbox_convos = [x for x in conversations if x["mailboxId"] == mailbox["id"]]

    print(f"{mailbox['name']} ({len(mailbox_convos)})")

    for x in mailbox_convos:
        subject = x["subject"]
        customer = x["createdBy"]["email"]
        url = x["_links"]["web"]["href"]
        print(f"{subject} - {customer} | href={url} length=30")

    print("---")

print("Open HelpScout | href=https://secure.helpscout.net/")
print("Refresh | refresh=true")
