import dd_content
import datetime

class DailyDigestEmail:
    
    def _init_(self):
        self.content= {'quote': {'include': True, 'content':dd_content.get_random_quote()},
                       'weather': {'include': True, 'content':dd_content.get_weather_forecast()},
                       'twitter': {'include': True, 'content':dd_content.get_twitter_trends()},
                       'wikipedia': {'include': True, 'content':dd_content.get_wikipedia_article()}}
    
    def send_email(self) :
        pass

    def format_message(self) :
        ##############################
        #### Generate Plaintext#######
        ##############################
        text= f'*~*~*~*~* Daily Digest - {datetime.date.today().strftime}'

if __name__ == '_main_' :
    pass

    