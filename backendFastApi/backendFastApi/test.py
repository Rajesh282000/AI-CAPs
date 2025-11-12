from google import genai
from google.genai import types


with open('D:\\backendFastApi\\backendFastApi\\\premium_photo-1664474619075-644dd191935f.jpg', 'rb') as f:
    image_bytes = f.read()

client = genai.Client(api_key="AIzaSyAERYuycX_GNJ-LvMQWwfxJGH28-G17_mM")

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/jpeg',
        ),
        'Caption this image.'
    ]
)

print(response.text)
