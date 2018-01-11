# Jay Williams 2017
# This module is included as part of https://github.com/codingJWilliams/jw_utils
# Liscenced according to ../../LISCENCE
# Contact codingJWilliams on github with any queries

import jw_utils

class Menu:
  def __init__(self, name):
    self.name = name
    self.options = []
    self.endLoop = False
  def endOptionLoop(self):
    self.endLoop = True
  def addOption(self, optionName, callback, shouldShowExit = True):
    self.options += [
      {
        "name": optionName,
        "cb": callback,
        "number": str(len(self.options) + 1),
        "showExit": shouldShowExit
      }
    ]
    return True
  def doMenu(self):
    self.endLoop = False
    tableArray = [["Key", "Action"]]
    for option in self.options:
      tableArray += [
        [
          str(option['number']),
          option['name']
        ]
      ]
    tableText = self.name + "\n\n"
    tableText += jw_utils.graphics.tables.get_table(tableArray);
    while self.endLoop != True:
      print(tableText)
      choice = input("> ")
      opt = self.getOption(choice)
      if opt == False:
        print("----- Invalid Choice. Please choose again -----")
      else:
        opt['cb']()
        if opt["showExit"]:
          input("Press enter to go back to menu.")
  def getOption(self, number):
    for opt in self.options:
      if opt['number'] == number:
        return opt
    return False
