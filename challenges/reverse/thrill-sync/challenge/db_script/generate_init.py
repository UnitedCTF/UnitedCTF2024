import hashlib
import random
import string


def generate_password(length=20):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(length))
    return password


class User:
    def __init__(self, username, email, password=None, hash=None):
        self.username = username
        self.email = email
        if password:
            self.password = password
        else:
            self.password = generate_password()

        if hash:
            self.password_hash = hash
        else:
            self.password_hash = hashlib.sha256(self.password.encode()).hexdigest()

    def __str__(self):
        return f"INSERT INTO users (username, password, email) VALUES ('{self.username}','{self.password_hash}','{self.email}');"


class Token:
    def __init__(self, token=None, user_id=None, username=None):
        if token:
            self.token = token
        else:
            self.token = hashlib.sha256(generate_password(40).encode()).hexdigest()

        if username:
            self.username = username
        else:
            self.username = None

        if username:
            self.user_id = None
        else:
            if user_id:
                self.user_id = user_id
            else:
                self.user_id = random.randint(1, 100)

    def __str__(self):
        if self.username:
            return f"INSERT INTO tokens (token, user_id) VALUES ('{self.token}', (SELECT id FROM users WHERE username = '{self.username}'));"
        else:
            return f"INSERT INTO tokens (token, user_id) VALUES ('{self.token}',{self.user_id});"


class Flag:
    def __init__(self, username, flag):
        self.username = username
        self.flag = flag

    def __str__(self):
        return f"INSERT INTO flags (flag, user_id) VALUES ('{self.flag}', (SELECT id FROM users WHERE username = '{self.username}'));"


class Attraction:
    def __init__(self, name, status, calendar):
        self.name = name
        self.status = status
        self.calendar = calendar

    def __str__(self):
        return f"INSERT INTO attractions (name, status, calendar) VALUES ('{self.name}','{self.status}','{self.calendar}');"

