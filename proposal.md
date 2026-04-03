# Project Proposal

## 1. Project Identification
- **Project Title: Card Game Discord Bot**
- **Course: Process Automation CPT-273**
- **Term: Spring 2026**
- **Student Name(s): Hayden Allen, Zarin Deane**
- **Primary Contact: Hayden Allen**
- **Proposed Start Date: 4/1/2026**
- **Proposed End Date:5/3/2026**

---

## 2. Project Selection & Motivation
Describe why you selected this project and why you are a good fit.

Include:
- Personal or professional motivation
- Alignment with career goals
- Relevant interests or prior exposure

We selected the idea of a card game based discord bot that because we both enjoy playing card games and we have experience with making a discord bot. We got our idea from the assignment providing an example of a bot that assits dungeons and dragon campaigns and we think a bot with card games is kind of similar but different enough. We both know a handful of card games that would be plausible as a text based game that can operate through a discord bot using python. We both enjoy coding and we plan on persuing careers in coding so this is a nice test of our skill.

---

## 3. Problem Statement
Clearly describe the problem, need, or opportunity this project addresses.

Answer:
- What problem exists?
- Who is affected?
- Why does this problem matter?

Limit to 1–2 focused paragraphs.

The problem that exists is that students within the class server sometimes don't get to know one another and sometimes they don't bond. The wordle within the server is pretty popular and I see a lot of people playing it and I think having another game that can be more playable with peers will promote more people talking to one another. I think at least getting to know a couple of your peers is somewhat important in computer based environments especially for jobs as you work in teams and I think having a bot that allows you to play games with one another may make it easier to branch out who you know.

---

## 4. Proposed Solution Overview
Provide a high-level description of your proposed solution.

Include:
- What you intend to build, deploy, or configure
- Core features or capabilities
- Explicit exclusions (what the project will *not* include)

We plan on making a discord bot that is easy to start, run, and play games through. This bot will be accessed with the command !games and will prompt the user with a list of all the games and leaderboards associated with the game. We plan on making at least 4 core games which will be War, Blackjack, Poker, Higher or Lower, and hopefully more. For the leaderboards we want to store the highscores of most games like most money in Poker and highest streak in higher or lower. This will hopefully add a element of competiveness and make people talk about it. We also intend on adding a multiplayer aspect so if you want someone to join in you can have a option of sharing it to the server so others can play with you. This bot however will not include gambling with real money and will just use money earned for a leaderboard. The bot will also not have advanced decision making for poker along with the full mechanics of betting. 

---

## 5. Technical Stack & Tools
List the technologies you expect to use.  Please note that this solution MUST live within the cpt.internal network and must be maintainable by future students.

- **Operating System(s):** Linux and windows
- **Programming Language(s):** Python
- **Frameworks / Libraries:** discord.py, python-dotenv, pillow, colorama, emoji
- **Databases / Storage:** sqlite3
- **Infrastructure (VMs, containers, etc.):** schools server and VM, Dockerfile, Docker Compose
- **Tools (Git, CI, monitoring, APIs, etc.):** GIT, GitHub

---

## 6. Prerequisite Knowledge & Skills
Assess your readiness for this project.

Include:
- Skills you already have
- Skills you need to learn
- Relevant coursework completed
- Prior projects or experience

Be honest—this section helps scope the project appropriately.

Zarin and I have learned how to make a discord bot together for CAPSTONE so hopefully we can get a better discord bot up and running that is more complex through code so it can support the games. What we will need to learn is how to host a multiplayer game setting through the discord bot. We both have completed python classes so we are fairly confident in our abilities.

---

## 7. Project Scope & Deliverables
Define what success looks like.

Include:
- Minimum viable deliverable (MVP)
- Required outputs (application, scripts, documentation, etc.)
- Optional stretch goals (if time permits)

