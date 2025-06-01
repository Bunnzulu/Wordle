import pygame, sys, string, random
pygame.init()
WIDTH, HEIGHT = 550, 550
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wordle")
Clock = pygame.time.Clock()
file = open("W.txt","r")
words = file.read().upper()
WORDCHOICES = words.split("\n")
WORD = random.choice(WORDCHOICES).upper()
file.close()
Running = True
Game_Font = pygame.font.SysFont("roboto",30,False,False)
Title = Game_Font.render("Wordle",True,"White")
Title_rect = Title.get_rect(center = (WIDTH/2,25))
Result = ""
Result_Text = Game_Font.render(str(Result), True, "White")
Result_rect = Result_Text.get_rect(center = (250,466))
Final_Text = Game_Font.render(f"The Correct word was {WORD}", True, "White")
Final_rect = Final_Text.get_rect(center = (250,520))
PA = Game_Font.render("Space to play again", True, "White")
PA_rect = PA.get_rect(center = (350,490))
IW = Game_Font.render("Invalid Guess", True, "White")
IW_rect = IW.get_rect(center = (330,490))
Invaild_Word = False

class Keys:
    def __init__(self, pos_x, pos_y, letter):
        self.rect = pygame.Rect(pos_x, pos_y, 30, 30)
        self.Text = letter
        self.Text_Type = pygame.font.Font(None, 36)
        self.Display_Text = self.Text_Type.render(self.Text, True, "Black")
        x,y = self.rect.center
        self.Display_Text_rect = self.Display_Text.get_rect(center = (x,y))
        self.Color = "White"

    def Draw(self):
        pygame.draw.rect(SCREEN, self.Color, self.rect)
        SCREEN.blit(self.Display_Text,self.Display_Text_rect)
    
    def Update(self, color):
        self.Color = color
        self.Draw()

class Boxes:
    def __init__(self, pos_x, pos_y, Tag_num):
        self.rect = pygame.Rect(pos_x, pos_y, 64, 64)
        self.Text = ""
        self.TN = Tag_num
        self.GuessColor = "Black"
        self.Text_Type = pygame.font.Font(None,52)
        self.Display_Text = self.Text_Type.render(self.Text,True,"White")
        x,y = self.rect.center
        self.Display_Text_rect = self.Display_Text.get_rect(center = (x - 10,y))
        self.color_act = pygame.Color('lightskyblue3')
        self.Color = "White"
        self.Entered = False
        self.Typing = False
        self.Display_Color = pygame.Surface((60,60))
        self.Display_Color_rect = self.Display_Color.get_rect(center = self.rect.center)

    def Draw(self):
        if self.Typing: self.Color = self.color_act
        else: self.Color = "White"
        self.Display_Color.fill(self.GuessColor)
        pygame.draw.rect(SCREEN, self.Color, self.rect, 2)
        self.Display_Text = self.Text_Type.render(self.Text,True,"White")
        SCREEN.blit(self.Display_Color,self.Display_Color_rect)
        SCREEN.blit(self.Display_Text,self.Display_Text_rect)

#First Row
FirstRow_Y = 50
B11 = Boxes(70, FirstRow_Y,0)
B12 = Boxes(135, FirstRow_Y,1)
B13 = Boxes(200, FirstRow_Y,2)
B14 = Boxes(265, FirstRow_Y,3)
B15 = Boxes(330, FirstRow_Y,4)

#Second Row
SecondRow_Y = 118
B21 = Boxes(70, SecondRow_Y,5)
B22 = Boxes(135, SecondRow_Y,6)
B23 = Boxes(200, SecondRow_Y,7)
B24 = Boxes(265, SecondRow_Y,8)
B25 = Boxes(330, SecondRow_Y,9)

#Third Row
ThirdRow_Y = 186
B31 = Boxes(70, ThirdRow_Y,10)
B32 = Boxes(135, ThirdRow_Y,11)
B33 = Boxes(200, ThirdRow_Y,12)
B34 = Boxes(265, ThirdRow_Y,13)
B35 = Boxes(330, ThirdRow_Y,14)

