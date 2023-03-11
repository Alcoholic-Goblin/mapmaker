# mapmaker
Program to generate randomised region maps from a list of tiles. Uses wave function collapse to generate.

To run the mapmaker

First run seedgenerator.exe which will ask for a height and width, this determines the final size of the map.

If you want to force certain features you can edit seed.csv, set values to numbers which correspond to files in /tileimgs (so if you want to force some mountains add some 3s in), currently this is the best way to add large features

Then run mapmaker.exe. It will open a window which allows you to edit the relationships between tiles. Each tab controls a different tile and the sliders set how much this tile type wants to connect to the respective other tile. It will automatically load your most recent set of relationships (I have preloaded one which gives okay maps). 

If you want a gif of the generation tick the appropriate checkbox, however this will dramatically increase the time it takes to make the map, from testing, roughly by a factor of 10.

Hit the makemap button and you will see a progress update in the log. It will then save your png (and gif) as YYYYMMDD-HHMMSS (current time/date) in the mapmaker folder.



If you want to add/edit the tiles change files in the /tilesimgs folder. The folder must always be a list of files going 0.png, 1.png, 2.png... (NB:0.png is used as a void by the system and is not useable by the algorithm, custom tiles must start at 1.png)

The program has only been tested with 16x16 pixel tiles. It should work with any dimension but try at your own risk.



TODO

Hide tile 0 from editor

Tidy code and comment

Optimise where possible, especially gif creation as its a dirty hack at the moment.

Add a dithering option to certain tiles so that the boundries are less obvious (Especially for water))
