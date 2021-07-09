# Возьмите классы Deck и Card с GIST'а второго занятия и доработайте их
from black_jack_classes import Deck, Card

player_money = 100  # Деньги игрока
rate_value = 10  # Размер ставки

deck = Deck()


def sum_points(cards):
    """
    Напишите отдельную функцию для нахождения суммы очков всех карт в списке
    :param cards: список карт(рука игрока или диллера)
    :return: сумму очков
    """
    # Совет: храните кол-во очков за карту внутри класса Колоды(колода "знает", сколько дает очков каждая карта)

    #  Сначала считаем сумму карт, считая ТУЗ за 11-очков
    sum_points = 0
    # Если сумма > 21, то перечитываем сумму, считая ТУЗ за 1(единицу)
    for card in cards:
        sum_points += Deck.POINTS[card.value]
    if sum_points <= 21:
        return sum_points

    sum_points = 0
    for card in cards:
        if card.value == "A":
            sum_points +=1
        else:
            sum_points += Deck.POINTS[card.value]
    return sum_points


while True:
    # 0. Игрок делает ставку
    player_money -= rate_value
    # 1. В начале игры перемешиваем колоду
    Deck.shuffle(deck)
    # 2. Игроку выдаем две карты
    player_cards = Deck.draw(deck, 2)
    # 3. Дилер берет одну карту
    dealer_cards = Deck.draw(deck, 1)
    # 4. Отображаем в консоли карты игрока и дилера
    print(f"{player_cards} - карты игрока ; {dealer_cards} - карты диллера")
    # 5. Проверяем нет ли у игрока блэкджека (21 очко)
    if sum_points(player_cards) == 21:
        # Выплачиваем выигрышь 3 и 2
        player_money += rate_value * 1.5
        print("Black Jack!!! Игрок победил")
        break
        # Заканчиваем игру
    # Если нет блэкджека, то
    while True:  # Игрок добирает карты пока не скажет "достаточно" или не сделает перебор (>21)
        player_choice = input("еще(1)/достаточно(0): ")
        if player_choice == "1":
            player_cards += Deck.draw(deck, 1)
            # Если перебор (>21), заканчиваем добор
            if sum_points(player_cards) > 21:
                print(f"Перебор: {sum_points(player_cards)} очков")
                player_money -= rate_value
                break
        if player_choice == "0":
            # Заканчиваем добирать карты
            break

    # Если у игрока не 21(блэкджек) и нет перебора, то
    if sum_points(player_cards) != 21 and sum_points(player_cards) <= 21:
        print("Диллер добирает карты")
        dealer_cards += Deck.draw(deck, 1)
        if sum_points(player_cards) == 21:
            print(f"Диллер победил!")
            player_money -= rate_value
            break
        else:
            while sum_points(dealer_cards) < 17:
                dealer_cards += Deck.draw(deck, 1)

            # Смотри подробные правила добора дилера в задании

    # Выясняем кто набрал больше очков. Выплачиваем/забираем ставку
    if sum_points(player_cards) > sum_points(dealer_cards):
        print(f"Игрок победил! Карты игрока {player_cards}. Карты диллера{dealer_cards}")
    else:
        print(f"Диллер победил! Карты игрока {player_cards}. Карты диллера{dealer_cards}")

        
 #Доделал не до конца, что успел...
