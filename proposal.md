# GOAL
to make a URL shortening tool, similar to bit.ly

# Parts of the whole
things that will be needed to deploy this project in a working fashion

## Backend
Store links in a relational database, likely sql. Match a full link with a shortened link.
When a request is made with the shortened link, see if it exists in the database, if so, redirect to the full URL

## Frontend (?) 
Create an HTML Webpage where users can create these shortened links by entering the full link, and choosing a name for the shortened link
