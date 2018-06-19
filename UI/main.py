
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App


class RootWidget(FloatLayout):
    '''This is the class representing your root widget.
       By default it is inherited from BoxLayout,
       you can use any other layout/widget depending on your usage.
    '''
    # Definição do tipo de usuario
    # A aplicação deve cuidar para ativar o tipo correto
    user_tipo1 = False
    user_tipo2 = False
    user_tipo3 = False

    te = 444

    # Variáveis da UI
    teste = 1


    # Colocar o login aqui


    # Criar verificação de segurança: ao menos um tipo de usuário == true
    # if !(user_tipo1 && user_tipo2 && user_tipo3):
        # ERRO


    pass


class MainApp(App):
    '''This is the main class of your app.
       Define any app wide entities here.
       This class can be accessed anywhere inside the kivy app as,
       in python::

         app = App.get_running_app()
         print (app.title)

       in kv language::

         on_release: print(app.title)
       Name of the .kv file that is auto-loaded is derived from the name
       of this class::

         MainApp = main.kv
         MainClass = mainclass.kv

       The App part is auto removed and the whole name is lowercased.
    '''

    def build(self):
        return RootWidget()

if '__main__' == __name__:
    MainApp().run()
