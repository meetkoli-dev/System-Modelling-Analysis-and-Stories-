# System-Modelling-Analysis-and-Stories-
My all assignment of course SMAS are uploaded in this Repository.

# Image Transformation Toolbox

## About the Project

This project is a simple image transformation toolbox made using Python. It allows the user to select an image and perform different transformations on it.

The program provides the following options:

* **Rotate:** Rotates the image by an angle entered by the user.
* **Resize:** Increases or decreases the size of the image according to the given factor.
* **Flip:** Flips the image horizontally, vertically, or in both directions.
* **Shear:** Slants the image in the x or y direction using the given shear values.
* **Custom Matrix:** Allows the user to enter their own 2×3 transformation matrix.
* **Reset:** Brings the image back to its original form.
* **Exit:** Closes the program.

## How the Program Works

First, the user selects an image from the computer. The image is then loaded into the program.

After that, a menu is displayed where the user can choose the required transformation. Depending on the selected option, the program asks for the required values, such as rotation angle, resize factor or shear value.

The transformation is then applied to the current image and the result is displayed.

The program uses OpenCV for performing the image transformations and Matplotlib for displaying the image. Since OpenCV reads images in BGR format and Matplotlib uses RGB format, the image is converted before displaying it so that the colours appear correctly.

One useful feature is that the transformations can be performed one after another. If the user wants to start again from the original image, the **Reset** option can be used.

## Main Idea

The main purpose of this project is to understand how different **image transformations** work practically. It helps in understanding rotation, resizing, flipping, shearing and matrix-based transformations using a real image.

