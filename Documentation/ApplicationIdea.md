# Factorio Benchmark

## Factorio

Factorio is a video game where you can design blueprints of factories. Each blueprint can be measured in terms of production speed, electricity used, materials, etc.

## Idea

Create a web application that allows users to upload their blueprints from Factorio. The website should be similar to [LeetCode](https://leetcode.com/), but instead of uploading code, users will upload their blueprints.

### Login

Each user will create an account using a unique email, unique username and a password. Users will sign in with (email + password) or (username + password). Users should be allowed to change their password via their email.

Each account also has a profile picture and a description. The users can edit their personal information at any time.

### Scenarios

Similar to how LeetCode has a wide variety of **problems** that users can solve, this site needs to have many **Scenarios**. The users will submit their solution (a blueprint string) to different Scenarios and get ranked based on different criteria.

### Submissions

A **submission** is a blueprint string along with a description document (text + images). The website should automatically evaluate the performance of a submission based on the following criteria:

1. Production speed
2. Cost of materials
3. Electricity consumption
4. Surface area
5. Research stage

More criteria could be added in the future.

### Comments

Each scenario and each submission have a comment section.

## How are the blueprints evaluated

A live version of Factorio will be running and evaluating the blueprints.

## Possible future requirements

* Factorio Mods should be supported
* The latest version of Factorio should always be supported
