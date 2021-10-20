# Intro To HTML

1. [Context](#context)
2. [Objectives](#objectives)
3. [Setup](#setup)
4. [Launch](#launch)
5. [The Lesson](#the-lesson)
6. [Extensions](#extensions)
6. [Related Resources](#related-resources)

## Context

### Social-emotional Launch!

This is the first day of the course - with that in mind, this lesson is designed to be a bit shorter than many of the rest of the lessons in this course. The idea is to preserve about 30 minutes at the start of the lesson for you to get to know your students. 

One of the best ways to launch a class is with a whip-around - start with yourself, and then call on each student and ask them to share three things:
1. Name + pronouns
2. One simple piece of biographical info (like what city you live in or are from)
3. One opinion question that lets students express their opinions or show off their personality ("Are you a cat person or a dog person?", "What was the last great meal you had?", or "What's your least favorite chore?")

Then, you can segue into an energizer that makes space for each student to share a piece of their identity (in a virtual setting, a show-and-tell or a scavenger hunt is amazing for this purpose).

### Why HTML?

It's important to remember that this first unit focuses on HTML not because need to achieve a certain level of mastery in order to progress, but rather because HTML is a really forgiving language to explore Git and GitHub with, and also because HTML can be a really creative medium and an amazing opportunity for students to get to know one another. 

Over the course of this week, students will build a team page in HTML. The primary purpose of this page is to give the team members an incentive to get to know one another and start to view their group members as collaborators, not competitors or dead weight. That means it's critically important for you, the teacher, to lower the stakes. 

### Heterogeneous Mix

Remember that students are coming from all different contexts. Some have been studying CS for years, and some began coding much more recently. The only way for a group of differing experience levels to gel as a team is to lower the stakes. That means making it clear that the purpose of working in a team is collaborative, not competitive. The goal isn't to find out who on each team is the most experienced in a given content area, or to find out which team is the strongest, but rather for the most experienced team member to step into a leadership capacity and immediately make themselves available to help upskill their partners. 

Rather than try to hide these different levels of expertise, embrace them! Be explicit about the fact that some students have spent lots of time with HTML, and others will be seeing it for the first time today, so it wouldn't make sense for you, the instructor, to go over everything. 

Tell them that instead of stepping through all of HTML, you're going to give a high-level introduction to some foundational concepts and then make space for students to get to work. Explain that you expect the more experienced members of each group to step into the mentoring role that senior engineers take. It's their job to make 100% sure that everyone in their group understands the code they're writing. 

### Lab Difficulty

This lesson also includes the first lab of the course, and it's intended to be relatively easy. The stated purpose of the lab is to get students to practice nesting HTML elements and writing `class` and `id` attributes correctly, but the more hidden secondary purpose is to give the instructional team a chance to see how well students do working together as a team, and to help troubleshoot environment issues at this early stage with anyone who has them without totally derailing their progress. 

## Objectives

* SW (students will) write basic web pages in HTML and open a preview to view those pages.
* SW add attributes like `class` and `id` to their HTML elements. 
* SW properly nest HTML elements inside one another. 
* SW write basic ID and class selectors in CSS, and add `background-color` and `padding` to those elements.

## Setup

Decide which environment you want students to use for this activity, and prepare your sample code in that environment. While the majority of this course will be taught in Google Cloud Shell or in a local IDE, it is recommended that for ease of setup, this first week is taught in a ready-to-use cloud-based IDE that is optimized for HTML. Repl.it and Glitch are the two environments that make distributing code snippets to students the easiest - simply share the link to your workspace, and show students how to remix or clone the workspace you share. 

To set up this lesson, you only need an `index.html` file and a linked `style.css` file. The CSS file should be blank, and the `index.html` file should contain the following code:

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Berto's!</title>
    <link rel="stylesheet" href="style.css" type="text/css">
</head>
<body>
    <h1>Welcome to Berto's Bakery</h1>
</body>
</html>
```

## Launch

Show students the overall trajectory of the three units of this course. Explain that we'll ultimately be building full-fledged web-applications, but that basically everything they interact with in their browsers uses HTML in some way, so it's a really good place to start. 

Name that while everyone likely has different experience levels in HTML, that there's always more to learn, and then direct them to the [NYT Science Website](https://www.nytimes.com/section/science). Demonstrate how to open the inspector in Chrome, and then show the sheer volume of code that has been used to create this site. 

Then, show students how to identify an **element** in the inspector (either by color code, or by the fact that it immediately follows a `<` symbol) and challenge students to a scavenger hunt - find at least 8 different elements in under 2 minutes.

Have students share their answers aloud or in chat, and then emphasize that almost no one would know how to code all of the elements from scratch. Anytime you're learning something new, you'll spend a lot of time consulting **documentation**, and one of the best places to go for HTML documentation is [w3schools](https://www.w3schools.com/tags/default.asp). 

Demo the documentation for any simple element (like a [paragraph](https://www.w3schools.com/tags/tag_p.asp)) and then pause to point out that while some people call HTML elements "tags", a tag is only part of an element. An HTML element is usually made up of three parts:
* An opening tag, like `<p>`
* A closing tag, which has a slash in it, like `</p>`
* The contents or innerHTML - the stuff in between those two tags, which is usually either text or other entire elements. 

Finish the launch by encouraging students to look at w3schools as often as possible. Let them know that while w3schools is a GREAT place to learn about individual elements it can be hard to imagine how they all fit together without practicing or seeing them in context, so it's time to start coding. 

## The Lesson

### Hello Bakery

Let students know that we'll be building a webpage for a restaurant together. The sample code here involves text for a restaurant called "Berto's Bakery" but feel free to theme the restaurant to your own name and culinary interests, or to one of the TAs or even one of the students. 

Have students look at the code itself on your screen before opening it themselves.

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Berto's!</title>
    <link rel="stylesheet" href="style.css" type="text/css">
</head>
<body>
    <h1>Welcome to Berto's Bakery</h1>
</body>
</html>
```

#### Helpful Questions
* On what line number is the **opening** tag of the body? What about the closing tag?
* How many elements are inside the body?
* How many elements are inside the head?

Point out any useful features in the syntax highlighting of the coding environment you've chosen to work in, including any relevant color coding, and demonstrate that clicking on any opening tag highlights the corresponding closing tag and vice versa. 

Then open the preview and show that the h1 element has made a level 1 heading. 

At this point, you're ready to start coding with students. It may be wise to name that some people learn best by coding along, and others learn best by watching and taking notes. Give students space to reflect on which learning style suits them better, and then ask them to tell you which one they'll be doing today. 

Share the code with them and ensure that everyone who is coding along is able to get the code up and running. 

### Divide and Conquer

As we build out our website, it's important to organize our code as clearly as possible. One of the best ways to do that is with dividers - since this is a restaurant page, we should have at least two divisions of our page: a menu section and an about section. 

```html
<body>
    <h1>Welcome to Berto's Bakery</h1>
    <div id="about">

    </div>
    <div id="menu">
        
    </div>
</body>
```

#### Helpful Questions
* Especially if today is your first day with HTML, why do you think we've added `id`s to both of our new dividers?
* How does HTML appear to use quotation marks? How is that different from other languages you've written in?

Open the preview and show that each `div` is essentially invisible - while we can write additional code to MAKE them visible later, for now think about them simply as ways to group other elements together for our organizational peace of mine as web developers.

So it's time to add some content to our "About" div. We'll add a level 3 heading with our restaurant's motto, and a paragraph with some additional information.

```html
<body>
    <h1>Welcome to Berto's Bakery</h1>
    <div id="about">
        <h3>The best bread you've ever broken!</h3>
        <p>Come join us at 123 Division Drive and try some of our incomparable croissants.</p>
    </div>
    <div id="menu">
        
    </div>
</body>
```

### Comments

As our code gets longer, it's going to be easier and easier to get lost. Pause to add a comment, and explain that it doesn't do anything to our actual website. 


```html
<body>
    <h1>Welcome to Berto's Bakery</h1>
    <div id="about">
        <h3>The best bread you've ever broken!</h3>
        <p>Come join us at 123 Division Drive and try some of our incomparable croissants.</p>
    </div> <!-- End of ABOUT -->
    <div id="menu">
        
    </div> <!-- End of MENU -->
</body>
```

#### Helpful Questions
* Why do you think we've added these comments?
* Why else might comments be useful in HTML?

### Menu Items

Let's move on and build the menu. In the same way that the menu is a division on our page, we'll want to divide the menu up into individual items:

```html
<body>
    <h1>Welcome to Berto's Bakery</h1>
    <div id="about">
        <h3>The best bread you've ever broken!</h3>
        <p>Come join us at 123 Division Drive and try some of our incomparable croissants.</p>
    </div> <!-- End of ABOUT -->
    <div id="menu">
        <div class="food">

        </div>
        <div class="food">
            
        </div>
    </div> <!-- End of MENU -->
</body>
```

#### Helpful Questions
* Especially if today is your first day with HTML, you may have been surprised that we didn't give `id`s to these divs. We gave them classes instead? Why do you think it would be bad practice to use `id="food"` twice on the same page?

> A helpful analogy here: As a student, you likely have an ID number at your college or university. That's unique! You should be the only one who has that number. But as a student, you're also enrolled in lots of classes, and there are dozens of other students in those classes with you. As a rule of thumb, it's generally better to use classes when you want to create a group, and to use IDs when you want to create something one-of-a-kind.

Next up, let's add some details to each of our two menu items.

```html
<body>
    <h1>Welcome to Berto's Bakery</h1>
    <div id="about">
        <h3>The best bread you've ever broken!</h3>
        <p>Come join us at 123 Division Drive and try some of our incomparable croissants.</p>
    </div> <!-- End of ABOUT -->
    <div id="menu">
        <div class="food">
            <h4>Croissant</h4>
            <p>The flakiest, butteriest pastry we have</p>
            <h6>$2.79</h6>
        </div>
        <div class="food">
            <h4>Old-fashioned Donut</h4>
            <p>A delicious, deep-fried classic treat</p>
            <h6>$3.29</h6>
        </div>
    </div> <!-- End of MENU -->
</body>
```

This is basic, but it's also basically done!

> Note: At this point, students have enough info to do the lab, but if time allows, making some space for students to practice could go a long way. Some good tasks to encourage students to explore might include how to add a link or an image, or simply have them add another few foods. 

### Add Some Style

> Note: It's recommended that students have a chance to practice with HTML as a standalone concept, even if it's just for 5-10 minutes, before moving on to CSS. If they've done the lab, a lot of these concepts, including the shorthand for `id` and `class` will already be a bit familiar. 

So we have the core content of our restaurant's site made, but it looks pretty basic. 

If we want to add fonts, colors, or complicated layouts to our page, we're going to need some CSS - the language that works right alongside HTML to tell a user's browser how to display the content. There are hundreds of different bits of CSS we could learn, but let's start with some of the tools that give a beginner the most control over how their page looks. 
* We'll learn `text-align` to center some of our text.
* We'll learn `background-color` to make different sections of our page look like discrete elements. 
* We'll learn `padding` and maybe even `margin` to give our content a lot more breathing room. 

Open up the `style.css` file, which should be blank, and walk students through writing each of the following rulesets.

Let's start be getting our page title centered. 

```CSS
h1 {
    text-align: center;
}
```

Refresh the HTML page preview and show students how this rule has impacted our page. Pause and point out the significance of each punctuation mark. 

Then, explain that we can give a blue background to our "About" section to help separate it from the rest. It's a `div`, but we can't just select divs the same way we did our h1 - there are tons of divs on our page. 

```CSS
div#about {
    background-color: azure;
}
```

Explain that `#` is shorthand for `id`, so this selector can be read as "the div with an id of 'about'". Revise `div#about` to just `#about` and explain that this just means "the element with an id of 'about'"; we don't _need_ to specify that it's a div since it should be the only element with that ID anyways - remember, IDs are supposed to be unique. 

Let's revise that out and add in another ruleset for our other div - the menu:

```CSS
#about {
    background-color: azure;
}

#menu {
    background-color: aliceblue;
}
```

By now students are wondering whether you're making up colors - share the [CSS colors page](https://www.w3schools.com/cssref/css_colors.asp) from w3schools. 

Let's also write something for our foods - instead of a `#`, we'll use a `.` to indicate that we're looking for a class this time. 

```CSS
.food {
    background-color: cadetblue;
}
```

Last but not least, let's add some breathing room. We use `padding` to space the contents of an element away from it's own edge, and `margin` to space the whole element away from its neighbors. 


```CSS
#about {
    background-color: azure;
    padding: 30px;
}

#menu {
    background-color: aliceblue;
    padding: 30px;
}

.food {
    background-color: cadetblue;
    padding: 30px;
    margin: 20px;
}
```

This is great - what we have now looks a lot more like a real webpage, albeit a somewhat barebones one. But we've barely scratched the surface of what CSS can do, so it's important to learn how to look for additional answers. Be sure to use the w3schools documentation as a first step, and if you can't figure it out from there, be sure to include the phrase "in CSS" in whatever you search online. 

For example, "how to make text bold" is going to give you lots of answers about Google Docs and Microsoft Word - you want to search "how to make text bold in CSS" to get your answer. 

> NOTE: As before, if time allows you'll want to give students a chance to implement something new in CSS. Consult the extensions below for more ideas.

## Extensions

Extensions are generally presented in order of difficulty, and should be offered to students with that caveat in mind. It's not critical that students do these activities specifically, but these are a good starting place. 
* Add an image to each of the foods.
* Add a link to an article where people can learn more about the food you serve. 
* Change the color scheme of the restaurant to suit your liking. 
* Put your restaurant name inside a div, and color the background of that div. 
* Make each food appear to hover in 3d space by giving it a box shadow. You may need to Google this.
* Find a way to get the foods to appear tiled next to one another instead of in a column. 

## Related Resources

* [w3schools HTML Tutorial](https://www.w3schools.com/html/default.asp) - written and video HTML tutorial
* [w3schools CSS Tutorial](https://www.w3schools.com/css/default.asp) - written intro to CSS
* [Scrimba HTML & CSS](https://scrimba.com/learn/htmlcss) - interactive video tutorial on HTML basics
* [CSS Tricks Complete Guides](https://css-tricks.com/guides/) - easy-to-follow introductions to really advanced CSS
