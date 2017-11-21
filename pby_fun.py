import bpy
import random as rand
from math import sin, cos, pi, asin, acos, atan2

def create_random_cube(
        objID='', 
        R=0.0,
        range_theta=[0,2*pi], 
        range_phi=[0,pi],
        size = [0.01, 0.03]
        ):
    """
    this function has been created to generate randomly sized triangles between
    user-defined dimensions, reflectivity, color, and 
    """
    theta = (range_theta[1]-range_theta[0])*rand.random(); phi = (range_phi[1]-range_phi[0])*rand.random();
    x = R*cos(theta)*sin(phi)
    y = R*sin(theta)*sin(phi)
    z = R*cos(phi)
    loc = (x,y,z)

    # create a cube object
    bpy.ops.mesh.primitive_cube_add( 
        location= loc,
        radius=rand.uniform(size[0], size[1])
        )
    bpy.ops.transform.rotate(
            value=rand.random()*3.14, 
            axis=(rand.random(),rand.random(), rand.random()),
            constraint_orientation='GLOBAL',
            mirror=False,
            proportional='DISABLED',
            proportional_edit_falloff='SMOOTH',
            proportional_size=1
            )
    

    # create and add a texture and color
    bpy.ops.material.new()
    if not len(objID):
        mat = bpy.data.materials['Material']
        mat.diffuse_color = ( rand.random(), rand.random(), rand.random())
        bpy.data.objects['Cube'].data.materials.append(mat)
    else:
        mat = bpy.data.materials['Material.'+objID]
        mat.diffuse_color = ( rand.random(), rand.random(), rand.random())
        bpy.data.objects['Cube.'+objID].data.materials.append(mat)
    

def create_random_sphere(
        objID='', 
        R=0.0,
        range_theta=[0,2*pi], 
        range_phi=[0,pi],
        size = [0.01, 0.03]
        ):
    """
    this function has been created to generate randomly sized triangles between
    user-defined dimensions, reflectivity, color, and 
    """
    theta = (range_theta[1]-range_theta[0])*rand.random(); phi = (range_phi[1]-range_phi[0])*rand.random();
    x = R*cos(theta)*sin(phi)
    y = R*sin(theta)*sin(phi)
    z = R*cos(phi)
    loc = (x,y,z)    
    
    # create a cube object
    bpy.ops.mesh.primitive_sphere_add( 
        location= loc,
        radius=rand.uniform(size[0], size[1])
        )
    bpy.ops.transform.rotate(
            value=rand.random()*3.14, 
            axis=(rand.random(),rand.random(), rand.random()),
            constraint_orientation='GLOBAL',
            mirror=False,
            proportional='DISABLED',
            proportional_edit_falloff='SMOOTH',
            proportional_size=1
            )
    

    # create and add a texture and color
    bpy.ops.material.new()
    if not len(objID):
        mat = bpy.data.materials['Material']
        mat.diffuse_color = ( rand.random(), rand.random(), rand.random())
        bpy.data.objects['Sphere'].data.materials.append(mat)
    else:
        mat = bpy.data.materials['Material.'+objID]
        mat.diffuse_color = ( rand.random(), rand.random(), rand.random())
        bpy.data.objects['Sphere.'+objID].data.materials.append(mat)

def create_background():
    """
    create a background composed of 3 planes
    """
    bpy.ops.mesh.primitive_plane_add( 
            radius=10, 
            enter_editmode=False, 
            location=(-8, 0, 0), 
            rotation=(0,0,0),
            layers=(
                 True, False, False, False, False,
                False, False, False, False, False,
                False, False, False, False, False,
                False, False, False, False, False
                )
            )
    bpy.ops.transform.rotate(
            value=1.5708,
            axis=(0,1,0),
            constraint_axis=(False, True, False),
            constraint_orientation='GLOBAL',
             mirror=False,
             proportional='DISABLED',
             proportional_edit_falloff='SMOOTH',
             proportional_size=1
             )
    # create plane 2
    bpy.ops.mesh.primitive_plane_add( 
            radius=10, 
            enter_editmode=False, 
            location=(0, -8, 0), 
            rotation=(0,0,0),
            layers=(
                 True, False, False, False, False,
                False, False, False, False, False,
                False, False, False, False, False,
                False, False, False, False, False
                )
            )
    bpy.ops.transform.rotate(
            value=-1.5708,
            axis=(1,0,0),
            constraint_axis=(True, False, False),
            constraint_orientation='GLOBAL',
             mirror=False,
             proportional='DISABLED',
             proportional_edit_falloff='SMOOTH',
             proportional_size=1
             )
             
    # create plane 3
    bpy.ops.mesh.primitive_plane_add( 
            radius=10, 
            enter_editmode=False, 
            location=(0, 0, -4), 
            rotation=(0,0,0),
            layers=(
                 True, False, False, False, False,
                False, False, False, False, False,
                False, False, False, False, False,
                False, False, False, False, False
                )
            )
    bpy.ops.transform.rotate(
            value=0,
            axis=(0,0,0),
            constraint_axis=( False, False, False),
            constraint_orientation='GLOBAL',
             mirror=False,
             proportional='DISABLED',
             proportional_edit_falloff='SMOOTH',
             proportional_size=1
             )
             
