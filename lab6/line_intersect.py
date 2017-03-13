def line_intersect(line1, line2):
    """
    Find the intersection of two lines.
    :param line1: list of first line coordinates
    :param line2: list of second line coordinates
    :return: coordinates of the intersection point
    """
    b1 = (line1[1][1] - line1[0][1]) / (line1[1][0] - line1[0][0])
    b2 = (line2[1][1] - line2[0][1]) / (line2[1][0] - line2[0][0])
    a1 = line1[0][1] - b1 * line1[0][0]
    a2 = line2[0][1] - b2 * line2[0][0]

    if a1 == a2 and b1 == b2:
        return line1

    xi = - (a1 - a2) / (b1 - b2)
    yi = a1 + b1 * xi
    if (line1[0][0] - xi) * (xi - line1[1][0]) >= 0\
       and (line2[0][0] - xi) * (xi - line2[1][0]) >= 0\
       and (line1[0][1] - yi) * (yi - line1[1][1]) >= 0\
       and (line2[0][1] - yi) * (yi - line2[1][1]) >= 0:
        return xi, yi
    return None
