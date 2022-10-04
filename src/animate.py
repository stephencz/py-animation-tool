import numpy as np
from PIL import Image
from PIL import ImageFilter

"""
Quantizes and dithers an image and reduces its overall color count.
@param image The image to quantize and dither
@param colors The number of colors to have in the image
@return Image
"""
def quantize(image, colors):
  image.quantize(colors)
  return image.convert(mode='RGB')

"""
Quantizes and dithers an image and reduces it to a black and white image.
@param image The image to quantize and dither.
@return Image
"""
def two_bit_quantize(image):
  image.quantize(2)
  return image.convert(mode='1')

"""
Applies the pixel shift image to the passed in image.
@param base_image The base image to generate the pixel shift from.
@return Image
"""
def pixel_shift(base_image):
  pass

"""
Generates the desired number of image frames with the pixel 
shift effect applied.
@param base_image The base image to generate pixel shift frames from.
@return Array of Images
"""
def generate_pixel_shift_frames(base_iamge):
  pass

"""
Makes a GIF from the provided frames.
@param frames An array of image frames which the GIF will be made from
@param output The output path and filename of the GIF.
@param duration The duration of the GIF.
"""
def make_gif_from_images(frames, output, duration):
    first_frame = frames[0]
    first_frame.save(output, format="GIF", append_images=frames, save_all=True, duration=duration, loop=0)

"""
Makes a GIF using the pixel shift effect
@param output The output path and filename of the GIF.
@param base_image The path and filename of the input image.
@param The number of frames to generate (60 frames)
@param The overall length of the GIF (1000ms)
"""
def make_pixel_shift_gif(output, base_image, frames = 60, duration = 1000):
  image = Image.open(base_image)
  image = two_bit_quantize(image)
  frames = generate_pixel_shift_frames(image)
  make_gif_from_images(frames, output, duration)

make_pixel_shift_gif("output.gif", "sample/sample.jpg")