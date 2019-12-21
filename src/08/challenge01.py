def main():
    print("AdventOfCode - 08 - Challenge 01")
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

        layer_fewest_zeros = layers[0]
        for layer in layers:
            if layer_fewest_zeros.count_str('0') > layer.count_str('0'):
                layer_fewest_zeros = layer

        print("The layer with the fewest zeros include {} '1' and {} '2' -> {}".format(
          layer_fewest_zeros.count_str('1'),
          layer_fewest_zeros.count_str('2'),
          layer_fewest_zeros.count_str('1') * layer_fewest_zeros.count_str('2')))


class Layer:
    width = 0
    height = 0
    pixels = ''

    def __init__(self, height, width, pixels):
        self.height = height
        self.width = width
        self.pixels = pixels

    def count_str(self, search_str):
        return self.pixels.count(search_str)



if __name__ == "__main__":
    main()
