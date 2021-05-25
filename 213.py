from instapy import InstaPy

session = InstaPy(username = 'league.twix', password = 'alisina123', headless_browser = True)

session.login()

session.unfollow_users(amount=10, allfollowing=True,unFollow_after=0,sleep_delay=600)

session.end()