usernames = [
User('JohnDoe', 'JohnDoe@gmail.com'),
User('JaneSmith', 'JaneSmith@gmail.com'),
User('MichaelBrown', 'MichaelBrown@gmail.com'),
User('EmilyJohnson', 'EmilyJohnson@gmail.com'),
User('WilliamJones', 'WilliamJones@gmail.com'),
User('OliviaDavis', 'OliviaDavis@gmail.com'),
User('JamesMiller', 'JamesMiller@gmail.com'),
User('SophiaWilson', 'SophiaWilson@gmail.com'),
User('BenjaminMoore', 'BenjaminMoore@gmail.com'),
User('IsabellaTaylor', 'IsabellaTaylor@gmail.com'),
User('ElijahAnderson', 'ElijahAnderson@gmail.com'),
User('MiaThomas', 'MiaThomas@gmail.com'),
User('AlexanderJackson', 'AlexanderJackson@gmail.com'),
User('CharlotteHarris', 'CharlotteHarris@gmail.com'),
User('MatthewThompson', 'MatthewThompson@gmail.com'),
User('AmeliaWhite', 'AmeliaWhite@gmail.com'),
User('DanielMartin', 'DanielMartin@gmail.com'),
User('HarperLee', 'HarperLee@gmail.com'),
User('EthanClark', 'EthanClark@gmail.com', hash='0e10928301293805664131284751240752418731236547650814601298468273'),
User('EvelynWalker', 'EvelynWalker@gmail.com'),
User('JosephYoung', 'JosephYoung@gmail.com'),
User('AbigailAllen', 'AbigailAllen@gmail.com'),
User('DavidHall', 'DavidHall@gmail.com'),
User('ElizabethScott', 'ElizabethScott@gmail.com'),
User('LoganGreen', 'LoganGreen@gmail.com'),
User('SofiaBaker', 'SofiaBaker@gmail.com'),
User('NoahWard', 'NoahWard@gmail.com'),
User('EmilyNelson', 'EmilyNelson@gmail.com'),
User('LiamCarter', 'LiamCarter@gmail.com'),
User('AvaMitchell', 'AvaMitchell@gmail.com'),
User('JacksonPerez', 'JacksonPerez@gmail.com'),
User('HarperRoberts', 'HarperRoberts@gmail.com'),
User('AidenTurner', 'AidenTurner@gmail.com'),
User('EmmaPhillips', 'EmmaPhillips@gmail.com'),
User('SamuelCollins', 'SamuelCollins@gmail.com'),
User('GraceStewart', 'GraceStewart@gmail.com'),
User('GabrielReed', 'GabrielReed@gmail.com'),
User('ChloeCox', 'ChloeCox@gmail.com'),
User('RyanHoward', 'RyanHoward@gmail.com'),
User('ZoeWright', 'ZoeWright@gmail.com', password='425kailua'),
User('ThomasCampbell', 'ThomasCampbell@gmail.com'),
User('VictoriaPeterson', 'VictoriaPeterson@gmail.com'),
User('CharlesBeck', 'CharlesBeck@gmail.com'),
User('AveryEvans', 'AveryEvans@gmail.com'),
User('MateoEdwards', 'MateoEdwards@gmail.com'),
User('StellaParker', 'StellaParker@gmail.com'),
User('DanielRichardson', 'DanielRichardson@gmail.com'),
User('ScarlettWood', 'ScarlettWood@gmail.com'),
User('AnthonyWatson', 'AnthonyWatson@gmail.com'),
User('MadisonBrooks', 'MadisonBrooks@gmail.com'),
User('JoshuaFoster', 'JoshuaFoster@gmail.com'),
User('LunaGray', 'LunaGray@gmail.com'),
User('CarterMorris', 'CarterMorris@gmail.com'),
User('LilyMurphy', 'LilyMurphy@gmail.com'),
User('OwenBell', 'OwenBell@gmail.com'),
User('AriaSanders', 'AriaSanders@gmail.com'),
User('DylanRoss', 'DylanRoss@gmail.com'),
User('PenelopeOrtiz', 'PenelopeOrtiz@gmail.com'),
User('LukeHenderson', 'LukeHenderson@gmail.com'),
User('LaylaColeman', 'LaylaColeman@gmail.com'),
User('AsherRamirez', 'AsherRamirez@gmail.com'),
User('RileyGrant', 'RileyGrant@gmail.com'),
User('JonathanPerry', 'JonathanPerry@gmail.com'),
User('ChloePrice', 'ChloePrice@gmail.com'),
User('ChristianSanchez', 'ChristianSanchez@gmail.com'),
User('HazelPowell', 'HazelPowell@gmail.com'),
User('JoseLong', 'JoseLong@gmail.com'),
User('MadisonFoster', 'MadisonFoster@gmail.com'),
User('JacobReynolds', 'JacobReynolds@gmail.com'),
User('EllaHunter', 'EllaHunter@gmail.com'),
User('LeviHayes', 'LeviHayes@gmail.com'),
User('AddisonJenkins', 'AddisonJenkins@gmail.com'),
User('GabrielPatterson', 'GabrielPatterson@gmail.com'),
User('NoraSimmons', 'NoraSimmons@gmail.com'),
User('EliJordan', 'EliJordan@gmail.com'),
User('LillianReed', 'LillianReed@gmail.com'),
User('WyattHudson', 'WyattHudson@gmail.com'),
User('ZoeGibson', 'ZoeGibson@gmail.com'),
User('GabrielLloyd', 'GabrielLloyd@gmail.com'),
User('AveryMason', 'AveryMason@gmail.com'),
User('JaydenGraham', 'JaydenGraham@gmail.com'),
User('AriaKim', 'AriaKim@gmail.com'),
User('LucasKnight', 'LucasKnight@gmail.com'),
User('AveryWard', 'AveryWard@gmail.com'),
User('MasonPorter', 'MasonPorter@gmail.com'),
User('AveryCruz', 'AveryCruz@gmail.com'),
User('EthanFisher', 'EthanFisher@gmail.com'),
User('HarperWatkins', 'HarperWatkins@gmail.com'),
User('GabrielHart', 'GabrielHart@gmail.com'),
User('EvelynCrawford', 'EvelynCrawford@gmail.com'),
User('JosiahAustin', 'JosiahAustin@gmail.com'),
User('EmiliaRussell', 'EmiliaRussell@gmail.com'),
User('MaddoxBurns', 'MaddoxBurns@gmail.com'),
User('HarperHarrison', 'HarperHarrison@gmail.com'),
User('CarterSutton', 'CarterSutton@gmail.com'),
User('AmeliaPowers', 'AmeliaPowers@gmail.com'),
User('OliverPierce', 'OliverPierce@gmail.com'),
User('AveryGomez', 'AveryGomez@gmail.com'),
User('CalebMoreno', 'CalebMoreno@gmail.com'),
User('ScarlettShaw', 'ScarlettShaw@gmail.com')
]

