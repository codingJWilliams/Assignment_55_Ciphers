# Jay Williams 2017
# This module is included as part of https://github.com/codingJWilliams/jw_utils
# Liscenced according to ../../LISCENCE
# Contact codingJWilliams on github with any queries

import jw_utils, os, json

class Bucket:
  def __init__(self, uid, location=("." + os.sep + "buckets.json")):
    print(location)
    if os.path.exists(location) == False:
      print("MAKING")
      with open(location, "w") as f:
        f.write(json.dumps( {uid: ""} ))
    else:
      with open(location, "r") as f:
        bc = json.loads(f.read())
      try:
        bc[uid]
      except:
        bc[uid] = ""
      with open(location, "w") as f:
        f.write(json.dumps( bc ))
    self.location = location
    self.uid = uid
  def __repr__(self):
    return "< JW_Bucket('" + self.location + "', '" + self.uid + "') >"
  def get(self):
    with open(self.location, "r") as f:
      BucketCollection = json.loads(f.read())
      bucket = BucketCollection[self.uid]
    return bucket
  def set(self, value):
    with open(self.location, "r") as f:
      BucketCollection = json.loads(f.read())
    BucketCollection[self.uid] = value
    with open(self.location, "w") as f:
      f.write(json.dumps(BucketCollection))
  