from tweepy import API
from tweepy import Cursor
from tweepy import OAuthHandler

import json
import re


class TwitterAuthenticator():
    '''
    Twitter authentication
    '''
    def authenticateTwitterApp(self):
        twitterkey = {}
        with open("Twitterkey.json") as json_file:
            twitterkey = json.load(json_file)

        auth = OAuthHandler(twitterkey["consumer_key"],twitterkey["consumer_secret"])
        auth.set_access_token(twitterkey["access_token"],twitterkey["access_token_secret"])
        return auth


class TwitterClient():
    '''
    Client reader for various Twitter accounts
    '''
    def __init__(self, twitter_user=None):
        self.auth = TwitterAuthenticator().authenticateTwitterApp()
        self.twitter_client = API(self.auth,wait_on_rate_limit=True)
        self.twitter_user = twitter_user

    def get_twitter_client_api(self):
        return self.twitter_client

    def getUserTweets(self, num=None):
        tweets = []
        for tweet in Cursor(self.twitter_client.user_timeline, id=self.twitter_user,tweet_mode='extended',wait_on_rate_limit=True).items(num):
            tweets.append(tweet)
            
        return tweets


class TextParser():
    def removeLink(self,text):
        text_list = text.split(' ')

        text_list = [word for word in text_list if ("https://t.co/" not in word)]
        text = ' '.join(text_list)
        return(text)

    def removeEmoji(self,text):
        return text.encode('ascii', 'ignore').decode('ascii')

    def removeEntities(self,text):
        text = text.replace('&gt;','>')
        text = text.replace('&lt;','<')
        text = text.replace('&amp;','&')
        return text

    def removeWhitespace(self,text):
        text = text.replace('\n',' ')
        text = re.sub(' +',' ',text)
        return text
    

class wordDB():
    def __init__(self):
        self.users = []
        self.rawText = str()
        self.tweets = []

    def runAnalysis(self):
        client = TwitterClient()
        #api = client.get_twitter_client_api()

        for user in self.users:
            try:
                client.twitter_user = user
                print(f"Collecting data for {user}!~")
                tweets = client.getUserTweets(10)
                for text in [tweet.full_text for tweet in tweets]:
                    self.rawText += ' ||| '+text
                
            except Exception as e:
                print(f"Could not collect data for {user}!\n{e}")
    
    def cleanupText(self):
        self.rawText = self.rawText.rstrip()
        self.rawText = TextParser().removeLink(self.rawText)
        self.rawText = TextParser().removeEmoji(self.rawText)
        self.rawText = TextParser().removeEntities(self.rawText)
        self.rawText = TextParser().removeWhitespace(self.rawText)
        self.rawText = self.rawText.casefold()
    
    def splitIntoTweets(self):
        self.tweets = self.rawText.split(' ||| ')
        self.tweets.pop(0)
    



