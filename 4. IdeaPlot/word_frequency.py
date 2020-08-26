from wordcloud import WordCloud 
import matplotlib.pyplot as plt 
import csv 
  
file_ob = open("../3. TrendsToIdeas/words.csv") 
reader_ob = csv.reader(file_ob) 
reader_contents = list(reader_ob) 
text = "" 

for row in reader_contents : 
    for word in row : 
        text = text + " " + word 

wordcloud = WordCloud(width=1280, height=720, collocations=False, max_words=1000).generate(text) 
 
plt.figure(figsize=(19.2, 10.8)) 
plt.imshow(wordcloud, interpolation="bilinear") 
plt.axis("off") 
plt.margins(x=0, y=0) 
plt.show() 