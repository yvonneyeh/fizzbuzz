# Pingout

```

████████╗██╗  ██╗██╗  ██╗      ██╗ ██╗██████╗  █████╗
╚══██╔══╝██║  ██║╚██╗██╔╝     ███║███║╚════██╗██╔══██╗
   ██║   ███████║ ╚███╔╝█████╗╚██║╚██║ █████╔╝╚█████╔╝
   ██║   ██╔══██║ ██╔██╗╚════╝ ██║ ██║ ╚═══██╗██╔══██╗
   ██║   ██║  ██║██╔╝ ██╗      ██║ ██║██████╔╝╚█████╔╝
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝      ╚═╝ ╚═╝╚═════╝  ╚════╝

```

## Running Pingout

1. Clone this repository:
```shell
git clone https://github.com/yvonneyeh/fizzbuzz.git
```

2. To execute, run the following in your terminal:
```shell
python3 pingout.py
```

3. To execute unit-tests, run the following in your terminal:
```shell
python3 tests.py
```

## Info

Integrated Connectivity Solutions is making a new cellular modem, the THX-1138, that has a unique system for checking its connections to nearby towers. It tries to check its connection on a regular interval, but the kind of check it runs varies according to how many checks it has made since powering on:

- On the first check, it sends a PING message. It sends a PING every time, except:

- If the number of checks is divisible by three (i.e. on the third check, and the sixth, and so on), it sends a CHECK_SIGNAL_STRENGTH message instead

- If the number of checks is divisible by five, it sends a CHECK_CHANNEL_NOISE message instead

- If the number of checks is divisible by three and five, it sends a SCAN_FOR_TOWERS message instead of any other messages
