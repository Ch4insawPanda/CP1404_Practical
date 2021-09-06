from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):

    def __init__(self, **kwargs):
        """Initialize the list."""
        super().__init__(**kwargs)
        self.names_list = ['Bryan', 'Jedidiah', 'Wally', 'Hiroyuki', 'Matilda']

    def build(self):
        """Main build of the app."""
        self.title = 'Dynamic Labels'
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from list initialized."""
        for name in self.names_list:
            label_name = Label(text=name)
            self.root.ids.main.add_widget(label_name)


DynamicLabelsApp().run()
