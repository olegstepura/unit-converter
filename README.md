# 🌐 Unit Converter – Flask Web App

A modern unit conversion web application built with **Python**, **Flask**, and **WebSockets** for real-time conversions. Features a clean, user-friendly interface with internationalization support.

---

## 🌍 Live Demo

🔗 Try it now: [Unit Converter](https://convert.cdstudio.org)

---

## ✨ Features

* ⚡ **Real-time Conversions** – Powered by WebSockets for instant results
* 🌍 **Multi-language Support** – Available in English, Russian, German, and Chinese
* 📏 **10+ Conversion Categories** – Length, Mass, Time, Temperature, Speed, Volume, Area, Data Storage, Energy, Pressure
* 🔧 **Utility Tools** – URL Encode/Decode and Base64 Encode/Decode
* 🎨 **Modern UI** – Clean, responsive design with Ghibli-inspired styling
* 🐳 **Docker Ready** – Containerized for easy deployment

---

## 🔄 Supported Conversion Categories

* 📏 **Length / Distance** – mm, cm, m, km, in, ft, yd, mi
* ⚖️ **Mass / Weight** – mg, g, kg, tonne, oz, lb, stone
* ⏱ **Time** – seconds, minutes, hours, days, weeks, months, years
* 🌡 **Temperature** – Celsius, Fahrenheit, Kelvin
* 🚗 **Speed** – m/s, km/h, mph, knots
* 🧪 **Volume** – ml, L, cc, m³, tsp, tbsp, fl oz, cups, pints, gallons
* 🧱 **Area** – m², km², ft², yd², acre, hectare
* 💾 **Data Storage** – bit, byte, KB, MB, GB, TB
* 🔋 **Energy** – J, kJ, cal, kcal, Wh, kWh
* 🌬 **Pressure** – Pa, bar, atm, mmHg, psi
* 🔗 **URL Encode/Decode** – Encode and decode URL-encoded strings
* 📦 **Base64 Encode/Decode** – Encode and decode Base64 strings

---

## 🛠 Built With

* 🐍 **Python 3.11**
* 🌐 **Flask 3.1.0** – Web framework
* 🔌 **Flask-SocketIO 5.3.6** – WebSocket support for real-time conversions
* 🌍 **Flask-Babel 4.0.0** – Internationalization (i18n)
* 🐳 **Docker** – Containerization
* 🚀 **Gunicorn** – Production WSGI server
* 🧾 **HTML5, CSS3, JavaScript** – Frontend

---

## 🚀 Getting Started

### Prerequisites

* Python 3.11+
* Docker (optional, for containerized deployment)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/olegstepura/unit-converter.git
   cd unit-converter
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Compile translations** (optional, for i18n)
   ```bash
   ./compile_translations.sh
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

   The app will be available at `http://localhost:5000`

### Docker Deployment

**Pull the pre-built image:**
```bash
docker pull ghcr.io/olegstepura/unit-converter:latest
docker run -p 5000:5000 ghcr.io/olegstepura/unit-converter:latest
```

**Or build locally:**
```bash
docker build -t unit-converter .
docker run -p 5000:5000 unit-converter
```

---

## 🌍 Internationalization

The application supports multiple languages:
* 🇺🇸 English (en)
* 🇷🇺 Russian (ru)
* 🇩🇪 German (de)
* 🇨🇳 Chinese (zh)

Language can be changed using the dropdown in the header. The preference is saved in the session.

---

## 📁 Project Structure

```
unit-converter/
├── unit_converter/          # Main application package
│   ├── __init__.py          # Flask app initialization, SocketIO, Babel
│   ├── route.py             # Routes and WebSocket handlers
│   ├── length.py            # Length conversion logic
│   ├── mass.py              # Mass conversion logic
│   └── ...                  # Other conversion modules
├── templates/               # Jinja2 templates
│   ├── base.html            # Base template
│   ├── index.html           # Home page
│   └── *.html               # Conversion pages
├── static/                  # Static files
│   ├── css/                 # Stylesheets
│   └── js/                  # JavaScript files
├── translations/            # i18n translation files
│   ├── ru/LC_MESSAGES/      # Russian translations
│   ├── de/LC_MESSAGES/      # German translations
│   └── zh/LC_MESSAGES/      # Chinese translations
├── Dockerfile               # Docker configuration
├── requirements.txt         # Python dependencies
└── wsgi.py                  # WSGI entry point for production
```

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Ways to Contribute

* 🐛 **Report Issues** – Found a bug or inaccurate conversion? Open an issue
* 🌟 **Suggest Enhancements** – Want to add a new unit category or improve the UI/UX?
* 🧩 **Submit Pull Requests** – Fix bugs, clean up code, or add new features

---

## 📝 License

This project is open source and available for use and modification.

---

## 🙏 Acknowledgments

* Original inspiration from [Roushan-77/Unit-converter](https://github.com/Roushan-77/Unit-converter)
