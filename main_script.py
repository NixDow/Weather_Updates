from weather_api import get_weather
from weather_api import message_gen
from tel_notifier import telegram_message
from config import city

def main():
    data = get_weather(city)
    if data:
        message = message_gen(data)
        telegram_message(message)
        print(message)  # Optional: for logs

if __name__ == "__main__":
    main()