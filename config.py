import os
import datetime as dt
import hashlib

ts = str(dt.datetime.now().timestamp())
apikey = os.environ.get("API_KEY")
private_key = os.environ.get("PRIVATE_KEY")
encoder = hashlib.md5()
encoder.update(ts.encode('utf8'))
encoder.update(private_key.encode('utf8'))
encoder.update(apikey.encode('utf8'))

hash = encoder.hexdigest()
