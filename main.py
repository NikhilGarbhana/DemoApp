from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
import requests

help_str = '''
ScreenManager:
    WelcomeScreen:
    MainScreen:
    LoginScreen:
    AdminScreen:
    SignupScreen:
    MenuScreen:
    ProfileScreen:
    UploadScreen:
<WelcomeScreen>:
    name:'WelcomeScreen'
    MDLabel:
        text:'Welcome to NIT Kurukshetra'
        font_style:'H2'
        halign:'center'
        pos_hint: {'center_y':0.9}
    
    Image:
        source:"Nit.png"
        pos_hint: {'center_x': 0.5, 'center_y':0.55}
    
    MDRaisedButton:
        text:'Admin'
        pos_hint : {'center_x':0.4,'center_y':0.2}
        size_hint: (0.13,0.1)
        on_press: 
            root.manager.current = 'AdminScreen'
            root.manager.transition.direction = 'left'
    MDRaisedButton:
        text:'Student'
        pos_hint : {'center_x':0.6,'center_y':0.2}
        size_hint: (0.13,0.1)
        on_press:
            root.manager.current = 'LoginScreen'
            root.manager.transition.direction = 'left'

<LoginScreen>:
    name:'LoginScreen'
    MDLabel:
        text:'Login'
        font_style:'H2'
        halign:'center'
        pos_hint: {'center_y':0.9}
        
    MDTextField:
        id:login_email
        pos_hint: {'center_y':0.6,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Email'
        helper_text:'Required'
        helper_text_mode: 'on_error'
        icon_right: 'email'
        icon_right_color: app.theme_cls.primary_color
        required: True
    MDTextField:
        id:login_password
        pos_hint: {'center_y':0.4,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Password'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'eye-off'
        password: True
        icon_right_color: app.theme_cls.primary_color
        required: True
    MDRaisedButton:
        text:'Login'
        size_hint: (0.13,0.07)
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press:
            app.login()
            app.username_changer() 

    MDTextButton:
        text: 'Create an account'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press:
            root.manager.current = 'SignupScreen'
            root.manager.transition.direction = 'up'
   
<AdminScreen>:
    name: 'AdminScreen'
             
<SignupScreen>:
    name:'SignupScreen'
    MDLabel:
        text:'Signup'
        font_style:'H2'
        halign:'center'
        pos_hint: {'center_y':0.9}
    MDTextField:
        id:signup_email
        pos_hint: {'center_y':0.6,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Email'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'email'
        icon_right_color: app.theme_cls.primary_color
        required: True
    MDTextField:
        id:signup_username
        pos_hint: {'center_y':0.75,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Username'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True

    MDTextField:
        id:signup_password
        pos_hint: {'center_y':0.45,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Password'
        helper_text:'Required'
        password: True
        helper_text_mode:  'on_error'
        icon_right: 'eye-off'
        icon_right_color: app.theme_cls.primary_color
        required: True

    MDRaisedButton:
        text:'Signup'
        size_hint: (0.13,0.07)
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press: app.signup()
    MDTextButton:
        text: 'Already have an account'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press:
            root.manager.current = 'LoginScreen'
            root.manager.transition.direction = 'down'


<MainScreen>:
    name: 'MainScreen'
    MDLabel:
        id:username_info
        text:'Hello Main'
        font_style:'H1'
        halign:'center'

    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Demo'
                        left_action_items: [["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation:5

                    Widget:

        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                orientation: 'vertical'
                padding: "8dp"
                spacing: "8dp"

                Image:
                    id: avatar
                    size_hint: (1,1)
                    source: "pic.png"

                ScrollView:

                    DrawerList:
                        id: md_list

                        MDList:
                            OneLineIconListItem:
                                text: "Menu"
                                on_press: root.manager.current = 'MenuScreen'
                                IconLeftWidget:
                                    icon: "menu"
                                    on_press: root.manager.current = 'MenuScreen'


                            OneLineIconListItem:
                                text: "Logout"
                                on_press: 
                                    root.manager.current = 'WelcomeScreen'
                                    root.manager.transition.direction = 'down'
                                IconLeftWidget:
                                    icon: "logout"
                                    on_press: 
                                        root.manager.current = 'WelcomeScreen'
                                        root.manager.transition.direction = 'down'


<MenuScreen>:
    name : 'MenuScreen'
    MDLabel:
        id:profile_name
        text:'Menu Screen'
        font_style : 'H2'
        halign : 'center'
        pos_hint : {'center_y':0.7}
    MDRectangleFlatButton:
        text: 'Profile'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_press: root.manager.current = 'ProfileScreen'
    MDRectangleFlatButton:
        text: 'Upload'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.manager.current = 'UploadScreen'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'MainScreen'

<ProfileScreen>:
    name: 'ProfileScreen'
    
    MDTextField:
        id:name
        pos_hint: {'center_y':0.9,'center_x':0.4}
        size_hint : (0.6,0.1)
        hint_text: 'Full Name'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right_color: app.theme_cls.primary_color
        required: True
        
    MDTextField:
        id:roll_number
        pos_hint: {'center_y':0.8,'center_x':0.4}
        size_hint : (0.6,0.1)
        hint_text: 'Roll Number'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right_color: app.theme_cls.primary_color
        required: True
    MDTextField:
        id:branch
        pos_hint: {'center_y':0.7,'center_x':0.4}
        size_hint : (0.6,0.1)
        hint_text: 'Branch'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right_color: app.theme_cls.primary_color
        required: True
    MDTextField:
        id:cgpa
        pos_hint: {'center_y':0.6,'center_x':0.4}
        size_hint : (0.6,0.1)
        hint_text: 'CGPA'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right_color: app.theme_cls.primary_color
        required: True
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'MenuScreen'

<UploadScreen>:
    name: 'UploadScreen'
    MDLabel:
        text: 'Upload'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'MenuScreen'


'''


