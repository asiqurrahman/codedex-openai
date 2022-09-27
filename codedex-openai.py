import openai
from dotenv import dotenv_values

config = dotenv_values('.env')

# Set API key
openai.api_key = config['API_KEY']

def generate_blog(paragraph_topic):
  # Makes a http request and returns an object
  response = openai.Completion.create(
    model = 'text-davinci-002',
    prompt = 'Write a paragraph about the following topic.' + ' ' + paragraph_topic,
    max_tokens = 400,
    temperature = 0.3
  )
  # Accessing the property in the returned object that holds the paragraph  
  retrieve_blog = response.choices[0].text

  return retrieve_blog

keep_writing = True

# Keep writing paragraph until user stops
while keep_writing:
  answer = input('Write a paragraph? Y for yes, anything else for no')
  if (answer == 'Y'):
    paragraph_topic = input('What should this paragraph talk about?')
    print(generate_blog(paragraph_topic))
  else:
    keep_writing = False