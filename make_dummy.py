import torch
import os
from torchvision.utils import save_image

def create_dummy(num_images, image_size, path):
    os.makedirs(path, exist_ok=True)
    
    for i in range(num_images):
        image_data = torch.rand(3, image_size, image_size) 
        save_path = os.path.join(path, f'dummy_{i}.jpeg')
        save_image(image_data, save_path)

num_images = 3000 
image_size = 256  
output_path = 'dummy_data' 

create_dummy(num_images, image_size, output_path)