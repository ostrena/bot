@classmethod
        def getExtPar (cls, id):
            return cls.parametrs.pop (id, None)

        @classmethod
        def setExtParc(cls, parameter):
            import uuid
            id = uuid.uuid4().hex
            cls.parametrs [id] = parameter
            return id
        @classmethod
        def getMenu (cls, name):
           menu = cls.hash.get (name)
           if menu != None:
               cls.cur_menu = menu
               return menu

m_main = Menu ("Главное меню", buttons=["Несмешые анекдоты и тд", "Игры", "Помощь (мне)"])
m_games = Menu ("Игры", buttons=["Камень, ножницы, бумага", "Кнопка для вида", "Тут тоже ничего нет", "Выход"], parent=m_main)
m_game_knb = Menu ("Камень, ножницы, бумага", buttons=["Камень", "Ножницы", "Бумага", "Выход"], parent=m_games, action="game_knb")
m_fun = Menu ("Несмешные анекдоты и тд", buttons= ["Прислать собаку", "Прислать анекдот", "Выход"], parent=m_main)