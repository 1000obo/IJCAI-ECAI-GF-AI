# Geometry Friends AI Competition @ IJCAI-ECAI 22

This is the Geometry Friends Game AI Competition repository that will be used at the IJCAI-ECAI 2022 conference, in particular, for visitors interested in knowing more about the submission process, as well as on-going work related to the competition. It also includes a compilation of all public levels of this year's competitions and previous implementations of agents for the game. Visitors will be able to play these levels with PC controllers. Follow this link for more information: https://gaips.inesc-id.pt/geometryfriends/.

The goal of the competition is to build AI agents for a 2 player collaborative physics-based puzzle platformer game (Geometry Friends). Each agent controls a different character (circle or rectangle) with distinct characteristics. Their goal is to collaborate in order to collect all diamonds in a set of levels as fast as possible. The competition raises interesting problems for AI agents. For example, to successfully solve a GF level the AI players need to: (1) deal with coordination at different layers: from motion control (e.g. achieving perfect timing) to level resolution (e.g. devising shared plans); deal with limited actuation situated in a simulated physics environment (with gravity and friction); (3) solve platform (skill) based puzzles, which involves discovering the proper order to collect the diamonds and identifying the points where collaboration is needed; and (4) do all the above in real-time.

<p align="center">
  <img src="media/level.png" width="500" title="Geometry Friends level" alt="Example of level in the Geometry Friends Game">
</p>

## How to run the game and the agents:
  * Clone repository
  * Open folder <i>IJCAI-ECAI-GF-AI\GeometryFriendsGame\Release</i>
  * Run <i>GeometryFriends.exe</i>
  * Play Geometry Friends - Single Player, Multiplayer or Only Agents (Warning: change security properties of agents in the <i>Agents</i> folder for them to run)

If you want to play with controllers, you just need to connect them to your computer. In this repository, you can find a set of public levels of 2019 and 2022 competitions.

## How to create agents for the competition:
  * Open the solution in Visual Studio
  * Add <i>GeometryFriends.exe</i> (in the <i>IJCAI-ECAI-GF-AI\GeometryFriendsGame\Release</i> folder) as a start-up project
  * Change files in the <i>IJCAI-ECAI-GF-AI\python</i> folder: this solution shows a Python version of <i>Random Agents</i> (Circle and Rectangle) for the competition, which works locally. However, the original C# version of the agents can be found in the competition submission website (https://geometryfriends.gaips.inesc-id.pt/). We are currently working on improving the former version to allow future participants to submit their agents in Python.

## Batch Simulator

You can run several simulations of the agents by running the game in the command line using a specific flag <i> GeometryFriendsGame.exe –batch-simulator </i>. It’s useful to train or test your agents, and you can easily select the level and agent you want to test, how many simulations,etc. It will return a file with the simulation results (time, collectibles caught, …).

<p align="center">
  <img src="media/batchSimulator.png" width="500" title="Geometry Friends batch simulator" alt="Batch simulator of the Geometry Friends Game">
</p>

## Contact us!
If you have any questions about this, contact us through this email:
gfcompetition@gaips.inesc-id.pt

  
