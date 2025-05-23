from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "eskimai" #your ai model here
CHANNEL_URL = "https://discord.com/channels/@me/IDCHANNEL"


options = webdriver.EdgeOptions()
options.add_argument("--user-data-dir=C:\\Users\\adam\\AppData\\Local\\Microsoft\\Edge\\User Data")
options.add_argument("--profile-directory=Default")
options.add_argument("--remote-debugging-port=9222")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=options)

driver.get(CHANNEL_URL)
time.sleep(5)

seen_messages = set()


def get_eskimai_response(prompt):
    prompt = f"{prompt}\n(short answer pls)"
    payload = {"model": MODEL_NAME, "prompt": prompt, "stream": False}
    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code == 200:
        return response.json().get("response", "Error: No response from AI.")
    return f"Error: {response.status_code}"


def send_message(message):
    try:
        message_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'textArea')]//div[@role='textbox']"))
        )
        message_box.send_keys(message)
        message_box.send_keys(Keys.ENTER)
        print("Message sent:", message)
    except Exception as e:
        print("Error while sending message:", e)


while True:
    try:
        messages = driver.find_elements(By.XPATH, "(//div[contains(@class, 'messageContent_')]//span)")

        if messages:
            latest_message = messages[-1]
            message_text = latest_message.text

            if message_text and message_text not in seen_messages:
                seen_messages.add(message_text)
                print(f"New message: {message_text}")

                ai_response = get_eskimai_response(message_text)

                print(f"AI response: {ai_response}")

                time.sleep(3)

                send_message(ai_response)

    except Exception as e:
        print("Error in main loop:", e)

    time.sleep(5)