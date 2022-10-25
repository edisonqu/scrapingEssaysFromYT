import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("API")

def formatAndGenerate(essayTranscript):
  # prompt is preset and pre-determined

  response = openai.Completion.create(
    model="text-davinci-002",
    prompt= "Copy and format the essay part in this paragraph." + essayTranscript +"\n",
    temperature=0.2,
    max_tokens=1718,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )

  print(response)
  generated_text = response["choices"][0]["text"]

  return generated_text


def find_prompt(generated_text):
  response = openai.Completion.create(
    model="text-davinci-002",
    prompt= "Copy the prompt used: \n" + generated_text +"\n",
    temperature=0.2,
    max_tokens=1718,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )
  print(response)
  the_prompt = response["choices"][0]["text"]

  return the_prompt


