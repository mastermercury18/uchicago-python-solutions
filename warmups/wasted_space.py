def total_wasted_space(shipments, bin_size):
    total_wasted = 0
    for shipment in shipments:
        left_over = shipment % bin_size 
        wasted_space = bin_size - left_over 
        total_wasted += wasted_space 
    return total_wasted 
print(total_wasted_space([23, 31], 10))