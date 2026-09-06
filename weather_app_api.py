import os
import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter City Name:", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")
        self.setFixedSize(500, 600)

        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)
        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.city_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.description_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        self.setStyleSheet("""
            QWidget {
                background-color: #1a1a2e;
            }
            QLabel#city_label {
                font-size: 40px;
                font-style: italic;
                color: #e0e0e0;
                font-weight: bold;
                padding-top: 20px;
            }
            QLineEdit#city_input {
                font-size: 40px;
                background-color: #16213e;
                color: #ffffff;
                border: 2px solid #0f3460;
                border-radius: 10px;
                padding: 10px;
                margin: 10px 30px;
            }
            QLineEdit#city_input:focus {
                border: 2px solid #00d2ff;
            }
            QPushButton#get_weather_button {
                font-size: 30px;
                font-weight: bold;
                background-color: #0f3460;
                color: #ffffff;
                border-radius: 15px;
                padding: 15px;
                margin: 10px 80px;
            }
            QPushButton#get_weather_button:hover {
                background-color: #1a4f8a;
            }
            QPushButton#get_weather_button:pressed {
                background-color: #0a1a3a;
            }
            QLabel#temperature_label {
                font-size: 75px;
                color: #00d2ff;
                font-weight: bold;
                padding-top: 20px;
            }
            QLabel#emoji_label {
                font-size: 100px;
                font-family: Segoe UI Emoji;
                padding: 10px;
            }
            QLabel#description_label {
                font-size: 50px;
                color: #e0e0e0;
                font-weight: bold;
                padding-bottom: 20px;
            }
        """)

        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        api_key = os.environ.get("OPENWEATHER_API_KEY")
        if not api_key:
            self.display_error("API Key Not Found.\nPlease Set OPENWEATHER_API_KEY Environment Variable.")
            return

        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            print(data)

            self.display_weather(data)
        except requests.exceptions.HTTPError as errh:
            match response.status_code:
                case 400:
                    self.display_error("Bad Request\nPlease Check Your Input")
                case 401:
                    self.display_error("Unauthorised\nInvalid API Key")
                case 403:
                    self.display_error("Forbidden\nAccess Is Denied")
                case 404:
                    self.display_error("Not Found\nCity Not Found")
                case 500:
                    self.display_error("Internal Server Error\nPlease Try Again Later")
                case 502:
                    self.display_error("Bad Gateway\nInvalid Response From The Server")
                case 503:
                    self.display_error("Service Unavailable\nPlease Check Your Input")
                case 504:
                    self.display_error("Gateway Timeout\nNo Response From The Server")
                case _:
                    self.display_error(f"HTTP Error\n{errh}")
        except requests.exceptions.ConnectionError as errc:
            self.display_error(f"Connection Error\nCheck Your Connection\n{errc}")
        except requests.exceptions.Timeout as errt:
            self.display_error(f"Connection Timeout Error\n{errt}")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Connection Redirect Error\nCheck Your URL")
        except requests.exceptions.RequestException as err:
            self.display_error(f"Connection Request Error\n{err}")

    def display_error(self, message):
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()

    def display_weather(self, data):
        temperature_k = data["main"]["temp"]
        temperature_c = temperature_k - 273.15
        weather_id = data["weather"][0]["id"]
        weather_description = data["weather"][0]["description"]
        self.temperature_label.setText(f"{temperature_c:.0f}°C")
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.description_label.setText(f"{weather_description.capitalize()}")

    @staticmethod
    def get_weather_emoji(weather_id):
        if 200 <= weather_id <= 232:
            return "⛈️"
        elif 300 <= weather_id <= 321:
            return "☁️"
        elif 500 <= weather_id <= 531:
            return "🌧️"
        elif 600 <= weather_id <= 622:
            return "❄️"
        elif 701 <= weather_id <= 741:
            return "🌫️"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return "💨"
        elif weather_id == 781:
            return "🌪️"
        elif weather_id == 800:
            return "☀️"
        elif 801 <= weather_id <= 804:
            return "💭"
        else:
            return ""


def main():
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
