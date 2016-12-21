# Day 17: Two Steps Forward

import queue
from hashlib import md5

def main():
    key = 'pslxynzg'
    print("Part 1: {}".format(find_shortest_path(key, False)))
    print("Part 2: {}".format(max(map(len, find_shortest_path(key, True)))))

def find_shortest_path(key, return_all):
    valid_paths = []
    pos_x = 0
    pos_y = 0
    path = ''
    rooms_to_visit = queue.Queue()
    rooms_to_visit.put((path, pos_x, pos_y))

    while not rooms_to_visit.empty():
        path, pos_x, pos_y = rooms_to_visit.get()
        if pos_x == 3 and pos_y == 3:
            if return_all:
                valid_paths.append(path)
                continue
            return path

        for idx, state in enumerate(get_door_states(key, path)):
            if state == 1:
                if idx == 0 and pos_y > 0:
                    rooms_to_visit.put((path + 'U', pos_x, pos_y - 1))
                elif idx == 1 and pos_y < 3:
                    rooms_to_visit.put((path + 'D', pos_x, pos_y + 1))
                elif idx == 2 and pos_x > 0:
                    rooms_to_visit.put((path + 'L', pos_x - 1, pos_y))
                elif idx == 3 and pos_x < 3:
                    rooms_to_visit.put((path + 'R', pos_x + 1, pos_y))

    return valid_paths

def get_door_states(key, path):
    m = md5()
    m.update(key.encode('utf_8'))
    m.update(path.encode('utf_8'))
    for d in m.hexdigest()[:4]:
        if d >= 'b':
            yield 1
        else:
            yield 0

if __name__ == "__main__":
    main()