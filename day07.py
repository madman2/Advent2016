# Day 07: Internet Protocol Version 7

def main():
    tls_ips = []
    ssl_ips = []

    with open('day07.txt') as f:
        for line in f:
            if (supports_tls(line)):
                tls_ips.append(line)
            if (supports_ssl(line)):
                ssl_ips.append(line)

    print("Part 1: {}".format(len(tls_ips)))
    print("Part 2: {}".format(len(ssl_ips)))

def supports_tls(ip):
    in_brace = False
    abba_found = False
    for idx, c in enumerate(ip):
        if idx > len(ip) - 3:
            break
        if c == '[':
            in_brace = True
        elif c == ']':
            in_brace = False
        if is_abba(ip[idx:idx + 4]):
            if in_brace:
                return False
            else:
                abba_found = True

    return abba_found

def supports_ssl(ip):
    abas = []
    babs = []
    in_brace = False
    for idx, c in enumerate(ip):
        if idx > len(ip) - 3:
            break
        if c == '[':
            in_brace = True
        elif c == ']':
            in_brace = False
        if is_aba_or_bab(ip[idx:idx + 3]):
            if in_brace:
                babs.append((c, ip[idx + 1]))
            else:
                abas.append((c, ip[idx + 1]))

    for aba in abas:
        for bab in babs:
            if aba[0] == bab[1] and aba[1] == bab[0]:
                return True

    return False

def is_abba(segment):
    return segment[1] == segment[2] and segment[0] == segment[3] and segment[0] != segment[1]

def is_aba_or_bab(segment):
    return segment[0] == segment[2] and segment[0] != segment[1]

if __name__ == "__main__":
    main()