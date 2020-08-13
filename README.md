# Twitter Trend Finder
#### I'm a frequent Reddit user. One of my favorite subreddits is r/dataisbeautiful, where users frequently will post data from anything they find interesting. The data is posted in an (often aesthetically-pleasing) image of graphs, an animation, or another visual representation. I want to try my hand at a project like this, mostly because it involves getting information from a website (or group of websites) and representing the information in a compelling way.

#### I have used Twitter (in a social media way) for less than an hour to date. I made myself a personal account in 2017, followed lots of familiar names, and immediately turned off the notifications. In 2019, after the billionth email update from Twitter, I deactivated my account. However, in thinking of ideas for this project, I realized Twitter has a "Trending" feature. Every day, fifty new or recurring strings appear as trends on the website. I made a Twitter developer account to access their API, and was disappointed to find that they do not publicly allow access to historical trends. I looked on many different websites for options. I found exactly one that was free and with more than one year of trends. 

#### The next steps are to learn and use features of the following (either because I am required to, or because it will get the job done and I want to use that specific tool):
- [ ] **datetime** for accessing all dates on the website (formatted as "https://website.com/YYYY-MM-DD") and passing the date to the scraper.
- [ ] **selenium** for accessing the webpage and getting Trends
      (Yes, Selenium is absolutely overkill as a web scraper. Unfortunately, the website requires a button press to get the full set of data to load.)
- [ ] **PYDAL** for storing each trend with its date and frequency. Also, PYDAL makes it easy to find if an entry contains a substring. This will be useful for finding if a topic repeats frequently. E.g: "#TrumpKillsUSPS" is trending as of today (2020/08/12), but perhaps "Trump" or "USPS" are substrings of other trends that occur frequently.
- [ ] **numpy** and/or a library to visualize the data gathered. As I have never used numpy, I'm unfamiliar with if it does any kind of graphical representation of data. Will update as necessary.

Note: The website being used to gather trends has two ordered lists of trends. The first is visible before the button press, and the second is not.
