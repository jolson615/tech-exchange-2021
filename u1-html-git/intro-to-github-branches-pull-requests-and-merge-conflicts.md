# Intro to Github Branches, Pull Requests, and Merge Conflicts

1. [Context](#context)
2. [Objectives](#objectives)
3. [Setup](#setup)
4. [Launch](#launch)
5. [The Lesson](#the-lesson)
6. [Extensions](#extensions)
6. [Related Resources](#related-resources)

## Context

Now that students have been introduced to Github and the clone, add, commit, and push commands, we will take one step further into the world of collaboration through Github. Students will learn how to use Github to work collaboratively on a single project. 

Make sure to start the lesson by letting students know that using Github to work collaboratively is a skill that takes practice. They will most likely run into some frustrating bugs or get confused about why a certain outcome occurred. This is normal when first starting to use Git and Github. 

## Objectives

* SW understand what branches are and why they are used
* SW create new local branches
* SW create remote branches to mirror their new local branches 
* SW initiate pull requests on GitHub
* SW resolve merge conflicts 
* SW merge pull requests

## Setup

Create a repository on Github with the following starter code:
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Cafe Tech Exchange</title>
    <link rel="stylesheet" href="style.css" type="text/css">
</head>
<body>
    <h1>Welcome to Cafe Tech Exchange</h1>
    <h3>Hours: XX:XXam - XX:XXpm</h3>
    <hr>

    <h2>Appetizers</h2>
    <h3>...</h3>
    <h3>...</h3>
    <hr>

    <h2>Entrees</h2>
    <h3>...</h3>
    <h3>...</h3>
    <hr>

    <h2>Desserts</h2>
    <h3>...</h3>
    <h3>...</h3>
    <hr>

</body>
</html>
```


## Launch

Imagine you and two of your friends are hosting a dinner party. Dinner is in a few hours and everyone knows how many people are coming over and how many dishes to cook. You and your two friends are standing in the kitchen. Where do you all start?

Have the students come up with suggestions on how they would get started in this situation. By the end of the conversation, the students should come to a general conclusion that tasks are delegated and everyone handles a different task to prepare dinner. It wouldn't make sense for everyone to be boiling the water or cutting up the same vegetables right?

Working collaboratively on a coding project is the same. When working in a team, it doesn't make sense for multiple people to tackle the exact same feature. Instead, features are delegated to different programmers and each programmer is contributing to the overall project through their own part.

## The Lesson

### Working Collaboratively with Github 
Start the lesson by sharing the link to the starter Github repository. Students should clone the repository into their workspaces. 

Guide the students through creating a new branch using, the git checkout command, and explain the importance of working on their individual branch to develop their own features. Name their branch as their name for easy identification. 

The git command should look similar to: 
````
git checkout -b myFirstName-LastName
````

#### Helpful Questions
* What issues do you think would arise if everyone started editing the existing files?
* When everyone is on their own branch, can we see the changes that are being made on those branches yet?

Give the students 5-10 minutes to make at least one change to the menu. They do not have to edit everything. Instructors should make sure that there is at least two students who have made changes to the same part of the code to trigger a merge conflict later. Once students have added their changes, have them push their code. 

### Dealing with Merge Conflicts
Walk through the Github repository on the browser and show how the branches and notifications for the branches appear on the webpage. Click on the dropdown list of all of the branches and identify a few students' branches that are visible. 

Now that the branches have been pushed to the repository, they are visible to all collaborators. However, if we click the main branch's HTML file, no changes are displayed there. 

In order to merge the students' changes and have the changes reflected on the main branch, we will have to do several pull requests. Guide the students through creating a pull request. Optionally, you can have one of the students demo from their point of view as you verbally guide them through each of the steps. Students should see a button to 'Compare & pull request' at the top of their repository on the browser. Once they click it, they should be able to identify the branch they are attempting to create a pull request on and the branch they are trying to add it to. Add a comment and create the pull request!

As the pull requests come in, point out the merge conflicts that occurred as you resolve them. Make sure that the students understand why the conflicts were created and how to identify and resolve them. 

## Extensions

Extensions are generally presented in order of difficulty, and should be offered to students with that caveat in mind. It's not critical that students do these activities specifically, but these are a good starting place. 
* Try to resolve a merge conflict yourself.
* Create a branch and make a change that will not cause any merge conflicts.
* Initiate another pull request with new changes.
* Create a branch from an existing branch.
* Starting in a repository that was branched off from another branch, merge the changes down into the parent branch.

## Related Resources

* [About Branches](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches) - Github Docs
* [About Pull Requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) - Github Docs
* [Branching Tutorial](https://www.atlassian.com/git/tutorials/using-branches) - A quick guide to creating Github branches
