import bpy
import random as rand

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
    #bpy.ops.transform.rotate(value=rand.random()*3.14, 
    # create plane 2
    
def clean_up_scene():
    # clear scene of all stuff (from the depthmap_dataset) 
    for material in bpy.data.materials:
        material.user_clear();
        bpy.data.materials.remove(material);

    for texture in bpy.data.textures:
        texture.user_clear();
        bpy.data.textures.remove(texture);

    # clear default nodes
    bpy.context.scene.use_nodes = True
    tree = bpy.context.scene.node_tree
    links = tree.links
    
    for n in tree.nodes:
        tree.nodes.remove(n)
                
    #Remove objects from previsous scenes
    for item in bpy.data.objects:  
        if item.type == "MESH":  
            bpy.data.objects[item.name].select = True
            bpy.ops.object.delete()

    for item in bpy.data.meshes:
         bpy.data.meshes.remove(item)
         
    return tree, links

def render_scene( links, scene, rl):
                                                                           
    #output the stereoscopic images:                                   
    links.new(rl.outputs['Image'],composite.inputs['Image'])           
                                                                       
    scene.render.use_multiview = True                                  
                                                                       
    scene.render.filepath = 'StereoImages/Stereoscopic_'+str(ii)+'.png'
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
    render_scene( links, scene, rl)
#    create_background()

makeascene()
