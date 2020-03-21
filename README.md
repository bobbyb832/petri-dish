# petri-dish
pygame project with dots multiplying and killing eachother

every dot has the following properties
health
attack
defence
size(only cosmetic no affect on stats)
color
combat range
and a team identifier

It is a turn based game amongst all the dots, all the options are chosen psedo randomly
for each turn they have the option to 
  1:attack another dot that is within its combat range
  2:move, if it choses this option it then chooses in which of the one of the 8 directions
    N W S E NE NW SW SE
    it moves x pixels in the selected direction where x is its speed
    
when a dot kills another dot it gets a bonus to health and slightly increases size and a choice of
  incresing its attack
  increasing its defence
  increasing its health
  increasing its combat range
  increasing its speed
  
on every 500th turn for each dot it duplicates another dot that is on its team

this goes on and on until there is only one team remaining...
well the game still goes on because i have been too lazy to put a win condition
its still a work in progress, and more for learning :)


