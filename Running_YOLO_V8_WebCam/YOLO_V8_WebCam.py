import math
from flask import app
from matplotlib import image
from ultralytics import YOLO
import cv2
import mysql.connector
from mysql.connector import Error
from roboflow import Roboflow



# Establish connection to MySQL database
def connect_to_mysql():
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',  # Your MySQL host
            database='test_schema',  # Your database name
            user='shreya',  # Your database username
            password='root')  # Your database password
        if connection.is_connected():
            return connection
    except Error as e:
        print("Error while connecting to MySQL", e)
        return None

# Insert detected ingredient name into the Ingredients table
# def insert_ingredient_name(ingredient_name):
#     connection = connect_to_mysql()
#     if connection:
#         try:
#             cursor = connection.cursor()
#             sql_insert_query = """INSERT INTO Ingredients (Ingredient_Name) VALUES (%s) ON DUPLICATE KEY UPDATE Ingredient_Name = VALUES(Ingredient_Name);"""
#             cursor.execute(sql_insert_query, (ingredient_name,))
#             connection.commit()
#             print("Ingredient name inserted successfully into Ingredients table")
#         except mysql.connector.Error as error:
#             print(f"Failed to insert into MySQL table {error}")
#         finally:
#             if connection.is_connected():
#                 cursor.close()
#                 connection.close()
                
def process_captured_images(image_path):
    # Initialize Roboflow model
    rf = Roboflow(api_key="FBQSwgHbiaU0halM4Nxb")
    project = rf.workspace().project("hackattackk")
    model = project.version("1").model
    img=cv2.imread(image_path)
    results=model.predict(img,confidence=40,overlap=30).json()

    for results in results["predictions"]:
        class_name=results["class"]
        confidence=results["confidence"]
        insert_ingredient_name(class_name)
        print(f"Detected: {class_name} with confidence: {confidence}")

    return class_name




# Initialize video capture and YOLO model
# cap = cv2.VideoCapture(0)
# frame_width = int(cap.get(3))
# frame_height = int(cap.get(4))
# out = cv2.VideoWriter("output.avi", cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width, frame_height))
#model = YOLO("../YOLO-Weights/yolov8n.pt")  # Ensure the path to your YOLO model weights is correct

# Define your class names here
# class_names = [
#     "apple", "banana", "beetroot", "bell pepper", "cabbage","capsicum", "carrot","cauliflower","chilli pepper","corn",
#     "cucumber","eggplant","garlic","ginger", "grapes", "jalepeno","kiwi","lemon", "lettuce","mango","onion","orange",
#     "paprika", "pear","peas", "pineapple", "pomegranate", "potato", "raddish", "soybeans", "spinach","sweetcorn",
#     "sweetpotato", "tomato", "turnip", "watermelon"
# ]

# Initialize the counter for limiting iterations
# counter = 0

# Main loop for object detection and database insertion
# while counter < 1000:  # Limit to 1000 iterations
#     success, img = cap.read()
#     if not success:
#         print("Failed to capture image")
#         break  # Exit the loop if image capture fails

    #results = model.predict(img, stream=True)

#test for tomato
print(model.predict("C:/Users/reyha/Documents/HackAttack/HackAttack/captured_images/captured_image.png", confidence=40, overlap=30).json())

    # for r in results:
    #     boxes = r.boxes
    #     for box in boxes:
    #         x1, y1, x2, y2 = map(int, box.xyxy[0])
    #         conf = math.ceil((box.conf[0] * 100)) / 100
    #         cls = int(box.cls[0])
    #         if cls < len(class_names):
    #             class_name = class_names[cls]
    #             label = f'{class_name} {conf}'

                # Insert detected ingredient name into MySQL database
    #             insert_ingredient_name(class_name)

    #             # Drawing the bounding box and label on the image
    #             cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
    #             t_size = cv2.getTextSize(label, 0, fontScale=1, thickness=2)[0]
    #             c2 = x1 + t_size[0], y1 - t_size[1] - 3
    #             cv2.rectangle(img, (x1, y1), c2, [255, 0, 255], -1, cv2.LINE_AA)
    #             cv2.putText(img, label, (x1, y1 - 2), 0, 1, [255, 255, 255], thickness=1, lineType=cv2.LINE_AA)

    # out.write(img)
    # cv2.imshow("Image", img)
    # if cv2.waitKey(1) == ord("q"):
    #     break

    # counter += 1  # Increment the counter after each iteration

# Cleanup
# cap.release()
# out.release()
# cv2.destroyAllWindows()

# print("Completed 1000 iterations or exited manually.")
