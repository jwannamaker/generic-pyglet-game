import pyglet


class MainWindow(pyglet.window.Window):
    def __init__(self):
        super().__init__(fullscreen=True)
        
        self.alive = 1
        
    def on_draw(self):
        self.render()
        
    def on_close(self):
        self.alive = 0
        
    def render(self):
        self.clear()
        