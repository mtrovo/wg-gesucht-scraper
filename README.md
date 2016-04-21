# wg-gesucht-scraper
Scraper for wg-gesucht that sends emails on new apartment posts

## Building
Same old pip install -r requirements.txt

To make the trick with mail work you need to config postfix on your machine to make the command `mail` work.
On Mac you can follow this tutorial: https://benjaminrojas.net/configuring-postfix-to-send-mail-from-mac-os-x-mountain-lion/

## Running
The script scraper executes and extract the last posts from wg-gesucht one time.

If you wanna be notified for new posts in a time interval you can use some bash to make it work.

For example to run it on a 10 minutes interval run it like this:
```
while sleep 600; do python scraper.py > body.tmp && cat body.tmp | mail -s "New Apartment $(date +'%d.%m %H:%M')" your_email@here
```

You should receive an email every 10 minutes when there's a new post, when there's no new post, no email is sent :+1:.

