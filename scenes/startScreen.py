from scenes.scene import Scene
class StartScreen(Scene):
    def render(self):
        self.screen.fill("#30C864")
        super().render()
        