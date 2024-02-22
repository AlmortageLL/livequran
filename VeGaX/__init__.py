from VeGaX.core.bot import Ayush
from VeGaX.core.dir import dirr
from VeGaX.core.git import git
from VeGaX.core.userbot import Userbot
from VeGaX.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Ayush()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
