from datetime import datetime

from bottle import response
from twitter import Api
from json import dumps


CONSUMER_KEY = 'mQiyurSlNoOnpScDZhbvNZ4vK'
CONSUMER_SECRET = 'dfyzdoD7FrGhW7uXcyMX7g9NXgl7YE0Lygftkhgtzbo7SEcwqO'
ACCESS_TOKEN = '825848481126445056-9Dfryl1JkmugOoGhYpdSIC9k3ikvWGU'
ACCESS_TOKEN_SECRET = 'iA3IFfc8gQvwzdFfOgKUZQT1UfZBTp8a9UHCd1jG2fAoy'
twitter_image_link = 'https://g.twimg.com/about/feature-corporate/image/twitterbird_RGB.png'


def get_twits_list(request):
    request.content_type = 'application/json'
    request_id = request.json.get('requestId')
    version = request.json.get('version')
    queries = request.json.get('queries')
    period = request.json.get('period')
    queries_search = {}
    for word in queries:
        queries_search[word] = 'q=' + word.replace('#', '%23') + '%20'
        queries_search[word] += 'since%3A' + period['fromDate'] + '%20until%3A' + period['toDate'] + '&count=100'

    api = Api(consumer_key=CONSUMER_KEY,
              consumer_secret=CONSUMER_SECRET,
              access_token_key=ACCESS_TOKEN,
              access_token_secret=ACCESS_TOKEN_SECRET)
    tweets = {}
    rv = {
        'requestId': request_id,
        'version': version,
        'grabber': {
            'name': 'TwitterGrabber',
            'version': version,
            'authors': [
                {
                    'name': 'Иларионов Дмитрий',
                    'email': 'd.ilarionov@pflb.ru'
                }
            ],
            'source': {
                'title': 'Твиттер',
                'url': 'https://twitter.com',
                'logo': twitter_image_link
            }
        },
        'results': [
        ]
    }
    try:
        for word in queries:
            tweets[word] = api.GetSearch(raw_query=queries_search[word])
        response.body = return_result(rv, queries, tweets)
        return return_result(rv, queries, tweets)
    except Exception as e:
        response.body = return_error(rv, e)
        return return_error(rv, e)


def return_error(rv, error):
    rv['results'].append({'error': str(type(error))})
    print(dumps(rv, indent=4, sort_keys=False, ensure_ascii=False))
    f = open("error - " + datetime.strftime(datetime.now(), "%Y.%m.%d - %H.%M.%S") + ".txt", 'wb')
    f.write(dumps(rv, indent=4, sort_keys=False, ensure_ascii=False).encode("UTF-8"))
    f.close()
    return dumps(rv, indent=4, sort_keys=False, ensure_ascii=False)


def return_result(rv, queries, tweets):
    for word in queries:
        result = {'query': word}
        posts = []
        errors = []
        processing = {"start": datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%S")}
        for tweet in tweets[word]:
            try:
                tweet.retweeted_status.id
                continue
            except AttributeError:
                1
            try:
                media = tweet.media
                images = []
                for m in media:
                    images.append(str(m.media_url))
            except (AttributeError, TypeError):
                images = []
            originals = tweet.urls
            original = []
            for o in originals:
                original.append(o.url)
            posts.append(
                {
                    'url': 'http://twitter.com/' + tweet.user.screen_name + '/status/' + tweet.id_str,
                    'original': original,
                    'language': tweet.lang,
                    'title': tweet.text,
                    'popularity': tweet.favorite_count + 10 * tweet.retweet_count,
                    'image': images
                }
            )
        result['posts'] = posts
        result['errors'] = errors
        processing['finish'] = datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%S")
        result['processing'] = processing
        rv['results'].append(result)
    f = open("success - " + datetime.strftime(datetime.now(), "%Y.%m.%d - %H.%M.%S") + ".txt", 'wb')
    f.write(dumps(rv, indent=4, sort_keys=False, ensure_ascii=False).encode("UTF-8"))
    f.close()
    print(dumps(rv, indent=4, sort_keys=False, ensure_ascii=False))
    return dumps(rv, indent=4, sort_keys=False, ensure_ascii=False)
