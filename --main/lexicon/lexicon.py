class Lexicon:
    def __init__(self):
        self.start = "Привет!\n\nДавай сыграем в игру'Камень,ножницы,бумага'?"
        self.yes_button ='Давай'
        self.no_button ='Не хочу'
        self.yes = "Отлично! Делай свой выбор!"
        self.rock = 'Камень'
        self.paper = 'Бумага'
        self.scissors='Ножницы'

        self.bot_winner = "Я победил!\n\nСыграем ещё?"
        self.player_winner = "Ты победил!\n\nСыграем ещё?"
        self.nobody_winner = "Ничья!\n\nПродолжим?"
        
lexicon = Lexicon()