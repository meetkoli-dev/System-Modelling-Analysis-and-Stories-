# System-Modelling-Analysis-and-Stories-
My all assignment of course SMAS are uploaded in this Repository.



QUESTION 10 -->


# Image Transformation Using Matrices

## 1. Introduction

This Python program applies different **linear transformations** to an image using **2×2 matrices**.

The program allows the user to select one of five transformations:

* A1 – Scaling
* A2 – 90° Rotation
* A3 – Horizontal Shear
* A4 – Reflection in y-axis
* A5 – Projection onto x-axis

## 2. Libraries Used

```python
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
```

* **NumPy** – Used for matrices and mathematical calculations.
* **Matplotlib** – Used to display the images.
* **PIL** – Used to open and read the image.

## 3. Taking the Image

```python
image_path = input("Enter image file name/path: ")
img = Image.open(image_path).convert("RGB")
```

The user enters the image path.
The image is opened and converted to **RGB** so that its original colors are maintained.

## 4. Selecting the Transformation

The program asks the user to enter:

```text
A1 / A2 / A3 / A4 / A5
```

Each option represents a different matrix transformation.

## 5. Transformation Matrices

### A1 – Scaling

```text
[ 2    0 ]
[ 0   0.5]
```

* x-direction becomes 2 times larger.
* y-direction becomes 0.5 times smaller.

### A2 – 90° Rotation

```text
[ 0  -1 ]
[ 1   0 ]
```

Rotates the image by **90 degrees**.

### A3 – Horizontal Shear

```text
[ 1  1 ]
[ 0  1 ]
```

Moves points horizontally depending on their y-position.

### A4 – Reflection in y-axis

```text
[-1   0 ]
[ 0   1 ]
```

Reverses the x-direction and produces a reflection about the **y-axis**.

### A5 – Projection onto x-axis

```text
[1  0]
[0  0]
```

Removes the y-component and projects the image onto the **x-axis**.

## 6. Basis Vectors

The program checks where the two basis vectors go:

```python
e1 = [1, 0]
e2 = [0, 1]
```

It calculates:

```python
T(e1) = A @ e1
T(e2) = A @ e2
```

This shows how the transformation changes the **x-axis and y-axis directions**.

## 7. Rank and Information Loss

```python
rank = np.linalg.matrix_rank(A)
```

The rank tells us whether the transformation keeps both dimensions.

* **Rank = 2:** No information loss.
* **Rank < 2:** Information is lost.

For example, A5 has rank 1 because the y-direction is completely removed.

## 8. Transforming the Image

The function:

```python
transform_image(image, A)
```

performs the actual image transformation.

It:

1. Finds the centre of the image.
2. Finds the four corners.
3. Applies the transformation matrix to the corners.
4. Calculates the new image size.
5. Uses the **inverse matrix** to find where each output pixel came from in the original image.
6. Copies the original RGB pixel values to the new image.

## 9. Special Case: A5

A5 has rank 1, so its inverse does not exist.

Therefore, the program temporarily uses a very small y-scale:

```text
[1    0   ]
[0   0.01 ]
```

This is only used to make the projection **visually displayable**.
The actual A5 matrix remains:

```text
[1  0]
[0  0]
```

## 10. Final Output

Finally, Matplotlib displays:

* **Original Image**
* **Transformed Image**

This makes it easy to compare the original image with the selected transformation.

## 11. Main Concept

The main idea of the program is:

**Image → Matrix Transformation → Inverse Mapping → Transformed Image**

The program demonstrates how basic linear algebra transformations can be applied to real images.
