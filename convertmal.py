import os 
import struct
import numpy as np
from PIL import Image

def determine_image_width(file_size):
    if file_size < 10 * 1024:
        return 32
    elif 10 * 1024 <= file_size <30 * 1024:
        return 64
    elif 30 * 1024 <= file_size <60 * 1024:
        return 128
    elif 60 * 1024 <= file_size <100 * 1024:
        return 256
    elif 100 * 1024 <= file_size <200 * 1024:
        return 384
    elif 200 * 1024 <= file_size <500 * 1024:
        return 512
    elif 500 * 1024 <= file_size <1024 * 1024:
        return 768
    else:
        return 1024
        
def binary_files_to_images(input_folder, output_folder):
    #create the output folder if it doesnt exist
    os.makedirs(output_folder, exist_ok=True)

    #process all binary files in the input folder
    for file_name in os.listdir(input_folder):
        #Make sure the file name has a non-empty extension
        #if '.' in file_name:
            #base_name, extension = os.path.splitext(file_name)
            #if file_name.endswith('.exe'):
            #if extension.lower() == '.exe':    
        input_file = os.path.join(input_folder, file_name)
        
        #get the size of the binary file
        file_size = os.path.getsize(input_file)
        
        #determine image width based on file size
        image_width = determine_image_width(file_size)
            
        with open(input_file, 'rb') as f:
            #read binary content and convert it to pixel values
            binary_data = f.read()
            pixel_values=[int(byte) for byte in binary_data]
        
        #calculate the height to maintain the aspect ratio
        image_height = (len(pixel_values) + image_width -1) // image_width
        
        #ensure pixel_values array has the correct size
        expected_size = image_height * image_width
        if len(pixel_values) < expected_size:
            pixel_values += [0] * (expected_size - len(pixel_values))
        elif len(pixel_values) > expected_size:
            pixel_values = pixel_values[:expected_size]
                
        #reshape the pixel values into a 2D array
        #image_array = np.array(pixel_values).reshape(image_size)
        image_array = np.array(pixel_values).reshape((image_height, image_width))
        
        #convert to PIL image
        image = Image.fromarray(image_array.astype('uint8'), mode='L')
            
        #get the base name of the input file without the extension
        #base_name = os.path.splitext(os.path.basename(input_file))[0]
        base_name, _ = os.path.splitext(file_name)
        
        #save the image with the same base name as the input file
        #output_image = f'{base_name}.png'
        output_image = os.path.join(output_folder, f'{base_name}.png')
        image.save(output_image)

#example usage
#binary_file = '/home/plaiground/Documents/dataset/bodmas/altered/0a0a38fa5884a8b109bad5572b2ab2d568a6fe4621b5f86641c42f7d0d713e79.exe'
#output_image='/home/plaiground/1.png'
input_folder = '/home/remnux/Documents/Example/Sampel Malware/'
output_folder = '/home/remnux/Documents/Example/Grayscale Malware/'
#binary_to_image(binary_file, output_image)
#binary_to_image(binary_file)
binary_files_to_images(input_folder, output_folder)