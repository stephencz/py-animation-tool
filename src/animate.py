import imageio
from PIL import Image
from PIL import ImageChops
from random import randint, choice

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
def pixel_shift(base_image, hmax=3, vmax=3, rmax=3, smax=3):

  horizontal_shift = randint(0, hmax)
  vertical_shift = randint(0, vmax)
  rotation_shift = randint(0, rmax)
  scale_shift = randint(0, smax)
  size = base_image.size

  shifted_image = base_image.copy()  

  if choice([True, False]):
    shifted_image = ImageChops.offset(base_image, horizontal_shift * -1, vertical_shift * -1)

  else:
    shifted_image = ImageChops.offset(base_image, horizontal_shift, horizontal_shift)

  if choice([True, False]):
    shifted_image = shifted_image.rotate(rotation_shift * -1, Image.Resampling.NEAREST, expand=False)

  else:
    shifted_image = shifted_image.rotate(rotation_shift * 1, Image.Resampling.NEAREST, expand=False)

  if choice([True, False]):
    shifted_image = shifted_image.resize((size[0] - scale_shift, size[1] - scale_shift), Image.Resampling.NEAREST)

  else:
    shifted_image = shifted_image.resize((size[0] + scale_shift, size[1] + scale_shift), Image.Resampling.NEAREST)

  return shifted_image



"""
Generates the desired number of image frames with the pixel 
shift effect applied.
@param base_image The base image to generate pixel shift frames from.
@return Array of Images
"""
def generate_pixel_shift_frames(base_image, frames=60, settings=(3, 3, 3, 3)):
  image_frames = []

  for i in range(0, frames):
    image_frames.append(pixel_shift(base_image, hmax=settings[0], vmax=settings[1], rmax=settings[2], smax=settings[3]))

  return image_frames


"""
Makes a GIF from the provided frames.
@param frames An array of image frames which the GIF will be made from
@param output The output path and filename of the GIF.
@param duration The duration of the GIF.
"""
def make_gif_from_images(frames, output, duration):
    first_frame = frames[0]
    first_frame.save(output, format="GIF", save_all=True, append_images=frames, duration=duration, loop=False)

"""
Makes a GIF using the pixel shift effect
@param output The output path and filename of the GIF.
@param base_image The path and filename of the input image.
@param The number of frames to generate (60 frames)
@param The overall length of the GIF (1000ms)
"""
def make_pixel_shift_gif(output, base_image, frames = 60, duration = 100, settings=(3, 3, 3, 3)):
  image = Image.open(base_image)
  image_frames = generate_pixel_shift_frames(image, frames, settings)
  make_gif_from_images(image_frames, output, duration)

make_pixel_shift_gif("output.gif", "sample/stick.png", frames=200, duration=100, settings=(3, 3, 3, 10))

# image = Image.open("sample/text.png")
# shifted = pixel_shift(image)

# shifted.save("output.png")