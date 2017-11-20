import bpy, random as rand
from math import cos, sin, pi

def create_lamp( R=10):                                                           
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

def clean_up_scene():                           
#    bpy.ops.wm.read_factory_settings()          
                                                
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

def create_camera(R=15,range_theta=[0,2*pi], range_phi=[0,pi]):
    scene = bpy.context.scene
    
    # create camera datablock
    cam_data = bpy.data.cameras.new(name="Camera")
    
    # create camera object with the camera data block
    cam_object = bpy.data.objects.new(name="Camera", object_data=cam_data)
    
    # Link camera object to the scene so it'll appear in the scene
    scene.objects.link(cam_object)
    
    # Place the camera in a random location within the given range
    theta = (range_theta[1]-range_theta[0])*rand.random(); phi = (range_phi[1]-range_phi[0])*rand.random();
    x = R*cos(theta)*sin(phi)
    y = R*sin(theta)*sin(phi)
    z = R*cos(phi)
    cam_object.location = (x,y,z)
    
    # Aim camera at the origin

def render_scene():
    bpy.ops.render.render(write_still=True)
    
clean_up_scene()

for i in range(1000):
    create_lamp()
    
create_camera()
render_scene()