

def point_in_rect(point : tuple, figure) -> (bool):
    """Detecta si un punto en coordenada pasa por la coordenadas de una figura

    Args:
        point (tuple, figure): Tupla de dos puntos en eje x y y

    Returns:
        _type_: Devuelve un Bool para confirmar si se detecta el punto en figura
    """
    x, y = point  # Esto se llama desempaquetado de tuplas
    
    return x <= figure.right and x >= figure.left and y >= figure.top and y <= figure.bottom


def detected_colition(figure_1, figure_2) -> (bool):
    """Detecta si dos figura hacen colision 

    Args:
        figure_1 (RectValue): figura a detectar 
        figure_2 (RectValue): figura a detectar
    Returns:
        bool: Retorna si han colicionado o no los dos objetos
    """
    colition = False
    # Otra manera de usar el desempaquetamiento de tuplas
    for r1, r2 in [(figure_1, figure_2),(figure_2, figure_1)]:
        if point_in_rect(r1.topleft, r2) or \
            point_in_rect(r1.topright, r2) or \
            point_in_rect(r1.bottomleft, r2) or \
            point_in_rect(r1.bottomright, r2):
                colition = True
    
    return colition


def cal_ratio(figure) -> (int):
    """Calcula el radio de una figura que se pasa por argumento

    Args:
        figure (RectValue): figura a calcular radio

    Returns:
        int: Devuelve un numero de tipo int
    """
    return figure.height // 2


def distance_between_points(point_1 : tuple, point_2 : tuple) -> (float):
    """Calcula la distancia entre dos puntos ingresados como parametro 

    Args:
        point_1 (tupla): punto de figura 1
        point_2 (tupla): punto de figura 2
    Returns:
        _type_: _description_
    """
    x1, y1 = point_1
    x2, y2 = point_2
    
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def detected_colition_circle(figure_1, figure_2) -> (bool):
    """Detecta la colicion de dos circulos 

    Args:
        figure_1 (RectValue): Figura creada a detectar
        figure_2 (RectValue): Figura creada a detectar
    Returns:
        bool: Devuelve false por defecto si no detecta colision
    """
    colition = False
    
    r1 = cal_ratio(figure_1)
    r2 = cal_ratio(figure_2)
    
    distance = distance_between_points(figure_1.center, figure_2.center)
    
    if distance <= (r1 + r2):
        colition = True
    
    return colition