import os
# official openai module
import openai

# Set Api Key
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_blog(blog_topic):
    # Makes a http request and returns an object
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt="Write a paragraph about the following topic." + " " + blog_topic,
        max_tokens=300,
        temperature=0.3,
    )
    
    retrieve_blog = response.choices[0].text

    return retrieve_blog


keep_writing = True

# Keep writing paragraph until user stops
while keep_writing:
  write_paragraph = input('Write a paragraph? Y for yes, anything else for no')
  if(write_paragraph == "Y"):
    blog_topic = input("What should this paragraph talk about?")
    print(generate_blog(blog_topic))
  else:
    keep_writing = False