import telebot
import time
import random

# Telegram Bot Token
TOKEN = "HTTP API:
8081619949:AAGI-Vep5vNLDdcgE0ZDvTZftfpx5DdP2Cg"
CHAT_ID = "1688402340"

bot = telebot.TeleBot(TOKEN)

# Dummy function to simulate chart reversal detection
def check_chart_for_reversal():
    # Replace with real logic or image analysis if needed
    return random.choice([True, False])

# Send alert message with optional sound
def send_alert():
    bot.send_message(CHAT_ID, "⚠️ Possible chart reversal detected!")

# Main loop
def monitor_charts():
    while True:
        if check_chart_for_reversal():
            send_alert()
        time.sleep(60)  # Check every 60 seconds

# Start monitoring
if __name__ == "__main__":
    print("📊 Bot is running...")
    monitor_charts()
    # binary-chart-alert-bot
