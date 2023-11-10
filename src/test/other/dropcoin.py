import asyncio
import sys
import httpx
from loguru import logger

g_success, g_fail = 0, 0

logger.remove()
logger.add(sys.stdout, colorize=True, format="<w>{time:HH:mm:ss:SSS}</w> | <r>{extra[fail]}</r>-<g>{extra[success]}</g> | <level>{message}</level>")
logger = logger.patch(lambda record: record["extra"].update(fail=g_fail, success=g_success))


class DropCoin:
    def __init__(self, auth_token, wallet, referral, agent_ip):
        self.http = httpx.AsyncClient(verify=False, proxies=f'http://{agent_ip}')
        self.Twitter = httpx.AsyncClient(verify=False, proxies=f'http://{agent_ip}')
        self.Twitter.headers = {
            'Accept-Language': 'en-US,en;q=0.8',
            'Authority': 'twitter.com',
            'Origin': 'https://twitter.com',
            'Referer': 'https://twitter.com/',
            'Sec-Ch-Ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': "Windows",
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Gpc': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',

        }
        self.Twitter.cookies.update({'auth_token': auth_token})
        self.oauth_token, self.authenticity_token, self.oauth_verifier, self.token, self.tw_user_id = None, None, None, None, None
        self.wallet, self.referral = wallet, referral

    async def get_points(self):
        try:
            response = await self.http.get('https://dropcoin.online/auth/profile',timeout=20)
            if 'points_amount' in response.text:
                logger.success(f"总分：{response.json()['points_amount']}")
                logger.success(f"邀请分：{response.json()['referrals_amount']}")
                return True
            logger.error(f'{self.wallet} 获取分数失败')
            return False
        except Exception as e:
            logger.error(e)
            return False

    async def get_twitter(self):
        try:
            response = await self.http.post('https://dropcoin.online/auth/twitter',timeout=20)
            if 'oauth_token' in response.text:
                self.oauth_token = response.json()['result']
                self.oauth_token = self.oauth_token.split('=')[-1].strip()
                return True
            logger.error(f'{self.wallet} 获取oauth_token失败')
            return False
        except Exception as e:
            logger.error(e)
            return False

    async def get_twitter_token(self):
        try:
            if not await self.get_twitter():
                return False
            response = await self.Twitter.get(f'https://api.twitter.com/oauth/authorize?oauth_token={self.oauth_token}',timeout=20)
            if 'authenticity_token' in response.text:
                self.authenticity_token = response.text.split('authenticity_token" value="')[1].split('"')[0]
                return True
            logger.error(f'{self.wallet} 获取authenticity_token失败')
            return False
        except Exception as e:
            logger.error(e)
            return False

    async def twitter_authorize(self):
        try:
            if not await self.get_twitter_token():
                return False
            data = {
                'authenticity_token': self.authenticity_token,
                'redirect_after_login': f'https://api.twitter.com/oauth/authorize?oauth_token={self.oauth_token}',
                'oauth_token': self.oauth_token
            }
            response = await self.Twitter.post('https://api.twitter.com/oauth/authorize', data=data,timeout=20)
            if 'oauth_verifier' in response.text:
                self.oauth_verifier = response.text.split('oauth_verifier=')[1].split('"')[0]
                return True
            logger.error(f'{self.wallet} 获取oauth_verifier失败')
            return False
        except Exception as e:
            logger.error(e)
            return False

    async def twitter_login(self):
        try:
            if not await self.twitter_authorize():
                return False
            response = await self.http.get(f'https://dropcoin.online/auth/twitter?oauth_token={self.oauth_token}&oauth_verifier={self.oauth_verifier}',timeout=40)
            if 'token' in response.text:
                self.token = response.json()['token']
                self.http.headers.update({'Authorization': f'Token {self.token}'})
                return True
            logger.error(f'{self.wallet} 登录失败')
            return False
        except Exception as e:
            logger.error(e)
            return False

    # Stop%20fighting%20for%201%25%20of%20supply%20while%20devs%20and%20infls%20take%20everything.%0A%0AIn%20%40DropCoinEth%2C%20things%20are%20done%20differently%3A%0A%0A🟨%2050%25%3A%20airdrop%20for%20free%20social%20tasks.%0A%0ANow%20is%20the%20time%20when%20everyone%20can%20make%20it.%0A%0ALet%27s%20farm%20%24DROP%20together%3A%20www.dropcoin.club%2Ffarming%0A%0Ahttps%3A%2F%2Ftwitter.com%2FDropCoinEth%2Fstatus%2F1720847819450310896


    async def create_twitter(self):
        tweet_text = "Stop fighting for 1% of supply while devs and infls take everything.\n\nIn @DropCoinEth, things are done differently:\n\n🟨 50%: airdrop for free social tasks.\n\nNow is the time when everyone can make it.\n\nLet's farm $DROP together: www.dropcoin.club/farming\n\nhttps://twitter.com/DropCoinEth/status/1720847819450310896 "
        variables = {
            'tweet_text': tweet_text,
            'dark_request': False,
            'media': {
                'media_entities': [],
                'possibly_sensitive': False,
            },
            'semantic_annotation_ids': [],
        }
        cookies = self.Twitter.cookies
        # guest_id=v1:169115932809926709;
        # kdt=XWUfyqycgOLZKzs8RoHVZ5e8q3vMSdASMdRsrDcP;
        # auth_token=d694c51d4ca494ab31bb8c0c18441f6ec2b8c372;
        # ct0=4fd4580ac269f766e4cb9011c704df2d20b7e9e1d6cc483e31cbd2dcf0e82ad0ec838ca809f353b7aafc4ec9ae6b82378d0fedf2bd3e95b9787342c1a3baf381806f42c358921a8f4cc47614c88b381f;
        # att=1-iDQsGqBobzHRJyRh9bCGcwhG5BgrWruw7sFVnR0K;
        # twid=u=411470799;
        # d_prefs=MToxLGNvbnNlbnRfdmVyc2lvbjoyLHRleHRfdmVyc2lvbjoxMDAw;
        # guest_id_ads=v1:169115932809926709;
        # guest_id_marketing=v1:169115932809926709;
        # _ga=GA1.2.1322928227.1691457012;
        # _gid=GA1.2.701108083.1691457012;
        # dnt=1;
        # _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%0ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCAJ888CJAToMY3NyZl9p%0AZCIlMGNkY2Q4Y2MwNzA4NWFmMzNkMTRjNzA2MjJlZWE3ZGY6B2lkIiUzYzU0%0ANDY2ZGFlN2EyMTczZjgyOTk3ZjM3NTY4ODk5YQ%3D%3D--123cf8e930e2092a6edb0354a3b302e593814299;
        # lang=en;
        # external_referer=padhuUp37zhYbqzxlg7ds9cKHQyrkYiY|0|8e8t2xd8A2w=;
        # personalization_id="v1_iXFFmeWrrfwWwlddWjOt4A=="


        # 'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
        self.Twitter.cookies = {
            'guest_id': cookies.get('guest_id'),
            'kdt': cookies.get('kdt'),
            'auth_token': cookies.get('auth_token'),
            'ct0': cookies.get('ct0'),
            'twid': cookies.get('twid'),
            'guest_id_marketing': cookies.get('guest_id_marketing'),
            'guest_id_ads': cookies.get('guest_id_ads'),
            'external_referer': 'padhuUp37zhYbqzxlg7ds9cKHQyrkYiY|0|8e8t2xd8A2w=',
            'lang': 'en',
            'personalization_id': cookies.get('personalization_id')
        }


        qid = '5V_dkq1jfalfiFOEZ4g47A'
        features = {
          "c9s_tweet_anatomy_moderator_badge_enabled": True,
          "tweetypie_unmention_optimization_enabled": True,
          "responsive_web_edit_tweet_api_enabled": True,
          "graphql_is_translatable_rweb_tweet_is_translatable_enabled": True,
          "view_counts_everywhere_api_enabled": True,
          "longform_notetweets_consumption_enabled": True,
          "responsive_web_twitter_article_tweet_consumption_enabled": False,
          "tweet_awards_web_tipping_enabled": False,
          "responsive_web_home_pinned_timelines_enabled": True,
          "longform_notetweets_rich_text_read_enabled": True,
          "longform_notetweets_inline_media_enabled": True,
          "responsive_web_graphql_exclude_directive_enabled": True,
          "verified_phone_label_enabled": False,
          "freedom_of_speech_not_reach_fetch_enabled": True,
          "standardized_nudges_misinfo": True,
          "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": True,
          "responsive_web_media_download_video_enabled": False,
          "responsive_web_graphql_skip_user_profile_image_extensions_enabled": False,
          "responsive_web_graphql_timeline_navigation_enabled": True,
          "responsive_web_enhance_cards_enabled": False
        }
        data = {
            'queryId': qid,
            'features': features,
            'variables': variables
        }
        self.Twitter.headers.update({'authorization':'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA'})
        response = await self.Twitter.post(f'https://twitter.com/i/api/graphql/{qid}/CreateTweet',data=data,timeout=40)
        if 'errors' in response.text:
            if response.json()['errors'][0]['message'].find('Status is a duplicate') != -1:
                print('[1/4]已经发过贴')
                return ''
            else:
                print('[1/4]发帖错误：', data)
                return ''

        rest_id = data['data']['create_tweet']['tweet_results']['result']['rest_id']
        self.tw_user_id = data['data']['create_tweet']['tweet_results']['result']['core']['user_results']['result']['screen_name']
        url = f'https://twitter.com/{self.tw_user_id}/status/{rest_id}'
        print('[1/4]发帖成功：', url)
        return url

    async def spread_the_word_about(self):
        try:
            url = await self.create_twitter()
            data = {
              "posted_tweet_id": url
            }
            response = await self.http.post('https://dropcoin.online/quests/passing/7', data=data,timeout=20)

            await self.get_points()
            if 'true' in response.text:
                return True
            if 'already completed' in response.text:
                return True
            logger.error(f'{self.wallet} 发帖失败')
            return False
        except Exception as e:
            logger.error(e)
            return False


    async def set_wallet(self):
        try:
            response = await self.http.post('https://dropcoin.online/quests/passing/6', json={'wallet': self.wallet},timeout=20)
            if 'true' in response.text:
                return True
            if 'already completed' in response.text:
                return True
            logger.error(f'{self.wallet} 设置钱包失败')
            return False
        except Exception as e:
            logger.error(e)
            return False

    async def set_referral(self):
        try:
            response = await self.http.post('https://dropcoin.online/quests/passing/11', json={'referral_username': self.referral},timeout=20)
            if 'true' in response.text:
                return True
            if 'already completed' in response.text:
                return True
            logger.error(f'{self.wallet} 设置邀请人失败')
            return False
        except Exception as e:
            logger.error(e)
            return False


async def main(referral_username, file_name):
    global g_fail, g_success
    with open(file_name, 'r', encoding='UTF-8') as f, open('dropcoin_success.txt', 'a') as s, open('dropcoin_error.txt', 'a') as e:  # eth----auth_token
        lines = f.readlines()
        for line in lines:
            wallet, auth_token, agent_ip = line.strip().split('----')
            DC = DropCoin(auth_token, wallet, referral_username, agent_ip)
            if await DC.twitter_login() and await DC.set_wallet() and await DC.set_referral():
                # 发帖任务
                await DC.spread_the_word_about()
                g_success += 1
                logger.success(f'{wallet} 成功')
                # await DC.get_points()
                s.write(f'{wallet}----{auth_token}----{DC.token}\n')
            else:
                g_fail += 1
                logger.error(f'{wallet} 失败')
                e.write(f'{wallet}----{auth_token}\n')


if __name__ == '__main__':
    _referral = input('输入邀请码: ').strip()
    _file_name = input('账号文件(eth----auth_token): ').strip()
    asyncio.run(main(_referral, _file_name))