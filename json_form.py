#! /usr/bin/env python3

# JSON file 読み込んで整形して出力する

import json
import os
import sys

def main():
  args = sys.argv
  if len(args) != 2:
    print(f'json ファイルを整形して出力します\n　出力ファイル名は入力ファイル名 + "_f"\n')
    print(f'Usage:\n  {args[0]} <json file>\n')
    exit()

  jinfile = args[1]
  if not os.path.exists(jinfile):
    print(f'file({jinfile}) not exist.\n')
    exit()

  with open(jinfile) as f:
    j = json.load(f)

  joutfile = ".".join(jinfile.split(".")[:-1]) + '_f.json'
  with open(joutfile, "w") as f:
    json.dump(j, f, indent=2)

  print()

if __name__ == '__main__':
  main()
  