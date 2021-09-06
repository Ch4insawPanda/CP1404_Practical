from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.core.window import Window

MILES_TO_KM = 1.60934


class MilesToKm(App):
    km_output = StringProperty()

    def build(self):
        Window.size = (500, 250)
        self.title = 'Miles to Km'
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def validate_value(self):
        """Validate the value of the user input and return 0 if invalid."""
        if self.root.ids.miles_input.text == '':
            return 0.0
        else:
            try:
                value = float(self.root.ids.miles_input.text)
                return value
            except ValueError:
                return 0.0

    def handle_increment(self, integer):
        """Change the value of the input based on whether an increase or decrease is wanted."""
        user_input = self.get_value()
        self.root.ids.miles_input.text = str(user_input + integer)

    def handle_calculate(self):
        """Convert the mile value into km value."""
        m_value = self.get_value()
        km_value = m_value * MILES_TO_KM
        self.root.ids.km_output.text = str(km_value)


MilesToKm().run()
