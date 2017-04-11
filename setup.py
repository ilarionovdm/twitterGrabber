from distutils.core import setup

setup(
    name='twitterGrabber',
    version='',
    packages=[''],
    url='',
    license='',
    author='D. Ilarionov',
    author_email='d.ilarionov@pflb.ru',
    description='twitterGrabber', requires=['bottle', 'python-twitter', 'twitter']
)

#{  	"requestId": 13, 	"version": 1, 	"queries": [ 		"selenium", 		"#testautomation"     ], 	"period": {     	"fromDate": "2017-03-01", 		"toDate": "2017-03-09"     } }

# ПРИМЕР ТВИТА
#
# {
#     "created_at": "Tue Jan 31 12:01:25 +0000 2017",
#     "hashtags": [
#         {
#             "text": "istqbyfabuytyepyfzdtim"
#         }
#     ],
#     "id": 826399989505126400,
#     "id_str": "826399989505126400",
#     "lang": "en",
#     "media": [
#         {
#             "display_url": "pic.twitter.com/I8iWVJDSgg",
#             "expanded_url": "https://twitter.com/ilarionovdm/status/826399989505126400/photo/1",
#             "id": 826399745232998400,
#             "media_url": "http://pbs.twimg.com/media/C3f2MJkWEAAyYJW.jpg",
#             "media_url_https": "https://pbs.twimg.com/media/C3f2MJkWEAAyYJW.jpg",
#             "sizes": {
#                 "large": {
#                     "h": 1080,
#                     "resize": "fit",
#                     "w": 1920
#                 },
#                 "medium": {
#                     "h": 675,
#                     "resize": "fit",
#                     "w": 1200
#                 },
#                 "small": {
#                     "h": 383,
#                     "resize": "fit",
#                     "w": 680
#                 },
#                 "thumb": {
#                     "h": 150,
#                     "resize": "crop",
#                     "w": 150
#                 }
#             },
#             "type": "photo",
#             "url": "https://t.co/I8iWVJDSgg"
#         }
#     ],
#     "source": "<a href=\"http://twitter.com\" rel=\"nofollow\">Twitter Web Client</a>",
#     "text": "#istqbyfabuytyepyfzdtim\n\nwe enjoy typing https://t.co/I8iWVJDSgg",
#     "urls": [
#
#     ],
#     "user": {
#         "created_at": "Sun Jan 29 23:29:56 +0000 2017",
#         "default_profile": true,
#         "default_profile_image": true,
#         "friends_count": 2,
#         "id": 825848481126445056,
#         "lang": "ru",
#         "name": "\u0414\u043c\u0438\u0442\u0440\u0438\u0439 \u0418\u043b\u0430\u0440\u0438\u043e\u043d\u043e\u0432",
#         "profile_background_color": "F5F8FA",
#         "profile_image_url": "http://abs.twimg.com/sticky/default_profile_images/default_profile_0_normal.png",
#         "profile_link_color": "1DA1F2",
#         "profile_sidebar_fill_color": "DDEEF6",
#         "profile_text_color": "333333",
#         "screen_name": "ilarionovdm",
#         "statuses_count": 2
#     },
#     "user_mentions": [
#
#     ]
# }

