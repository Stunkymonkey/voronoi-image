#!/usr/bin/env python3
import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
from PIL import Image, ImageDraw
import os
from optparse import OptionParser
import random


parser = OptionParser()
parser.add_option("-i", "--image", type="string", dest="imagename",
                  help="Name of Image")
parser.add_option("-c", "--count", type="string", dest="count",
                  default=0, help="amount of voronoi-points")
parser.add_option("-r", "--randomcolor", action="store_true", dest="randomcolor",
                  default=False, help="random color in picture")

(options, args) = parser.parse_args()
img_path = options.imagename
if (img_path is None):
    print("No image file given")
    quit()
num_cells = int(options.count)
if (num_cells is None):
    print("No amount of cells given")
    quit()
randomcolor = bool(options.randomcolor)


def random_color():
    """
    return a random color
    """
    red = random.randrange(0, 255)
    blue = random.randrange(0, 255)
    green = random.randrange(0, 255)
    rgbl = [red, blue, green]
    return tuple(rgbl)


def scale_points(points, width, height):
    """
    scale the points to the size of the image
    """
    scaled_points = []
    for x, y in points:
        x = x * width
        y = y * height
        scaled_points.append([x, y])
    return scaled_points


def generate_voronoi_diagram(num_cells, width, height):
    """
    generate voronoi diagramm as polygons
    """
    # make up data points
    points = np.random.rand(num_cells - 4, 2)
    default = np.array([np.array([0., 0.]), np.array(
        [1., 0.]), np.array([0., 1.]), np.array([1., 1.])])
    points = np.concatenate((points, default), axis=0)
    # print (points)

    # scale them
    points = scale_points(points, width, height)
    # print (points)

    # compute Voronoi tesselation
    vor = Voronoi(points)

    # plot
    voronoi_plot_2d(vor)

    return vor, points


def get_color_of_point(point, rgb_im, width, height):
    """
    get the color of specific point
    """
    x = int(point[0])
    y = int(point[1])
    new_point = (x, y)

    try:
        return rgb_im.getpixel(new_point)
    except:
        # unsure if this is needed
        new_point = list(new_point)
        if (new_point[0] == width):
            new_point[0] -= 1
        if (new_point[1] == height):
            new_point[1] -= 1
        new_point = tuple(new_point)
        # print("new point = " + str(new_point) + "\n")
        return rgb_im.getpixel(new_point)


def makeup_polygons(draw, num_cells, width, height, rgb_im, random):
    """
    makeup and draw polygons
    """
    # print("calculating diagramm")
    voronoi, points = generate_voronoi_diagram(num_cells, width, height)

    for point, index in zip(points, voronoi.point_region):
        # getting the region of the given point
        region = voronoi.regions[index]

        # gettings the points ind arrays
        polygon = list()
        for i in region:
            # if vektor is out of plot do not add
            if i != -1:
                polygon.append(voronoi.vertices[i])

        # make tuples of the points
        polygon_tuples = list()
        for l in polygon:
            polygon_tuples.append(tuple(l))

        rgb = (0, 0, 0)
        if random:
            # gettings random color
            rgb = random_color()
        else:
            # getting colors of the middle point
            rgb = get_color_of_point(point, rgb_im, width, height)

        # drawing the calculated polygon with the color of the middle point
        if polygon and polygon_tuples:
            draw.polygon(polygon_tuples, rgb)


def make_image(img_path, num_cells, random):
    """
    make image out of the old image
    """

    try:
        im = Image.open(img_path).convert('RGB')
    except (FileNotFoundError):
        print("Image not found")
        quit()
    rgb_im = im.convert('RGB')
    width, height = im.size

    if (num_cells > ((width * height) / 10)):
        print("Sorry your image ist too small, or you want to many polygons.")
        quit()
    if num_cells <= 5:
        print("you have to have more than 5 cells")
        quit()

    image = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(image)

    makeup_polygons(draw, num_cells, width, height, rgb_im, random)

    path, imagename = os.path.split(img_path)
    imagename = imagename.split(".")[0]
    # print (imagename)

    image.save(imagename + "-voronoi.jpeg", "JPEG")
    # image.show()


if __name__ == '__main__':
    make_image(img_path, num_cells, randomcolor)