Our minimum viable deliverable goal is to deliver a bot that can host card games through it and those games can be multiplayer. A example of that would be playing higher or lower against a peer in the discord and having a functional game that ends and declares a winner when someone looses. We also intend on having a leaderboard that can be accessed within the command of !games. A required output would be a leaderboard CSV so it can call back who has the most points per week. Our optional stretch goals is to make the bot more flashy and easy to navigate as well as more games.

---

## 8. Milestones & Timeline
Provide a rough timeline broken into phases.

Example:
- Phase 1: Research & Design
- Phase 2: Core Implementation
- Phase 3: Testing & Refinement
- Phase 4: Documentation & Presentation

Dates do not need to be exact, but planning is required.

Week 1: Set up the discord bot and research how to make a bot multiplayer/certain people can only see the bots output.
Week 2: Start coding the bot to run command !games and make games within the bot playable.
Week 3: Finish the code and play test.
Week 4: Make a presentation and make the bot have a clean UI and make it easy to play.
---

## 9. Risks, Constraints & Dependencies
Identify potential challenges.

Include:
- Technical risks
- Time constraints
- External dependencies (APIs, credentials, access)
- Mitigation strategies

Zarin and I both have Capstone as well as this so we will be juggling 2 big projects for the next 4 weeks along with our other classes. Finding time with all of this work and researching how to make a game through a discord bot may be challenging. A technical risk may be that the bot would rely solely on discord and if the school were to deny discord access that could scrap the whole project. A way we plan on mitigating our risks for time is to set aside specified amount of time and working a lot on the bot upfront to get as much work done as we can.

---

## 10. Security, Ethics & Safety Considerations
Address any relevant concerns, such as:
- Authentication and authorization
- Data sensitivity
- Network exposure
- Logging, monitoring, or automation impact
- Ethical considerations

A brief assessment of all of these is required, even if it is "N/A".

Our biggest consideration is to make the bot not spam the chat when someone plays it, this can be through a seperate discord chat tab and by making the bot only show to the people playing. Our bot will also only store the discord username along with the points they have no other information will be collected. Our bot permissions are limited to only what is necessary for commands. The logging is limited to basic bot activity and errors for debugging. The bot follows a privacy-first approach, minimizing data collection and avoiding sensitive information.

---

## 11. Team Structure (If Applicable)
If working in a group, describe:
- Team roles
- Communication plan
- Conflict resolution approach
- Workload distribution

Hayden: Researches, codes, proposes main ideas of bot, and is the Captain of the project.
Zarin: Researches, codes, proposes main ideas of bot, plays a major role in developing games for the bot.

---

## 12. Documentation & Knowledge Transfer Plan
Explain how this project will be documented.  Please note that this should include documentation in the UVDesk knowledgebase at the very least.  Programming projects should include readme.md files. 

Include:
- README or user documentation
- Deployment or maintenance guides
- How another student or administrator could continue the project

There will be a README document explaining how the bot works and a description of the !games command and what it does as well as how the games work. There will be a document on how to deploy the bot into the discord and a detailed list walking a person through the code. There will also be a document listing what we didn't want to implement, and if we think of other things, what we would've liked to implement.

---

## 13. Faculty/cpt.internal Resources Requested
List any required resources:
- VM access
- Network access
- Credentials or APIs
- Special permissions
- Hardware (if applicable)

Please be sure to consider any future tickets you may need to submit to complete this work as those will need to be generated and assigned to the appropriate groups as soon as feasibly possible once the project kicks off to ensure timely delivery.  I will step in to help where required but you will likely be working with students in other classes so please be cognizant of their time!

We will use GitHub a lot along with our VM's so we can share the code easily and work together accurately. A future ticket to consider could be improving the bot with any feedback from students in the future or adding a better version of the bot that includes other card like games.

---

## 14. Acknowledgement of Expectations
By submitting this proposal, I acknowledge that:
- This is a self-directed technical project
- I am responsible for research and troubleshooting
- Evaluation will consider process, documentation, and professionalism

**Signature (Name & Date):**

Student 1:  Hayden Allen               Date: 4/2/2026
Student 2:  Zarind Deane               Date: 4/2/2026


Instructor: ____________________________ Date: _______________
