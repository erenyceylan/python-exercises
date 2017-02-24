#Cost of tile based on floor

def tiles(tilew, tileh, floorw, floorh, cost):
    floorh = float(floorh)
    floorw = float(floorw)
    tileh = float(tileh)
    tilew = float(tilew)
    cost = float(cost)

    tiles_for_h = floorh // tileh
    tiles_for_w = floorw // tilew
    
    if floorw % tilew != 0:
        tiles_for_w += 1
    if floorh % tileh != 0:
        tiles_for_h += 1
    
    total_cost = tiles_for_w * tiles_for_h * cost
    return total_cost


print(tiles(input("Type widht of tile: "),input("Type height of tile: "),input("Type width of floor: "),input("Type height of floor: "),input("Type cost per tile: ")))