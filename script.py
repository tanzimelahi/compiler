import mdl
from lighting import *

def run(filename):
    """
    This function runs an mdl script
    """
    p = mdl.parseFile(filename)

    if p:
        (commands, symbols) = p
    else:
        print("Parsing failed.")
        return

    view = [0,
            0,
            1];
    ambient = [50,
               50,
               50]
    light = [[0.5,
              0.75,
              1],
             [255,
              255,
              255]]

    #my naming conventions
    A=ambient
    P=light[1]
    L=light[0]
    V=view
    color = [0, 0, 0]
    transform = new_matrix()
    ident( transform )
    stack=[]
    stack.append(transform)
    screen = new_screen()
    buffer = new_zbuffer()
    edge=empty_matrix()
    triangle_matrix=empty_matrix()
    step_3d = 100
    consts = ''
    coords = []
    coords1 = []
    symbols['.white'] = ['constants',
                         {'red': [0.2, 0.5, 0.5],
                          'green': [0.2, 0.5, 0.5],
                          'blue': [0.2, 0.5, 0.5]}]
    reflect = '.white'

    for command in commands:
        if command["op"]=="push":
            push(stack)
        elif command["op"]=="pop":
            pop(stack)
        elif command["op"]=="move":
            coord=command["args"]
            a=int(coord[0])
            b=int(coord[1])
            c=int(coord[2])
            transform=move(a,b,c)
            apply(stack[-1],transform)
            stack[-1]=transform
        elif command["op"]=="rotate":
            coord=command["args"]
            axis=coord[0]
            angle=coord[1]
            transform=rotation(angle,axis)
            apply(stack[-1],transform)
            stack[-1]=transform
        elif command["op"]=="scale":
            coord=command["args"]
            sx=int(coord[0])
            sy=int(coord[1])
            sz=int(coord[2])
            transform=scale(sx,sy,sz)
            apply(stack[-1],transform)
            stack[-1]=transform
        elif command["op"]=="sphere":
            coord=command["args"]
            cx=int(coord[0])
            cy=int(coord[1])
            cz=int(coord[2])
            radius=int(coord[3])
            constants=command["constants"]
            Ka=[]
            Kd=[]
            Ks=[]
            if constants==None:
                sphere(triangle_matrix,cx,cy,cz,radius)
                apply(stack[-1],triangle_matrix)
                info=symbols[".white"][1]
                Ka.append(info["red"][0])
                Ka.append(info["green"][0])
                Ka.append(info["blue"][0])
                Kd.append(info["red"][1])
                Kd.append(info["green"][1])
                Kd.append(info["blue"][1])
                Ks.append(info["red"][2])
                Ks.append(info["green"][2])
                Ks.append(info["blue"][2])
                newA=A
                newP=P
                newL=L
                newV=V
                add_polygons(screen,buffer,triangle_matrix,newA,newP,newL,newV,Ka,Kd,Ks)
                triangle_matrix=empty_matrix()
                
            else:
                sphere(triangle_matrix,cx,cy,cz,radius)
                apply(stack[-1],triangle_matrix)
                info=symbols[constants][1]
                Ka.append(info["red"][0])
                Ka.append(info["green"][0])
                Ka.append(info["blue"][0])
                Kd.append(info["red"][1])
                Kd.append(info["green"][1])
                Kd.append(info["blue"][1])
                Ks.append(info["red"][2])
                Ks.append(info["green"][2])
                Ks.append(info["blue"][2])
                newA=A
                newP=P
                newL=L
                newV=V
                add_polygons(screen,buffer,triangle_matrix,newA,newP,newL,newV,Ka,Kd,Ks)
                triangle_matrix=empty_matrix()
        elif command["op"]=="torus":
            coord=command["args"]
            cx=coord[0]
            cy=coord[1]
            cz=coord[2]
            r=coord[3]
            R=coord[4]
            torus(triangle_matrix,cx,cy,cz,r,R)
            apply(stack[-1],triangle_matrix)
            constants=command["constants"]
            Ka=[]
            Kd=[]
            Ks=[]
            if constants==None:
                info=symbols[".white"][1]
                Ka.append(info["red"][0])
                Ka.append(info["green"][0])
                Ka.append(info["blue"][0])
                Kd.append(info["red"][1])
                Kd.append(info["green"][1])
                Kd.append(info["blue"][1])
                Ks.append(info["red"][2])
                Ks.append(info["green"][2])
                Ks.append(info["blue"][2])
                newA=A
                newP=P
                newL=L
                newV=V
                add_polygons(screen,buffer,triangle_matrix,newA,newP,newL,newV,Ka,Kd,Ks)
                triangle_matrix=empty_matrix()
            else:
                info=symbols[constants][1]
                Ka.append(info["red"][0])
                Ka.append(info["green"][0])
                Ka.append(info["blue"][0])
                Kd.append(info["red"][1])
                Kd.append(info["green"][1])
                Kd.append(info["blue"][1])
                Ks.append(info["red"][2])
                Ks.append(info["green"][2])
                Ks.append(info["blue"][2])
                newA=A
                newP=P
                newL=L
                newV=V
                add_polygons(screen,buffer,triangle_matrix,newA,newP,newL,newV,Ka,Kd,Ks)
                triangle_matrix=empty_matrix()
                
        elif command["op"]=="save":
            coord=command["args"][0]
            coord=coord+".png"
            save_ppm(screen,coord)
        elif command["op"]=="box":
            coord=command["args"]
            x=coord[0]
            y=coord[1]
            z=coord[2]
            width=coord[3]
            height=coord[4]
            depth=coord[5]
            constants=command["constants"]
            Ka=[]
            Kd=[]
            Ks=[]
            box(triangle_matrix,x,y,z,width,height,depth)
            apply(stack[-1],triangle_matrix)
            if constants==None:
                p
                info=symbols[".white"][1]
                Ka.append(info["red"][0])
                Ka.append(info["green"][0])
                Ka.append(info["blue"][0])
                Kd.append(info["red"][1])
                Kd.append(info["green"][1])
                Kd.append(info["blue"][1])
                Ks.append(info["red"][2])
                Ks.append(info["green"][2])
                Ks.append(info["blue"][2])
                newA=A
                newP=P
                newL=L
                newV=V
                add_polygons(screen,buffer,triangle_matrix,newA,newP,newL,newV,Ka,Kd,Ks)
                triangle_matrix=empty_matrix()
            else:
                info=symbols[constants][1]
                Ka.append(info["red"][0])
                Ka.append(info["green"][0])
                Ka.append(info["blue"][0])
                Kd.append(info["red"][1])
                Kd.append(info["green"][1])
                Kd.append(info["blue"][1])
                Ks.append(info["red"][2])
                Ks.append(info["green"][2])
                Ks.append(info["blue"][2])
                newA=A
                newP=P
                newL=L
                newV=V
                add_polygons(screen,buffer,triangle_matrix,newA,newP,newL,newV,Ka,Kd,Ks)
                triangle_matrix=empty_matrix()
        elif command["op"]=="line":
            coord=command["args"]
            x0=int(coord[0])
            y0=int(coord[1])
            z0=int(coord[2])
            x1=int(coord[3])
            y1=int(coord[4])
            z1=int(coord[5])
            add_edge(edge,x0,y0,z0,x1,y1,z1)
            apply(stack[-1],edge)
            add_lines(screen,buffer,edge,color)
            edge=empty_matrix()
        elif command["op"]=="ambient":
            A=[]
            data=symbol["ambient"]
            A.append(data[1])
            A.append(data[2])
            A.append(data[3])
run("face.mdl")
print("face.png")
            
