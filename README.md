# Harassment Monitor

<p align="center">
  <img src="https://raw.githubusercontent.com/hdubel94/Hack2017/master/images/HHLogo.png" alt="Hack Harassment Monitor" width="250px"/>
</p>

## Inspiration
In a rapidly evolving digital world, it can become easy to forget that there is another individual on the other side of the screen. This can lead to the victimization of individuals through online harassment. As the world becomes ever more connected it has become of even greater importance to catch, report, and prevent any form of online harassment, ensuring that each individual can have a safe and enjoyable experience.

## What it does
Our hack uses a neural network which is trained to identify between positive and negative words. To help demonstrate the network, it was implemented onto an Amazon Echo. Upon using the Echo's wake word and asking for "Harassment Monitor", the Echo will listen silently in the background for any words and forward them into the neural network. If the network deems that the conversation can be considered harassment, the user is notified by Alexa and an e-mail and an SMS text message is sent to the supplied contact. We hope that by catching harassment and reporting it, the spread of it can be prevented for the greater good of society.

## How we built it
We used python to implement our entire project. The neural network is designed in a separate file so that it can be used in myriad of applications. The HarassmentMonitor.py script is what AWS Lambda utilizes to collect and send information to the network and send any messages should they be needed.

## Challenges we ran into
One large challenge is that Amazon's Alexa service cannot listen silently in the background indefinitely. This is to prevent a breach of individual privacy. Since our Alexa Skill cannot be left running, if Alexa does not hear any input our skill will be exited.

Another challenge was training the network. Many words can have both a negative and a positive connotation. This made it difficult at times for the network to properly determine whether what is being said is harassment.

## Accomplishments that we're proud of
This is the team's first implementation of the Alexa Voice Service and utilizing some of the features AWS has to offer.

## What we learned
Gained further familiarity with Python. Learned the basics of an Alexa Skill and how to debug it. How to implement AWS features into our project.

## What's next for Harassment Monitor
The neural network will be expanded upon and trained. Ideally, it could be utilized through other voice and text recognition scenarios and help fight harassment across multiple mediums.