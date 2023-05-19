import os
from urllib import response
import openai
import requests
import wget

openai.api_key = ""


# Sad/Happy - Sad
# Subject - Pinetree


# EDM/Hiphop 3-D Futuristic/Sci Fi Visuals Style (Happy, sad)
# result=openai.Image.create(
#   prompt="Dreamy, futuristic, 3-D render of vast forest in the style of Beeple",
#   n=2,
#   size="256x256"
# )

# result=openai.Image.create(
#   prompt="A futuristic 3-D image of stocks floating in mid-air, with the logos of Activision Blizzard, Chipotle, First Republic Bank and others flickering and glowing brightly.",
#   n=2,
#   size="256x256"
# )


#EDM (Happy, sad)
# result=openai.Image.create(
#   prompt="Dreamy Electronic Dance Music art of vast forest",
#   n=2,
#   size="1024x1024"
# )

# result=openai.Image.create(
#   prompt="Comic book art of musician submitting his song to a playlist in the style of kieron gillen",
#   n=2,
#   size="256x256"
# )

# James Gurney? kieron gillen?

# Cinematography style
# result=openai.Image.create(
#   prompt="Intense cinematography from scene of mystery",
#   n=2,
#   size="256x256"
# )

# Lofi animated vibe
# result=openai.Image.create(
#   prompt="Dreamy, animated, vintage inspired tones of a mystery in the style of lofi",
#   n=2,
#   size="256x256"
# )

#Synthwave
# result=openai.Image.create(
#   prompt="Dreamy Synthwave pink headphones",
#   n=2,
#   size="1024x1024"
# )

#Trippy isometric
result=openai.Image.create(
  prompt="A 3-D render of a baloon animal that looks like OJ Simpson ",
  n=4,
  size="256x256"
)




print(result)



