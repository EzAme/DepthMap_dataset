import bpy


def createMaterials():

    #Marble texture
    mbtex = bpy.data.textures.new("Marble", 'MARBLE')
    # print(mbtex)
    # mbtex.type = 'MARBLE'
    # print(mbtex)
    # mbtex = mbtex.recast_type()
    mbtex.noise_depth = 1
    mbtex.noise_scale = 1.6
    mbtex.noise_basis_2 = 'SIN'
    mbtex.turbulence = 5


    # Cloud texture
    cltex = bpy.data.textures.new("CloudsTex", 'CLOUDS')
    # cltex.type = 'CLOUDS'
# Cloud texture by default, don't need to recast
    cltex.noise_basis = 'BLENDER_ORIGINAL'
    cltex.noise_scale = 1.05
    cltex.noise_type = 'SOFT_NOISE'

# Create new material
    mat = bpy.data.materials.new('TexMat')
    mat.alpha = 0
    print(mat)
# Map marble to specularity
#     mat.add_texture(texture = mbtex, texture_coordinates = 'UV', map_to = 'SPECULARITY')
    slot= mat.texture_slots.add()
    # print(slot)
    slot.texture = mbtex
    slot.texture_coords = 'UV'
    print(slot)
    # mb_mtex = mat.textures[0]

# Map cloud to alpha, reflection and normal, but not diffuse
#     mat.MaterialTextureSlot(texture = cltex, texture_coordinates = 'UV', map_to = 'ALPHA')
#     cl_mtex = mat.textures[1]
#     cl_mtex.map_reflection = True
#     cl_mtex.map_normal = True
#
# # Create new material
#     mat2 = bpy.data.materials.new('Blue')
#     mat2.diffuse_color = (0.0, 0.0, 1.0)
#     mat2.specular_color = (1.0, 1.0, 0.0)

# Pick active object, remove its old material (assume exactly one old material).
    ob = bpy.context.object
    bpy.ops.object.material_slot_remove()

    # Add the two materials to mesh
    me = ob.data
    # me.add_material(slot)
    me.materials[0]=mat
    # me.add_material(mat2)

# Assign mat2 to all faces to the left, with x coordinate > 0
    for f in me.faces:
        left = True
    for v in f.verts:
        vert = me.verts[v]
    if vert.co.x < 0:
        left = False
    if left:
        f.material_index = 0
    else:
        f.material_index = 1
    return
createMaterials()