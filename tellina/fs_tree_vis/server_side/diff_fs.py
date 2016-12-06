import json
from pprint import pprint

def fsdiff(fs1, fs2):
  new_fs = {}
  fs1_type = "children" in fs1
  fs2_type = "children" in fs2
  if fs1["name"] != fs2["name"] or fs1_type != fs2_type:
    print "[ERROR] root is not the same"
  new_fs["name"] = fs1["name"]

  if "children" not in fs1:
    return new_fs

  new_fs["children"] = []

  cname1 = {}
  for child in fs1["children"]:
    cname1[gen_id(child)] = child

  cname2 = {}
  for child in fs2["children"]:
    cname2[gen_id(child)] = child

  for cname in cname1:
    if cname in cname2:
      child = fsdiff(cname1[cname], cname2[cname])
      new_fs["children"].append(child)
    elif cname not in cname2:
      child = cname1[cname]
      recursive_set_tag(child, "removal")
      new_fs["children"].append(child)

  for cname in cname2:
    if cname not in cname1:
      child = cname2[cname]
      recursive_set_tag(child, "addition")
      new_fs["children"].append(child)    

  return new_fs

def recursive_set_tag(fs, tag):
  fs["tag"] = tag
  if "children" in fs:
    for c in fs["children"]:
      recursive_set_tag(c, tag)

def tag_intermediate(fs):
  tag = "child_diff"

  modified = False
  if "children" in fs:
    for c in fs["children"]:
      modified = tag_intermediate(c) or modified

  if "tag" in fs:
    return True

  if modified and ("tag" not in fs):
    fs["tag"] = tag
    return True

  return False

def find_highest_non_modified(fs):
  tag = "higest_non_modified"
  if "children" in fs and "tag" not in fs:
    fs["tag"] = tag
    return    

  if "children" in fs:
    for c in fs["children"]:
      find_highest_non_modified(c)

def gen_id(f):
  return f["name"] + "{[" + str("children" in f) + "]}"

if __name__=="__main__":
  with open('fs1.json') as data_file:    
    fs1 = json.load(data_file)
  with open('fs2.json') as data_file:    
    fs2 = json.load(data_file)
  
  diff_fs = fsdiff(fs1, fs2)
  tag_intermediate(diff_fs)
  find_highest_non_modified(diff_fs)
  print json.dumps(diff_fs)