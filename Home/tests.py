# from django.test import TestCase

# Create your tests here.
from lyzr import ChatBot
import os
os.environ['OPENAI_API_KEY'] = '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'

my_chatbot = ChatBot.pdf_chat(input_files=["/home/ubuntu/hackthon/PortfilioManager/enhanced_investor_trading_bot_report.pdf"])
response = my_chatbot.chat("what is this  doc?")
print(response)
