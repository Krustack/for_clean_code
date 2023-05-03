def cc(n, h, d):
    return {'name': n, 'health': h, 'damage': d, 'defense': 0}

def is_a(cc):
    return cc['health'] > 0

def a(at, df):
    if is_a(df):
        dd = max(0, at['damage'] - df['defense'])
        df['health'] -= dd
        print(f"{at['name']} attacks {df['name']} for {dd} damage.")
        df['defense'] = 0
    else:
        print(f"{df['name']} has already been defeated.")

def d(c):
    c['defense'] = 10
    print(f"{c['name']} is defending.")

def h(c): #ใช้ในการฟื้นฟู
    c['health'] += 15
    if c['health'] > 100:
        c['health'] = 100
    print(f"{c['name']} heals. Current health: {c['health']}.")


def game():
    p = cc("Player", 100, 20)
    d = cc("dragon", 100, 15)

    while is_a(p) and is_a(d):
        print(f"\n{p['name']}'s Health: {p['health']}, {d['name']}'s Health: {d['health']}")
        ch = input("Enter 1 to attack\nEnter 2 to defend \nEnter 3 to heal\nplease enter 1 - 3 for play!: ")
        if ch == "1":
            a(p, d)
        elif ch == "2":
            d(p)
        elif ch == "3":
            h(p)
        else:
            print("Invalid choice. You lose your turn.")
        
        if is_a(d):
            import random
            dc = random.choice(["1", "2", "3"])
            if dc == "1":
                a(d, p)
            elif dc == "2":
                d(d)
            elif dc == "3":
                h(d)

    if is_a(p):
        print("\nPlayer wins!")
    else:
        print("\nNPC wins!")

game()
