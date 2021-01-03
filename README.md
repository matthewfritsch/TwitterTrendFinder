# Twitter Trend Finder

#### This project is intended to gather, analyze, and visualize frequencies and variances from the Twitter Trending page. Ideally, the results will be easy to understand for both data analysis fans and the layman.

##### Backstory: I'm a frequent Reddit user. One of my favorite subreddits is r/dataisbeautiful, where users frequently will post data from anything they find interesting. The data is posted in an aesthetically-pleasing image of graphs, animations, or other visual representations. My goal with this project was to gather data online, analyze the data, and visualize my findings programmatically using a set of libraries I have not used before. In thinking of ideas for this project, I realized Twitter has a "Trending" page; Every day, fifty new or recurring strings appear as trends on the website. Unfortunately the Twitter API does not allow for gathering of historical trend data. Instead, I found a different website that was free and with over four years of trends.

#### The next steps are to learn and use features of the following (either because I am required to, or because it will get the job done and I want to use that specific tool):
- [x] **datetime** for accessing all dates on the website (formatted as "https://website.com/YYYY-MM-DD") and passing the date to the scraper.
- [x] **selenium** for accessing the webpage and getting Trends
      (Yes, Selenium is absolutely overkill as a web scraper. Unfortunately, the website requires a button press to get the full set of data to load.)
- [x] **PYDAL** for storing each trend with its date and frequency. Also, PYDAL makes it easy to find if an entry contains a substring. This will be useful for finding if a topic repeats frequently. E.g: "#TrumpKillsUSPS" is trending as of today (2020/08/12), but perhaps "Trump" or "USPS" are substrings of other trends that occur frequently.
- [x] **matplotlib/numpy** for moving the database of trends and dates into legible data, and plotting it according to its relevant statistic.

	Things to plot:
	- [x] Frequency of a word (word cloud)
	- [x] How the use of hashtags has changed over time (line plot)
	- [x] Frequency of a trend (bar graph)
	- [x] Most popular day-of-the-week trends e.g 'ThrowbackThursday', etc. (multi-line plot)
	- [x] Top word frequencies and how recently they're used (multi-line plot)

**EDIT:** This project is, while greatly imperfect, considered complete. The execution of all aspects of this program is not ideal, but all desired topics were covered and implemented. There are many things I would change given the opportunity to work on this a second time, though the result is satisfying. I may add another plot or two in order to track relevant topics (current political/social topics).
