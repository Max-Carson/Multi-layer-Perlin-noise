# Multi-layer-Perlin-noise
Multi-Layer Perlin noise generation programed in python with 2 graphical representation methods using the Pygame library.

#This code is used to generate multi-layer Perlin noise. It uses the pygame library to create a graphical representation of the noise. It uses two noise functions to generate two layers of noise, which are then combined to create the final noise. It also calculates the minimum and maximum values of the noise and uses them to determine the intensity of the colors used to represent the noise. If you select "grayscale" as the representation_method below, it will display the noise in grayscale which is the default. If you select "terrain", it will display the noise as terrain. (Any misspelling in the representation_method variable will result in grayscale as default.)

#At the beginning of the code, two variables are set: the num_rows variable which determines the number of rows and columns of noise, and the screen_size variable which determines the size of the window where the noise will be displayed. There is also a representation_method variable which can be set to either "grayscale" or "terrain", with "grayscale" being the default option.

#Next, two noise functions are defined. The first noise function is used to generate a noise array with the given noise intensity, change amount, and smoothing amount. The second noise function is used to generate a second noise array, with different settings.

#Once the two noise arrays are generated, the code then combines them to create the final noise. It does this by adding the first noise array to the second multiplied by a factor of 7.

#The display function is then used to create the window and draw the noise on the screen. It calculates the minimum and maximum values of the noise and uses them to determine the intensity of the color used to represent the noise. If the representation_method variable is set to "terrain", the code will draw different colors based on the intensity of the noise. Otherwise, it will draw the noise in grayscale.

#Finally, the code calls both the gen_noise and display functions, which generates and displays the noise.
