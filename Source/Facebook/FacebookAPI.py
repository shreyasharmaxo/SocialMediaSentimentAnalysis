import requests
import json

'''
Class for creating and managing Facebook API
'''


class FacebookAPI(object):

    def __init__(self):
        self.access_token = 'EAAf78o62tCsBAOyBA0Uv37IphzgMjvBUT2dUapa9I73svLgDN9CZA3c5HpBFdGNcKaLr1CHIjOYgUlZCV2HLorHY1MKpAdNTleC2omIvQubSASZCIL8KmpcJfVb6UiygQ1ov8i30beN4YM5VGvBLB5WC2qIPU7k69xBJHa5cgUkPiz8RgXfZB3XAkx31IZBx244ZBktGPrRQZDZD'
        self.user_id = '2652154258191504'
        self.post_id = '2330822763657990'
        self.url = 'https://graph.facebook.com/v3.2/{}_{}/comments?summary=1&filter=stream'.format(self.user_id, self.post_id)

    def fetch_comments(self):
        query_comments = []
        r = requests.get(self.url, params={'access_token': self.access_token})

        while True:
            data = r.json()

            if 'error' in data:
                raise Exception(data['error']['message'])

            for comment in data['data']:
                query_comments.append(comment['message'])

            if 'paging' in data and 'next' in data['paging']:
                r = requests.get(data['paging']['next'])
            else:
                break

        return query_comments

    def fetch_fake_data(self):
        with open("../../Data/FacebookData/election.json", "r", encoding='utf8', errors='ignore') as json_file:
            data = json.load(json_file)
            print(data)

