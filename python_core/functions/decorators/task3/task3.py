from functools import wraps


def validate(fn):
  '''
  Add corresponded arguments and implementation here. 
  '''
  @wraps(fn)
  def wrapper(*args):
    for pixel in args:
      if pixel > 256 or pixel < 0:
        return "Function call is not valid!"

    return fn(*args)
  return wrapper


@validate
def set_pixel(x: int, y: int, z: int) -> str:
  return "Pixel created!"

