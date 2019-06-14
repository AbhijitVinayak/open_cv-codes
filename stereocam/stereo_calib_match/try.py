from numpy import *

def sph_to_cart(epsilon, alpha, r):
  """
  Transform sensor readings to Cartesian coordinates in the sensor frames.
  """
  p = zeros(3)  # Position vector
  epsilon=deg2rad(epsilon)
  alpha=deg2rad(alpha)
  p[0]=r*cos(alpha)*cos(epsilon)
  p[1]=r*sin(alpha)*cos(epsilon)
  p[2]=r*sin(epsilon)
  # Your code here

  return p

def estimate_params(P):
  """
  Estimate parameters from sensor readings in the Cartesian frame.
  Each row in the P matrix contains a single measurement.
  """
  param_est = zeros(3)

  # Your code here
  A=P[:,:-1]
  b=P[:,-1]
  z=ones((3,1))
  A=append(z,A,axis=1)
  param_est= dot(dot(pinv(dot(transpose(A),A)),transpose(A)),b)

  return param_est

if __name__ == '__main__':
	print(sph_to_cart(5,10,4))
