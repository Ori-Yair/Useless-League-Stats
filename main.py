import pandas

from riotwatcher import LolWatcher, ApiError


def main():
    watcher = LolWatcher(get_key())
    region = ''
    summoner = ''

    summoner_info = watcher.summoner.by_name(region, summoner)
    print(summoner_info)


def get_key():
    with open('api-key', 'r') as key_file:
        return key_file.read()


if __name__ == '__main__':
    main()

