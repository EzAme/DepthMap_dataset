import bpy
import random as rand

def create_random_cube( 
        objID,
        magnitude, 
        boundary=[(0,1),(0,1),(0,1)],
        ):
    """
    this function has been created to generate randomly sized triangles between
    user-defined dimensions, reflectivity, color, and 
    """
    magn = 5
    loc = ( (0.5-rand.random())*magn, (0.5-rand.random())*magn, (0.5-rand.random())*magn)

    # create a cube object
    bpy.ops.mesh.primitive_cube_add( location= loc)
    bpy.ops.transform.rotate(
            value=rand.random()*3.14, 
            axis=(rand.random(),rand.random(), rand.random()),
            constraint_orientation='GLOBAL',
            mirror=False,
            proportional='DISABLED',
            proportional_edit_falloff='SMOOTH',
            propoartional_size=1
            )
    bpy.ops.material.new()

    # create a texture and color
    mat1 = bpy.data.materials['Material'+objID]
    mat1.diffuse_color = ( rand.random(), rand.random(), rand.random())
    bpy.data.objects['Cube'+objID].data.materials.append(mat1)


def create_background():
    """
    create a background composed of 3 planes
    """
    bpy.ops.mesh.primitive_plane_add( 
            radius=1, 
            enter_editmode=False, 
            location=(7, 8, -1), 
            rotation=(0,0,0),
            layers=(
                 True, False, False, False, False,
                False, False, False, False, False,
                False, False, False, False, False,
                False, False, False, False, False
                )
            )
    # create plane 2
    
def clean_up_scene():
    #Remove objects from previsous scenes
    for item in bpy.data.objects:  
        if item.type == "MESH":  
            bpy.data.objects[item.name].select = True
            bpy.ops.object.delete()

        for item in bpy.data.meshes:
            bpy.data.meshes.remove(item)

def makeascene():
    clean_up_scene()
    create_background()