# ПРИМЕР РЕТВИТА
# {
#     "created_at": "Tue Feb 07 23:57:00 +0000 2017",
#     "hashtags": [
#         {"text": "Art"},
#         {"text": "artworker"},
#         {"text": "Artwork"},
#         {"text": "design"},
#         {"text": "cowboybebop"},
#         {"text": "anime"}
#     ],
#     "id": 829116784460566528,
#     "id_str": "829116784460566528",
#     "lang": "en",
#     "retweet_count": 1,
#     "retweeted_status": {
#         "created_at": "Mon Feb 06 00:48:43 +0000 2017",
#         "favorite_count": 1,
#         "hashtags": [
#             {"text": "Art"},
#             {"text": "artworker"},
#             {"text": "Artwork"},
#             {"text": "design"},
#             {"text": "cowboybebop"}
#         ],
#         "id": 828405023897960449,
#         "id_str": "828405023897960449",
#         "lang": "en",
#         "retweet_count": 1,
#         "source": "<a href=\"http://twitter.com\" rel=\"nofollow\">Twitter Web Client</a>",
#         "text": "Ed - Cowboy Bebop Sticker:  https://t.co/Kfy5mMYIUa via @redbubble #Art #artworker #Artwork #design #cowboybebop\u2026 https://t.co/wmHeTH3OBM",
#         "truncated": true,
#         "urls": [
#             {"expanded_url": "http://www.redbubble.com/people/jamiegothard/works/24164911-ed-cowboy-bebop?p=sticker", "url": "https://t.co/Kfy5mMYIUa"},
#             {"expanded_url": "https://twitter.com/i/web/status/828405023897960449", "url": "https://t.co/wmHeTH3OBM"}
#         ],
#         "user": {
#             "created_at": "Sat Jun 25 16:54:25 +0000 2011",
#             "description": "Freelance Artworker\n\nCommissions: Jamiegothard@hotmail.com",
#             "favourites_count": 557,
#             "followers_count": 17387,
#             "friends_count": 17894,
#             "id": 323906506,
#             "lang": "en",
#             "listed_count": 159,
#             "location": "England",
#             "name": "Jamie Gothard",
#             "profile_background_color": "131516",
#             "profile_background_image_url": "http://abs.twimg.com/images/themes/theme14/bg.gif",
#             "profile_background_tile": true,
#             "profile_banner_url": "https://pbs.twimg.com/profile_banners/323906506/1479055563",
#             "profile_image_url": "http://pbs.twimg.com/profile_images/802682943890161664/LB9XpqYJ_normal.jpg",
#             "profile_link_color": "4A913C", "profile_sidebar_fill_color": "EFEFEF",
#             "profile_text_color": "333333",
#             "screen_name": "JamieGothard",
#             "statuses_count": 5243,
#             "time_zone": "Casablanca",
#             "url": "http://t.co/BCtI1vNynm"
#         },
#         "user_mentions": [
#             {"id": 15276618, "name": "Redbubble", "screen_name": "redbubble"}]
#     },
#     "source": "<a href=\"http://www.twitter.com\" rel=\"nofollow\">Twitter for Windows</a>",
#     "text": "RT @JamieGothard: Ed - Cowboy Bebop Sticker:  https://t.co/Kfy5mMYIUa via @redbubble #Art #artworker #Artwork #design #cowboybebop #anime #\u2026",
#     "urls": [
#         {"expanded_url": "http://www.redbubble.com/people/jamiegothard/works/24164911-ed-cowboy-bebop?p=sticker", "url": "https://t.co/Kfy5mMYIUa"}
#     ],
#     "user": {
#         "created_at": "Sat Jun 25 16:54:25 +0000 2011",
#         "description": "Freelance Artworker\n\nCommissions: Jamiegothard@hotmail.com",
#         "favourites_count": 557, "followers_count": 17387,
#         "friends_count": 17894, "id": 323906506,
#         "lang": "en", "listed_count": 159,
#         "location": "England",
#         "name": "Jamie Gothard",
#         "profile_background_color": "131516",
#         "profile_background_image_url": "http://abs.twimg.com/images/themes/theme14/bg.gif",
#         "profile_background_tile": true,
#         "profile_banner_url": "https://pbs.twimg.com/profile_banners/323906506/1479055563",
#         "profile_image_url": "http://pbs.twimg.com/profile_images/802682943890161664/LB9XpqYJ_normal.jpg",
#         "profile_link_color": "4A913C",
#         "profile_sidebar_fill_color": "EFEFEF",
#         "profile_text_color": "333333",
#         "screen_name": "JamieGothard",
#         "statuses_count": 5243,
#         "time_zone": "Casablanca",
#         "url": "http://t.co/BCtI1vNynm"},
#     "user_mentions": [
#         {"id": 323906506, "name": "Jamie Gothard", "screen_name": "JamieGothard"},
#         {"id": 15276618, "name": "Redbubble", "screen_name": "redbubble"}
#     ]
# }


