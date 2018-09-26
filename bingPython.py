import webbrowser
import time



url = ["Microsoft","Playstation","Xbox","Apple","Nintendo","Star Trek","Star Wars","Overwatch", "Disney","marvel","for+you", "top+stories", "Northeast", "South", "Midwest", "West", "World", "Africa", "Asia", "Americas", "Asia Pacific", "Europe", "Middle East", "Movies+TV", "Music", "Technology", "Science", "Business", "Politics", "Fact Check", "Health", "Products", "Auto", "Fashion"]

# # google = raw_input('Google search:')
for parameters in url:
    webbrowser.open('https://www.bing.com/news/search?q={}'.format(parameters))
    time.sleep(5)   # Delays for 5 seconds. You can also use a float value.
    # webbrowser.close()

webbrowser.open('https://account.microsoft.com/rewards/')

