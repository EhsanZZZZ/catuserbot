from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 9380984
    API_HASH = "08393e7c12f2f3a5385a1afef3e9766b"
    # the name to display in your alive message
    ALIVE_NAME = "DrUnknownUser_bot"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://befkwcxw:zF-afPW218yKSW5beNacZcPFb_Ms0NWG@lallah.db.elephantsql.com/befkwcxw"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1BJWap1wBu3c0lFCajxCSQOARgIDLWuGcL-Hp3A3AG2y-l7_ZcAX_UdUlEKR28-ZR1K2QDeLxRJ7-TE4BSmVXQ4cAltjXp5BwglUZYDF1kdP2eib_f0WIBVuIDNZgG4D_ZnmOSaTmVWeqJESJs8vEEzX_ud9N6k86ULsvhjXiNBFVVHN1O9P09o0GGFTVA3O84bOcquIUQDJ-5TsKTXiCD4OY1-cPwN4SH7UtvOleAt8CX1YnTGbSgQK1NzV5p5ONTU-FXK7MIpgRedkmmpcW8nwzasxdFFGDsnH2S1zZLCyNTiTC-gc5Ut1dJDeuz56-iyzwW8qrMW7_DToELm6hFU603iL32e8="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "6103249043: "6103249043:AAEzDGwLGCsYf-NsYns4APuFVcH4FmdyIOE"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1002077340906 
    # command handler
    COMMAND_HAND_LER = "$"
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "$"
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "True"
