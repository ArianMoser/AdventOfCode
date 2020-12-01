def main():
    print("AdventOfCode - 08 - Challenge 02")
    f = open("input.txt", "r")
    image_width = 25
    image_height = 6
    layer_length = image_width * image_height
    layers = []
    if f.mode == 'r':
        f_content = f.read()
        chunks = [f_content[i:i+layer_length] for i in range(0, len(f_content), layer_length)]
        for chunk in chunks:
            if len(chunk) == image_width * image_height:
                layers.append(Layer(image_height, image_width, chunk))

        print("Found {} different layers".format(len(layers)))

        final_picture = layers[0]
        for pixel_position in range(0, image_width*image_height):
            try:
                for layer in layers:
                    final_picture.pixels[pixel_position] = layer.pixels[pixel_position]
                    if layer.pixels[pixel_position] != 2:
                        raise NonTransparentPixelFound
            except NonTransparentPixelFound:
                pass

        print(final_picture.print_pixel().replace('0', ' '))

        print("\n\nPicture: \n {}".format(final_picture.pixels))

class Error(Exception):
    pass

class NonTransparentPixelFound(Error):
    pass

class Layer:
    width = 0
    height = 0
    pixels = ''

    def __init__(self, height, width, pixels):
        self.height = height
        self.width = width
        self.pixels = list(map(int, list(pixels)))

    def count_str(self, search_str):
        return self.pixels.count(search_str)

    def print_pixel(self):
        pixel_str = ''
        for i in range(0, self.height * self.width):
            if i%self.width == 0:
                pixel_str += '\n'
            pixel_str += str(self.pixels[i])
        return pixel_str




if __name__ == "__main__":
    main()
