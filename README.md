# 🌤️ Weather App

A clean and user-friendly desktop weather application built with Python and PyQt5 that displays real-time weather information using the OpenWeatherMap API.

## 📸 Screenshot

![Weather App Screenshot](<img width="400" height="517" alt="image" src="https://github.com/user-attachments/assets/f3f520a0-41c4-4060-a617-0f34d28c4565" />
)

## 📋 Project Overview

This desktop application provides users with instant weather information for any city worldwide. It features a clean graphical interface with visual weather indicators and comprehensive error handling.

## 🎯 Core Features

- **Real-time Weather Data** - Fetches current weather conditions from OpenWeatherMap API
- **Temperature Display** - Shows temperature in Celsius with clear formatting
- **Visual Weather Indicators** - Emoji icons representing different weather conditions
- **City Search** - Simple input field for entering any city name
- **Comprehensive Error Handling** - User-friendly messages for API errors, network issues, and invalid inputs

## 🎨 Weather Emoji Mapping

| Weather Condition | ID Range | Emoji |
|-------------------|----------|-------|
| Thunderstorm | 200-232 | ⛈️ |
| Drizzle | 300-321 | ☁️ |
| Rain | 500-531 | 🌧️ |
| Snow | 600-622 | ❄️ |
| Mist/Fog | 701-741 | 🌫️ |
| Volcano | 762 | 🌋 |
| Sandstorm | 771 | 💨 |
| Tornado | 781 | 🌪️ |
| Clear Sky | 800 | ☀️ |
| Clouds | 801-804 | 💭 |

## 🛠️ Technologies Used

- **Python 3.7+** - Core programming language
- **PyQt5** - GUI framework for desktop application
- **Requests** - HTTP library for API calls
- **OpenWeatherMap API** - Weather data provider

## 📁 Project Structure

Weather-App-API/
├── weather_app.py # Main application code
├── requirements.txt # Python dependencies
├── .env.example # Example environment variables
├── .gitignore # Git ignore rules
├── LICENSE # MIT License
├── screenshot.png # Application screenshot
└── README.md # Project documentation


## 🐛 Error Handling

The application handles various error scenarios:

| HTTP Status | Error Type |
|-------------|------------|
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 500 | Internal Server Error |
| 502 | Bad Gateway |
| 503 | Service Unavailable |
| 504 | Gateway Timeout |

**Additional Error Handling:**
- Connection errors
- Timeout errors
- Too many redirects
- General request exceptions
- Missing API key detection

## 📄 License

This project is licensed under the MIT License.

## 👤 Author

**Mohamed Tamer**
- GitHub: [@mohamed-tamer-UT](https://github.com/mohamed-tamer-UT)

## 🙏 Acknowledgments

- [OpenWeatherMap](https://openweathermap.org/) for providing the free weather API
- [PyQt5](https://www.riverbankcomputing.com/software/pyqt/) for the GUI framework

## ⭐ Support

If you find this project useful, please give it a star ⭐ on GitHub!

---

Made with ❤️ by Mohamed Tamer
