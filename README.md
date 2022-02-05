# AppleMusic2HTML
A simple python tool I made to convert songs from my apple music playlist. I'm not too experienced with python, or whatever the hell I just made, so the max is 100 songs. Not sure how I could get the page to load the rest of the songs as they load as you scroll to the bottom.

# Dependencies 
```
pip install beautifulsoup4
pip install youtube-search-python
```
# Usage
Using this tool is pretty easy, it takes a good amount of time to output to a file though.
Near the top of the file input your apple music playlist
```python
#get page and parse (set your own playlist url)

URL = "_your_apple_music_playlist_url_here"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
```
For example I'll use my playlist fjørd.
```python
#get page and parse (set your own playlist url)
URL = "https://music.apple.com/ca/playlist/fj%C3%B8rd/pl.u-d2b0vbVt4l6yMl"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
```
After you've input your playlist URL, you're ready to run the program. It will create a text file called songs.txt in the (parent?) directory.

### Example output:
![](https://i.imgur.com/MQa2QHA.png)

# Possible additions
I could try to figure out how to add more than 100 songs, and taking user input instead of editing it in the file is easy, but I'm lazy.