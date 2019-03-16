from aip import AipNlp

# APP_ID = '11968223'
# API_KEY = 'bS0VMOnsymYtRGvB5YXEbr1K'
# SECRET_KEY = '7ThNTz1lDjqzX6VxjZh0YieAMZ1As6TT'

#pbcsfnlp01-Wjbb12345
APP_ID = '15771747'
API_KEY = 'bTKfcVBinZfhfFqL6X6zoQEh'
SECRET_KEY = 'y5yoBOyBkLa0pUwn3YQpDls0tRM8epH0'

bd_client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

urltoken ='https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials'\
          +'&client_id=' + API_KEY\
          +'&client_secret=' + SECRET_KEY
