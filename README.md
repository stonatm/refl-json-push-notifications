# Refl: Free JSON Push Notifications and Messages ![refl.png](refl.png)

Simple python script thats sends your custom message as response to request from Refl android app.

## Requirements

- linux system with python3 interpreter installed
- android app:
[Google Play Store](https://play.google.com/store/apps/details?id=me.refl)

## Quick install guide
- download python script: [refl.py](refl.py)
- edit script to customize response
- edit crontab to run automatically script with system reboot

```
crontab -e
```

- add below line:

```
@reboot python3 ./PATH/TO/YOUR/SCRIPT/refl.py &
```

- save file and reboot system

## Response customization
Find in source file this section and change to your own values

```
#create response headers
refl = True
notification = False
sound = False
vibration = False
stealth = True
refresh = 288

# create response message
title = "MESSAGE TITLE"
image_url = None
message = "MESSAGE CONTENT"
```

The **refl** key must always be true, otherwise an error will be called.

The **message** key is responsible for the notification text (max 360 characters). Empty "message" is ignored.

**title** - notification title (maximum 36 characters).

**image** - http(s) reference to the image.

**refresh** - number of checks in 24 hours (0 - manual update, 288 - maximum, 96 - default).

**stealth** - set "true" if you want to covertly update the data on the user's device without any notifications.

**notification** - set "false" if you want to disable the text notification on the user's device.

**sound** - set "false" if you want to disable the sound notification on the user's device.

**vibration** - set "false" if you want to disable the vibration notification on the user's device.
