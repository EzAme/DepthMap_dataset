# import the enviroment randomization function file
import sys
import pby_fun as fun
from random import randint


def makeascene():
    # remove all object from current scene
    clean_up_scene()

    # create a background
    create_background()


if __name__ == "__main__":
    # the number of scenes
    N = 6

    for i in range(N):
        # create a scene
        makeascene()
        
        j = randint(1,5)
        # add objects randomly
        if i<N/2:
            # add j random shapes
            for k in range(j):
                add_random_shape()
        else:
            # add rowdy and add j random shapes with textures
            fun.import_rowdy("rowdy.stl",
                    R=[0,2]
                    range_theta=[-0.7853981634,2.3561944902],
                    range_pi=[0,1.8325957146])
            for k in range(j-1):
                add_random_shape()

        # now that the scene has been created we need to now render the scene
        for k in range(5):
            fun.create_camera(R=15, 
                    range_theta=[0,1.5707963268],
                    range_phi=[0,1.5707963268])

