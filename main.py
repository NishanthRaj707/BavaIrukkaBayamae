from yt_dlp import YoutubeDL
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button,ButtonBehavior
from kivy.lang import Builder
from kivy.core.text import LabelBase
from kivy.uix.videoplayer import VideoPlayer
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen,ScreenManager,SlideTransition
from kivy.properties import ListProperty,StringProperty
import threading
import time,os

os.environ['KIVY_VIDEO'] = 'ffpyplayer'

LabelBase.register(name='myfont', fn_regular='assets/nightmare.ttf')

Builder.load_file("ytclone.kv")

class Player(Screen):
    video_url=StringProperty("")
    def __init__(self, **kw):
        super().__init__(**kw)
    
    def on_video_url(self,instance,value):
        if value:
            self.ids.video_engine.state="play"
            self.ids.video_engine.source=value

    def stop_and_go_back(self):
        self.ids.video_engine.state="stop"
        self.ids.video_engine.source=""
        self.manager.transition=SlideTransition(direction="right",duration=1)
        self.manager.current='menu'

class MenuCard(ButtonBehavior,BoxLayout):
    title=StringProperty("")
    thumbnail=StringProperty("")
    url=StringProperty("")
    duration=StringProperty("")
    original_url=StringProperty("")
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
    def on_release(self):
        app = App.get_running_app()
        player_screen = app.root.get_screen('player')
        player_screen.video_url = self.url
        app.root.transition=SlideTransition(direction="right",duration=1)
        app.root.current = 'player'
    def download_video(self):
        threading.Thread(target=self._run_download).start()
        
    def _run_download(self):
        # 1. SET STORAGE PATH
        # Standard Android Download folder
        if os.name == 'posix' and os.path.exists('/sdcard'):
            # Create a specific folder so it's easy to find in Gallery
            save_path = '/sdcard/Download/BavaDownloads/%(title)s.%(ext)s'
        else:
            # PC fallback
            save_path = os.path.expanduser('~/Downloads/BavaDownloads/%(title)s.%(ext)s')
        

        # 2. OPTIMIZED OPTIONS
        ydl_opts = {
            'format': 'best[ext=mp4][height<=480]/best', # Best for Oppo A5
            'outtmpl': save_path,
            'quiet': True,              # NO console output
            'no_warnings': True,        # FIXES: 'str' object has no attribute 'write'
            'noprogress': True,         # Faster execution
            'logger': None,             # Stops the logger conflict
            # Add a common User-Agent to prevent 403 Forbidden
            'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        with YoutubeDL(ydl_opts) as ydl:
            try:
                print(f"Bava: Download started for {self.title}")
                # Ensure we use original_url (https://www.youtube.com/watch?v=...)
                ydl.download([self.original_url])
                print(f"Bava: Successfully saved to /sdcard/Download/BavaDownloads/")
            except Exception as e:
                print(f"Bava Download Error: {e}")
                

class Menu(Screen):
    details_of_video=ListProperty()
    def on_details_of_video(self,instance,value):
        self.ids.results_list.clear_widgets()
        for video in value:
            card=MenuCard(
                title=video.get("title",""),
                thumbnail=video.get("thumbnail",""),
                duration=str(round(video.get("duration",0.0)/60,2)),
                url=video.get("url",""),
                original_url=f"https://www.youtube.com/watch?v={video.get('id')}"
            )
            self.ids.results_list.add_widget(card)

class Home(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
    def start_search(self,query):
        response=youtube_search(query=query)
        menu_screen=self.manager.get_screen("menu")
        menu_screen.details_of_video=response
        self.manager.transition=SlideTransition(direction='left',duration=1)
        self.manager.current="menu"

class Intro(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)        
    def switch_page(self):
        self.manager.transition=SlideTransition(direction='left',duration=1)
        self.manager.current="home"

class BavaApp(App):
    def build(self):
        sm=ScreenManager()
        sm.add_widget(Intro(name="intro"))
        sm.add_widget(Home(name="home"))
        sm.add_widget(Menu(name="menu"))
        sm.add_widget(Player(name="player"))
        return sm


params={
    'quite':"True",
    'skip_download':"True",
    'format': 'best[ext=mp4][height<=480]',
    'no_warnings': True,
    'logger':None,
    'user_agent': 'Mozilla/5.0 (Android 13; Mobile; rv:109.0) Gecko/114.0 Firefox/114.0',
    'nocheckcertificate': True,
    'source_address': '0.0.0.0',           # Prevents certain 403 ipv6 issues
        # Force the "Android" client to get direct, mobile-friendly links
    'extractor_args': {'youtube': {'player_client': ['android']}}
}
client=YoutubeDL(params)

    
def youtube_search(query):
    response=client.extract_info(f"ytsearch10:{query}",download=False)
    metadata_of_videos=response["entries"]
    details_of_videos=[]

    for detail in metadata_of_videos:
        video_detail={}
        video_detail["Title"]=detail["title"]
        video_detail["url"]=detail["url"]
        video_detail["thumbnail"]=detail["thumbnail"]
        video_detail["duration"]=detail["duration"]
        video_detail["id"]=detail["id"]

        details_of_videos.append(video_detail)
    
    return details_of_videos

if __name__ == '__main__':
    BavaApp().run()


 






    
