#This code is used to generate multi-layer Perlin noise. 
#It uses the pygame library to create a graphical representation of the noise. 
#It uses two noise functions to generate two layers of noise, which are then combined to create the final noise. 
#It also calculates the minimum and maximum values of the noise and uses them to determine the intensity of the colors used to represent the noise. 
#If you select "grayscale" as the representation_method below, it will display the noise in grayscale which is the default. If you select "terrain", it will display the noise as terrain. (any misspelling in the representation_method variable will result in grayscale as default)

def gen_noise():
  #random number library
  import random

  global num_rows
  global screen_size
  global representation_method
  
  representation_method = "terrain" 
  #(Recomended) "grayscale"=grayscale, 
  #"terrain" = terain
  #mispellings will result in grayscale as default
  
  num_rows = 100 #rows and colomns of the noise (intensity)
  screen_size = 500
  
  #first noise array
  noise_intensity = 2000
  change_amount = 0
  smoothing_amount = 4
  
  #second noise array settings
  second_noise_intensity = 2000
  second_change_amount = 0
  second_smoothing_amount = 50
  
  #initialize the variables
  placeholder = 0  #temporary var used to store values during calculation
  first_noise_array = []
  second_noise_array = []
  
  global combined_noise_array
  combined_noise_array = []
  
  #create a 2D array of 0s
  for x in range(num_rows):
      nested = []
      for y in range(num_rows): 
        nested.append(0)
      combined_noise_array.append(nested[:])
  
  #noise function
  def noise(intensity, change, smoothing, rows):
    list = []
    #create a 2D array of 0s
    for x in range(rows):
      nested = []
      for y in range(rows): 
        nested.append(0)
      list.append(nested[:])
    
    #fill the array with random numbers
    for x in range(rows):
        for y in range(rows):
          list[x][y]=random.randint(-intensity, intensity)
    
    #define the smooth function
    def smooth(it):
      for x in range(it):
        for x in range(rows):
            for y in range(rows):
                #check the edges of the array
                if x == 0:
                    if y == 0:
                        placeholder = round((list[x][y+1]+list[x+1][y]+list[x+1][y+1])/3)
                    elif y == rows-1:
                        placeholder = round((list[x][y-1]+list[x+1][y]+list[x+1][y-1])/3)
                    else:
                        placeholder = round((list[x][y-1]+list[x+1][y-1]+list[x+1][y]+list[x+1][y+1]+list[x][y+1])/5)
                elif y == 0:
                    if x == rows-1:
                        placeholder = round((list[x-1][y]+list[x-1][y+1]+list[x][y+1])/3)
                    else:
                        placeholder = round((list[x-1][y]+list[x-1][y+1]+list[x][y+1]+list[x+1][y+1]+list[x+1][y])/5)
                elif x == rows-1:
                    if y == rows-1:
                        placeholder = round((list[x-1][y]+list[x-1][y-1]+list[x][y-11])/3)
                    else: 
                        placeholder = round((list[x][y-1]+list[x-1][y-1]+list[x-1][y]+list[x-1][y+1]+list[x][y+1])/5)
                elif y == rows-1:
                    placeholder = round((list[x-1][y]+list[x-1][y-1]+list[x][y-1]+list[x+1][y-1]+list[x+1][y])/5)
                else:
                    placeholder = round((list[x-1][y]+list[x-1][y-1]+list[x][y-1]+list[x+1][y-1]+list[x+1][y]+list[x-1][y+1]+list[x][y+1]+list[x+1][y+1])/8)
                #add the change to the random numbers
                list[x][y] = random.randint(placeholder-change,placeholder+change)
  
    #smooth function
    smooth(smoothing)
    #return the list
    return(list)
  
  #generate the two layers of noise
  first_noise_array = noise(noise_intensity, change_amount, smoothing_amount, num_rows)
  second_noise_array = noise(second_noise_intensity, second_change_amount, second_smoothing_amount, num_rows)
  
  #combine two layers of noise
  for x in range(num_rows):
      for y in range(num_rows):
          combined_noise_array[x][y]=first_noise_array[x][y]+second_noise_array[x][y]*7

def display():
  #pygame library
  import pygame

  square_size = screen_size/num_rows+num_rows/10
  
  #initiate variables
  maximum = 0
  minimum = 0
  total = 0
  
  #make pygame work
  pygame.init()
  
  #create the screen
  screen = pygame.display.set_mode((screen_size, screen_size))
  
  #set the title
  pygame.display.set_caption("Multi layer perlin noise generator")
  
  #calculate the minimum and maximum values of the noise
  for x in range(num_rows):
        for y in range(num_rows):
          if combined_noise_array[x][y] < minimum:
            minimum = combined_noise_array[x][y]
          if combined_noise_array[x][y] > maximum:
            maximum = combined_noise_array[x][y]
  total = maximum + minimum*-1
  
  running = True

  if representation_method == "terrain":
    #run the loop
    while running:
      #draw the noise on the screen
      for x in range(num_rows):
        for y in range(num_rows):
            #calculate the intensity of the color
            color_intensity = 255 - maximum*(255/total) + (combined_noise_array[x][y]*(255/total))
            #calculate color based on intensity
            color_intensity = int(color_intensity)
            red = 0
            green = 0
            blue = 0
            if color_intensity < 40:
              blue = 150
            elif color_intensity < 70:
              blue = 215
              green = 75
            elif color_intensity < 90:
              blue = 215
              red = 50
              green = 150
            elif color_intensity < 110:
              red = 217
              green = 202
              blue = 128
            elif color_intensity < 120:
              green = 180
            elif color_intensity < 160:
              green = 150
            elif color_intensity < 200:
              green = 100
            elif color_intensity < 230:
              red = 50
              green = 50
              blue = 50
            elif color_intensity < 256:
              red = 200
              green = 200
              blue = 200
              #draw the rectangles
            pygame.draw.rect(screen,(red,green,blue),(x*(screen_size/num_rows),y*(screen_size/num_rows),square_size,square_size))
      while True:
        pygame.display.update()

  else:
    #run the loop
    while running:
      #draw the noise on the screen
      for x in range(num_rows):
        for y in range(num_rows):
              #calculate the intensity of the color
              color_intensity = 255 - maximum*(255/total) + (combined_noise_array[x][y]*(255/total))
              color_intensity = int(color_intensity)
              #draw the rectangles
              pygame.draw.rect(screen,(color_intensity,color_intensity,color_intensity),(x*(screen_size/num_rows),y*(screen_size/num_rows),square_size,square_size))
          
      #update the screen
      while True:
        pygame.display.update()

#run both functions
gen_noise()
display()
