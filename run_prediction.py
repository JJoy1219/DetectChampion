from ultralytics import YOLO
from PIL import Image
from create_minimap import create_minimap

def predict_position():
  model = YOLO("models/balanced-approach/weights/best.pt")
  #buf = Image.open("minimapexample.png")
  minimap_image = create_minimap()
  results = model.predict(minimap_image)
  result = results[0]
  output = []
  for box in result.boxes:
    x1, y1, x2, y2 = [
      round(x) for x in box.xyxy[0].tolist()
    ]
    class_id = box.cls[0].item()
    prob = round(box.conf[0].item(), 2)
    x = ((x1 + x2)/512)*15000
    y = (1 - ((y1 + y2)/512)) * 15000
    output.append([
      round(x), round(y), result.names[class_id], prob
    ])
  [print(f"{name}: ({x},{y}) - {prob} chance") for x, y, name, prob in output]
  return output
  
predict_position()