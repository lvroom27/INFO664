# INFO664

My project uses the API from RAWG to access, select, and reorganize videogame metadata to fit into the Video Game Metadata Schema. 

RAWG is an online database of over 400,000 videogames. Users on the site can keep track of and rate games that they have played or want to play. They can also use the site to search for games using tags, such as searching for multiplayer games, action games, etc. The API allows users to access a large amount of information about a game, such as ratings, tags, popularity, platforms, game play clips, and more. 

The Video Game Metadata Schema (VGMS) is a project from the University of Washington Information School Game Research (GAMER) Group and Seattle Interactive Media Museum. They developed a the VGMS as a response to a lack of a uniform and videogame specific metadata schema in archives, libraries, museums, and other repositories. 

For my project, I downloaded the VGMS template and compared which entities were both in the schema and in the game data from RAWG. I used the API to access the information of the most popular games from 2019. My code selects and prints only these similar entities so that a cataloger can more quickly and efficiently input data into their own VGMS game record. Users of this code can input any year range into the payload and receive the information of the top games on RAWG. I chose these parameters as game libraries would be most likely to have these games. The list of entities includes the game name, rating, release date, genres, platforms, gameplay screenshots, tags, and gameplay clips. 

One setback I had was with the tag list. The VGMS has a more nuanced set of entities relating to tags, such as separate entities for gameplay, artistic style, mood, tropes, etc. The RAWG API lacks organization in its tagging system as well as the ability to access a full list of every single tag the site uses, which numbers in the thousands. In the future, I would hope to further research different tagging systems from other databases to explore solutions to this problem. As the project is now, the cataloger would have a list of the tags and have to use their own judgement when deciding which entity to place them into. 


 
