class Game:
  def __init__(self):
    self.field = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    self.available_moves = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    self.man_moves = []
    self.ai_moves = []
    self.win_combs = [[0, 4, 8],
                      [2, 4, 6],
                      [1, 4, 7],
                      [0, 3, 6],
                      [2, 5, 8],
                      [0, 1, 2],
                      [3, 4, 5],
                      [6, 7, 8]]
    self._win_combs = [[0, 4, 8],
                       [2, 4, 6],
                       [1, 4, 7],
                       [0, 3, 6],
                       [2, 5, 8],
                       [0, 1, 2],
                       [3, 4, 5],
                       [6, 7, 8]]
    self.middle_move = 4
    self.man_move = bool
    self.next_move = bool

  def start_game(self):
    first_move_ans = input('u?')
    if first_move_ans != '':
      self.next_move = True
      self.man_move = True
    else:
      self.next_move = False
      self.man_move = False

  def guard_move(self):
    if len(self.man_moves) == 1:
      if self.man_moves[0] != self.middle_move:
        return self.middle_move
      else:
        return self.middle_move // 2
    else:
      i = 0
      print(self.win_combs)
      for comb in self.win_combs:
        if len(comb) != 0:
          print('comb' + str(comb))
          for j in self.man_moves:
            if self.man_moves[i] in comb and self.man_moves[i] != j and j in comb:
              comb.remove(self.man_moves[i])
              comb.remove(j)
              c = comb[0]
              comb.remove(comb[0])
              return c

  def attack_move(self):
    if self.middle_move in self.available_moves:
      return self.middle_move

    for comb in self.win_combs:
      print(comb)
      if len(comb) != 0:
        for move in self.man_moves:
          if move in comb:
            comb.clear()

    x = self.check_man_move()
    if x:
      return x

    for comb in self.win_combs:
      if len(comb) != 0:
        for i in self.ai_moves:
          if i in comb:
            for j in comb:
              if j != i and j in self.available_moves:
                return j
          else:
            return self.available_moves[0]

  def check_man_move(self):
    if len(self.man_moves) > 1:
      i = 0
      a = self.man_moves[i]
      b = self.man_moves[i + 1]
      for comb in self._win_combs:
        if a in comb and b in comb:
          comb.remove(a)
          comb.remove(b)
          return comb[0]
      if i != len(self.man_moves):
        i += 1
      else:
        return False
    else:
      return False

  def main(self):
    self.start_game()
    while len(self.available_moves) != 0:
      if self.next_move:
        x = int(input('man move: '))
        self.man_moves.append(x)
        self.available_moves.remove(x)
        print('---man---')
        self.next_move = False
      else:
        if self.man_move:
          x = self.guard_move()
        else:
          x = self.attack_move()
        print('ai move: ' + str(x))
        self.ai_moves.append(x)
        self.available_moves.remove(x)
        print('---ai---')
        self.next_move = True

  def info(self):
    print('man' + str(self.man_moves))
    print('ai' + str(self.ai_moves))
    print('available moves' + str(self.available_moves))


if __name__ == '__main__':
  print("0|1|2\n3|4|5\n6|7|8")
  game = Game()
  game.main()
