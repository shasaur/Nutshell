import filepaths as FILES
# import matplotlib.pyplot as plt

#example = '"[{""text"":""TrumpTrain""},{""text"":""Trump""},{""text"":""Putin""}]",2016-11-01T00:00:00.000Z'

# If there were any hashtags
def tokens_to_hashtags(tweet):
    hashtags = []

    if len(tweet) > 1 and not tweet[0] == "[]":
        tweet[0] = tweet[0].replace('"[', '')
        tweet[len(tweet)-2] = tweet[len(tweet)-2].replace(']"', '')
        prefix = '{""text"":""'
        suffix = '""}'
        for e in range(len(tweet)-1):
            tweet[e] = tweet[e].replace(prefix, '')
            tweet[e] = tweet[e].replace(suffix, '')

            hashtags.append(tweet[e])

    return hashtags

def format_tweet(tweet):
    entries = tweet.split(',')

    dttm = entries[len(entries)-1] # datetime
    hashtags = tokens_to_hashtags(entries)

    return dttm, hashtags


def load_hashtags(filepath):
    data = []
    with open(FILES.get_filepath("nov-hashtags.data"), 'r') as file:

        ignore = 1
        for line in file:
            line = line.replace('\n', '')

            if ignore == 0:
                data.append((format_tweet(line)))
            else:
                ignore -= 1

    return data

hashtag_occurrences = load_hashtags("nov-hashtags.data")

hashtag_counts = {}
for h_o in hashtag_occurrences:

    # Hashtags
    for h in h_o[1]:
        print(h_o[1])
        if not h in hashtag_counts:
            hashtag_counts[h] = 1
        else:
            hashtag_counts[h] += 1

hashtag_count_distribution = []
with open(FILES.get_filepath("nov-hashtags-occurrences.data"), 'w') as file:
    for h_c in hashtag_counts.keys():
        file.write(h_c + ',' + str(hashtag_counts[h_c]) + '\n')
        hashtag_count_distribution.append(hashtag_counts[h_c])

# fig, ax = plt.subplots()
#
# ax.hist(hashtag_count_distribution)
#
# plt.show()