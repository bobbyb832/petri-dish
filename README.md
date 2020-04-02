pygame project with dots multiplying and killing each other.
It is a turn based game among all the dots. 
I Am currently studying machine learning, this will be a game for the AI to train in.



Every dot has the following properties
health
attack
defense
size(only cosmetic no affect on stats)
color
combat range
a team identifier

1:attack another dot that is within its combat range
or
2:move, if it chooses this option it then chooses in which of the one of the 8 directions 
  N W S E NE NW SW SE 
  it moves x pixels in the selected direction where x is its speed

when a dot kills another dot it gets a bonus to health and slightly increases size and a choice of increasing its attack 
increasing its defense 
increasing its health 
increasing its combat range 
increasing its speed

all the options are chosen pseudo randomly. 

on every 500th turn for each dot it duplicates another dot that is on its team

this goes on and on until there is only one team remaining...

Future features
  -UI where you can adjust parameters such as , population, starting stats, trail(on or off), etc...
  -Win conditions
  
Requirements
  -python 3
  -pygame
  

  
