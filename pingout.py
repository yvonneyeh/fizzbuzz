def pingout(i):
    """
    Returns message that a THX-1138 will send during a connection check.

    Args:
        i: connection check number (int)

    Returns:
        THX-1138 message
    """

    if i % 3 == 0 and i % 5 == 0:
        return "SCAN_FOR_TOWERS"
    elif i % 3 == 0:
        return "CHECK_SIGNAL_STRENGTH"
    elif i % 5 == 0:
        return "CHECK_CHANNEL_NOISE"
    return i


def main():
    for i in range(1, 101):
        print(pingout(i))


if __name__ == '__main__':
    main()
