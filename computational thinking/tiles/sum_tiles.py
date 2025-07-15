from tile import Tile


def sum_tiles(matrix: list[list[int]], tiles: list[Tile]) -> int:
    """
    Return the sum of the tile values.

    Inputs:
      matrix: the matrix of values
      tiles: a list of Tiles.

    Return: the sum of the tile values.
    """
    # TODO: complete this function.
    
    total_tile_sum = 0

    for tile in tiles:
        str_tile = str(tile)
        coor_1, coor_2 = eval(str_tile)

        r0, c0 = tuple(coor_1)
        r1, c1 = tuple(coor_2)

        tile_sum = 0

        for i in range(r0, r1+1):
            for j in range(c0, c1+1):
                tile_sum += matrix[i][j]
        total_tile_sum += tile_sum 
    return total_tile_sum

tile_1 = Tile(0, 0, 0, 0)
tile_2 = Tile(0, 0, 1, 1)
tile_3 = Tile(0, 0, 2, 2)

tile_list = [tile_1, tile_2, tile_3]

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

print(sum_tiles(matrix, tile_list))

    