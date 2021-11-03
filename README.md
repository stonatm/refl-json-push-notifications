# Refl: Free JSON Push Notifications and Messages ![refl.png](refl.png)

Simple python scripts thats sends your custom message as response to request from Refl android app.

## Requirements

- linux system with python3 interpreter installed
- android app:
[Google Play Store](https://play.google.com/store/apps/details?id=me.refl)

## Quick install guide
- download python script: [refl.py](refl.py)
- edit script to customize response
- edit crontab

```
crontab -e
```

- add below line:

```
@reboot python3 ./PATH/TO/YOUR/SCRIPT/refl.py &
```

- save file and reboot system
