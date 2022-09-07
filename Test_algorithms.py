    
def main():    
    
    voxel_grid = []
    minimum_index = 0
    maximum_index = 0
    voxel_size = 0.5
    points_to_remove = 10

    # Iterate through Voxel Grid and find when certain points are nearby
    for iX in range(int(10.0/voxel_grid_size * lowestVal[0]), int(10.0/voxel_grid_size * highestVal[0])):
        for iY in range(int(10.0/voxel_grid_size * lowestVal[1]), int(10.0/voxel_grid_size * highestVal[1])):
            for iZ in range(int(10.0/voxel_grid_size * lowestVal[2]), int(10.0/voxel_grid_size * highestVal[2])):
                print("X is: " + str(iX) + ", Y is " + str(iY) + ", Z is " + str(iZ))
                # Updates minimum index to the lowest possible X value of np_input at index that is in a cube around the voxel grid intersection
                for index in range(minimum_index, len(np_input)):
                    if (np_input[index][0] * (10.0/voxel_grid_size)  - iX > -voxel_grid_size/2):
                        minimum_index = index
                        break
                
                # Updates maximum index to the highest possible X value of np_input at index that is in a cube around the voxel grid intersection
                for index in range(minimum_index, len(np_input)):
                    if (np_input[index][0] * (10.0/voxel_grid_size) - iX > voxel_grid_size/2):
                        maximum_index = index - 1
                        break

                shortestDistFromVoxel = [iX + voxel_grid_size/2, iY + voxel_grid_size/2, iZ + voxel_grid_size/2]
                found = False
                for index in range(minimum_index, maximum_index):
                    if ((np_input[index][0] * (10.0/voxel_grid_size) - iX)**2 + (np_input[index][1] * (10.0/voxel_grid_size) - iY)**2 + (np_input[index][2] * (10.0/voxel_grid_size) - iZ)**2 <= (shortestDistFromVoxel[0]  - iX)**2 + (shortestDistFromVoxel[1] - iY)**2 + (shortestDistFromVoxel[2] - iZ)**2):
                        shortestDistFromVoxel = [float(np_input[index][0]) * (10.0/voxel_grid_size), float(np_input[index][1]) * (10.0/voxel_grid_size), float(np_input[index][2]) * (10.0/voxel_grid_size)]
                        found = True
                
                if found:
                    print(shortestDistFromVoxel)
                    output.append(shortestDistFromVoxel)
                else:
                    print("Not found")



    # Search
        for index in range(len(np_input)):
        print("New index taken and starting process over again !!!!!!")
        currPoint = np_input[index]
        count = 0
        
        for remove_index in range(index + 1, len(np_input)):  
            if (np_input[remove_index][0] - currPoint[0])**2 + (np_input[remove_index][1] - currPoint[1])**2 + (np_input[remove_index][2] - currPoint[2])**2 <= (voxel_size/2)**2:
                print("removed index at", remove_index)
                count += 1
                np.delete(np_input, remove_index)
            if count >= points_to_remove:
                break