def clean_up_scene():
    for scene in bpy.data.scenes:
        for obj in scene.objects:
            scene.objects.unlink(obj)

    # only worry about data in the startup scene
    for bpy_data_iter in (
        bpy.data.objects,
        bpy.data.meshes,
        bpy.data.lamps,
        bpy.data.cameras,
        ):
        for id_data in bpy_data_iter:
            bpy_data_iter.remove(id_data)

def create_camera(
        R=8,
        range_theta=[0,2*pi], 
        range_phi=[0,pi]
        ):
    scene = bpy.context.scene

    # create camera datablock
    cam_data = bpy.data.cameras.new(name="Camera")

    # create camera object with the camera data block
    cam_object = bpy.data.objects.new(name="Camera", object_data=cam_data)

    # Link camera object to the scene so it'll appear in the scene
    scene.objects.link(cam_object)
    cam_object.select = True

    # Place the camera in a random location within the given range
    theta = (range_theta[1]-range_theta[0])*rand.random(); phi = (range_phi[1]-range_phi[0])*rand.random();
    x = R*cos(theta)*sin(phi)
    y = R*sin(theta)*sin(phi)
    z = R*cos(phi)
    cam_object.location = (x,y,z)

    # Aim camera at the origin
    zang = atan2(y,x)
    xang = acos(z/R)
    if ( z<0):
        cam_object.rotation_euler = (xang, 0, pi-zang)
    else:
        cam_object.rotation_euler = (xang, 0, -zang)

    cam_object.data.stereo.convergence_distance = 10000
    cam_object.data.lens = 15
    cam_object.data.stereo.interocular_distance = 0.3
    cam_object.select = False

    return cam_object

def create_lamp( 
        R=10,
        range_theta=[0,2*pi], 
        range_phi=[0,pi]):
    scene = bpy.context.scene

    # Create new lamp datablock
    lamp_data = bpy.data.lamps.new(name="New Lamp", type='POINT')

    # Create new object with our lamp datablock
    lamp_object = bpy.data.objects.new(name="New Lamp", object_data=lamp_data)

    # Link lamp object to the scene so it'll appear in this scene
    scene.objects.link(lamp_object)

    # Place lamp to a specified location
    theta = (range_theta[1]-range_theta[0])*rand.random(); phi = (range_phi[1]-range_phi[0])*rand.random();
    x = R*cos(theta)*sin(phi)
    y = R*sin(theta)*sin(phi)
    z = R*cos(phi)
    lamp_object.location = (x,y,z)

    # And finally select it make active
    lamp_object.select = True
    scene.objects.active = lamp_object

    return scene
    
def render_scene( id=""):
    bpy.context.scene.camera = bpy.data.objects['Camera'+str(id)]
    bpy.data.scenes['Scene'].render.filepath = 'image'+str(id)+".jpg"
    bpy.ops.render.render(write_still=True)

def makeascene():
    clean_up_scene()
    
    create_background()
    create_random_cube('',0,  [0,pi/2], [0,pi/2], size=[0.7,1.0])
    create_random_cube('001',1.5,[0,pi/2], [0,pi/2], size=[0.7,1.0])
    create_lamp(15,[0,pi/2], [0,pi/2])
    create_lamp(15,[0,pi/2], [0,pi/2])
    create_camera(6,[0,pi/2], [0,pi/2])
    render_scene( )
#    create_background()

makeascene()
