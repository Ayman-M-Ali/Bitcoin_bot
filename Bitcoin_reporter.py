import requests
import time

# Global variables
api_key = "b8b27f15-d5f7-4ecb-8d36-3b4a86d2b39a"
bot_key = "1618572260:AAER80nP9G1vX53nJOkQr3S7XNrp08grLlU"         # Token
chat_id = "1110797457"
limit = 35000                                                      # Get alert when price less than limit
time_interval = 15 * 60                                            # every 15 minute get alert

def get_price() :
  url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

  parameters = {
    'start':'1',
    'limit':'3',
    'convert':'USD'
  }

  headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': api_key,
  }

  response = requests.get(url, headers=headers, params=parameters).json()
  btc_price = response['data'][0]['quote']['USD']['price']
  return btc_price
  

def send_update(chat_id, msg) :
  url = f"https://api.telegram.org/bot{bot_key}/sendMessage?chat_id={chat_id}&text={msg}"
  requests.get(url)


def main() :
  while True :
    price = get_price()
    if price < limit :
      send_update(chat_id, f"سعر البيتكون الآن قد أصبح: {price}")
      time.sleep(time_interval)
main()