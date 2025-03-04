import csv
import random

# Retrieve colours from csv file and put them in a list
file = open("Support data/00_colour_list_hex_v3.csv", "r")
all_colors = list(csv.reader(file, delimiter=","))
file.close()

# remove the first row
all_colors.pop(0)

round_colours = []
colour_scores = []

# loop until we have four colours with different scores
while len(round_colours) < 4:
    potential_colour = random.choice(all_colors)

    # Get the score and check its not a duplicate
    if potential_colour[1] not in colour_scores:
        round_colours.append(potential_colour)
        colour_scores.append(potential_colour[1])

print(round_colours)
print(colour_scores)

# find target score (median)

# change scores to integers
int_scores = [int(x) for x in colour_scores]
int_scores.sort()

median = (int_scores[1] + int_scores[2]) / 2