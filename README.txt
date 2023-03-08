To run the mapmaker

First run seedgenerator.py which takes a height and width and makes a csv which is just 0s in that dimension WARNING: currently the program does not like non square maps, I will fix this later, something in the coords system is getting x and y mixed up

If you want to manually seed certain elements into the map edit the csv and add numbers according to what you want (/tileimgs/ has te tiles the program uses and their number code, so if you want a region of mountain replace its 0s with 3s)

run mapmaker.py which will run then output a timestamped png. 

Note: if you want the script to also generate a gif of the process change line 31 to animation=1 (this will be sorted when I implement a gui)