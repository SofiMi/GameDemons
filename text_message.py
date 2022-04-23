import pygame
from settings import *

class text_message():
    def __init__(self, screen):
        self.screen = screen
        self.shop_mess_hero = ["Незуко \n" \
                               "   Незуко - младшая сестра \n"
                               "Танжиро, обращенная \n"
                               "в демона \n \n" \
                               "Обладает способностями: \n " \
                               " - Изменять размер тела \n "\
                               " - Регенерация \n " \
                               " - Техника демонической \n"
                               "   крови \n ",

                               "Зеницу \n" \
                               "   Зеницу - простой перенек, \n"
                               "обладающий большой \n"
                               "скрытой силой \n \n" \
                               "Обладает способностями: \n " \
                               " - Повышенный слух \n "\
                               " - Бой без сознания \n " \
                               " - Дыхание грома \n",

                               "Иноске \n" \
                               "   Иноске - охотник на \n"
                               "демонов, выросший с \n"
                               "кабанами \n \n" \
                               "Обладает способностями: \n " \
                               " - Улучшенное чувство \n "
                               "   осязания \n " \
                               " - Стойкость к отравлению \n " \
                               " - Дыхание зверя"
                               ]
        self.shop_mess_skills = ['   Яд из глицинии \n\n' \
            "   Способен парализовать \nобычных демонов и \nограничить подвижность \nнизших лун",
                                 '   Дыхание воды \n\n' \
            "- Рассекающая водная \nгладь \n- Водяное колясо \n- Танец быстротечного \nпотока \n"
                                 "- Удар волной \n- Поток водопада",
                                 '   Тренировка в поместье \n          бабочки \n\n'
            "   Повышение: \n - Ловкости \n - Выносливости \n - Скорости и рефлексов",
                                 '   Дыхание солнца \n\n'
            " - Радуга паргелия \n - Огненная колесница\n - Палящее солнце\n - Копьё подсолнуха\n - Пламенный вальс",
                                 '   Тренировкa со столпами\n\n'
            "   Специальная тренировка,\nнаправленная на \nулучшение способностей\nи физического\nздоровья всех\nохотников на демонов",
                                 '        Метка \nистребителя демонов\n\n'
            " - Расширенные \nфизические возможности \n - Прозрачный мир\n - Багровый Красный\nНичирин Клинок"
                                 ]
        self.shop_mess_lamp = "   Привет, \nЯ подсказка по управлению! \n \n " \
                              " - Если ты хочешь купить \nпредмет, то нажми \nна иконку левой \nкнопкой мышки. \n " \
                              " - Если хочешь узнать \nо нем больше, \nто - правой кнопкой мышки."

        self.mess_demon = [["\n???", "Кёгай (響凱 Kyōgai) - демон, который ранее занимал позицию Шестой Низшей Луны"],
                           ["\n???", "Аказа (猗あ窩か座ざ Akaza?) — демон двенадцати лун, занимающий позицию третьей высшей луны."
                                 "[1] Когда он был человеком, его звали Хакуджи."],
                           ["\n???", "Музан Кибуцуджи (鬼き舞ぶ辻つじ無む惨ざん Kibutsuji Muzan?) "
              "— первый в своем роде демон, прародитель остальных демонов. "
              "Антагонист аниме и манги 'Клинок, рассекающий демонов'. "
              "Он убил большинство из семьи Камадо и обратил Незуко в демона."]]
        self.mess_count_demons = ['    Победа над 1-м\n         демоном!\n\n'
                                  '    Вы ступили на тяжелый\nпуть охотника за демонами:\nни каждый справляется \nс этой ношей.\n'
                                  '    Сможете ли вы достичь\nуровня силы столпов\nи победить главного злодея?',
                                 '    Победа над 5-ю\n          демонами!\n\n'
                                 '    Вы постепенно\nнабираетесь опыта.\n'
                                 '    С каждым побежденным \nдемоном ваши\n'
                                  'силы возрастают, а\nумения становятся\nоточеннее.',
                                 '     Победа над 10-ю\n         демонами!\n\n'
                                 '    Вы достигли среднего\nуровня убитых демонов\n'
                                 '    Ваше развитие \nпроисходит стремительно,\n'
                                  'из-за чего о вас\nуже пошли славные\nслухи.',
                                  '    Победа над 25-ю\n         демонами!\n\n'
                                  '    Вы одолели больше\nдемонов, чем некоторые\nстолпы!\n'
                                  '    Становится ясно, что\nвы будущий герой,\n'
                                  'который сможет победить\nвысшие луны.',
                                  '    Победа над 50-ю\n         демонами!\n\n'
                                  '    Вы избавили мир\nот многих ранее \nнедосягаемых демонов!\n'
                                  '    Пора ли отправиться\n в бой с Мудзаном?',
                                 ]
        self.mess_forse =       ["\n\n\n\n    Ваша сила больше \n      5 кликов за раз!",
                                 "\n\n\n\n    Ваша сила больше \n     10 кликов за раз!",
                                 "\n\n\n\n    Ваша сила больше \n     50 кликов за раз!",
                                 "\n\n\n\n    Ваша сила больше \n    100 кликов за раз!",
                                 "\n\n\n\n    Ваша сила больше \n    500 кликов за раз!"
                                 ]
        self.mess_dont_many = "У вас \nнедостаточно \nденег!"

        self.mess_start_6_demon = ["    Последовав за криками\nдетей, вы набрели\nна ужасающий дом...\n",
                                   "    Вы пересиливаете страх\nи ступаете на ветхий,\n скрипущий пол.\n",
                                   "    Но вдруг на голову\nобрушивается ошеломительный\n грохот барабанов.\n"
                                   "    Что же это?\nПочему пространство\nто расширяется, то сжимается?\n",
                                   "Становится отчетливо ясно:\n"
                                   "          Вас ждет бой\n    с 6 низшей луной!\n"]

        self.mess_start_3_demon = ["    Вы отправляетесь в \nквартал красных фонарей\nчтобы узнать\n",
                                   "    почему пропадают\nмолодые девушки.\n",
                                   "    Как и ожидалось,\nвсему виной\nдемон высшей луны!\n\n"
                                   "    Вам предстоит\nсразиться с Даки...",
                                   "         Будьте осторожны!\n"
                                   "          Уклоняйтесь от\n"
                                   "          желтых поясов!\n"]
        self.win = "Вы победили!"

    def draw_many_lines(self, x, y, text, size):
        lines = text.split("\n")
        self.font = pygame.font.SysFont("Verdana", size)
        for i, l in enumerate(lines):
            self.screen.blit(self.font.render(l, True, TEXT_COLOR, (255, 255, 255)), (x, y + (size + 5) * i))


