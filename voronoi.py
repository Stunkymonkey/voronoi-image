#!/usr/bin/env python3
import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
from matplotlib import path
from PIL import Image, ImageDraw
import ntpath
from optparse import OptionParser
import random


parser = OptionParser()
parser.add_option("-i", "--image", type="string", dest="imagename",
                  help="Name of Image")
parser.add_option("-c", "--count", type="string", dest="count",
                  default=0, help="amount of voronoi-points")

(options, args) = parser.parse_args()
img_path = options.imagename
num_cells = int(options.count)


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
    points = np.random.rand(num_cells, 2)
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
    x = int(point[0] + 0.5)
    y = int(point[1] + 0.5)
    new_point = (x, y)
    # print (new_point)

    rgb = (0, 0, 0)

    try:
        rgb = rgb_im.getpixel(new_point)
    except:
        print (new_point)
        new_point = list(new_point)
        if (new_point[0] == width):
            new_point[0] -= 1
        if (new_point[1] == height):
            new_point[1] -= 1
        new_point = tuple(new_point)
        # print (str(new_point) + "\n")
        rgb = rgb_im.getpixel(new_point)
        # deswegen hier kommen schwarze punkte
    return rgb


def makeup_polygons(draw, num_cells, width, height, rgb_im):
    """
    makeup and draw polygons
    """
    voronoi, points = generate_voronoi_diagram(num_cells, width, height)

    for region in voronoi.regions:
        if not (-1 in region):

            # for point_region in voronoi.point_region:
                # print (point_region)
                # print (region[point_region])

            polygon = [voronoi.vertices[i] for i in region]
            # print (str(polygon) + "\n")

            polygon_tuples = [tuple(l) for l in polygon]
            # print (str(polygon_tuples) + "\n")

            point_list = []
            # print (points[asdf])
            for point in points:
                try:
                    p = path.Path(polygon)
                    if (p.contains_point(point)):
                        rgb = get_color_of_point(point, rgb_im, width, height)
                        point_list.extend(point)
                        points.remove(point)
                        # print (point)
                        # print ("just found")
                except:
                    try:
                        p = path.Path(polygon)
                        if (p.contains_point(point)):
                            rgb = get_color_of_point(
                                point, rgb_im, width, height)
                            point_list.extend(point)
                            points.remove(point)
                            # print ("just found")
                    except:
                        pass
                        # print ("Found Nothing")

            # rgb = random_color()

            # print (rgb)

            if polygon_tuples:
                draw.polygon(polygon_tuples, rgb)


def make_image(img_path, num_cells):
    """
    make image out of the old image
    """

    try:
        im = Image.open(img_path).convert('RGB')
    except (FileNotFoundError):
        print ("Image not found")
        quit()
    rgb_im = im.convert('RGB')
    width, height = im.size

    if (num_cells > ((width * height) / 10)):
        print ("Sorry your image ist too small, or you want to many polygons.")
        quit()

    print ("Making the Voronoi Image...")

    image = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(image)

    makeup_polygons(draw, num_cells, width, height, rgb_im)

    path, imagename = ntpath.split(img_path)
    # print (imagename)

    image.save(imagename + "-voronoi.jpeg", "JPEG")
    image.show()


if __name__ == '__main__':
    make_image(img_path, num_cells)
