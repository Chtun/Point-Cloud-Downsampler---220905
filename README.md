# Downsampling_Pointcloud
Created for Nova coding challenge on 9/6/2022

In this project, I sought to downsample the pointcloud by using a voxel grid. I averaged all points in a voxel grid cube and included the averaged point in the final 'output.csv' file. This was done by taking each point included in the 'input.csv' file and finding which corresponding voxel grid cube it will fall in. Then, the component values of the point (x, y, z) were added to a sum for each of the component values of all the points in the corresponding voxel grid cube. A count for the number of points in the corresponding voxel grid cube was also tallied, and the (x, y, z) coordinates of the corresponding voxel grid cube was stored in another array 'has_point'.

Once all points were run through this loop, then I removed non-unique points in 'has_point' array. I then iterated through the 'has_point' array and calculated the averages for each of the voxel grid cubes by dividing the 3 sums of the respective component values (x, y, z) by the count of number of points in the corresponding voxel grid cube. Finally, the averaged point was appended to the 'output.csv' file.

Note that the size of the voxel grid cube can be changed depending on how many points you want conserved and how long you want the program to run. The variable 'voxel_size' will determine the length of the side of the voxel grid cube, in meters. I recommend using the setting voxel_size = 0.05, as this leaves about 20,000 points left with a relatively quick runtime and a moderate level of memory usage.


_See relevant comments in 'Downsampling_pointcloud.py' file for breakdown of code according to description above._