# {
#     "created_at": "Tue Feb 07 20:12:35 +0000 2017",
#     "favorite_count": 6,
#     "hashtags": [
#         {"text": "kagome"}, {"text": "art"}, {"text": "anime"}, {"text": "artwork"}, {"text": "drawing"}, {"text": "csp"}
#     ], "id": 829060308463394816,
#     "id_str": "829060308463394816",
#     "lang": "en",
#     "retweet_count": 2,
#     "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>", "text": "Despite difficulties it is now almost finished :) @DempseyRollBoy #kagome #art #anime #artwork #drawing #csp\u2026 https://t.co/Tb5XaZdztt", "truncated": true, "urls": [{"expanded_url": "https://twitter.com/i/web/status/829060308463394816", "url": "https://t.co/Tb5XaZdztt"}], "user": {"created_at": "Sun Sep 18 12:28:03 +0000 2016", "description": "Manga Artist from Germany \u0298\u0325\ua03e\u0298\u0325 \nhttps://t.co/MrWGD0c9QQ", "favourites_count": 423, "followers_count": 39, "friends_count": 107, "id": 777484326028083204, "lang": "de", "listed_count": 2, "location": "Hamburg, Deutschland", "name": "Summer McAllen", "profile_background_color": "000000", "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png", "profile_banner_url": "https://pbs.twimg.com/profile_banners/777484326028083204/1474201913", "profile_image_url": "http://pbs.twimg.com/profile_images/777485123642064896/SKj1n_af_normal.jpg", "profile_link_color": "7FDBB6", "profile_sidebar_fill_color": "000000", "profile_text_color": "000000", "screen_name": "summer_mcallen", "statuses_count": 101}, "user_mentions": [{"id": 702339066507841536, "name": "Kami-Sama \u4ef2\u9593", "screen_name": "DempseyRollBoy"}]}

# {
#     "created_at": "Tue Feb 07 22:44:04 +0000 2017",
#     "favorite_count": 7,
#     "hashtags": [
#         {"text": "PantyVigilante"}, {"text": "art"}, {"text": "illustration"}, {"text": "comic"}, {"text": "comics"}, {"text": "webcomic"}, {"text": "webcomics"}, {"text": "painting"}, {"text": "watercolor"}, {"text": "ink"}
#     ],
#     "id": 829098430635114501,
#     "id_str": "829098430635114501",
#     "lang": "en",
#     "retweet_count": 4,
#     "source": "<a href=\"http://twitter.com\" rel=\"nofollow\">Twitter Web Client</a>",
#     "text": "Finished! &lt;3\n\n#PantyVigilante #art #illustration #comic #comics #webcomic #webcomics #painting #watercolor #ink\u2026 https://t.co/Hl4nNSFMpJ",
#     "truncated": true,
#     "urls": [
#         {"expanded_url": "https://twitter.com/i/web/status/829098430635114501",
#          "url": "https://t.co/Hl4nNSFMpJ"}
#     ],
#     "user": {
#         "created_at": "Sun Dec 21 20:49:49 +0000 2008",
#         "description": "Comic Artist. Illustrator. Shameless trollop. I write and draw a webcomic called Panty Vigilante.\n\nSupport my work: https://t.co/KPCXZnXuLV",
#         "favourites_count": 1163,
#         "followers_count": 5327,
#         "friends_count": 3246,
#         "geo_enabled": true,
#         "id": 18292632,
#         "lang": "en",
#         "listed_count": 108,
#         "location": "Kansas City, MO",
#         "name": "Erica Batton",
#         "profile_background_color": "0099B9",
#         "profile_background_image_url": "http://abs.twimg.com/images/themes/theme4/bg.gif",
#         "profile_banner_url": "https://pbs.twimg.com/profile_banners/18292632/1486503180",
#         "profile_image_url": "http://pbs.twimg.com/profile_images/823658358326427649/3GSIa5ST_normal.jpg",
#         "profile_link_color": "0099B9",
#         "profile_sidebar_fill_color": "95E8EC",
#         "profile_text_color": "3C3940",
#         "screen_name": "erica_prime", "statuses_count": 3154,
#         "time_zone": "Central Time (US & Canada)",
#         "url": "https://t.co/IiqjBIiS8P", "utc_offset": -21600},
#     "user_mentions": [
#
#     ]
# }
