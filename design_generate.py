from io import BytesIO

import openai
import requests
import matplotlib.pyplot as plt
from PIL import Image

# Set up OpenAI API credentials
openai.api_key =

# Text prompt describing the 3D model
text_prompt = "A red car on a grassy field under a sunny sky"

# Generate image using DALL-E API
response = openai.Completion.create(
    engine="",


    prompt=text_prompt,
    max_tokens=50,
    temperature=0.7,
    top_p=1.0,
    n=1,
    stop=None
)
# Extract the generated image URL from the API response
image_url = response.choices[0].raw['image']

# Download and display the image
image_response = requests.get(image_url)
image_data = Image.open(BytesIO(image_response.content))
plt.imshow(image_data)
plt.axis("off")
plt.show()
