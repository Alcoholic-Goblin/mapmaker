import random
import time
from PIL import Image
import numpy as np
import csv
import copy
from datetime import datetime
import glob
import contextlib
import os
#find the current time for datestamping
current_time = datetime.now()
#set start time to a timestamp
stime_stamp = current_time.timestamp()
#initialise some variables for the process time calcualtion
start= time.time()
cur_iter=0
max_iter=0

#I can't remember where I found this code, just  makes the time left and estimated finish time. Might remove it
def calcProcessTime(starttime, cur_iter, max_iter):

    telapsed = time.time() - starttime
    testimated = (telapsed/cur_iter)*(max_iter)

    finishtime = starttime + testimated
    finishtime = datetime.fromtimestamp(finishtime).strftime("%H:%M:%S")  # in time

    lefttime = testimated-telapsed  # in seconds

    return (int(telapsed), int(lefttime), finishtime)

###SET TO 1 to enable gif generation, this dramatically slows down the process, not recommended for large maps
animation=1
###
##Clear the working folder as it will have old parts of the gif maker
files = glob.glob('working/*')
for f in files:
         os.remove(f)

##two subroutines to merge images together. hmerge does side by side and vmerge does one on top of the other         
def hmerge_images(file1, file2):
    """Merge two images into one, displayed side by side
    :param file1: path to first image file
    :param file2: path to second image file
    :return: the merged Image object
    """
    image1 = file1
    image2 = Image.open(file2)

    (width1, height1) = image1.size
    (width2, height2) = image2.size

    result_width = width1 + width2
    result_height = max(height1, height2)

    result = Image.new('RGB', (result_width, result_height))
    result.paste(im=image1, box=(0, 0))
    result.paste(im=image2, box=(width1, 0))
    return result

def vmerge_images(file1, file2):
    """Merge two images into one, displayed one ontop of the other
    :param file1: path to first image file
    :param file2: path to second image file
    :return: the merged Image object
    """
    image1 = file1
    image2 = Image.open(file2)

    (width1, height1) = image1.size
    (width2, height2) = image2.size

    result_width = max(width1, width2)
    result_height = height1 + height2

    result = Image.new('RGB', (result_width, result_height))
    result.paste(im=image1, box=(0, 0))
    result.paste(im=image2, box=(0,height1))
    return result

#
def printtiles():
        print("Tiles")
        for xyz in tiles:
                print(xyz)
        xyz=0
def printoptions():
        print("Options")
        for xyz in options:
                print(xyz)
        xyz=0        
#2d array to hold the allowed relationships from tiles. The index of the array is the tile number and the list is what tiles it can connect to
reftable = [[],[1,2,3,5],[1,2,3],[1,2,3],[4,5],[1,4,5]]
#2d array used to choose what tile should be used, multiple of the same entry weighs the program to choose certain tiles more often
weighttable= [[],[1,2,3,5,5,5],[1,1,2,2,3],[1,1,2,1,3],[4,5,5],[1,4,5,1,1,1]]
#load the seed.csv file into a var "lis" (pulls them as floats)
with open("seed.csv", newline='') as file:
    lis = list(csv.reader(file, quoting = csv.QUOTE_NONNUMERIC))

#loads the contents of lis into tiles as ints
tiles=lis
for i in range(len(lis)):
        for j in range(len(lis[0])):
                tiles[i][j]=int(lis[i][j])
               
#defines the grid height and width


        
gridwidth=len(tiles)
##print("gridwidth",gridwidth)
gridheight=len(tiles[0])
##print("gridheight",gridheight)

##if the tiles grid is empty then set the middle cell to 1, this should be changed to be more random
if sum(x.count(0) for x in tiles) == gridheight*gridwidth:
        tiles[1][1]=1


options=copy.deepcopy(tiles)


x=0
y=0
for i in options:
##        printoptions()
##        printtiles()
        for j in i:
##                
##                print("i",i,"/",len(options))
##                print("j",j,"/",len(i))
##                
##                print("j",j)
##                print("x",x)
##                print("y",y)
                if tiles[y][x] == 0:
                        options[y][x] = len(reftable)-1
                        
                elif tiles[y][x] != 0:
                        options[y][x]=0
                        print("found")
                        printoptions
                        
                x+=1
        x=0        
        y+=1        
        
x=0
y=0


        
for i in options:
        i[0]=0
        i[gridheight-1]=0
for j in range(len(options[0])):
        options[0][j]=0
        options[gridwidth-1][j]=0
for i in tiles:
        i[0]=0
        i[gridheight-1]=0
for j in range(len(tiles[0])):
        tiles[0][j]=0
        tiles[gridwidth-1][j]=0



todo=sum(x.count(0) for x in tiles)-gridheight-gridheight-gridwidth-gridwidth+3



for z in range (gridheight*gridwidth):
        x=0
        y=0
        for j in tiles:
            for i in j:
                    
                
                if tiles[y][x] != 0:
##                               print(tiles[x][y])
##                               print("if len(reftable[tiles[", x, "][", y, "]]) < options[", x, "-1][", y, "] : options[", x, "-1][", y, "] = len(reftable[tiles[", x, "][", y, "]]))")
                               if len(reftable[tiles[y][x]]) < options[y-1][x] : options[y-1][x] = len(reftable[tiles[y][x]])
                               if len(reftable[tiles[y][x]]) < options[y][x-1] : options[y][x-1] = len(reftable[tiles[y][x]])
                               if len(reftable[tiles[y][x]]) < options[y+1][x] : options[y+1][x] = len(reftable[tiles[y][x]])
                               if len(reftable[tiles[y][x]]) < options[y][x+1] : options[y][x+1] = len(reftable[tiles[y][x]])

                x+=1
            y+=1
            x=0

        x=0
        y=0

