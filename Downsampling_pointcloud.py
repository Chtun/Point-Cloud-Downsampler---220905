def main():
    input = []
    output = [['x', 'y', 'z']]
    highestVal = [-100, -100, -100]
    lowestVal = [100, 100, 100]

    # Create 2D array 'input' from data table in 'input.csv' file
    with open('input.csv', newline='') as csvfile:
        
        
        input_table = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(input_table)
        for row in input_table:
            input.append(row)
            for i in range(len(row)):
                if float(row[i]) > highestVal[i]:
                    highestVal[i] = float(row[i])
                elif float(row[i]) < lowestVal[i]:
                    lowestVal[i] = float(row[i]) 
    
    # Sort input array by 'x' column
    np_input = np.array(input)
    np_input = np_input.astype(float)
    np_input = np_input[np_input[:, 0].argsort()]

    # Initialize size of voxel cube and size of voxel grid
    voxel_size = 0.05
    voxel_x_range = ToVoxel(highestVal[0], lowestVal[0], voxel_size) + 1 #int(1.0/voxel_size * highestVal[0]) + 1 - int(1.0/voxel_size * lowestVal[0])
    voxel_y_range = ToVoxel(highestVal[1], lowestVal[1], voxel_size) + 1#int(1.0/voxel_size * highestVal[1]) + 1 - int(1.0/voxel_size * lowestVal[1])
    voxel_z_range = ToVoxel(highestVal[2], lowestVal[2], voxel_size) + 1 #int(1.0/voxel_size * highestVal[2]) + 1 - int(1.0/voxel_size * lowestVal[2])
    print(voxel_x_range, voxel_y_range, voxel_z_range)
    print("Voxel x, y, and z range")

    #initialize voxel_grid and array 'has_point' to hold voxel cube points that have points from input in them
    voxel_grid = [[[VoxelPoint(0.0, 0.0, 0.0, 0) for z in range(voxel_z_range)] for y in range(voxel_y_range)] for x in range(voxel_x_range)]
    has_point = []

    print("Grid initialized.")

    # iterate through points in the input file and keep talley of their components in the voxel grid to later use to average the points
    for index in range(len(np_input)):
        Voxel_X = ToVoxel(np_input[index][0], lowestVal[0], voxel_size) #int((1.0 / voxel_size) * np_input[index][0]) - int(1.0 / voxel_size * lowestVal[0])
        Voxel_Y = ToVoxel(np_input[index][1], lowestVal[1], voxel_size) #int((1.0 / voxel_size) * np_input[index][1]) - int(1.0 / voxel_size * lowestVal[1])
        Voxel_Z = ToVoxel(np_input[index][2], lowestVal[2], voxel_size) #int((1.0 / voxel_size) * np_input[index][2]) - int(1.0 / voxel_size * lowestVal[2])
        voxel_grid[Voxel_X][Voxel_Y][Voxel_Z].x += np_input[index][0]
        voxel_grid[Voxel_X][Voxel_Y][Voxel_Z].y += np_input[index][1]
        voxel_grid[Voxel_X][Voxel_Y][Voxel_Z].z += np_input[index][2]
        voxel_grid[Voxel_X][Voxel_Y][Voxel_Z].count += 1
        if (voxel_grid[Voxel_X][Voxel_Y][Voxel_Z].count == 1):
            has_point.append([Voxel_X, Voxel_Y, Voxel_Z])

    print("Finished Adding to Voxel Grid.")

    # Iterate through each cube in the voxel grid and average their x, y, and z components to find the average point in each cube. Then append average point to output file 
    for index in range(1, len(has_point)):
        averaged_point = [0, 0, 0]
        Voxel_X = has_point[index][0]
        Voxel_Y = has_point[index][1]
        Voxel_Z = has_point[index][2]
        averaged_point[0] = round(voxel_grid[Voxel_X][Voxel_Y][Voxel_Z].x / voxel_grid[Voxel_X][Voxel_Y][Voxel_Z].count, 3)
        averaged_point[1] = round(voxel_grid[Voxel_X][Voxel_Y][Voxel_Z].y / voxel_grid[Voxel_X][Voxel_Y][Voxel_Z].count, 3)
        averaged_point[2] = round(voxel_grid[Voxel_X][Voxel_Y][Voxel_Z].z / voxel_grid[Voxel_X][Voxel_Y][Voxel_Z].count, 3)
        output.append(averaged_point)
        print(Voxel_X, Voxel_Y, Voxel_Z, "voxel point calculated and appended")

    # Output the downsampled file
    OutputCSV(output, "output")





# Output a csv table
def OutputCSV(CSV_Table, name):
    with open(name + '.csv', 'w', newline='') as csvfile:
        cars_table = csv.writer(csvfile, delimiter=',',
                                quoting=csv.QUOTE_NONE, escapechar='\\')
        for i in range(len(CSV_Table)):
            cars_table.writerow(CSV_Table[i])

# Take a point component value and convert it to the correct index in the 'voxel_grid' array
def ToVoxel(value, lowestVal, voxel_size):
        return (int((1.0 / voxel_size) * value) - int(1.0 / voxel_size * lowestVal))

# Store info about points within a Voxel Cube, including the sum of their x, y, and z components, and a count of them.
class VoxelPoint():
    
    def __init__(self, x, y, z, count):
        self.x = x
        self.y = y
        self.z = z
        self.count = count

if __name__ == '__main__':
    import csv
    import numpy as np
    main()
