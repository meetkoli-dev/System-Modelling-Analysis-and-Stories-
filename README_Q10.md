# System-Modelling-Analysis-and-Stories-
My all assignment of course SMAS are uploaded in this Repository.



# Image Transformation Using Matrices

## About the Project

This project is about applying different matrix transformations to an image using Python. The program first asks the user to enter the image path and then gives five options to choose from.

The five transformations are:

* **A1 – Scaling:** Changes the size of the image in the x and y directions.
* **A2 – 90 Degree Rotation:** Rotates the image by 90 degrees.
* **A3 – Horizontal Shear:** Slants the image in the horizontal direction.
* **A4 – Reflection in y-axis:** Flips the image with respect to the y-axis.
* **A5 – Projection onto x-axis:** Removes the y-direction and projects the image onto the x-axis.

## How the Program Works

First, the image is loaded and converted into RGB format so that the original colours of the image are maintained.

Then, the program asks the user which transformation they want to perform. According to the selected option, the corresponding 2×2 matrix is used.

The program also calculates the transformed basis vectors, which helps to understand how the x and y directions change after applying the matrix.

After that, the rank of the matrix is calculated. If the rank is less than 2, it means some information is lost. This mainly happens in **A5**, because the y-direction is removed.

Finally, the transformation is applied to the image and both the original and transformed images are displayed side by side.

## Main Idea

The main purpose of this project is to understand how **linear algebra and matrix transformations can be applied to images**. It also helps in understanding concepts such as basis vectors, rank, information loss, scaling, rotation, shear, reflection and projection.

