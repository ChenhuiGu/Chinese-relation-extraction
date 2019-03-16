from aip import AipNlp

# APP_ID = '11968223'
# API_KEY = 'bS0VMOnsymYtRGvB5YXEbr1K'
# SECRET_KEY = '7ThNTz1lDjqzX6VxjZh0YieAMZ1As6TT'

#pbcsfnlp01-Wjbb12345
APP_ID = '15709863'
API_KEY = 'DuawmmStVg9UuBhvtRc4oieP'
SECRET_KEY = 'eo8tyyErCZlP8vzcz7bCRiEuZWuPlS3w'

bd_client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

urltoken ='https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials'\
          +'&client_id=' + API_KEY\
          +'&client_secret=' + SECRET_KEY

APP_ID_MAP = '15337368'
API_KEY_MAP = 'yYVDtPm57GllrGCyzFOo1xOuiIOlpNLt'