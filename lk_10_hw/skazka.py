class Hero:
    def __init__(self, name):
        self.name = name

    def say_name(self):
        return self.name


class Grandfather(Hero):
    def request(self):
        print(f"{self.say_name()}: Испеки, старуха, колобок!")

    def answer(self):
        print(f"{self.say_name()}: Э-эх, старуха! По коробу поскреби, по сусеку помети; авось муки и наберется.")


class Grandmother(Hero):
    def answer_to(self):
        print(f"{self.say_name()}: Из чего печь — то? Муки нету.")

    def actions(self):
        print("Взяла старуха крылышко, по коробу поскребла, по сусеку помела, и набралось муки пригоршни с две.\nЗамесила на сметане, изжарила в масле и положила на окошечко постудить.")


class Kolobok(Hero):
    def escape_from_parents(self):
        print("Колобок полежал — полежал, да вдруг и покатился — с окна на лавку, с лавки на пол, по полу да к дверям,\nперепрыгнул через порог в сени, из сеней на крыльцо, с крыльца — на двор, со двора за ворота, дальше и дальше.")

    def meet_hare(self):
        print("Катится колобок по дороге, а навстречу ему заяц:")

    def answer_hare(self):
        print(f"{self.say_name()}: Не ешь меня, косой зайчик! Я тебе песенку спою, — сказал колобок и запел:")

    def song_for_hare(self):
        print(f"{self.say_name()}: Я Колобок, Колобок!\nЯ по коробу скребен,\nПо сусеку метен,\nНа сметане мешон,\nДа в масле пряжон,\nНа окошке стужон;\nЯ от дедушки ушел,\nЯ от бабушки ушел,\nИ от тебя, зайца, не хитро уйти!\nИ покатился себе дальше; только заяц его и видел!")

    def meet_wolf(self):
        print("Катится колобок, а навстречу ему волк:")

    def answer_wolf(self):
        print("Не ешь меня, серый волк! Я тебе песенку спою, — сказал колобок и запел:")

    def song_for_wolf(self):
        print("Я Колобок, Колобок!\nЯ по коробу скребен,\nПо сусеку метен,\nНа сметане мешон,\nДа в масле пряжон,\nНа окошке стужон;\nЯ от дедушки ушел,\nЯ от бабушки ушел,\nЯ от зайца ушел,\nИ от тебя, волка, не хитро уйти!\nИ покатился себе дальше; только волк его и видел!")

    def meet_bear(self):
        print("Катится колобок, а навстречу ему медведь:")

    def answer_bear(self):
        print(f"{self.say_name()}: Не ешь меня, косолапый! Я тебе песенку спою, — сказал колобок и запел:")

    def song_for_bear(self):
        print(f"{self.say_name()}: Я Колобок, Колобок!\nЯ по коробу скребен,\nПо сусеку метен,\nНа сметане мешон,\nДа в масле пряжон,\nНа окошке стужон;Я от дедушки ушел,\nЯ от бабушки ушел,\nЯ от зайца ушел,\nЯ от волка ушел,\nИ от тебя, медведь, не хитро уйти!\nИ опять укатился, только медведь его и видел!")

    def meet_fox(self):
        print("Катится, катится «колобок, а навстречу ему лиса:")

    def answer_fox(self):
        print(f"{self.say_name()}: Не ешь меня, лиса! Я тебе песенку спою, — сказал колобок и запел:")

    def song_for_fox(self):
        print(f"{self.say_name()}: Koлобок, Колобок!\nЯ по коробу скребен,\nПо сусеку метен,\nНа сметане мешон,\nДа в масле пряжон,\nНа окошке стужон;\nЯ от дедушки ушел,\nЯ от бабушки ушел,\nЯ от зайца ушел,\nЯ от волка ушел,\nИ от медведя ушел,\nА от тебя, лиса, и подавно уйду!")

    def second_song_for_fox(self):
        print("Колобок вскочил лисе на мордочку и запел ту же песню.")

class Hare(Hero):
    def to_kolobok(self):
        print(f"{self.say_name()}: Колобок, колобок! Я тебя съем.")


class Wolf(Hero):
    def to_kolobok(self):
        print(f"{self.say_name()}: Колобок, колобок! Я тебя съем.")


class Bear(Hero):
    def to_kolobok(self):
        print(f"{self.say_name()}: Колобок, колобок! Я тебя съем.")


class Fox(Hero):
    def to_kolobok(self):
        print(f"{self.say_name()}: Здравствуй, колобок! Какой ты хорошенький. Колобок, колобок! Я тебя съем.")

    def second_to_kolobok(self):
        print(f"{self.say_name()}: Какая славная песенка! — сказала лиса. — Но ведь я, колобок, стара стала, плохо слышу;\nсядь-ка на мою мордочку да пропой еще разок погромче.")

    def die_kolobok(self):
        print(f"{self.say_name()}: Спасибо, колобок! Славная песенка, еще бы послушала! Сядь-ка на мой язычок да пропой в последний разок, — сказала лиса и высунула свой язык;\nколобок прыг ей на язык, а лиса — ам его! И съела колобка…")



grandfather = Grandfather('dedyshka')
grandmother = Grandmother('babyshka')
kolobok = Kolobok('kolobok')
hare = Hare('zayac')
wolf = Wolf('wolk')
bear = Bear('medved`')
fox = Fox('lisa')


def tale():
    grandfather.request()
    grandmother.answer_to()
    grandfather.answer()
    grandmother.actions()
    kolobok.escape_from_parents()
    kolobok.meet_hare()
    hare.to_kolobok()
    kolobok.answer_hare()
    kolobok.song_for_hare()
    kolobok.meet_wolf()
    wolf.to_kolobok()
    kolobok.answer_wolf()
    kolobok.song_for_wolf()
    kolobok.meet_bear()
    bear.to_kolobok()
    kolobok.answer_bear()
    kolobok.song_for_bear()
    kolobok.meet_fox()
    fox.to_kolobok()
    kolobok.answer_fox()
    kolobok.song_for_fox()
    fox.second_to_kolobok()
    kolobok.second_song_for_fox()
    fox.die_kolobok()


tale()