##        print ("Tiles------------")
##        for j in tiles:
##                print (j)

#Searches the options file see if there are any further steps, if not then it finishes the generation
        allzero=0
        for k in options:
##                print(k)
                for i in k:
                        if i != 0:
                                allzero=1
        if allzero == 0:
                print("finished")
                break

        coords=[]
        lowest=99999999

        
## FIND LOWEST Option

        for j in options:
##                print("options",j,"tiles  ",tiles[y])
                
                for i in j:
                        
                        
                        tgtcell=options[y][x]
                        if options[y][x] < lowest and options[y][x] != 0:
                                coords=[]
                                lowest = options[y][x]
                        if options[y][x] == lowest and options[y][x] != 0:
                                coords.append([y,x])                          
                                
                               
                        x+=1
                y+=1
                x=0
##        print(coords)
        x=0
        y=0
        
##        print(coords)
        ntile=random.choice(coords)
##
##        printoptions()
##        printtiles()
##     


##        print(ntile)
        neighbours=[tiles[ntile[0]][ntile[1]-1], tiles[ntile[0]-1][ntile[1]] , tiles[ntile[0]+1][ntile[1]] , tiles[ntile[0]][ntile[1]+1]]
##        print(neighbours)
        neighbouroptions=[]
        for j in neighbours:
            neighbouroptions.append(len(reftable[j]))
            
##        print(neighbouroptions)
        
        tgtind=999999
        indices=[]
        for j in range(4):
##            print(tgtind)
##            print(j)
            if neighbouroptions[j] != 0 and neighbouroptions[j] < tgtind:
                        indices=[]
                        tgtind=neighbouroptions[j]
##                        print("wiped")
            if neighbouroptions[j] != 0 and neighbouroptions[j] == tgtind:
                        indices.append(j)

    
        i=random.choice(indices)
        tiles[ntile[0]][ntile[1]]=random.choice(weighttable[neighbours[i]])
        options[ntile[0]][ntile[1]]=0
        
        if animation==1:
                       
                
                file1="tileimgs/1.png"
                file2="tileimgs/2.png"
                hcount=0
                vcount=0
                
                for i in tiles:
                        currentimage= Image.open("tileimgs/"+str(tiles[vcount][0])+".png")
                        for j in i:         
                                if hcount != len(i)-1:
                                        file1=currentimage
                                        file2="tileimgs/"+str(i[hcount+1])+".png"
                                        currentimage=hmerge_images(file1,file2)
                                hcount+=1
                        hcount=0       
                        currentimage.save("rows/row"+str(vcount)+".png")
                        if vcount == 0:    
                                finalimage=Image.open("rows/row0.png")
                        if vcount != 0:           
                                        file1=finalimage
                                        file2="rows/row"+str(vcount)+".png"
                                        finalimage=vmerge_images(file1,file2)
                                        
                        vcount+=1

                if z<10:
                        finalimage.save("working/00000"+str(z)+".png")
                elif z<100:
                        finalimage.save("working/0000"+str(z)+".png")
                elif z<1000:
                        finalimage.save("working/000"+str(z)+".png")
                elif z<10000:
                        finalimage.save("working/00"+str(z)+".png")
                elif z<100000:
                        finalimage.save("working/0"+str(z)+".png")
                        
                
       
                
        prstime=calcProcessTime(start, z+1 ,todo+1)
        
        print(z,"/",todo,int((z/todo)*100) , "%", "time elapsed: %s(s), time left: %s(s), estimated finish time: %s"%prstime)
if animation==1: 
         # filepaths
        fp_in = "working/*.png"
        fp_out = (datetime.now().strftime("%Y%m%d-%H%M%S")+".gif")

        # use exit stack to automatically close opened images
        with contextlib.ExitStack() as stack:

            # lazily load images
            imgs = (stack.enter_context(Image.open(f))
                    for f in sorted(glob.glob(fp_in)))

            # extract  first image from iterator
            img = next(imgs)

            # https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#gif
            img.save(fp=fp_out, format='GIF', append_images=imgs,
                     save_all=True, duration=50, loop=0)        
                 

######## TILE MAP IS DONE NOW CONVERT IDS INTO IMAGES
########


file1="tileimgs/1.png"
file2="tileimgs/2.png"
hcount=0
vcount=0
for i in tiles:
        currentimage= Image.open("tileimgs/"+str(tiles[vcount][0])+".png")
        for j in i:         
                if hcount != len(i)-1:
                        file1=currentimage
                        file2="tileimgs/"+str(i[hcount+1])+".png"
                        currentimage=hmerge_images(file1,file2)
                hcount+=1
        hcount=0       
        currentimage.save("rows/row"+str(vcount)+".png")
        if vcount == 0:    
                finalimage=Image.open("rows/row0.png")
        if vcount != 0:           
                        file1=finalimage
                        file2="rows/row"+str(vcount)+".png"
                        finalimage=vmerge_images(file1,file2)
                        
        vcount+=1
finalimage.save(datetime.now().strftime("%Y%m%d-%H%M%S")+".png")

current_time = datetime.now()
  
etime_stamp = current_time.timestamp()

time=etime_stamp-stime_stamp
print("time= ", int(time), "s")
