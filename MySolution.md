# My SOLUTION to The API - Smartia Backend Developer Challenge :)

I'll be explaining my approach to this problem, I went for a simple solution as I'm of the belief that complicated solutions aren't necessarily the best.

I went through a decision phase trying to decide what API pattern to use, then settled for REST mostly considering the fact that data scientists will also be consuming the API, and REST is more universal. RPC or GraphQL aren't as popular.

##NEXT STEPS:

- Understanding the data models and all relationships 
- Drafting out the endpoints while also considering relationships for filtering
- Moved on to the serialization and made certain decisions, mostly separating the write-only and read-only attributes
- Created a Custom View Class to be inherited by other Views, adding some extra things i explained in the `data_sources/utils.py` file
- Set up my views and urls
- Set up Redoc documentation
- Dockerize the Application


##CHALLENGES:

-Not exactly a challenge but I had some troubles setting up Vagrant and VirtualBox and didn't want to waste too much time on those, so I ran it locally at first then dockerized eventually.
-I was unable to complete the documentation as there were a few things I had problems figuring out using the drf_yasg library.

##DOCUMENTATION: 

Check `/redoc`

##IF I HAD MORE TIME
I had a stopwatch to make sure I didn't exceed 3hrs. Made sure not to spend too much time on anything.
If I had more time, I'll improve the documentation as I believe that's what makes any API a pleasure to work with. Proper, developer-friendly documentations are nothing short of great. It has influenced my choice of API as a developer as good documentations make the entire development process faster. 
