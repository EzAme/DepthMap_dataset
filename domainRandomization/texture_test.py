import bpy
import random as rand


def createMaterials():

    #Marble texture
    mbtex = bpy.data.textures.new("Marble", 'MARBLE')

    mbtex.noise_depth = 1
    mbtex.noise_scale = 1.6
    mbtex.noise_basis_2 = 'SAW'
    mbtex.turbulence = 5


# Create new material
    mat = bpy.data.materials.new('TexMat')
    mat.diffuse_shader='LAMBERT'
    mat.alpha = 0
    mat.diffuse_color = (rand.random(), rand.random(), rand.random())

# Map marble to specularity
#     mat.add_texture(texture = mbtex, texture_coordinates = 'UV', map_to = 'SPECULARITY')
    slot= mat.texture_slots.add()
    # print(slot)
    slot.texture = mbtex
    slot.texture_coords = 'OBJECT'
    slot.blend_type = 'MIX'
    slot.color=(rand.random(), rand.random(), rand.random())

# Pick active object, remove its old mate# Delete excess materials
# for material in bpy.data.materials:
#     if not material.users:
#         bpy.data.materials.remove(material)rial (assume exactly one old material).
#     ob = bpy.context.object  #uncomment
    # bpy.ops.object.material_slot_remove()

    # Add the two materials to mesh
    # me = ob.data #uncomment
    # me.materials.append(mat) #uncomment
######################################################################################
    # mbtex = bpy.data.textures.new("Blend", 'BLEND')
    # mbtex.progression = 'QUADRATIC'
    # i =rand.randint(0,1)
    # if i is 0:
    #     mbtex.use_flip_axis = 'HORIZONTAL'
    # elif i is 1:
    #     mbtex.use_flip_axis = 'VERTICAL'
    # # Create new material
    # mat = bpy.data.materials.new('TexMat')
    # mat.diffuse_shader = 'LAMBERT'
    # mat.alpha = 0
    # mat.diffuse_color = (rand.random(), rand.random(), rand.random())
    #
    # # Map marble to specularity
    # #     mat.add_texture(texture = mbtex, texture_coordinates = 'UV', map_to = 'SPECULARITY')
    # slot = mat.texture_slots.add()
    # # print(slot)
    # slot.texture = mbtex
    # slot.texture_coords = 'OBJECT'
    # slot.blend_type = 'MIX'
    # slot.offset[0]=2.0
    # slot.offset[1] = 1.0
    # slot.scale[0]=0.2
    # slot.scale[1] = 0.2
    # slot.scale[2]=0.2
    #
    # slot.color = (rand.random(), rand.random(), rand.random())

    return mat


# createMaterials()