#Fourth Row
FourthRow_Y = 254
B41 = Boxes(70, FourthRow_Y,15)
B42 = Boxes(135, FourthRow_Y,16)
B43 = Boxes(200, FourthRow_Y,17)
B44 = Boxes(265, FourthRow_Y,18)
B45 = Boxes(330, FourthRow_Y,19)

#Fifth Row
FifthRow_Y = 322
B51 = Boxes(70,FifthRow_Y,20)
B52 = Boxes(135, FifthRow_Y,21)
B53 = Boxes(200, FifthRow_Y,22)
B54 = Boxes(265, FifthRow_Y,23)
B55 = Boxes(330, FifthRow_Y,24)

#Sixth Row
SixthRow_Y = 390
B61 = Boxes(70,SixthRow_Y,25)
B62 = Boxes(135, SixthRow_Y,26)
B63 = Boxes(200, SixthRow_Y,27)
B64 = Boxes(265, SixthRow_Y,28)
B65 = Boxes(330, SixthRow_Y,29)

def Check(letter,Word, part_of_word):
    if letter == Word[part_of_word]: return "Green"
    elif letter in Word: return "Yellow"
    else: return "Gray"
Rows = [B11,B12,B13,B14,B15,B21,B22,B23,B24,B25,B31,B32,B33,B34,B35,B41,B42,B43,B44,B45,B51,B52,B53,B54,B55,B61,B62,B63,B64,B65]
Checker = ""

# First row of keys
AKEY = Keys(0, 460, "A")
BKEY = Keys(40, 460, "B")
CKEY = Keys(80, 460, "C")
DKEY = Keys(120, 460, "D")
EKEY = Keys(160, 460, "E")
FKEY = Keys(200, 460, "F")
GKEY = Keys(240, 460, "G")
HKEY = Keys(280, 460, "H")
IKEY = Keys(320, 460, "I")
JKEY = Keys(360, 460, "J")
KKEY = Keys(400, 460, "K")
LKEY = Keys(440, 460, "L")
MKEY = Keys(480, 460, "M")

NKEY = Keys(0, 490, "N")
OKEY = Keys(40, 490, "O")
PKEY = Keys(80, 490, "P")
QKEY = Keys(120, 490, "Q")
RKEY = Keys(160, 490, "R")
SKEY = Keys(200, 490, "S")
TKEY = Keys(240, 490, "T")
UKEY = Keys(280, 490, "U")
VKEY = Keys(320, 490, "V")
WKEY = Keys(360, 490, "W")
XKEY = Keys(400, 490, "X")
YKEY = Keys(440, 490, "Y")
ZKEY = Keys(480, 490, "Z")

Keys_List = [AKEY,BKEY,CKEY,DKEY,EKEY,FKEY,GKEY,HKEY,IKEY,JKEY,KKEY,LKEY,MKEY,NKEY,OKEY,PKEY,QKEY,RKEY,SKEY,TKEY,UKEY,VKEY,WKEY,XKEY,YKEY,ZKEY]

def find_key(letter):
    for index,key in enumerate(Keys_List):
        if key.Text == letter:
            return index
    return None


