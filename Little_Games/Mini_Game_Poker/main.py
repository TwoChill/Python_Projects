import base as clss
import time
sleeptime = 3
test_loop = 4

try:
    # TESTING #
    while test_loop >= 0:
        while True:

            # Starts scriptwith a clear screen
            clss.sys_clear()

            # Tries left
            if test_loop <= 2:
                print(f'{test_loop} Tries Left!')
            else:
                print(f'{test_loop} Trie Left!')
            try:
                nr_of_cards = int(input('\nHow Many Cards to Generate? :> '))

                if nr_of_cards == 0:
                    clss.sys_clear()
                    print('\nWell Now.. Suit Yourself...')
                    time.sleep(sleeptime)
                    raise KeyboardInterrupt
                elif nr_of_cards > 5:
                    clss.sys_clear()
                    print('\nPoker Hands have a Maximum of \'5\'')
                    time.sleep(sleeptime)
                    continue
                break
            except ValueError:
                clss.sys_clear()
                print('\nI Only Need a Number ;)')
                time.sleep(sleeptime)
                continue
        # TESTING #

        cards = clss.Cards()
        dealer = clss.Dealer()

        # Create nr_of_cards
        ascii_cards, random_result = cards.create_cards(nr_of_cards)

        result = []
        for next_down in range(9):
            for next_side in range(1):
                result.append('  '.join(ascii_cards[next_side][next_down]))
        print()

        for card in result:
            print(card)

        # TESTING #
        input('\nPRESS ENTER')
        test_loop -= 1

        continue

    raise KeyboardInterrupt
except KeyboardInterrupt:
    clss.sys_clear()
    print('\nGoodBye..\n')
    quit()
        # TESTING #