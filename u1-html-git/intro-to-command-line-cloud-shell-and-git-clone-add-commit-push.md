# Intro to Command Line, Cloud Shell, and Git clone-add-commit-push

1. [Context](#context)
2. [Objectives](#objectives)
3. [Setup](#setup)
4. [Launch](#launch)
5. [The Lesson](#the-lesson)
6. [Extensions](#extensions)
6. [Related Resources](#related-resources)

## Context

In this lesson, we will introduce Git and Github as version control and collaboration tools. This will create the foundation to the skills they will develop as students continue to use Github to collaborate with their team members in future lessons. 

## Objectives

* SW develop fluency with the ls, pwd, cd, and cloudshell open commands. 
* SW know what Git and GitHub are, and why they are used. 
* SW learn the git clone, git add, git commit, and git push commands - both what they mean and how to execute them.
* SW create git auth tokens and understand why they are used.
* SW create and preview an HTML page in Cloud Shell.
* SW create a new repository and commit at least one HTML page to it. 
* SW learn to use GitHub Pages to host static HTML pages. 

## Setup

Instructors and students should have created accounts on Github and on Cloud Shell. 

Instructors should also organize their Github repositories to make it easy to demo in the introduction of Github. 

Prepare a Github repository with an index.html file that contains links to the students' files. These links will not be functional yet but are placeholders for now. 
Example: 
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Roster</title>
</head>
<body>
    <h1>Meet the class</h1>
    <a href="student1.html">[Insert Student1 Name]</a>
    <a href="student2.html">[Insert Student2 Name]</a>
</body>
</html>
```
Also add an HTML file that contains the following code:

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Meet Me</title>
</head>
<body>
  <!--replace with your fun facts!-->
    <h1>Hello! My Name is </h1>
    <h2>School: </h2>
    <h2>Major: </h2>

    <h1>Fun Facts: </h1>
    <h2>Food I would recommend: </h2>
    <h2>Last song I had on repeat: </h2>
    <h2>Random fun fact about me: </h2>
    
</body>
</html>
```

## Launch

Prompt the students to try to think back to when computers were still new and storing documents in the cloud didn't exist yet. How did we save our files and how did we share our work?

#### Helpful Questions
* If we wanted to save a new version of our file, what would we have to do?
* How could this older process get tedious and confusing?

## The Lesson

### What is Git and Github 

lesson text, followed by code snippet(s), and then ###Helpful Questions

Provide a brief introduction of Git and Github. Make sure that students understand the difference between Git and Github. 

Git is a version control system that allows you to track the history of your files. Github is a web based service that allows you to host Git repositories. 

Take the students on a tour through Github. Browse through your own repositories to show how code files and its version history are stored and displayed. Then do a search for other public repositories. 

#### Helpful Questions
* What are the benefits of being able to access past versions of your files?
* What are some benefits to seeing other public repositories?

### Navigating Through  Files
When students are coding, it is important that they know where their files are being stored. WHen they first open the Cloud Shell editor guide them to the Terminal and navigate through the workspace by using the commands: 
* pwd
* ls
* cd

Also point out that these commands can be used in their machine's Terminal (Mac/Linux) or Command Prompt (Windows).

#### Helpful Questions
* What is the output when the pwd command is run? What do you think each part means?
* What is the output when the ls command is run?
* What is the difference between pwd and ls?
* Are you able to run the cd command?
* How is this process similar to how you navigate through your files on your computer through your File Explorer or Finder?

### Git Commands
Share the link to the starter code repository and guide the students through cloning the repo into their Cloud Shell workspace. When the students clone the repo, they will be prompted to enter their username and password. The username will be their Github username and the password will be a personal access token that they will have to generate through their Github accounts. (Settings>Developer Settings>Personal access tokens>Generate new token) 
Explain to the students why a personal access token is used rather than the traditional password. 

#### Helpful Questions
* Why is it more secure to use a personal access token over a password?

### Using Cloud Shell
Once the students have cloned the repository, guide them through a tour of Cloud Shell's user interface. Prompt them to open the HTML file in the repo and preview the page. Then, have them make a new HTML file using the naming template: firstname_lastname.html and copy the starter code into their new file. 

Give them 10 minutes to personalize their new page with their own fun facts! 


### Git add, commit, push
Now that every student has customized their own page, go over the Git add, commit, and push commands to push their new files into the repository. Make sure to remind the students run the terminal commands that we learned earlier to make sure that they are on the correct directory. 

#### Helpful Questions
* What is the difference between the three git commands? 
* Why is it important to write a message when running the git commit command?
* How can you tell if you were able to successfully push your files?

### Viewing A Website Through Github Pages
Once all of the students have pushed their code to the Github repository, demo how to change the visibility of the repository on Github pages. Set the visibility to public and share the link to the class. 

Open the Github page of the repository and navigate through each of the new pages. Have each student introduce themselves and talk through their fun facts! Create an opportunity for each of the students to connect around their shared facts, as well as any challenges they encountered through this activity and how they overcame them. 


## Extensions

Extensions are generally presented in order of difficulty, and should be offered to students with that caveat in mind. It's not critical that students do these activities specifically, but these are a good starting place. 
* Navigate to another directory on your machine using the pwd, ls and cd commands.
* Navigate to the root directory.
* Find a directory on your machine that has at least three files listed.
* Check out other cool projects. Find another public repository you are interested in and clone it down to your workspace. 
* Create a brand new repository on Github and add your own code project to it. Host it on Github pages and share it!

## Related Resources

* [Github Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/changing-the-visibility-of-your-github-pages-site) - Changing the visibility of your Github pages site
* [Personal Access Tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) - How to create a personal access token on Github and why you should create one
