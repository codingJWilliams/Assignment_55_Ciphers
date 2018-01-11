# Jay Williams 2017
# This module is included as part of https://github.com/codingJWilliams/jw_utils
# Liscenced according to ../../LISCENCE
# Contact codingJWilliams on github with any queries

def get_table(grid):
  max_cols = [max(out) for out in map(list, zip(*[[len(item) for item in row] for row in grid]))]
  rst = table_div(max_cols, 1)

  for i, row in enumerate(grid):
    header_flag = False
    if i == 0 or i == len(grid)-1: header_flag = True
    rst += normalize_row(row,max_cols)
    rst += table_div(max_cols, header_flag )
  return rst

def table_div(max_cols, header_flag=1):
  out = ""
  o = ""
  if header_flag == 1:
    style = "="
    o = "\n"
  else:
    style = ""

  if header_flag == 1:
    for max_col in max_cols:
      out += max_col * style + " "
  else:
    for max_col in max_cols:
      out += max_col * style + ""
  out += o
  return out

def normalize_row(row, max_cols):
  r = ""
  for i, max_col in enumerate(max_cols):
    r += row[i] + (max_col  - len(row[i]) + 1) * " "
  return r + "\n"