tokens = [
Token() for i in range(1000)
]

tokens[623] = Token(username='HarperWatkins')

flags = [
Flag('EthanClark', 'flag-PHP_m4g1c_h4sh_3897568204d82619'),
Flag('ZoeWright', 'flag-P4ssw0rd_Spr4y_3cb3029478777704167e1a'),
Flag('HarperWatkins', 'flag-S3ssi0n_H1jack1ng_7d73cacb3dd28'),
Flag('CarterMorris', 'flag-R4c3_c0d1tion_91de6d9165949e'),
]

attractions = [
Attraction('Alien Autopsy', 'open', '''Monday: 8:00 AM - 6:00 PM
Tuesday: 8:00 AM - 6:00 PM
Wednesday: 8:00 AM - 6:00 PM
Thursday: 8:00 AM - 6:00 PM
Friday: 8:00 AM - 8:00 PM
Saturday: 8:00 AM - 8:00 PM
Sunday: Closed'''),
Attraction('The Phantom''s Phantom','open','''Monday: 9:00 AM - 5:00 PM
Tuesday: 9:00 AM - 5:00 PM
Wednesday: 9:00 AM - 5:00 PM
Thursday: 9:00 AM - 5:00 PM
Friday: 9:00 AM - 7:00 PM
Saturday: 9:00 AM - 7:00 PM
Sunday: Closed'''),
Attraction('Food stand','open','''Monday: 9:00 AM - 5:00 PM
Tuesday: 9:00 AM - 5:00 PM
Wednesday: 9:00 AM - 5:00 PM
Thursday: 9:00 AM - 5:00 PM
Friday: 9:00 AM - 7:00 PM
Saturday: 9:00 AM - 7:00 PM
Sunday: Closed'''),
Attraction('Dragon''s Keep','shutdown','''Monday: 9:00 AM - 5:00 PM
Tuesday: 9:00 AM - 5:00 PM
Wednesday: 9:00 AM - 5:00 PM
Thursday: 9:00 AM - 5:00 PM
Friday: 9:00 AM - 7:00 PM
Saturday: 9:00 AM - 7:00 PM
Sunday: Closed'''),
Attraction('The Invisible Man','open','''Monday: 9:00 AM - 5:00 PM
Tuesday: 9:00 AM - 5:00 PM
Wednesday: 9:00 AM - 5:00 PM
Thursday: 9:00 AM - 5:00 PM
Friday: 9:00 AM - 7:00 PM
Saturday: 9:00 AM - 7:00 PM
Sunday: Closed'''),
Attraction('Time Twist Temporal Coaster','reparation', '''Monday: 9:00 AM - 5:00 PM
Tuesday: Closed
Wednesday: Closed
Thursday: 9:00 AM - 5:45 PM
Friday: 9:00 AM - 7:00 PM
Saturday: 9:30 AM - 7:00 PM
Sunday: Closed''')
]

with open('init.sql', 'w') as f:
    delete_everything = '''DELETE FROM users;
DELETE FROM tokens;
DELETE FROM flags;
DELETE FROM attractions;\n\n'''
    f.write(delete_everything)

    for user in usernames:
        f.write(str(user) + '\n')
    f.write('\n')
    for token in tokens:
        f.write(str(token) + '\n')
    f.write('\n')
    for flag in flags:
        f.write(str(flag) + '\n')
    f.write('\n')
    for attraction in attractions:
        f.write(str(attraction) + '\n')
