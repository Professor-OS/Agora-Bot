. ./venv/bin/activate 
- Install the requirements:   <br /> 
pip(3) install -U -r re*/st*/optional-requirements.txt 
pip(3) install -U -r requirements.txt 
- Generate your SESSION: 
  - For Linux users: 
    bash sessiongen 
     or 
    bash -c "$(curl -fsSL https://git.io/JY9JI)" 
  - For Termux users: 
    sh -c "$(curl -fsSL https://git.io/JqgsR)" 
  - For Windows Users: 
    cd desktop ; wget https://git.io/JY9JI -o Agora-Bot.py ; python Agora-Bot.py 
- Fill your details in a .env file, as given in [.env.sample](https://github.com/Professor-OS/Agora-Bot/blob/main/.env.sample). 
(You can either edit and rename the file or make a new file named .env.) 
- Run the bot: 
  - Linux Users: 
   bash resources/startup/startup.sh 
  - Windows Users: 
    python(3) -m pyAgora-Bot 
 
## Necessary Variables 
- SESSION - SessionString for your accounts login session. Get it from [here](#Session-String) 
- REDIS_URI - Redis endpoint URL, from [redislabs](http://redislabs.com/), tutorial [here.](./resources/extras/redistut.md) 
- REDIS_PASSWORD - Redis endpoint Password, from [redislabs](http://redislabs.com/), tutorial [here.](./resources/extras/redistut.md) 
 
## Session String 
Different ways to get your SESSION: 
* [![Run on Repl.it](https://replit.com/badge/github/Professor-OS/Agora-Bot)](https://replit.com/@Professor-OS/Agora-BotStringSession) 
* Linux : bash -c "$(curl -fsSL https://git.io/JY9JI)" 
* PowerShell : cd desktop ; wget https://git.io/JY9JI ; python Agora-Bot.py 
* Termux : sh -c "$(curl -fsSL https://da.gd/termux-tel)" 
* TelegramBot : [@SessionGeneratorBot](https://t.me/SessionGeneratorBot) 
 
Made with 💕 by [@Professor_agora](https://t.me/Professor_agora). <br /> 
 
# License 
Agora-Bot is licensed under [GNU Affero General Public License](https://www.gnu.org/licenses/agpl-3.0.en.html) v3 or later. 
 
[![License](https://www.gnu.org/graphics/agplv3-155x51.png)](LICENSE) 
 
# Credits 
* [![Professor-OS-Devs](https://img.shields.io/static/v1?label=Professor-OS&message=devs&color=critical)](https://t.me/Agora-BotDevs) 
* [Lonami](https://github.com/LonamiWebs/) for [Telethon.](https://github.com/LonamiWebs/Telethon) 
* [MarshalX](https://github.com/MarshalX) for [PyTgCalls.](https://github.com/MarshalX/tgcalls)
