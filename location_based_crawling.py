from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import utm
import codecs
import csv



consumer_key = "oZK8zCkcmNRBgbtivbRnl5q3O"
consumer_secret = "A8ulIRmX0ZztQVC28DHMQFiwVMSGl6zEHrVJ0AaoXRJUlYqJxE"

access_token = "943403501580963840-EOxBj00doUVvq31GKI0fkC83NyXpCYq"
access_token_secret = "qVFa7IVb3IPeDKb6yWACjbXouxX8aXF2wJyL1W5cQAwrr"

class StdOutListener(StreamListener):

    def on_status(self, status):

        # all keywords should be in lowercase
        keywords = ['vuurwerk', 'firework', 'fireworks', 'vuruwerk', 'vuuwerk']

        text = status.text.lower()
        if any(word in text for word in keywords):

        # if 'vuurwerk' in status.text.lower():

            print('\033[93m' + status.place.name + ' : ' + status.text + '\033[0m')
            # tweet = json.loads(status)
            # print(tweet)
            #
            # myFile = open('textfile_location_based.csv','a')
            #
            # try:
            #
            #     # texts = json_load['text']
            #     # texts=json_load['user']['location']
            #     # texts=json_load['user']['profile_image_url']
            #     # texts = tweet['user']['description']
            #     # coded = texts.encode('utf-8')
            #     # s = str(coded)
            #     print(status[2:-1])
            #     myFile.write(status[2:-1])
            #     myFile.write('\n')  # adds a line between tweets
            # except:
            # pass

            save_data = [status.id, status.author.id, status.created_at, status.text.encode('utf-8')]

            with codecs.open('textfile_location_based.csv.txt', 'a', encoding='utf8') as f:
                writer = csv.writer(f)
                writer.writerow(save_data)



        else:
            print(status.place.name + ' : ' + status.text)

        def on_error(self, status):
            print (status)

            myFile.close()
            return True

if __name__ == '__main__':
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, StdOutListener())
    #stream.sample()
    print("Start the job.")
    # stream.filter(track=['vuurwerk'])
    stream.filter(locations=[4.73, 52.27, 5.08, 52.43])
    print("Done")