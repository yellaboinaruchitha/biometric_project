import cv2
import numpy as np
import json

# ----------------------------
# Load database if it exists
# ----------------------------
try:
    with open("database.json", "r") as file:
        database = json.load(file)
except:
    database = {}

# ----------------------------
# Preprocess fingerprint
# ----------------------------
def preprocess(image_path):

    img = cv2.imread(image_path, 0)

    if img is None:
        print("Cannot read fingerprint image. Check the path.")
        return None

    img = cv2.resize(img, (256, 256))

    return float(np.mean(img))


print("1. Register")
print("2. Login")

choice = input("Choose option (1 or 2): ")

# ----------------------------
# REGISTER
# ----------------------------
if choice == "1":

    user_id = input("Enter User ID: ")
    image_path = input("Enter fingerprint image path: ")

    features = preprocess(image_path)

    if features is not None:

        database[user_id] = features

        # Save database
        with open("database.json", "w") as file:
            json.dump(database, file)

        print("User Registered Successfully")


# ----------------------------
# LOGIN
# ----------------------------
elif choice == "2":

    user_id = input("Enter User ID: ")
    image_path = input("Enter fingerprint image path: ")

    if user_id in database:

        input_features = preprocess(image_path)

        stored_features = database[user_id]

        difference = abs(input_features - stored_features)

        if difference < 5:
            print("Login Successful")

        else:
            print("Fingerprint Not Matched")

    else:
        print("User Not Found")