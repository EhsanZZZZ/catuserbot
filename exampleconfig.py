from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 17790826
    API_HASH = "dcdcd1a4e92fed00366d59f1e315b285"
    # the name to display in your alive message
    ALIVE_NAME = "DrUnknownUser_bot"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://nrtkpgyj:xhkvFxg91NxiPHyoa5ct530Lz9APNVZn@jelani.db.elephantsql.com/nrtkpgyj"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1BVtsOJwBu3izYZU3FmRLL6gFWig3VtPxFZbcR3z36_J7AIGzuv8CEvGYRYJ1UiMrNDaYF-rndOj_ch6Mvi5060Df21HRepeR1KkMOARRu8ElypIxseT9lBElNgD-5jmG895D1eFfkGIg4B9tmLhrDEJyHG7MdgHnJzsfKia2EZSRkc4-VzeF7LyJ-jLdjBruOVZAIOcXFZ35q_030_jLS2FNwYA6gTvqdhf3sf9Uj3hed4pzC4nHogd2rT0RfdsVSfdkpPNGsliPDMZfGAvsopjsUO68v_y0WBIhILu8EAu-6e261hfXDHItNljdPD69rhtfO8NfI80X2HVnRGU8tSuDa1eKxKA="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "6103249043:AAEzDGwLGCsYf-NsYns4APuFVcH4FmdyIOE"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1001818556010
    # command handler
    COMMAND_HAND_LER = "$"
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "$"
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "True"
