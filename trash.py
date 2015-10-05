
    regions = voronoi.regions
    point_region = voronoi.point_region

    """for i in range(num_cells):
        point = points[i]
        polygon = []

        for j in regions[point_region[i]]:
            polygon.append(voronoi.vertices[j])

        for k in polygon:
            if k.any() < 0:
                print ("test")

        if polygon == []:
            print ("empty")
            continue

        p = path.Path(polygon)

        # print (p)
        # print (point)

        if (p.contains_point(point)):
            print ("True")

        rgb = get_color_of_point(point, rgb_im, width, height)

        # print (polygon)
        polygon_tuples = tuple(polygon)
        # print (polygon_tuples)

        # rgb = random_color()

        try:
            draw.polygon(polygon_tuples, rgb)
            # print ("\n")
        except:
            print ("little Error")"""

    """"for i in voronoi.point_region:
        polygon = voronoi.vertices[i]
        polygon_tuples = tuple(polygon)

        print (polygon_tuples)

        p = path.Path(polygon_tuples)
        print (p)

        print (voronoi.vertices[1])"""

    # polygon = [voronoi.vertices[i] for i in the_regions[point_region[0]]]
    # p = path.Path(polygon)

    #  print (p)
    # if(p.contains_point(points[0])):
    #     print ("True")

    """
    for i in range(num_cells):
        # print (region)
        if not (-1 in voronoi.regions[i]):
            polygon = []
            for j in regions[point_region[i]]:
                polygon.append(voronoi.vertices[j])

            # print (str(polygon) + "\n")

            polygon_tuples = [tuple(l) for l in polygon]
            # print (polygon_tuples)

            p = path.Path(polygon)

            print (p)

            point = points[i]

            # print (point)

            rgb = random_color()

            if(p.contains_point(point)):
                try:
                    rgb = get_color_of_point(point, rgb_im, width, height)
                    print (rgb)
                except:
                    pass
                    # print ("Fail")

            if polygon_tuples:
                draw.polygon(polygon_tuples, rgb)
                # print ("\n")

"""

"""
    for point_region in voronoi.point_region:
        print (point_region)
        region = voronoi.regions[point_region]
        print (region)

        if not (-1 in region):
            polygon = []
            for j in regions[point_region[i]]:
                polygon.append(voronoi.vertices[j])
            # print (str(polygon) + "\n")

            polygon_tuples = [tuple(l) for l in polygon]
            print (polygon_tuples)

            p = path.Path(polygon)

            print (point_region)

            # print (region)

            try:
                print (str(points[point_region]) + "\n")
            except:
                pass

            # if(p.contains_point(points[point_region])):
            #     print ("True")

            rgb = random_color()
            try:
                rgb = get_color_of_point(points[point_region], rgb_im, width, height)
                # print (rgb)
            except:
                pass
                # print ("Fail")

            if polygon_tuples:
                draw.polygon(polygon_tuples, rgb)
"""


"""
    

"""