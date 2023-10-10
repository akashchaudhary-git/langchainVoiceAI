import keyboard
import os
import tempfile

import numpy as np
import openai
import sounddevice as sd
import soundfile as sf
from dotenv import load_dotenv
from elevenlabs import generate, play, set_api_key
from langchain.agents import initialize_agent, load_tools
from langchain.agents.agent_toolkits import ZapierToolkit
from langchain.llms.openai import AzureOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.tools import BaseTool
from langchain.utilities.zapier import ZapierNLAWrapper

load_dotenv()

set_api_key(os.getenv("ELEVENLABS_API_KEY"))
openai.api_key = os.getenv("AZURE_OPENAI_KEY")


# Set recording parameters
duration =5 #duration of each recording in seconds
fs =44100 #sampling frequency
channels = 1 #number of channels