while True:
  count = 0
  for e in pygame.event.get():
      if e.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
      if Running:
        for index,col in enumerate(Rows):
            if col.Text == "":
                if index - 1 in (4,9,14,19,24,29) and not Rows[index - 1].Entered:
                    Rows[index - 1].Typing = True
                else:
                    col.Typing = True
                    Rows[index - 1].Typing = False
                break
        if e.type == pygame.KEYDOWN:
            for Index,box in enumerate(Rows):
                if box.Typing:
                    if e.key == pygame.K_BACKSPACE:
                        if len(box.Text) == 1:
                            box.Text = box.Text[:-1]
                        elif len(box.Text) == 0 and Index > 0 and not Rows[Index - 1].Entered:
                            box.Typing = False
                            Rows[Index - 1].Typing = True
                            Rows[Index - 1].Text = ""
                            break
                    elif e.key == pygame.K_RETURN and Index in (4,9,14,19,24,29) and box.Text != "": 
                        for i in range(5):
                            Checker += str(Rows[Index - (4- i)].Text)
                        if Checker in WORDCHOICES:
                            Checker = ''; Invaild_Word = False
                            for b in range(5):
                                Rows[Index - b].Entered = True
                                Rows[Index - b].GuessColor = Check(Rows[Index - b].Text,WORD,4 - b)
                                keyindex = find_key(Rows[Index - b].Text)
                                Keys_List[keyindex].Update(Rows[Index - b].GuessColor)
                                if Rows[Index - b].GuessColor == "Green":
                                    count += 1
                                    if count == 5:
                                        Result = "Winner"
                                        Running = False
                                Checker += str(Rows[Index - (4- b)].Text)
                            for o,r in enumerate(Checker):
                                if Checker.count(r) > 1 and WORD.count(r) == 1:
                                    a = Checker.find(r,o+ 1)
                                    if Rows[Index - (4- o)].GuessColor == "Yellow" and Rows[Index - (4- a)].GuessColor == "Green":
                                        Rows[Index - (4- o)].GuessColor = "Gray"
                                    elif Rows[Index - (4- o)].GuessColor == "Green" and Rows[Index - (4- a)].GuessColor == "Yellow":
                                        Rows[Index - (4- a)].GuessColor = "Gray"
                                    elif Rows[Index - (4- o)].GuessColor == "Yellow" and Rows[Index - (4- a)].GuessColor == "Yellow":
                                        Rows[Index - (4- a)].GuessColor = "Gray"
                                    else: pass
                            Checker = ""
                            if Index == 29 and Result != "Winner":
                                Result = "Loser"
                                Running = False
                        else:
                            Invaild_Word = True
                            Checker = ""
                    else:
                        if len(box.Text) < 1 and e.unicode in string.ascii_letters:
                            box.Text += e.unicode.upper()
    
      else:
          if e.type == pygame.KEYDOWN:
              if e.key == pygame.K_SPACE:
                  Result = ""
                  for i,row in enumerate(Rows):
                      row.Text = ""
                      row.Typing = False
                      row.Entered = False
                      row.GuessColor = "Black"
                  WORD = random.choice(WORDCHOICES).upper()
                  Running = True
  if Running:
    SCREEN.fill("Black")
    SCREEN.blit(Title, Title_rect)
    if Invaild_Word: SCREEN.blit(IW, IW_rect)
    B11.Draw();B12.Draw();B13.Draw();B14.Draw();B15.Draw()
    B21.Draw();B22.Draw();B23.Draw();B24.Draw();B25.Draw()
    B31.Draw();B32.Draw();B33.Draw();B34.Draw();B35.Draw()
    B41.Draw();B42.Draw();B43.Draw();B44.Draw();B45.Draw()
    B51.Draw();B52.Draw();B53.Draw();B54.Draw();B55.Draw()
    B61.Draw();B62.Draw();B63.Draw();B64.Draw();B65.Draw()
    for key in Keys_List:
        key.Draw()
  else:
    SCREEN.fill("Black")
    Result_Text = Game_Font.render(str(Result), True, "White")
    Final_Text = Game_Font.render(f"The Correct word was {WORD}", True, "White")
    SCREEN.blit(Title, Title_rect)
    SCREEN.blit(Result_Text, Result_rect)
    SCREEN.blit(Final_Text,Final_rect)
    SCREEN.blit(PA,PA_rect)
    B11.Draw();B12.Draw();B13.Draw();B14.Draw();B15.Draw()
    B21.Draw();B22.Draw();B23.Draw();B24.Draw();B25.Draw()
    B31.Draw();B32.Draw();B33.Draw();B34.Draw();B35.Draw()
    B41.Draw();B42.Draw();B43.Draw();B44.Draw();B45.Draw()
    B51.Draw();B52.Draw();B53.Draw();B54.Draw();B55.Draw()
    B61.Draw();B62.Draw();B63.Draw();B64.Draw();B65.Draw()
    for key in Keys_List:
        key.Update("White")
  Clock.tick(60)
  pygame.display.update()