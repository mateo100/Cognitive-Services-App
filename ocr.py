import requests
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from PIL import Image
from io import BytesIO
from secret import subscription_key, endpoint, image_url


# OCR URL OF OUR RESOURCE
ocr_url = endpoint + "vision/v3.1/ocr"

# CONFIGURATION
headers = {'Ocp-Apim-Subscription-Key': subscription_key}
params = {'language': 'en', 'detectOrientation': 'true'}
data = {'url': image_url}
response = requests.post(ocr_url, headers=headers, params=params, json=data)
response.raise_for_status()
analysis = response.json()


# EXTRACT THE WORD BOUNDING BOXES AND TEXT
line_infos = [region["lines"] for region in analysis["regions"]]
word_infos = []
for line in line_infos:
    for word_metadata in line:
        for word_info in word_metadata["words"]:
            word_infos.append(word_info)


# DISPLAY THE IMAGE AND OVERLAY IT WITH THE EXTRACTED TEXT
plt.figure(figsize=(5, 5))
image = Image.open(BytesIO(requests.get(image_url).content))
ax = plt.imshow(image, alpha=0.5)
print(word_infos)
for word in word_infos:
    bbox = [int(num) for num in word["boundingBox"].split(",")]
    text = word["text"]
    origin = (bbox[0], bbox[1])
    patch = Rectangle(origin, bbox[2], bbox[3],
                      fill=False, linewidth=2, color='y')
    ax.axes.add_patch(patch)
    plt.text(origin[0], origin[1], text, fontsize=20, weight="bold", va="top")
plt.show()
plt.axis("off")
