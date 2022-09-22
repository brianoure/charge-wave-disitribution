import math

"""
x: left to right
y: bottom to top
z: front to back
sphere_elevation_rad: angle between x axis and the point_vector
sphere_azimuth_rad: angle between x axis and the point_vector_x_plane_component(+ve angle moves point_vector_x_plane_component into viewing field/page)
sphere_radius: point vector magnitude
cylinder_radius: magnitude of the point_vector_x_plane_component
cylinder_azimuth_rad: angle between x axis and the point_vector_x_plane_component(+ve angle moves point_vector_x_plane_component into viewing field/page)
cylinder_height: point_vector_z_plane_component
"""
def mag(x,y,z):
  return (((x*x)+(y*y)+(z*z))**0.5)
  
class POINT3D:
  def __init__(this,x,y,z,sph_radius=0,sph_elevation_rad=0,sph_azimuth_rad=0,cyl_radius=0,cyl_height=0,cyl_azimuth_rad=0):
    if( ((sph_radius*sph_elevation_rad*sph_azimuth_rad)+(cyl_radius*cyl_height*cyl_azimuth_rad)) ==0  ):
      this.x = x
      this.y = y
      this.z = z
      this.magnitude     = mag(x,y,z)
      this.sphere_radius = this.magnitude
      this.sphere_elevation_rad = math.acos( ( mag(x,y,0) )/(this.magnitude) )
      this.sphere_azimuth_rad   = math.atan( z/x )
      this.cylinder_radius = mag(x,0,z)
      this.cylinder_height = y
      this.cylinder_azimuth_rad = this.sphere_azimuth_rad
    if( sph_radius*sph_elevation_rad*sph_azimuth_rad ):
      pass
    if( cyl_radius*cyl_height*cyl_azimuth_rad        ):
      pass
    
