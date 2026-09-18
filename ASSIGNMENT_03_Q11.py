import cv2
import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog


root = Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title="Select an Image",
    filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
)

if file_path == "":
    print("No image selected.")
    exit()

# Read image
original = cv2.imread(file_path)

if original is None:
    print("Could not open image.")
    exit()

# Current image
image = original.copy()




def show_image(img, title="Image"):
    # OpenCV uses BGR, matplotlib uses RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(8, 6))
    plt.imshow(img_rgb)
    plt.title(title)
    plt.axis("off")
    plt.show()



def rotate(img):
    angle = float(input("Enter rotation angle (example 90): "))

    h, w = img.shape[:2]
    center = (w // 2, h // 2)

    matrix = cv2.getRotationMatrix2D(center, angle, 1)

    result = cv2.warpAffine(img, matrix, (w, h))

    return result



def resize(img):
    factor = float(input("Enter resize factor (example 2): "))

    h, w = img.shape[:2]

    new_w = int(w * factor)
    new_h = int(h * factor)

    result = cv2.resize(img, (new_w, new_h))

    return result



def flip(img):
    print("\n1. Horizontal Flip")
    print("2. Vertical Flip")
    print("3. Both")

    choice = input("Choose flip: ")

    if choice == "1":
        return cv2.flip(img, 1)

    elif choice == "2":
        return cv2.flip(img, 0)

    elif choice == "3":
        return cv2.flip(img, -1)

    else:
        print("Invalid choice.")
        return img



def shear(img):
    x = float(input("Enter X shear value (example 0.2): "))
    y = float(input("Enter Y shear value (example 0.2): "))

    h, w = img.shape[:2]

    matrix = np.float32([
        [1, x, 0],
        [y, 1, 0]
    ])

    result = cv2.warpAffine(
        img,
        matrix,
        (w + int(abs(x) * h), h + int(abs(y) * w))
    )

    return result



def custom_matrix(img):
    print("\nEnter the 2x3 transformation matrix.")

    print("Example:")
    print("1  0  0")
    print("0  1  0")

    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

    d = float(input("d = "))
    e = float(input("e = "))
    f = float(input("f = "))

    matrix = np.float32([
        [a, b, c],
        [d, e, f]
    ])

    h, w = img.shape[:2]

    result = cv2.warpAffine(img, matrix, (w, h))

    return result



while True:

    print("\n================================")
    print("   IMAGE TRANSFORMATION TOOLBOX")
    print("================================")

    print("1. Rotate")
    print("2. Resize")
    print("3. Flip")
    print("4. Shear")
    print("5. Custom Matrix")
    print("6. Reset")
    print("7. Exit")

    choice = input("\nEnter your choice: ")

    # Rotate
    if choice == "1":
        image = rotate(image)
        show_image(image, "Rotated Image")

    # Resize
    elif choice == "2":
        image = resize(image)
        show_image(image, "Resized Image")

    # Flip
    elif choice == "3":
        image = flip(image)
        show_image(image, "Flipped Image")

    # Shear
    elif choice == "4":
        image = shear(image)
        show_image(image, "Sheared Image")

    # Custom Matrix
    elif choice == "5":
        image = custom_matrix(image)
        show_image(image, "Custom Matrix Transformation")

    # Reset
    elif choice == "6":
        image = original.copy()
        show_image(image, "Original Image")
        print("Image reset successfully.")

    # Exit
    elif choice == "7":
        print("Program ended.")
        break

    else:
        print("Invalid choice. Please select 1-7.")