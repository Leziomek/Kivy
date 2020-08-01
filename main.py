import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
import socket



class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 3

        self.prev = Button(text='<<', font_size=40)
        self.prev.bind(on_press=self.previous)
        self.add_widget(self.prev)

        self.pause = Button(text='>||', font_size=40)
        self.pause.bind(on_press=self.pause_play)
        self.add_widget(self.pause)

        self.nx = Button(text='>>', font_size=40)
        self.nx.bind(on_press=self.next)
        self.add_widget(self.nx)

    def previous(self, instance):
        msg = 'pr_key'
        msg = f'{len(str(msg)):<{HEADERSIZE}}{msg}'.encode('utf-8')
        client_socket.send(msg)

    def pause_play(self, instance):
        msg = 'pl_key'
        msg = f'{len(str(msg)):<{HEADERSIZE}}{msg}'.encode('utf-8')
        client_socket.send(msg)

    def next(self, instance):
        msg = 'nx_key'
        msg = f'{len(str(msg)):<{HEADERSIZE}}{msg}'.encode('utf-8')
        client_socket.send(msg)

class MyApp(App):
    def build(self):
        return MyGrid()



if __name__ == '__main__':
    HEADERSIZE = 10
    IP = 'localhost'
    PORT = 2530

    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_socket.connect((IP,PORT))
    client_socket.setblocking(False)
    MyApp().run()
