import requests
import time
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from PIL import Image
from io import BytesIO
from secret import subscription_key, endpoint, image_url

# READ ANALYZE URL OF OUR RESOURCE
read_url = endpoint + "vision/v3.1/read/analyze"

# CONFIGURATION
headers = {'Ocp-Apim-Subscription-Key': subscription_key}
data = {'url': image_url}
response = requests.post(read_url, headers=headers, json=data)
response.raise_for_status()
operation_url = response.headers["Operation-Location"]
analysis = {}
poll = True
while (poll):
    response_final = requests.get(response.headers["Operation-Location"], headers=headers)
    analysis = response_final.json()
    time.sleep(1)
    if ("analyzeResult" in analysis):
        poll = False
    if ("status" in analysis and analysis['status'] == 'failed'):
        poll = False

polygons = []
if ("analyzeResult" in analysis):
    polygons = [(line["boundingBox"], line["text"])
                for line in analysis["analyzeResult"]["readResults"][0]["lines"]]

# DISPLAY THE IMAGE AND OVERLAY IT WITH THE EXTRACTED TEXT
image = Image.open(BytesIO(requests.get(image_url).content))
ax = plt.imshow(image)
print(polygons)
plt.figure(figsize=(5, 5))
image = Image.open(BytesIO(requests.get(image_url).content))
ax = plt.imshow(image, alpha=0.5)
for polygon in polygons:
    vertices = [(polygon[0][i], polygon[0][i + 1])
                for i in range(0, len(polygon[0]), 2)]
    text = polygon[1]
    patch = Polygon(vertices, closed=True, fill=False, linewidth=2, color='y')
    ax.axes.add_patch(patch)
    plt.text(vertices[0][0], vertices[0][1], text, fontsize=20, weight="bold", va="top")
plt.show()
