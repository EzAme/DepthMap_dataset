# import the enviroment randomization function file
import sys
import os
sys.path.append("/home/ez/DR/domainRandomization")
import pby_fun as fun
from random import randint
from math import pi


def add_random_shape(R=[2,6], size=[1.5,1], range_theta=[0,pi/2], range_phi=[0,pi/2]):
    i = randint(1,2)
    if i is 1:
        fun.create_random_cube(R=R,size=size);
    elif i is 2:
        fun.create_random_sphere(R=R,size=size);


def makeascene(val=0):
    # remove all object from current scene
    fun.clean_up_scene()

    val = 0
    # create a background
    if val == 0:
        fun.create_flat_background()
    elif val == 1:
        fun.create_corner_background()
    else:
        fun.create_sphere_background()


if __name__ == "__main__":
    # the number of scenes
    N = 100
    ncams = 3
    N = int(N/ncams)

    for i in range(N):
        # create a scene
        makeascene()
        
        j = randint(0,5)
        p = randint(1,5)
        # add objects randomly
        if i<N/2:
            # add j random shapes
            for k in range(j):
                add_random_shape()
        else:
            # add rowdy and add j random shapes with textures
            fun.import_rowdy(filename="rowdy.STL",
                    R=[4,6],
                    range_theta=[-0.7853981634,2.3561944902],
                    range_phi=[0,1.25],
                    size=[0.05,0.03])
            for k in range(j-1):
                add_random_shape()
        fun.randomize_texture()
        # now that the scene has been created we need to now render the scene
        for k in range(p):
            fun.create_lamp(R=15,
                    range_theta=[0,3.14159265],
                    range_phi=[0,1.5707963268])
            
        for k in range(3):
            fun.create_camera(R=15, 
                    range_theta=[0,1.5707963268],
                    range_phi=[0,1.5707963268],
                    view_range=[30,60])
            if k == 0:
                if i<N/2:
                    fun.render_scene(id="",ofilename="drimages/not_rowdy/set"+str(i)+"_image"+str(k)+".png")
                else:
                    fun.render_scene(id="",ofilename="drimages/rowdy/set"+str(i)+"_image"+str(k)+".png")
            else:
                if i<N/2:
                    fun.render_scene(id=".00"+str(k),ofilename="drimages/not_rowdy/set"+str(i)+"_image"+str(k)+".png")
                else:
                    fun.render_scene(id=".00"+str(k),ofilename="drimages/rowdy/set"+str(i)+"_image"+str(k)+".png")
