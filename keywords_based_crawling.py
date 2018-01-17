from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import csv
import codecs
import json
import utm


consumer_key = "oZK8zCkcmNRBgbtivbRnl5q3O"
consumer_secret = "A8ulIRmX0ZztQVC28DHMQFiwVMSGl6zEHrVJ0AaoXRJUlYqJxE"

access_token = "943403501580963840-EOxBj00doUVvq31GKI0fkC83NyXpCYq"
access_token_secret = "qVFa7IVb3IPeDKb6yWACjbXouxX8aXF2wJyL1W5cQAwrr"

class StdOutListener(StreamListener):


    def on_status(self, status):

        if status.place:

            if 'Amsterdam' in status.place.name:

                print('\033[93m' + status.place.name + ' : ' + status.text + '\033[0m')

                # tweet = json.loads(status)
                # print(tweet)
                # print(status[2:-1])

                # author_id = status.author.id

                save_data = [status.id, status.author.id, status.created_at, status.text.encode('utf-8')]

                with codecs.open('textfile_keywords_based.csv.txt', 'a', encoding='utf8') as f_l:
                    writer = csv.writer(f_l)
                    writer.writerow(save_data)

            else:
                print(status.place.name + ' : ' + status.text)
        else:
            print('Unknown place' + ' : ' + status.text)
            #save them into another file for further use

            save_data = [status.id, status.author.id, status.created_at, status.text.encode('utf-8')]
            with codecs.open('textfile_keywords_based_unknown_location.csv', 'a', encoding='utf8') as f:
                writer = csv.writer(f)
                writer.writerow(save_data)

            # myFile_un = open('textfile_keywords_based_unknown_location.csv', 'a')
            # try:
            #     # print(status)
            #     save_data = [status.id, status.created_at, status.text]
            #     # print(save_data)
            #     myFile_un.write(save_data)
            #     myFile_un.write('\n')  # adds a line between tweets




            # except:
            #     pass
            # f.close()


        def on_error(self, status):
            print (status)

            # f.close()
            return True


if __name__ == '__main__':
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, StdOutListener())
    #stream.sample()
    print("Start the job.")

    #customise keywords
    stream.filter(track=['vuurwerk','firework','fireworks'])
    # stream.filter(locations=[4.73, 52.27, 5.08, 52.43])
    print("Done")