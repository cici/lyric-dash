# Lyrics Dashboard Requirements Document

## Introduction

1. Purpose
The purpose of the lyrics dashboard is to be able to visualize a variety of data using graphs regarding song lyrics.

2. References
  - [Dash](https://dash.plotly.com/) -- For the graphing dashboard
  - [Lyrics Genius](https://github.com/johnwmillr/LyricsGenius) -- For grabbing lyrics from songs
  - [Create a MultiPage Dash Application](https://towardsdatascience.com/create-a-multipage-dash-application-eceac464de91)

## Overall Description
1. Product Perspective
  - Audience
    - Anyone interested in music lyric data

2. Product Features
3. User Classes and Characteristics
4. Operating Environment
    - Python 3.6+
    - Dash Open Source for dashboard
    - FaunaDB
    - Heroku (or possibly Netlify if serverless)
5. Design and Implementation Constraints
    - MVP will be only a small subset of artists/songs
6. User Documentation
7. Assumptions and Dependencies
    - [Genius](https://www.genius.com) will be used to extract the song lyrics


## External Interface Requirements
1. User Inferfaces
These describe what the user interface must include. I do not like to put UI design elements in the requirements as those tend to change often, and are not "requirements". But, having the elements such as describing the menu of options for a user is good. The alarms, warnings, and operator messages should be included. Include how erroneous input will be handled as well.
2. Software Interfaces
These describe what external interfaces and connections must be supported by the software, and proved detail of what will be supported. Protocols should be referenced in the SRS but not part of the SRS. For example:  Software shall support the the serial protocol per specification XYZ.
3. Input and Output Requirements
These should define what data being input acceptable, including the type of data (numerical, alpha-numeric..) ranges, limits and defaults used, and associated data output. These also describe the data storage requirements and event logging requirements.

## Functional Requirements
These should define the features being provided by the software - what the software needs to accomplish.  These should be traceable to system requirements and market requirements. They are generally discussed between the stake-holders and the engineers. These should include "happy path" and error handling.
1. System Features
- Graphs to show:
  -- Word Count by Album
  -- Word Count change over years
  -- Word Cloud by Album
  -- Digrams by Album
  -- Sentiment by Album
  -- Relationship between emotion and album year of release
  -- Song Duration Over Time
2. Use Cases
3. ER Diagram
4. Data Dictionary

## Non-Functional Requirements
1. Performance
2. Scalability
3. Security
What is required of authentication, authorization, audit trails, data protection?

4. Maintainability
5. Usability
6. Auditing and Logging
7. Availability
