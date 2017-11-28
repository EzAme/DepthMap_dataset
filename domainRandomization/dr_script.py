# import the enviroment randomization function file
import sys
import os
sys.path.append("/home/robro/DepthMap_dataset/domainRandomization")
import pby_fun as fun
from random import randint


def add_random_shape():
    i = randint(1,2)
    if i is 1:
        fun.create_random_cube(R=[6,2],size=[1.5,1]);
    elif i is 2:
        fun.create_random_sphere(R=[6,2],size=[1.5,1]);


def makeascene():
    # remove all object from current scene
    fun.clean_up_scene()

    # create a background
    fun.create_background()


if __name__ == "__main__":
    # the number of scenes
    N = 6

    for i in range(N):
        # create a scene
        makeascene()
        
        j = randint(1,5)
        p = randint(1,5)
        # add objects randomly
        if i<N/2:
            # add j random shapes
            for k in range(j):
                add_random_shape()
        else:
            # add rowdy and add j random shapes with textures
            fun.import_rowdy(filename="rowdy.stl",
                    R=[0,2],
                    range_theta=[-0.7853981634,2.3561944902],
                    range_phi=[0,1.25],
                    size=[0.05,0.03])
            for k in range(j-1):
                add_random_shape()
        fun.randomize_texture()
        # now that the scene has been created we need to now render the scene
        for k in range(p):
            fun.create_lamp(R=15,
                    range_theta=[-0.7853981634,2.3561944902],
                    range_phi=[0,1.5707963268])
            
        for k in range(5):
            fun.create_camera(R=15, 
                    range_theta=[0,1.5707963268],
                    range_phi=[0,1.5707963268])
            if k == 0:
                fun.render_scene(id="",ofilename="drimages/set"+str(i)+"_image"+str(k)+".png")
            else:
                fun.render_scene(id=".00"+str(k),ofilename="drimages/set"+str(i)+"_image"+str(k)+".png")
