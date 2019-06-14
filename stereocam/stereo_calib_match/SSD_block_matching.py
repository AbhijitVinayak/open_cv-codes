'''
https://erget.wordpress.com/2014/04/27/producing-3d-point-clouds-with-a-stereo-camera-in-opencv/


-> C++ tut https://sourishghosh.com/2017/dense-reconstruction-from-stereo-libelas/

'''
import numpy

fx = 942.8        # lense focal length
baseline = 54.8   # distance in mm between the two cameras
disparities = 64  # num of disparities to consider
block = 15        # block size to match
units = 0.001     # depth units

for i in xrange(block, left.shape[0] - block - 1):
    for j in xrange(block + disparities, left.shape[1] - block - 1):
        ssd = numpy.empty([disparities, 1])

        # calc SSD at all possible disparities
        l = left[(i - block):(i + block), (j - block):(j + block)]
        for d in xrange(0, disparities):
            r = right[(i - block):(i + block), (j - d - block):(j - d + block)]
            ssd[d] = numpy.sum((l[:,:]-r[:,:])**2)

        # select the best match
        disparity[i, j] = numpy.argmin(ssd)

# Convert disparity to depth
depth = np.zeros(shape=left.shape).astype(float)
depth[disparity > 0] = (fx * baseline) / (units * disparity[disparity > 0])

sbm = cv2.StereoBM_create(numDisparities=disparities,
                          blockSize=block)

disparity = sbm.compute(left, right)

depth = np.zeros(shape=left.shape).astype(float)
depth[disparity > 0] = (fx * baseline) / (units * disparity[disparity > 0])
