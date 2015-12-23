# print("calculating colors + draw")
    for region in voronoi.regions:
        if not (-1 in region):

            polygon = list()
            for i in region:
                polygon.append(voronoi.vertices[i])
            # print(str(polygons) + "\n")

            polygon_tuples = list()
            for l in polygon:
                polygon_tuples.append(tuple(l))

            # print(region)
            # print(str(polygon_tuples) + "\n")
            # quit()

            # point_list = []
            # print (points[asdf])

            # for polygon in polygon:
            #     print(str(polygon) + "\n")

            # print(polygon)

            rgb = (0, 0, 0)

            for point in points:
                if polygon:
                    if path.Path(polygon).contains_point(point):
                        rgb = get_color_of_point(point, rgb_im, width, height)
                        points.remove(point)
                        break
                else:
                    pass
                    # print("why is polygon is empyt")

            # rgb = random_color()
            # print (rgb)

            if polygon_tuples:
                draw.polygon(polygon_tuples, rgb)
        else:
            pass
            # print(region)