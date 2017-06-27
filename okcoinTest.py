import okcoin
import json

enJson = '[{"data":{"high":2040,"vol":579737.194,"last":1650,"low":1628,"buy":1650.01,"sell":1651.9,"close":1650,"open":1834,"timestamp":1498570280716},"channel":"ok_sub_spotcny_eth_ticker"}]'

deJson = json.loads(enJson)
okcoin.OkCoin().freshTicker(deJson)
okcoin.OkCoin().freshTicker(deJson)
