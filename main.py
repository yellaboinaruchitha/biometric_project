import cv2
import numpy as np

database = {}

def preprocess(image_path):
    img = cv2.imread(image_path, 0)
    img = cv2.resize(img, (256, 256))
    return np.mean(img)

print("1. Register")
print("2. Login")

choice = input("Choose option (1 or 2): ")

if choice == "1":
    user_id = input("Enter User ID: ")
    image_path = input("Enter fingerprint image path: ")
    
    features = preprocess(image_path)
    database[user_id] = features
    
    print("User Registered Successfully")

elif choice == "2":
    user_id = input("Enter User ID: ")
    image_path = input("Enter fingerprint image path: ")
    
    if user_id in database:
        input_features = preprocess(image_path)
        stored_features = database[user_id]
        
        if abs(input_features - stored_features) < 5:
            print("Login Successful")
        else:
            print("Fingerprint Not Matched")
    else:
        print("User Not Found")


