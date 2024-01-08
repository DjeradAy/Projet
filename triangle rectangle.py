def is_the_triangle_right_angle(list_edge_sizes):
    """
    This function return true when the triangle is right angle and false when it's not the case.
    """
    list_edge_sizes.sort()
    hypothenus = list_edge_sizes[-1]
    if hypothenus**2 == list_edge_sizes[0]**2 + list_edge_sizes[1]**2:
        return True
    else :
        return False
