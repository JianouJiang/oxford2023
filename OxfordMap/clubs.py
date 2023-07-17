from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.patches import Rectangle
import numpy as np
from PIL import Image

# Read the whole text.
with open('clubs.txt', 'r') as f:
    text = f.read()

# Define a set of stopwords
stopwords = set(STOPWORDS)
stopwords.update(["OXFORD", "UNIVERSITY", "SOCIETY", "OXFORD UNIVERSITY", "CLUB", "STUDENT", "SOC", "ASSOCIATION"])

# Generate a word cloud image
wordcloud = WordCloud(stopwords=stopwords, background_color='white').generate(text)

# Get the word cloud image as an array
image = wordcloud.to_array()

# Convert the image array to PIL Image
pil_image = Image.fromarray(np.uint8(image))

# Crop the image to remove white regions
pil_image = pil_image.crop(pil_image.getbbox())

# Convert back to numpy array
image = np.array(pil_image)

# Display the generated image with matplotlib
plt.imshow(image, interpolation='bilinear', aspect='auto')
plt.axis("off")
plt.savefig("clubs_word_cloud.png")
plt.show()



clubs = {
    'Academic': ['Anthropology Society', 'Classics Society', 'Cortex Club', 'Oxford University Biological Society', 'Oxford University Physics Society', 'Oxford Future Technology Medical Society', 'Oxford University Nature Conservation Society', 'Oxford Women in Computer Science', 'University of Oxford Nanotechnology Society'],
    'Cultural': ['American Society', 'Asia Soc', 'Oxford African and Caribbean Society', 'Oxford Chinese Students and Scholars Association', 'Oxford University Italian Society', 'Oxford Hispanic Society', 'Oxford Hungarian Society', 'Oxford India Society', 'Oxford Iraq Society', 'Oxford Mixed Heritage Society', 'Oxford Persian/Iranian Society', 'Oxford Philippines Society', 'Oxford Scandinavian Society', 'Oxford Scottish Society', 'Oxford South Asian Society', 'Oxford Tatar Society', 'Oxford University Africa Society', 'Oxford University Chinese Society OUCS', 'Oxford University Hindu Society', 'Oxford University Hong Kong Society', 'Oxford University Iranian Society', 'Oxford University Japan Society', 'Oxford University Malaysia Club', 'Oxford University Turkish Society'],
    'Social Causes': ['Effective Altruism Oxford', 'Disarm Oxford', 'Oxford Climate Society', 'Oxford Coalition Against Homelessness', 'Oxford Climate Justice Campaign', 'Oxford Human Rights Student Society', 'Oxford Women of Colour Society (WOC SOC)'],
    'Arts & Entertainment': ['Alternative Music Society', 'Oxford University Dance Society', 'Oxford University Jazz Society', 'Oxford University Film Foundation', 'Oxford University Art Club', 'Oxford University Gilbert and Sullivan Society [OUGSS]', 'Oxford University Music Society', 'Oxford University Society of Change Ringers', 'Oxford University Symphonic Band', 'The Oxford Gargoyles', 'The Oxford Recording Society', 'The Oxford University Salsa Society', 'The Society of Oxford Ukulele Players'],
    'Sports': ['Gymnastics Club', 'Handball', 'Karate-Do Shotokai', 'Oxford University Basketball Club (OUBBC)', 'Oxford University Canoe and Kayak Club', 'Oxford University Gliding Club', 'Oxford University Racing', 'Oxford University Taekwondo'],
    'Career': ['180 Degrees Consulting Oxford', 'Founders Society', 'Oxford Entrepreneurs', 'Oxford Law Society', 'Oxford Women in Business', 'Oxford University Advertising Society', 'Oxford University Alternative Dispute Resolution Society', 'Oxford University Bar Society', 'Oxford University Medico-Legal Society', 'Oxford Women* in Law Society (OWLSS)'],
    'Religious & Spiritual': ['Chosen Christian Fellowship', 'Ismaili Muslim Students\' Society', 'Oxford University Islamic Society', 'Oxford University Ahlulbayt Islamic Society', 'Oxford University Inter-Collegiate Christian Union'],
    'Membership': ['Oxford University Postgraduate Society'],
    'Music': ['Oxford Belles', 'Oxford Singers', 'Oxford University Jazz Orchestra - OUJO', 'Oxford University Ceilidh Band', 'Rocksoc', 'Sing Inside'],
    'Social': ['Oxford Character Project', 'Oxford Origami Society', 'Oxford University Tea Appreciation Society'],
    'Discussion': ['Oxford University Philosophy Society', 'Oxford Public Philosophy', 'Oxford Socratic Society'],
    'Gaming': ['Oxford Pokémon Society', 'Oxford Trading Card Game', 'Oxford University Chess Club', 'Oxford University Contract Bridge Association', 'Oxford University Go Society'],
    'Faith': ['Graduate Christian Forum', 'Oxford University Inter-Collegiate Christian Union'],
    'Dance': ['Oxford University Dance Society', 'The Oxford University Salsa Society'],
    'Political': ['Oxford University Conservative Association', 'Oxford University Liberal Democrats', 'Oxford University Marxists'],
    'Campaigning': ['Disarm Oxford', 'Oxford Climate Justice Campaign', 'Oxford Coalition Against Homelessness'],
    'Volunteering': ['Jacari Society', 'Make a Smile Charity', 'Oxford Coalition Against Homelessness', 'Oxford Trees for the Future'],
    'Sport': ['Gymnastics Club', 'Handball', 'Karate-Do Shotokai', 'Oxford University Basketball Club (OUBBC)', 'Oxford University Canoe and Kayak Club', 'Oxford University Gliding Club', 'Oxford University Racing', 'Oxford University Taekwondo'],
    'Fandom': ['Oxford Doctor Who Society', 'Oxford Harry Potter Society', 'Oxford Star Trek Society'],
    'Media': ['Industry Magazine', 'Oxford Media Society', 'The Oxford Blue Newspaper', 'The Quince Magazine'],
    'Performance': ['Arcadian Singers of Oxford', 'Oxford University Gilbert and Sullivan Society [OUGSS]', 'Oxford University Music Society', 'Oxford University Society of Change Ringers', 'Oxford University Symphonic Band', 'The Oxford Gargoyles', 'The Oxford Imps', 'The Oxford Recording Society'],
    'Health': ['Oxford Global Health and Care Systems Society', 'Oxford Nutritank Society'],
    'Not categorised': ['00Productions Society', 'Baking Society', 'Human Sciences Society', 'OAS', 'Oxford Character Project', 'Oxford Future Technology Medical Society', 'Oxford Human Rights Student Society', 'Oxford Textiles Society', 'Oxram', 'The Queen\'s College Ball 2022'],
    'Travel': ['GoToCo', 'Varsity Trip']
}


club_counts = {category: len(clubs) for category, clubs in clubs.items()}


# Create bar chart
# Create the bar chart
fig, ax = plt.subplots()
# Load the background image
background_image = mpimg.imread('clubs_word_cloud2.png')

# Plot the background image
ax.imshow(background_image, extent=[-0.5, len(club_counts)-0.5, 0, max(club_counts.values())], aspect='auto')

# Plot the bars on top of the background image
ax.bar(club_counts.keys(), club_counts.values())

# Remove the x-axis ticks and labels
ax.set_xticks([])
ax.set_xticklabels([])

# Set the x-axis labels
ax.set_xticks(np.arange(len(club_counts)))
ax.set_xticklabels(club_counts.keys(), rotation=40, fontsize='small', ha='right')

        
# Remove the y-axis ticks
ax.tick_params(axis='y', left=False)

# Set the y-axis label
ax.set_ylabel('Number of Clubs')

# Set the title
ax.set_title('Number of Clubs in Each Category at University of Oxford')

# Set the aspect ratio to 'auto' for the final plot
ax.set_aspect('auto')



# Save the figure with adjusted padding
plt.savefig("clubs_count.png", bbox_inches='tight', pad_inches=0.5)



# Show the plot
plt.show()

