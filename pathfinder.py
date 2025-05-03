import pprint
import random

CLUSTERS = [0,1,2,3,4,5]
SYMBOLS = [0,1,2]

HEX = 0
MOON = 1
ARROW = 2

RED = "Red"
YELLOW = "Yellow"
BLUE = "Blue"

def get_other_clusters(a, b):
    temp = []
    for c in CLUSTERS:
        temp.append(c)
    temp.remove(a)
    temp.remove(b)
    return temp

def get_third_symbol(a, b):
    temp = []
    for s in SYMBOLS:
        temp.append(s)
    temp.remove(a)
    temp.remove(b)
    return temp[0]

def get_intersection(a, b=None):
    resulta = []
    for row in CLUSTERS:
        for col in SYMBOLS:
            if row == a[0] or col == a[1]:
                resulta.append((row, col))
    if b:
        resulta = set(resulta)
        resultb = get_intersection(b)
        result = resulta.intersection(resultb)
        if a in result:
            result.remove(a)
        if b in result:
            result.remove(b)
        return result
    return set(resulta)

def does_intersect(a, b):
    return a[0] == b[0] or a[1] == b[1]

def make_cluster():
    result = {}
    for x in SYMBOLS:
        result[x] = None
    return result

def make_chart():
    result = {}
    for x in CLUSTERS:
        result[x] = make_cluster()
    return result

def remove_all(chart, color):
    for row in chart:
        cluster = chart[row]
        for col in cluster:
            x = cluster[col]
            if x == color:
                cluster[col] = None

def get_matching_meeples(chart, color):
    result = []
    for row in chart:
        cluster = chart[row]
        for col in cluster:
            x = cluster[col]
            if x == color:
                result.append((row, col, x))
    return result

def no_meeples(chart):
    for i in chart:
        cluster = chart[i]
        for symbol in cluster:
            x = cluster[symbol]
            if x is not None:
                return False
    return True

def build_bag(yellow, blue, red):
    result = []
    for i in range(0, yellow):
        result.append(YELLOW)
    for i in range(0, blue):
        result.append(BLUE)
    for i in range(0, red):
        result.append(RED)
    return result

def add_yellows_between_blues(chart, new_row, new_col, match):
    match_row = match[0]
    match_col = match[1]
    if match_row == new_row:
        third_symbol = get_third_symbol(new_col, match_col)
        chart[match_row][third_symbol] = YELLOW
    elif match_col == new_col:
        rows = get_other_clusters(new_row, match_row)
        for row in rows:
            chart[row][match_col] = YELLOW
    elif match_row != new_row and match_col != new_col:
        chart[match_row][new_col] = YELLOW
        chart[new_row][match_col] = YELLOW
    chart[new_row][new_col] = BLUE

def add_blue_to_chart(chart, planet):
    new_row = planet[0]
    new_col = planet[1]
    matches = get_matching_meeples(chart, BLUE)
    if len(matches) == 0:
        chart[new_row][new_col] = BLUE
    elif len(matches) == 1:
        match = matches[0]
        add_yellows_between_blues(chart, new_row, new_col, match)
    elif len(matches) == 2:
        match_col1 = matches[0][1]
        match_col2 = matches[1][1]
        match_row1 = matches[0][0]
        match_row2 = matches[1][0]
        if match_col1 == match_col2 and match_col1 == new_col:
            chart[new_row][new_col] = BLUE
        elif match_row1 == match_row2 and match_row1 == new_row:
            pprint.pp(chart)
            raise Exception("adding third blue to same row")
        else:
            remove_all(chart, YELLOW)
            xab = get_intersection(planet, matches[0])
            xbc = get_intersection(matches[0], matches[1])
            xabc = xab.intersection(xbc)
            if len(xabc) > 1:
                pprint.pp(chart)
                raise Exception("3 blues but can't uniquely id portal")
            x = list(xabc)[0]
            chart[x[0]][x[1]] = YELLOW
            chart[new_row][new_col] = BLUE

def add_red_to_chart(chart, planet):
    blues = get_matching_meeples(chart, BLUE)
    xs = [ blue for blue in blues if does_intersect(blue, planet) ]:
    if len(xs) > 0:
        


def add_to_chart(chart, color, planet):
    if color == BLUE:
        add_blue_to_chart(chart, planet)
    if color == RED:
        add_red_to_chart(chart, planet)

def test_add_blue():
    chart = make_chart()
    add_to_chart(chart, BLUE, (0,0))
    add_to_chart(chart, BLUE, (5,0))
    pprint.pp(chart)
    chart = make_chart()
    add_to_chart(chart, BLUE, (1,0))
    add_to_chart(chart, BLUE, (1,2))
    pprint.pp(chart)
    chart = make_chart()
    add_to_chart(chart, BLUE, (1,0))
    add_to_chart(chart, BLUE, (2,2))
    pprint.pp(chart)

def test_remove_all():
    chart = make_chart()
    add_to_chart(chart, BLUE, (0,0))
    add_to_chart(chart, BLUE, (5,0))
    pprint.pp(chart)
    remove_all(chart, YELLOW)
    pprint.pp(chart)

def test_get_intersection():
    x = get_intersection((0,1), (3,1))
    pprint.pp(x)


chart = make_chart()
add_to_chart(chart, BLUE, (0,0))
add_to_chart(chart, BLUE, (5,0))
add_to_chart(chart, BLUE, (3,1))
pprint.pp(chart)

# bag = build_bag(1, 7, 10)
# print(bag)
# print(random.choice(bag))

# def guess(chart):
#     if no_meeples(chart):
#         bag = build_bag(1, 7, 10)
