import datetime as dt
import hashlib

ts = str(dt.datetime.now().timestamp())
apikey = 'Your public key'
private_key = 'Your private key'

encoder = hashlib.md5()
encoder.update(ts.encode('utf8'))
encoder.update(private_key.encode('utf8'))
encoder.update(apikey.encode('utf8'))

hash = encoder.hexdigest()
