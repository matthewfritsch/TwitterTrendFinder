echo "Expect this to take about six hours. Good luck. If it fails at any point, please add as an issue on https://github.com/matthewfritsch/TwitterTrendFinder, and expect a response in <1 day."
cd 1.\ GetTrends/
python3 trendFinder.py
cd ..
cp 1.\ GetTrends/runningTrends.txt 2.\ SortTrends/runningTrends.txt
cd 2.\ SortTrends/
python3 trendSorter.py
cd ..
cd 3.\ TrendsToIdeas/
python3 trendBreaker.py
python3 wordsToCSV.py
cd ..
cp 3.\ TrendsToIdeas/words.csv 4.\ IdeaPlot/words.csv
python3 word_frequency.py && python3 hashtags.py && python3 trendfreq.py && python3 dotwTrends.py && python3 wordFreqByDate.py
echo "All done!"