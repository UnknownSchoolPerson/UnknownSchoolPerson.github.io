## Short Introduction
My name is Kevin, and this website was created for my final project in CS-499. I'm currently in my last year for my bachelor’s degree and computer science and it has come a long way since starting. In this small webpage you will see three programs I created and improved on.  
# Programs
## [Code Review](https://mega.nz/file/ch5VgD4J#ebPcmmSDuEUJyekUyWWkRYR580-JiIzpWIaV288Aye4)
Note that the video isn't embeded due to file size.  
Goes over the projects before being changed.  
## Projects with and without changes
[https://github.com/UnknownSchoolPerson/CS-499-Software-design-engineering](https://github.com/UnknownSchoolPerson/CS-499-Software-design-engineering)  
[https://github.com/UnknownSchoolPerson/CS-499-Algorithms-and-data-structures](https://github.com/UnknownSchoolPerson/CS-499-Algorithms-and-data-structures)  
[https://github.com/UnknownSchoolPerson/CS-499-Database](https://github.com/UnknownSchoolPerson/CS-499-Database)  
Note on each project the master branch was before any changes. Branch CS499 on each is the updated ones.  
## Enhancement One: Software Design and Engineering  
[https://github.com/UnknownSchoolPerson/CS-499-Software-design-engineering](https://github.com/UnknownSchoolPerson/CS-499-Software-design-engineering)  
  
With Computational Graphics and Visualization CS330, I had to take a picture of an object in real life and recreate it. Now I am awful at design, so I did not create an amazing-looking 3D scene, but I created a whole object editor to create the objects in real time. I was able to change the location, transform the shape, spawn a new one, get the current matrix of it, and also see what object is currently selected. Creating an object editor and updating objects in real time was not required or expected. We were expected to create static code that placed down the objects to create our scenes. Creating a whole editor has done more than required for the project and I finished this on 6/17/2023.  
  
Before any enchantments, this project shows how I went above and beyond for a project and created a whole editing tool to help me learn more about 3D rendering, C++, and creating 3D scenes. The whole object editing was just an idea I had no idea would work until I took the step and tried it. The artifact not only improved with new features, but while implementing these new features I found a few bugs and also improved some of the logic behind the scenes that would make adding more features in the future easier. I have finished implementing my enhancements of using Windows open dialog to load new textures, allowing objects to be deleted, and reworking the behind-the-scenes to allow textures to be deleted when used. Doing so also reviewed how keeping track of the objects was wrong and was impossible to delete, so I had to change the object list to be pointers and update all code to know the list is a bunch of pointers. How I noticed when looking up the compile error [https://gamedev.stackexchange.com/questions/164069/error-saying-attempting-to-reference-a-deleted-function-while-using-a-vector-lis](https://gamedev.stackexchange.com/questions/164069/error-saying-attempting-to-reference-a-deleted-function-while-using-a-vector-lis).

### Course outcomes met  
#### (Demonstrate an ability to use well-founded and innovative techniques, skills, and tools in computing practices to implement computer solutions that deliver value and accomplish industry-specific goals)  
I used an OS feature to help implement a new feature to the artifact, showing how I can use OS-specific features along with industry-standard documentation and libraries.
#### (Design and evaluate computing solutions that solve a given problem using algorithmic principles and computer science practices and standards appropriate to its solution, while managing the trade-offs involved in design choices)  
When creating my texture cleanup, I used a map to quickly keep track of how many references a texture has. The map requires the knowledge of knowing of how O notation works and to know when to implement it at logical points. Finally, to implement a texture cleanup system, some speed had to be given up determining when to clean up, but this trade-off is well worth it as it can help clean up countless amounts of unused memory.

### Reflection  

When I was enhancing this artifact, I did not expect to change so much, to be honest. My original plan of creating a second vector list and throwing deleted objects was never even tried when I had an idea when I woke up this morning and started working on this. My idea was to have two saved textures, a render texture, and an original texture. In the program what happens is when a new texture is created an ID is also attached to it, when I want to give an object a texture I give it the ID, so saving two textures is only as big as an integer. When changing the texture to see the selected texture the render texture is touched and when that is no longer selected, I just go back to the original texture. This made deleting textures easier as I am creating a new function bindTexture that would change the original texture of an object, update the references, and delete unused textures. The only real challenge I faced (besides rewriting a few systems) was my original vector list was a copy of anything it put in, not the original causing it to use 2n memory for each object. This was a problem because it took me the most time to figure all this out. After all, I was getting a C2280 error. Otherwise, the only other thing I learned was how to implement the Windows file dialog box as I never did that before besides in Windows Form Maker in Visual Studio. I’m thankful for Microsoft well well-documented use of the dialogs in C++.

## Enhancement Two: Algorithms and Data Structures  
[https://github.com/UnknownSchoolPerson/CS-499-Algorithms-and-data-structures](https://github.com/UnknownSchoolPerson/CS-499-Algorithms-and-data-structures)  
  
One of the things I did while learning C# and multi-threading was creating a map to calculate the distance between two cities in a game called Mount and Blade 2. I created this as at the time someone made an online mod for the game, and I wanted a way to create estimate times/distances between towns for trading. I was able to extract the town's locations using a Mod someone made that allowed me to run C# script files. I made this around May 4, 2021.  
  
Before any enhancement I need to go over what I did since I haven’t touched on this project in a while. The first thing I did before any coding in the project itself was convert all the files into a single file using a python script. The python script grabbed all the files and outputted it to console, I then just copy pasted that to a single file. I added a post build command that after it builds the program, it will copy the Towns folder in the project directory to directory of the .exe file, so I only needed to run this script once and copy its output.  
  
(Note you can click on the picture to view the file!)
[![qY7u6imLtG](https://github.com/UnknownSchoolPerson/UnknownSchoolPerson.github.io/assets/149096872/ac9d8e8b-0c1e-4e22-b0a7-cf5f1e856146)](https://github.com/UnknownSchoolPerson/UnknownSchoolPerson.github.io/blob/main/Convert.py) 
  
After rewriting a few functions, adding new ones, and reworking the logic to allow users to add new Towns it was finished. I went with my original plan of loading the premade town list from a huge file and the rest from a single file to show user created or edited ones. Before being added to my final portfolio I just need to add comments and change a few title names.  
  
### Course outcomes met  
#### (Design, develop, and deliver professional-quality oral, written, and visual communications that are coherent, technically sound, and appropriately adapted to specific audiences and contexts)
Tools like ReSharper, official documentation from [Microsoft](https://learn.microsoft.com/en-us/dotnet/csharp/) to create industry standard code/syntax, and had an exact target audience of people who played MB2 who also wanted to calculate distances was used to achieve this outcome.
  
#### (Design and evaluate computing solutions that solve a given problem using algorithmic principles and computer science practices and standards appropriate to its solution, while managing the trade-offs involved in design choices)
This program was eventually optimized with speed in mind by using dictionaries for O(1) access times, creating unique classes to help keep track of data and also use OOB (Object-oriented programming) specific features, and in order to create a better user experience a huge trade-off was creating an awkward toString() override.
  
#### (Demonstrate an ability to use well-founded and innovative techniques, skills, and tools in computing practices for the purpose of implementing computer solutions that deliver value and accomplish industry- specific goals)
This project followed some of the industry best practices and guidelines found on the Microsoft website. It also used tools like ReSharper to help follow some of the best practices. Furthermore, this project was made with being dynamic in mind allowing it to be easily changed if needed and having no data pre-programmed in, allowing easy expansion of data the program uses.
  
### Reflection  

I expected to change quite a bit for this change as it was never done with deleting or changing towns in mind. Funny enough, no challenge really took me more than 5 minutes to figure out as I have a good amount of experience using a debugger and knowing what I did in my code. The real challenge wasn’t the code itself, but figuring out how to implement the loading and creating new files as I wanted to have a master list that was untouched but have a way to change towns in this list. I ended up saving if a town was part of that list and the program would create a new file of the town, if that file was empty, it wouldn’t create the town, but if it had something it would overwrite from the town list. A lot of my errors ended up being from trying to find null stuff in my dictionary as something didn’t call the right functions. I ended up creating good delete functions for towns but would sometimes just forget to not look for the delete town or forgetting to update the listbox, causing it to look for deleted stuff. The main thing I learned from this is how much of a pain it can be to reread what you did years ago and try to figure out how to update it, as this took me the most time.

## Enhancement Three: Databases 
[https://github.com/UnknownSchoolPerson/CS-499-Database](https://github.com/UnknownSchoolPerson/CS-499-Database)  

This project was my final project for CS360. In this project I had to create an inventory app on android that allowed users to create an account, add items to a database, and enable sending notifications. The app has two separate databases (one for users, one for items), and had to follow some of Androids best practices. There was no requirement to test on real hardware, but I was able to get it to run on my real phone.  
  
This project showed how I was able to use Operating System functions in order to create a Database. Using Java, SQLite, and Android OS API calls I was able to create two working databases that was able to talk with Java. Using Java, I was able to also hash the User’s password using Java’s Built-in password hashing and have SQLite store these as raw data. Updating this project shows off how I was able to keep user data when updating a database and update an existing android app.  

### Course outcomes met  
  
#### (Develop a security mindset that anticipates adversarial exploits in software architecture and designs to expose potential vulnerabilities, mitigate design flaws, and ensure privacy and enhanced security of data and resources)
The app hashes passwords with some of industry best practices and uses Java built-in security features. This helps reduce the risk of people being able to steal passwords as the only way to get someone’s password would be a dictionary or brute force attack by a bad actor.
#### (Employ strategies for building collaborative environments that enable diverse audiences to support organizational decision making in the field of computer science)
This app heavily follows industry best practices as handling user’s passwords is a big deal. This follows Java’s and Android’s best practices, has no compiler warnings (besides never used values), and is commented for easy reading.
#### (Demonstrate an ability to use well-founded and innovative techniques, skills, and tools in computing practices for the purpose of implementing computer solutions that deliver value and accomplish industry- specific goals)
Android studio is a big tool that many places use to create Android apps. While MySQL was chosen to create a Database, the reason for it is very simple, Android has it built in. This shows the case of using an OS built in tools as well.

### Reflection  
  
I have fully implemented the planned enhancements for this project. Creating this was easier than expected. I feel from my time between and what I did learn when I created this app, what I learned helped me. One of my problems I faced when I opened up the app was, I was getting an error in the IDE. The app compiled fine, the app ran fine, just android studio was saying two arguments were wrong. It confused me as if this was true, the app would crash. When I looked this up it turned out this is an android studio bug (A new one!) [https://issuetracker.google.com/issues/293665984?pli=1](https://issuetracker.google.com/issues/293665984?pli=1). 
Updating the Database went as easy as I expected (Thanks to my Database class). Adding to the app to show the notes, last update, last user who changed stuff was easier than expected as I forgot that I used a single text label when I showed all the info. So, I just updated that label. When I wanted to keep track of who the active user was my idea of using a local global came up. I found this great idea of using a singleton to do so. https://stackoverflow.com/a/1944842. I added a new button for changing notes and after all this I finished my updates.  

## Credits
  
Theme: [https://github.com/pages-themes/hacker](https://github.com/pages-themes/hacker)  
Github for hosting this and [providing a formating help page.](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#links)https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#links
