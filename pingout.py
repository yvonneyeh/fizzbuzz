def pingout(i):
    """
    Returns message that a THX-1138 will send during a connection check.

    Throws an exception if the type is not an integer.

    Args:
        i: connection check number (int)

    Returns:
        THX-1138 message
    """
    if not isinstance(i, int):
        return "NOT_INT"
    elif i == 1:
        return "PING"
    elif i % 3 == 0 and i % 5 == 0:
        return "SCAN_FOR_TOWERS"
    elif i % 3 == 0:
        return "CHECK_SIGNAL_STRENGTH"
    elif i % 5 == 0:
        return "CHECK_CHANNEL_NOISE"
    else:
        # return "PING"
        if i % 2 == 0:
            return "PING"
        else:
            return "PONG"


def main():

    # i = "hello"
    # print(pingout(i))
    for i in range(1, 101):
        print(pingout(i))


if __name__ == '__main__':
    main()
