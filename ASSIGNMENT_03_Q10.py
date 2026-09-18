import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


image_path = input("Enter image file name/path: ")

img = Image.open(image_path).convert("RGB")

print("\nImage loaded successfully!")
print("Image size:", img.size)


print("\nWhat do you want to do?")
print("1. A1 - Scaling")
print("2. A2 - 90 degree Rotation")
print("3. A3 - Horizontal Shear")
print("4. A4 - Reflection in y-axis")
print("5. A5 - Projection onto x-axis")

choice = input("\nEnter your choice (A1/A2/A3/A4/A5): ").upper()


matrices = {

    "A1": np.array([
        [2, 0],
        [0, 0.5]
    ]),

    "A2": np.array([
        [0, -1],
        [1, 0]
    ]),

    "A3": np.array([
        [1, 1],
        [0, 1]
    ]),

    "A4": np.array([
        [-1, 0],
        [0, 1]
    ]),

    "A5": np.array([
        [1, 0],
        [0, 0]
    ])
}


names = {
    "A1": "Scaling",
    "A2": "90 Degree Rotation",
    "A3": "Horizontal Shear",
    "A4": "Reflection in y-axis",
    "A5": "Projection onto x-axis"
}


if choice not in matrices:
    print("Invalid choice!")
    print("Please enter A1, A2, A3, A4 or A5.")
    exit()


A = matrices[choice]



e1 = np.array([1, 0])
e2 = np.array([0, 1])

Te1 = A @ e1
Te2 = A @ e2

print("\n-----------------------------------------")
print(choice, "-", names[choice])
print("-----------------------------------------")

print("\n(a) Basis vectors:")
print("T(e1) =", Te1)
print("T(e2) =", Te2)



rank = np.linalg.matrix_rank(A)

print("\n(c) Rank of A =", rank)



if rank < 2:
    print("\n(d) Information loss: YES")
else:
    print("\n(d) Information loss: NO")



sentences = {

    "A1":
    "The columns of A1 show that the x-direction is scaled by 2 and the y-direction is scaled by 0.5.",

    "A2":
    "The columns of A2 rotate the coordinate directions by 90 degrees.",

    "A3":
    "The second column adds an x-component to the y-direction, producing a horizontal shear.",

    "A4":
    "The first column reverses the x-direction while the y-direction remains unchanged, producing reflection in the y-axis.",

    "A5":
    "The second column becomes zero, so the y-direction is removed and information is lost."
}

print("\n(e) Explanation:")
print(sentences[choice])



img_array = np.array(img)

h, w = img_array.shape[:2]

# Image centre
cx = (w - 1) / 2
cy = (h - 1) / 2


def transform_image(image, A):

    h, w = image.shape[:2]

    cx = (w - 1) / 2
    cy = (h - 1) / 2

    # Four corners relative to centre
    corners = np.array([
        [-cx, -cy],
        [ cx, -cy],
        [-cx,  cy],
        [ cx,  cy]
    ]).T

    # Transform corners
    new_corners = A @ corners

    min_x = np.floor(new_corners[0].min())
    max_x = np.ceil(new_corners[0].max())

    min_y = np.floor(new_corners[1].min())
    max_y = np.ceil(new_corners[1].max())

    new_w = int(max_x - min_x + 1)
    new_h = int(max_y - min_y + 1)



    A_visual = A.copy()

    if np.linalg.matrix_rank(A) < 2:

        print("\nNOTE:")
        print("A5 true matrix is:")
        print(A)

        print("\nA small y-scale is being used only")
        print("to make the projection visible.")

        A_visual = np.array([
            [1, 0],
            [0, 0.01]
        ])

        new_corners = A_visual @ corners

        min_x = np.floor(new_corners[0].min())
        max_x = np.ceil(new_corners[0].max())

        min_y = np.floor(new_corners[1].min())
        max_y = np.ceil(new_corners[1].max())

        new_w = int(max_x - min_x + 1)
        new_h = int(max_y - min_y + 1)


    # Inverse transformation
    A_inv = np.linalg.inv(A_visual)

    # Create output image
    output = Image.new(
        "RGB",
        (new_w, new_h),
        (255, 255, 255)
    )


    src = np.zeros((new_h, new_w, 2))

    for y in range(new_h):
        for x in range(new_w):

            # Coordinate relative to transformed centre
            p = np.array([
                x + min_x,
                y + min_y
            ])

            # Transform back to original coordinates
            original = A_inv @ p

            original_x = original[0] + cx
            original_y = original[1] + cy

            src[y, x] = [original_x, original_y]

    # Use nearest pixel to preserve original RGB values
    result = np.zeros((new_h, new_w, 3), dtype=np.uint8)
    result[:, :] = 255

    for y in range(new_h):
        for x in range(new_w):

            ox = int(round(src[y, x, 0]))
            oy = int(round(src[y, x, 1]))

            if 0 <= ox < w and 0 <= oy < h:
                result[y, x] = image[oy, ox]

    return result



result = transform_image(img_array, A)



print("\n(b) Displaying transformed image...")


plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(result)
plt.title(choice + " - " + names[choice])
plt.axis("off")

plt.tight_layout()
plt.show()