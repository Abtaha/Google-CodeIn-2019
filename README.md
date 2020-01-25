![Google CodeIn 2019](https://developers.google.com/open-source/gci/resources/downloads/GCI-new-logo.jpg)

# Google CodeIn 2019

This repo contains the collection of tasks that I completed in Google CodeIn.

## Tasks

### Make a GUI in Python to automate 3 most done tasks

Make a GUI application in Python using Tkinter which gets launched when your system starts. Automating 3 tasks incorporate something like (sample) Opening your Github account in a browser. Show your Twitter feed. Play your favourite music playlist.

In order to complete the part, where the GUI is launched on system boot, write the steps you followed in ".txt" file.

### Create a program to move the cursor of your computer using your webcam

Computer Vision is a field in Artificial Intelligence which teaches the computer to visualize the 3D world. Computer vision include methods for obtain, process, analyze and understand digital images, and drawing out data from the real world to produce numerical or symbolic information. In simple words, its main goal is to extract meaning from pixels. You need to create a project while detects your hand and then uses your hand as a mouse. You can use Open-CV in python to complete the project.

Deliverables:

Submit the code in Pagure/GitHub and screen records of your program controlling the mouse. Write a small documentation in the README.md file Do not copy the code from GitHub or Stack Overflow. Try making the program by yourself.

https://github.com/Abtaha/MouseCam

### 2048 Game GUI

Make a GUI to implement the 2048 game using Tkinter. Make sure you display the score in the GUI and use proper color scheme. Convert the GUI to a .rpm/.deb file for use on your favorite Linux distribution. Make a Github repository with the code and instructions to use it.

https://github.com/Abtaha/2048-Game

### Craft your custom port scanner in python

A port scanner is a tool for determining which ports are open on a network. Ports are used to send and receive information. Ports vary in their services offered. They are numbered from 0 to 65535, but certain ranges are more frequently used(For example 22 for SSH, 80 for HTTP). Craft a custom port scanner in python and run it on your network only.

Deliverables:

Share the code in Pagure/GitHub and also attach the Asciinema recording of the scanner running in your terminal.

https://github.com/Abtaha/Python-Port-Scanner

### Ping Pong game using JavaScript

Make a ping pong game using JavaScript canvas. The game must have the following features:

* It must be single player, the other player computer controlled
* Mouse controlled user.
* Enter to start first game.
* Display winner after every round, max score=5. Enter to start new game
* The speed of the computer controlled paddle should change according to the impact of ball on the user and computer panddle.

When you're done make a github repository and push the code. Host on github pages.

https://github.com/Abtaha/Ping-Pong-in-JS

### Create a script to know who is on your Wi-Fi

WiFi Reconnaissance is an important process in information gathering. You can know the number of people connected to your WiFi and get their MAC(Media Access Control) which will help you further in exploiting the device. You need to create a WiFi Recon tool that scans the whole network and finds all the devices connected to it.

Deliverables:

Share the code in Pagure/Github and attach the Asciinema showing the number of devices to the Wifi.

https://github.com/Abtaha/WiPy-Recon

### Create a font with FontForge

You can design your own font using FontForge, by following the Guide create your own font and output it as a .ttf file. The file must have the following:

* Name it like your GCI Nickname.
* Unique Design.

### Tic Tac Toe GUI

Make a GUI to implement Tic Tac Toe game using Tkinter. Convert the GUi to a .deb file for use on your favourite linux distribution. Make a github repository with the code and instructions to use it.

https://github.com/Abtaha/TicTacToe-Game

### Detect the XSS Vulnerability

XSS(Cross-Site Scripting) is a security vulnerability found in a web application that allows an attacker to inject client-side script(Ex. JavaScript) to a webpage through input areas like a search box, forms, file upload and execute it at user’s end without authorization. The severity of cross site scripting attack can range from showing the useless alert box to stealing cookies, user’s session ids & take over the account. You need to perform 4 XSS attacks as follows:

* Create an alert box saying "HACKED".
* Change the background color of the website to "RED" .
* Change the background of the website to an image of your choice.
* Redirect the website to another page saying "You Are Hacked"(You can use HTMLPASTA to create your own page and redirect it to the vulnerable web app).
* Keep your attack limited to the website provided to you. Please do not perform any type of XSS attack in someone else's website.

Deliverables:

Share the Screenshots of all 4 attacks in a PDF/Word file. Below the screenshots write the code snippet that you used to execute the preceding.

### Brute Forcing password protected zip files

A brute force attack is a trial and error method used by application programs to Crack encrypted data like passwords by trying many possible combinations. You need to create an application using python/shell that can crack open a password protected zip folder. You need to:

Create a zip file and encrypt it by giving a password.
Create a wordlist(Make sure your password is in the wordlist, if you actually start brute forcing a zip files using a big wordlist it might take a long time).
Run your script against the zip file you encrypted.
Deliverables:

You have to submit:

* The code for your own brute force tool
* The zip file you cracked, and
* The Asciinema

Put all of that in a Pagure/GitHub repo and share the link with me.

https://github.com/Abtaha/Zip-Cracker

### Spell checker with python

Ever felt how spell checking works? it instantly detects the errors and prompts you to fix them, based on the same idea. The program you create should:

* include 20 words to spell check.
* when given a paragraph it can detect the spelling error of the given 20 words.
* it should output the fixed or "correctly" spelled paragraph.

Please note that the paragraph will include many words but the program should ignore and only fix the words that are given to it.
Submit the code in .py format.
You are allowed to use the spellchecker pip package.

### Calculator GUI in Java 

Make a GUI using the Java Swing package which works as a scientific calculator, you might use Netbeans IDE to fascilitate the design process of the GUI.Make a github repository for the same.

https://github.com/Abtaha/Java-Swing-Calculator

### Bookmark Application

Create your own bookmark application where you can add/delete bookmarks from the browser's local storage. Make the web interface responsive and user-friendly. Host it on github pages.

### What is a makefile anyway?

Create a Makefile which will execute a small C++ program which would output some data to a text file. A python program will then read the data from this file and plot it.

Please provide the link for the git repository consisting of the source code. Bonus points for following convention.

### Shapefiles and maps

In this task you would be creating maps (using Python). Most of the maps that you see online are created using shapefiles. There are different types of shapefiles including, green-cover, water bodies and roads. You can download all the relevant shapefiles from https://extract.bbbike.org/ for any city that you want.

Now, to plot the shapefiles, you would need the geopandas library. With the geopandas library installed, you can read the shapefile, and plot it using the plot function.

Plot the shapefiles for 5 cities.

Please provide the github link consisting of the source code along with the maps that you've created.

https://extract.bbbike.org/

https://github.com/Abtaha/Shapefiles-and-Maps

### Pollution/Climate and Geographic Information System 

This task is an extension to shapefiles and maps (although, it can be completed independently)

* Try to download the relevant pollution / weather data for any city that you'd like (Normally, you can find such data easily for metro cities like New York, Chicago etc). Make sure that you download the data only from authentic sources.

* Download the shapefile for the relevant city and plot: roads, green cover, water bodies, and roads.

* The data that you'll obtain, typically it would be various locations within the city. Superimpose the map of the city (step 2) with the data that you obtained (step 1).

* Interpolate the data (https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.griddata.html#scipy.interpolate.griddata)

https://github.com/Abtaha/Geographic-Information-System-New-York

### Weather Forcast Webapp

You are required to make a weather forecasting web app using OpenWeatherMap. You could user manually enter his location . Weather data like current temperature, wind, rainfall, sunrise and sunset time need to be displayed.Enhance the look of your page.Host the web page on github pages.

API details:
https://openweathermap.org/api

### Implement Google News API

Google News provides the latest news that are published globaly in well known news networks, this API can be used anywhere so we want you to create a news app using this API.
You should create an app or a website that uses the given code combined with requests to show any news related to these keywords: Linux , Open-source and Android that are sorted from newest to oldest. You can use this guide to setup your app. Note that you can do this with javascript and use your browser as envirnoment.
Submit your python, Node.js or C# made app along with a recording of you running it. Having a GUI is mandatory.

http://news-cog.herokuapp.com/

### Analyzing pcap files to get details of a Network Traffic 

As Wikipedia says, pcap is an application programming interface (API) for capturing network traffic. These files are primarily utilized in analyzing the network characteristics of a certain data. These files are used to determine network status, allowing analyzers to attend to problems that may have occurred on the network and allowing them to study data communications. You will be given a pcap file and you need to analyse the following things from it:

* Visited Sites
* User-Agents
* Connection details(TCP, UDP, ICMP, IP, SMTP, SMB, ARP)
* Grep Mode
* IP List
* Ports Present

NOTE: You are allowed to use tshark, tcpdump, ngrep, and all the tools you need to achieve the task. Please try to keep the programming language limited to python/shell(If you are planning to use another language inform me beforehand.)

This is The Output of my program.

Deliverables:

Share the code in GitHub/Pagure with the ASCIINEMA included.

https://github.com/Abtaha/PCAP-Analyzer

### Hide text inside an image using Stegnography

Stenography is the practice of concealing a file, message, image, or video within another file, message, image, or video. It is related to cryptography and is just about as old. You can use it to transport sensitive data from point A to point B such that the transfer of the data is unknown. This helps data to conserve its integrity. You need to create a Script that encodes and decodes a text from an image(png and jpg). I have attached a link showing how your output should look like.

Deliverables:

Submit the code in Pagure/GitHub. Attach the image you encrypted along with the Asciinema recording while you perform the encryption and decryption.

https://github.com/Abtaha/Text-Encryptor-through-Steganography

### OSINT - Open Source Intelligence on Public Platform

Open-source intelligence is data collected from publicly available sources. The information comes from a variety of sources, including the social media pages, Personal Blogs, Websites, etc. These can be a humongous source of information, such as social media life, and information about the victims acquaintances. OSINT has been used by hackers for the Information Gathering process. You need to create a Python/shell script that checks out the presence of an individual in 3 different website. I have provided the link on how it should look like when a user is present in the specific website.

Deliverables:

Upload your script to GitHub/Pagure and attach a Asciinema of your terminal showing the script doing its job.

### Twitter Bot for posting articles from Fedora Magazine

Write a python script that automatically posts tweets of links of latest articles in Fedora Magazine along with their titles. For example Fedora and CentOS Stream https://fedoramagazine.org/fedora-and-centos-stream/. Learn more about scripting from https://www.guru99.com/python-tutorials.html. You can get recent articles from fedora magazine (https://fedoramagazine.org/). Don’t use Twitter API, for posting tweets, using Selenium or PhantomJS or any suitable web browser. Follow this article for more help https://realpython.com/modern-web-automation-with-python-and-selenium/

Output - Code of python script in Github Screencast of the blog getting posted.

https://github.com/Abtaha/Twitter-Bot

### Time Bound Computation (Python)

Write matrix multiplication programs in Python for a random(n,n) matrix. Write the same program with numpy. Measure time for n=10, 100, 1000 ... and so on until you get a good enough data set. Plot the Time Vs Input graph using matplotlib (for both normal python and numpy). Try to find the reason on why numpy is faster (if it is)

As a bonus you can also try adding @numba.jit to the for loop and see the improvement in timings (if any).

Please share the github link for the repo containing:

* PNG images of all the graphs
* Relevant source code
* The explanation in README.md

### Use python-fedora to find out the FAS ID corresponding to an email ID 

Given a FAS ID as input, provide the corresponding email for using python-fedora (https://github.com/fedora-infra/python-fedora)

Task Details Install python-fedora using pip. Create a script that asks the user to enter a username and prints the email associated with that user account.

Resources You can make use of the following resources to complete the task:

Official GitHub repository for python-fedora
Deliverables Please upload the script and submit a link to the repository (hosted either on GitHub or Pagure).

### Setup fedora-messaging on your local machine and publish & listen messgaes

Task Details Setup Fedora Messaging on your local machine and create a sample publisher and listener to test the installation.

Resources You can make use of the following resources to complete the task: Follow the official documentation of Fedora Messaging here.

Deliverables

* Please submit a GitHub link to the repository containing the script for the publisher build.
* Upload a screenshot or screen recording of the listener and publisher in action.

https://github.com/Abtaha/fedora-messaging-demo

### Create your first Telegram Bot

Make a simple bot which fetches the number of forks from the repo of Fedora-Infra. Scrape from https://api.github.com/orgs/fedora-infra/repos. Make a dedicated repository or show the code via gist. Make the bot in Python. Python - https://github.com/python-telegram-bot/python-telegram-bot (https://python-telegram-bot.readthedocs.io/en/stable/) Submit a link to your repository. Add an demo attachment(png).

https://github.com/Abtaha/Telegram-Bot

### ffmpeg and Climate/Pollution gifs 

This task is an extension of Pollution/Climate and Geographic Information System, although, it can be done independently.

This task will involve making GIFs for Pollution/Climate data for a given range (say 7 days). Repeat the process from the previous task: Pollution/Climate and Geographic Information System for the desired number of days. Each time save the plot as a .png file.

Finally, use ffmpeg to merge the all the .png to make a .gif file. https://unix.stackexchange.com/a/24103

https://github.com/Abtaha/Climate-of-New-York-with-Python

### Periodic table guessing game

Some of the mentors love to play with the elements of the periodic table. They have a hard time remembering the atomic symbols corresponding to the atomic numbers. To fascilitate the process of learning and giving hints this task requires you to create a GUI in python or Java where you need to have a display box in which an atomic number is generated randomly and a text box where you can enter the element symbol as a guess. There must be a submit button, get answer button, quit button and a generate new button(for changing the atomic no).

Rules:
* If the guess is correct show that its correct in the GUI itself or a popup and generate a new atomic number.
* If the guess is incorrect make some hints to guide the user to correct answer. example hint : The correct element is on the left/right of the element entered
* If incorrect more than 5 times then game over. Note: You need to check for a valid element is entered or not and show appropriate error

Submission format:

Github link with code and scrrenshots of the GUI

https://github.com/Abtaha/Periodic-Table-Guessing-Game

### Create a program to detect colors from an image

Image processing is a subset of computer vision. A computer vision program uses the image processing algorithms to try and perform emulation of vision at a human scale. Make a program using python and Open-CV that detects colors present in an image.

Deliverables:

Share the code in Pagure/GitHub. Send the screenshots of the output. You can also attach a Asciinema recording of your terminal. Do not copy someone else's code from GitHub/Stack Overflow.

https://github.com/Abtaha/Detect-Colors-from-Image

### University data managment

A university asks you, in order to determine the best applicants, you should create an algorithm that manages given data and selects the best applicants among them. Considering these factors to determine the best applicants: 40% academics, 30% IELTS socres and 30% Interview score.

* Academics: Out of 100, Average of scores. (Maths and Physics hold 2x value)
* IELTS: Out of 9, all 4 subjects are equally important.
* Interview: All factors equally important and are marked out of 10.

Your algorithm will read and process data from the given ODF files in the same format as here, then sort the applicants from the best to the worst according to their academics, Interview and IELTS and output it in a simple ODF or txt format. (Note that I will test further your code by giving it ODF files with different names, marks, student count etc.) Upload your code either in Zip or github along with the results.

https://github.com/Abtaha/University-data-managment

### Create a program to Identify Numerical Digits

Computer Vision is a field in Artificial Intelligence which teaches the computer to visualize the 3D world. Computer vision include methods for obtain, process, analyze and understand digital images, and drawing out data from the real world to produce numerical or symbolic information. In simple words, its main goal is to extract meaning from pixels. Make a program that detects Numerical Digits present in an image.

Deliverables:

Share the code in Pagure/GitHub. Screen Record the output and attach it in your README file. Do not copy the code from GitHub/Stack Overflow.

https://github.com/Abtaha/Identify-Numerical-Digits-OpenCV

### Pool Puzzle

Pool Puzzle is a coding puzzle that consists of completing the FlyTest java class with appropriate values to give exact output as required. More detail of the problem is ruled down in Rules.md This task requires to have good knowledge of Java and OOPs concept (Inheritance). Download or clone the project from here https://github.com/alishamohanty/Pool-Puzzle

### Astronomy and Python

Read up about fits file and download a sample file from https://fits.gsfc.nasa.gov/fits_samples.html

Using astropy, read the fits file in python (Jupyter notebook). Edit the headers and Manupulate the fits file.

Articulate your findings in the task and write a few paragraphs about it in the same Notebook.

https://github.com/Abtaha/Astronomy-with-Python

### Create a reverse WHOIS lookup using viewdns in python

WHOIS is a query-response protocol used for searching databases that store the information for registered users. It can search a domain name, an IP address or an autonomous system. WHOIS Reconnaissance is a crucial part in the process of Information Gathering. Create a python script that uses https://viewdns.info to find domain names owned by an individual person or a company.

Deliverables:

Share the code in Pagure/GitHub and provide the Asciinema recording while executing the script. Give a brief description on what is WHOIS lookup.

https://github.com/Abtaha/Reverse-WHOIS-lookup-using-viewdns

### Benchmark: Python, Julia, C++ 

Choose two matrix operations: Finding inverse, Transpose, Diagonalization etc.

* Start out with a large matrix n>10000 and benchmark the time taken as the n increases.
* For a particular matrix, log the operation 5 times and take the average.
* Compare the averages with the above-mentioned languages and give the formatted output in the text file.

Use Makefile for this task for bonus points.
Submit the link for git repo

https://github.com/Abtaha/Benchmark-Python-Julia-C-

### Image manipulation with python 

Bulk Images can sometimes be a lot time consuming if they need a marginal edit or a change in size, thus we want a help from you...
Create a python script that that scales images by 400 by 400 or less pixels and make sure they images won't exceed 64 kilobytes after the edit. for that you should mess with jpeg quality settings. The script should ask for the directory of the files, do the edit and finally save it in the same directory in a new folder. You are allowed to use pip packages. We are looking at high amounts here, so your code should ask for folder, and not the file, one by one.
The aspect ratio shouldn't change.(one of the side should be 400 while the other can be 400 or less)

### Remote Command Execution using reverse Shell

A reverse shell is a type of shell connection where the victim communicates with the attacker's computer. The attacker has a listening port active which listens from the victim's machine, this is how command execution works. You need to create a victim file and an attacker file in python/shell(Keep the exploit limited to Linux based OS. No need to create for windows or android). The attacker should have a listening port active and it should access the victim's shell.(Don't Cause Damage to someone else's Computer Files.)

Deliverables:

Submit the code in Pagure/GitHub and and Asciinema recording which shows you are controlling the victim.

https://github.com/Abtaha/Remote-Command-Execution-For-Hacking

### Create an Ansibile Role to automate the installation process of tensorflow

Ansible uses YAML(YAML Ain’t Markup Language) syntax. Unlike many programming languages, YAML is relatively easy to understand by just looking at the code. Ansible playbooks are cool tools widely used in automation of tasks that takes up time. Tensorflow is an open-source library with is capable of running machine learning algorithms. It was developed by google brain’s team. The installation processes can sometimes be tiresome. Learn more about Tensorflow and Create an Ansible Role to automate the installation process of Tensorflow(CLI-Command Line Interface) or GUI(Graphic User Interface).

Deliverables:

Upload the Code to Pagure/GitHub and give a small explanation about Tensorflow in the README file. Provide an Asciinema of your terminal while executing your code.

https://github.com/Abtaha/Ansibile-Role-to-automate-the-installation-process-of-tensorflow

### Hacking using Hardware (Craft a Rubber Ducky)

Hackers use many types of methods to gain access to a victim computer. Rubber duckies can be used to gain reverse shells, type key strokes, and even cause Code execution on behalf of the user. Rubber Duckies are usually in a form of a USB so that it can be plugged in and it can give us the required shell. For this task you need the following hardware:

* Arduino Nano OR Arduino Pro Micro OR Raspberry Pi 0/3/4 OR DIGISPARK

NOTE: In this task you need to use any of the hardware to gain a reverse shell to a Windows computer.

Deliverables: Share the Arduino code in a GitHub/Pagure repo with a documentation for the task including screenshots on how it works on a victim computer. It will be better if the documentation is in the README.

https://github.com/Abtaha/Rubber-Ducky-with-Arduino

### Avengers Endgame 

Alike the previous part, Thanos will again be visiting our blue planet but this will be his last visit there as he is going to be killed either by Iron Man or Captain America. Thanos has a total power P which is reduced by some amount while fighting. In order to be killed, his power must become smaller than or equal to Zero.

Both the Superheroes fight with Thanos on alternate days, Iron Man fighting on Day 1,3,5,7… . and Captain America on Day 2,4,6,8… and so on until Thanos doesn’t get killed. On any given day D they can reduce the power of Thanos either by D or D+1. Both the superheroes want Thanos to get killed by their hands and for this they fight optimally with him. Being the Director of this part, you want to know that for a given power P of Thanos, who will be the superhero killing him. Write a code to solve the following problem.

Note :
Think of the most optimal solution you can think of :) (Brute Force solution will not be accepted)

INPUT FORMAT
First line of input is N which is the number of test cases. Only line of test case is an integer D which is the power of Thanos.

OUTPUT FORMAT
For each test case, print "IRON MAN" if Iron Man kills Thanos and "CAPTAIN AMERICA" if Captain America kills Thanos, in a new line.

SAMPLE INPUT
5

1

2

4

1000000000000000

10000000000000000

SAMPLE OUTPUT
IRON MAN

IRON MAN

CAPTAIN AMERICA

IRON MAN

CAPTAIN AMERICA

Constraints

1<=T<=10^6

1<=P<=10^16

SUBMISSION FORMAT
Attach your code here. Languages- C,C++, Java, Python3 Test cases:

https://drive.google.com/open?id=11zJPw-X2_JQbJVXQHQ5Aw5YJ-6QrMBFh


## Thoughts

![Completed Tasks](./completed.png)

GCI was an amazing experience. It taught me many new technologies and gave me the chance
to hone my skills. It also finally managed to get me to switch to Linux ;p Hopefully will participate
next year too. Thanks to all the mentors over at fedora to give me a chance at CodeIn.

