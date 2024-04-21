from roboflow import Roboflow
import json
rf = Roboflow(api_key="otKMUXAELXaU2XZsT77M")
project = rf.workspace().project("biomedical-wastes")
model = project.version(3).model

# infer on a local image
json_response = model.predict("./syringe.jpg", confidence=40, overlap=30).json()

# save the JSON response to a file
with open('output.json', 'w') as f:
    json.dump(json_response, f)

# visualize your prediction
# model.predict("your_image.jpg", confidence=40, overlap=30).save("prediction.jpg")

# infer on an image hosted elsewhere
# print(model.predict("URL_OF_YOUR_IMAGE", hosted=True, confidence=40, overlap=30).json())