import bpy
import random as rand
from math import sin, cos, pi

def create_random_cube( 
        objID,
        magnitude, 
        boundary=[(0,1),(0,1),(0,1)],
        size = [0.01, 0.03]
        ):
    """
    this function has been created to generate randomly sized triangles between
    user-defined dimensions, reflectivity, color, and 
    """
    loc = ( (0.5-rand.random())*magnitude, (0.5-rand.random())*magnitude, (0.5-rand.random())*magnitude)

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
        objID,
        magnitude, 
        boundary=[(0,1),(0,1),(0,1)],
        size = [0.01, 0.03]
        ):
    """
    this function has been created to generate randomly sized triangles between
    user-defined dimensions, reflectivity, color, and 
    """
    loc = ( (0.5-rand.random())*magnitude, (0.5-rand.random())*magnitude, (0.5-rand.random())*magnitude)

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
    bpy.ops.wm.read_factory_settings()

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

def set_up_lighting(scene):
    #setup lighting:               
    # create a new lamp
    lamp_data = bpy.data.lamps.new(name="Lamp", type='POINT')
    
    # Create new object with our lamp datablock
    lamp_object = bpy.data.objects.new(name="New Lamp", object_data=lamp_data)

    # Link lamp object to the scene so it'll appear in this scene
    scene.objects.link(lamp_object)

    # Place lamp to a specified location
    lamp_object.location = (5.0, 5.0, 5.0)

    # And finally select it make active
    lamp_object.select = True
    scene.objects.active = lamp_object

    light = bpy.data.objects['Lamp']
    light.data.use_shadow = False   
    light.data.energy = 5.0         
    light.location = (8,8,8)        
    light.select = False            

     # create a new lamp
    lamp_data = bpy.data.lamps.new(name="Lamp.001", type='POINT')
    
    # Create new object with our lamp datablock
    lamp_object = bpy.data.objects.new(name="New Lamp", object_data=lamp_data)

    # Link lamp object to the scene so it'll appear in this scene
    scene.objects.link(lamp_object)

    # Place lamp to a specified location
    lamp_object.location = (5.0, 5.0, 5.0)

    # And finally select it make active
    lamp_object.select = True
    scene.objects.active = lamp_object

    light2 = bpy.data.objects['Lamp.001']
    light2.data.use_shadow = False   
    light2.data.energy = 5.0         
    light2.location = (8,-8,8)        
    light2.select = False  

def create_lamp(scene=None, R=10):
    if not scene:
        scene = bpy.context.scene

    # Create new lamp datablock
    lamp_data = bpy.data.lamps.new(name="New Lamp", type='POINT')

    # Create new object with our lamp datablock
    lamp_object = bpy.data.objects.new(name="New Lamp", object_data=lamp_data)

    # Link lamp object to the scene so it'll appear in this scene
    scene.objects.link(lamp_object)

    # Place lamp to a specified location
    theta = 2*pi*rand.random(); phi = pi*rand.random();
    x = R*cos(theta)*sin(phi)
    y = R*sin(theta)*sin(phi)
    z = R*cos(phi)
    lamp_object.location = (x,y,z)

    # And finally select it make active
    lamp_object.select = True
    scene.objects.active = lamp_object

    return scene
    
def render_scene( links, scene, rl, composite, ID):
                                                                           
    #output the stereoscopic images:                                   
    links.new(rl.outputs['Image'],composite.inputs['Image'])           
                                                                       
    scene.render.use_multiview = True                                  
                                                                       
    scene.render.filepath = 'StereoImages/Stereoscopic_'+str(ID)+'.png'
    bpy.ops.render.render( write_still=True )                          
                                                                   


def makeascene():
    tree,links = clean_up_scene()
    # uncooked
    scene = bpy.context.scene
    scene.render.use_multiview = True
    scene.render.views_format = 'STEREO_3D'
    rl = tree.nodes.new(type="CompositorNodeRLayers")
    composite = tree.nodes.new(type="CompositorNodeComposite")
    composite.location = 200,0

    scene = bpy.context.scene
    
    create_background()
    create_random_cube([], 2, size=[0.7,1.0])
    create_random_cube("001",5,size=[ 0.7, 1.0])
    render_scene( links, scene, rl, composite,1)
    set_up_lighting(2)
#    create_background()

makeascene()