def main():
    wdb = wordDB()
    wdb.users = ['zenithO_o','vandercat','Koorivlf','Lydemox','ZigZaggyZagg','oddafterdark','Painteddoq','SplashFusky','Kiro_Fennec','PunyPunyMouse','eeeeeeeson',
    'FrostThusky','chipfoxx','AshCoyote','inkiioni','EbiManokit','RazzDagon','chancehusky91','Avero_Stripes','R0rek','Splinter_Fox','ThatKrazyK9',
    'FlukeHusky','Aikowolf','FoxWithGuitar','Mocha_Aura','Malka_lion','That_One_Wofie','DeStar_Paw','greeny_woof','VandertheFolf','FoxNobia',
    'tobythefox28','PantherMage','maxxthefoxx','Kaomoro97','Shi_Tsume','TheGayJediAwoo','FibreKitty','DonDrakore','squeaklatex','DeliriousCorgi',
    'KitaKettu','KaimTime','fuchstraumer','timburrs','KyashKT','MysteryPaws','mango_husky','kinterdeer','Talcen','OrioMrow','ChatahSpots','CassiusF0x',
    'TheDizziest','Plush_Thoughts','frengersfur','Flotianchroma','norfdog','ShobaPaw','SepiaPaws','VassellChenelle','tallfuzzball','sparkpanda',
    'TeddyWynton','aejb_','5ushiroll','hiver_wolf','colliethecutie','Angelar24555510','Smart_Protogen','ZatchTheProto','TelstarProtogen',
    'cole_owo_bull','Cozwart1','MangoFox6','GlitchyFur','kaiserthebloo','Kiwi_Foxx','MoriMutt','DarkPhox','MastersRex','tmaxxnc','renegade_roo','ZincAwesome',
    'wryote','homphs','FireHazardCat','TukioAWD','TamariLion','syrianbryn','DatBlueHusky','Kurtt_Wuff','Lutufox','KitaKettu','DeiviHusky','SonoxxLion',
    'Meikurey','shane_deepwood','t0rafusky','BubblesPopAD','BigFruityWolf','DatHuskyAD','SnowSluttycat','CennyAD','Sulo_AD','_Sulo_','AardwolfEssex',
    'TavvyTiggy','BenzoHusky','MadeFurYou','phoenixwuff','VixNdwnq','BerryMeatArt','LongTailLaser','phoenixtheblade','vexwerewolf','CarcinLoring',
    'True_N8ure','SergalProjects','NatalyaGrey','WiccanRaccoon','KohtaloJC','unklesanik','just_leg','kobra_km','cryingbabydolls','BeatriceTheDeer',
    'radarrubbish','Sky_Fox_OwO','GayFuzzBall','Porxis','clayfurrrwhat','LilicSharp','OzzyTheOttsel','NorthySoren','Purols_','AboWoofers','MysticSnep',
    'KelwingDev','JasperSoot','FoxCobalt','OridtheCat','ArchieInSpace','TeaCatsCO','Asuvir_Bleats','NarukaLewd','Ronkeyroo','ThisBeSpitfire','TheFurstrument',
    'Mad__Machine','Krysiilys','yodelinyote','CEvandor','ClovisMint','Tropinck','PaskeeWusky','wereshiba','Neungsonie','wildsabercat','Kissyander',
    'phoenix_atlas','AceTheBlueWolf','magicalmoss','PIBBLEBITCH','Tikrekins','sherwiind','TinyDragon_Art','BobbyLontra','RamuneTigress','sailorrooscout',
    'Boltie_','merzb0w','TheRoyalGryphon','noronorii','Tsapushka','lukamaru','TwistHound','ShadowSOVKA','heresvix','MoxyJW','Noonek_co','cyamallo',
    'rottingseams','servalien','VenusHound','inkiioni','Kitchiki','LorekeeperWren','Pyttinski','Crash_Azarel','KaimTime','AtlasInu','Blajnart','DinkysaurusART',
    'MangopoptartART','FirriApril','BlakeeRoseyy','ThatsFurredUp','Chibbutts','OneCoolCanine','eclipticafusion','ploommy','SaberZelgrath','SnowRealm',
    'sei_kasu','sappycats','Foxtotss','opryee','nanalebae','Shikokubo','so_very_angry','Flooderino','TouyaKemone','bigboarjun','junichidraws','Art_Mutt',
    'LatchFox','solisthewolf','AtheoFreak','DarteriRoo','Peche_Eh','sailorrooscout','redTuwka','AyleenDeer','FrameshiftShark','KaeEsrial','CyrakhisDragon',
    'Yamishizen','fuchstraumer','hounds_teeth','CertifiedLeggy','dravendraws','pawgazer','crabbyraccoon','MOSFETbah','inksty','Growlbeast','Gingerbread_C',
    'poodlewool','kovolte','nrthss','softncrisp','lynxsprout','scyffi','osmoru','PhennieMeow','Skaifox','mestisoart','MestisoTiger','Teaselbone','rockiespeon','peachy_bat',
    'MochiIsaMonster','snow_kun','HoundGrey','Riisago','HumphreyMuski','ollisterwolf','Svixy','AceShepherd','TaniDaReal','FoxAmoore','Punk_Bat','Ambris_Art',
    'Qualzar','thekilinah','NicOpossum','ShniderMoon','slash0x','ShanetheWilddog','syrianbryn','ValeFuchs','JFETspeaks','Jinx_In_Boots','murkbone','dmnckh','puppkun',
    'soilpossum','beelzbat']

    wdb.runAnalysis()
    wdb.cleanupText()
    wdb.splitIntoTweets()

    print("File saved!~")
    with open('data.json','w') as json_file:
        json.dump({"rawText":wdb.rawText,"Tweets":wdb.tweets},json_file)
    
if __name__ == "__main__":
    main()
    