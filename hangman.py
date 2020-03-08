# tinyurl.com/h9q2cpc
def hangman(word):
    wrong = 0 #プレーヤー2の間違えた回数
    stages = ["",
             "________        ",
             "|     |      ",
             "|     0      ",
             "|    /|\     ",
             "|    / \     ",
             "|            "
              ]
    rletters = list(word) # word変数内の文字を1文字ずつリストにして、rlettersに代入 remember lettersの略？
    board = ["__"] * len(word) # word変数の中の文字数ぶん、__という文字列をboardに格納する
    win = False
    print("Welcome to Hangman")
    while wrong < len(stages) - 1: # wrongの数がstages(吊られた人のリストの数)より少ない間は続ける)
        print("\n")
        print(len(stages))
        msg = "Guess a letter : "
        char = input(msg)
        if char in rletters: #　文字が合ってた場合の処理
            cind = rletters.index(char) # cindはcharacter index? cindにヒットしたrlettersのインデックス値を代入
            
            board[cind] = char
            rletters[cind] = '$' # 同じ文字needのeなどが重複した場合に備え、最初のeを$(アルファベット以外)にしておく
        else:
            wrong += 1 #　文字が間違ってた場合の処理
        print((" ".join(board))) # リストの['__', '__', '__']を__ __ __にするため空白文字で結合する
        e = wrong + 1 # wrong間違い回数を1カウントアップする。 eはerror?
        print("\n↓吊られた男が表示されたら終わりです\n")
        print("\n".join(stages[0: e])) # 吊られた男リストのインデックス値0から間違えた回数値まで改行を結合して表示
        
        if "__" not in board: #　勝敗判定 もしboardに__が無ければ、
            print("You win!")
            print(" ".join(board)) #　boardの文字列を空白で区切って表示
            win = True # winフラグをTrueにする
            break # whileを抜ける。そのまま下の行へ進む
    if not win: # 
        print("\n".join(stages[0:wrong]))
        print("You lose! It was {}.".format(word))

hangman("need")