class WelcomeScreen(Screen):
    pass


class MainScreen(Screen):
    pass


class LoginScreen(Screen):
    pass


class MenuScreen(Screen):
    pass


class SignupScreen(Screen):
    pass


class ProfileScreen(Screen):
    pass


class UploadScreen(Screen):
    pass


class AdminScreen(Screen):
    pass


class ContentNavigationDrawer(BoxLayout):
    pass


class DrawerList(ThemableBehavior, MDList):
    pass


sm = ScreenManager()
sm.add_widget(WelcomeScreen(name='WelcomeScreen'))
sm.add_widget(MainScreen(name='MainScreen'))
sm.add_widget(LoginScreen(name='LoginScreen'))
sm.add_widget(MenuScreen(name='MenuScreen'))
sm.add_widget(SignupScreen(name='SignupScreen'))
sm.add_widget(ProfileScreen(name='ProfileScreen'))
sm.add_widget(UploadScreen(name='UploadScreen'))
sm.add_widget(AdminScreen(name='AdminScreen'))


class DemoApp(MDApp):
    def build(self):
        self.strng = Builder.load_string(help_str)
        self.url = "https://loginsetup-a6f02-default-rtdb.firebaseio.com/.json"
        return self.strng

    def signup(self):
        signupEmail = self.strng.get_screen('SignupScreen').ids.signup_email.text
        signupPassword = self.strng.get_screen('SignupScreen').ids.signup_password.text
        signupUsername = self.strng.get_screen('SignupScreen').ids.signup_username.text

        if signupEmail.split() == [] or signupPassword.split() == [] or signupUsername.split() == [] or \
                signupEmail.count("@") == 0 or signupEmail.count(".") == 0:
            self.invalid()
            self.strng.get_screen('SignupScreen').manager.current = 'SignupScreen'
        else:
            print(signupEmail, signupPassword)
            signup_info = str(
                {f'\"{signupEmail}\":{{"Password":\"{signupPassword}\","Username":\"{signupUsername}\"}}'})
            signup_info = signup_info.replace(".", "-")
            signup_info = signup_info.replace("\'", "")
            to_database = json.loads(signup_info)
            print(to_database)
            requests.patch(url=self.url, json=to_database)

    auth = 'Gx3QIUQtaH1OPYz4rW9zkDkjqkdL8ds6nDsOHzp4'

    def login(self):
        loginEmail = self.strng.get_screen('LoginScreen').ids.login_email.text
        loginPassword = self.strng.get_screen('LoginScreen').ids.login_password.text

        self.login_check = False
        supported_loginEmail = loginEmail.replace('.', '-')
        supported_loginPassword = loginPassword.replace('.', '-')
        request = requests.get(self.url + '?auth=' + self.auth)
        data = request.json()
        emails = set()
        for key, value in data.items():
            emails.add(key)
        if supported_loginEmail in emails and supported_loginPassword == data[supported_loginEmail]['Password']:
            self.username = data[supported_loginEmail]['Username']
            self.login_check = True
            self.strng.get_screen('MainScreen').manager.current = 'MainScreen'
        else:
            self.invalid()

    def invalid(self):
        cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialog)
        self.dialog = MDDialog(title='Invalid input', text="Please input a valid input", size_hint=(0.7, 0.2),
                               buttons=[cancel_btn_username_dialogue])
        self.dialog.open()

    def close_username_dialog(self, obj):
        self.dialog.dismiss()

    def username_changer(self):
        if self.login_check:
            self.strng.get_screen('MainScreen').ids.username_info.text = f"Welcome {self.username}"


DemoApp().run()
