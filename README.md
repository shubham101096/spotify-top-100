# spotify-top-100
This python program is used to create Spotify playlist of the top 100 songs that were on Billboard chart on a date entered by user. For example, we can send our friend the playlist of the songs that were popular on the day we met.
The user enters the date of his choice. The names of top 100 songs of that date are fetched from https://www.billboard.com/charts/hot-100/{date} using Beautiful Soup for web scraping.
Then these songs are searched on Spotify and a playlist is created by using the Spotify Api. The link of the playlist is returned to the user.

![alt text](https://github.com/shubham101096/spotify-top-100/blob/master/screenshots/playlist-link.png)
