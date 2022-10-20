from pprint import pprint

import requests


def main():
    my_herous = ['Hulk', 'Captain America', 'Thanos']
    base_url = 'https://akabab.github.io/superhero-api/api'
    all_url = f'{base_url}/all.json'
    response = requests.get(url=all_url)
    all_herous = response.json()
    max_intelligence = 0
    max_name_res = ""
    cnt = 0

    for hero in all_herous:
        if hero['name'] in my_herous:
            intelligence = hero["powerstats"]["intelligence"]
            if max_intelligence < intelligence:
                max_intelligence = intelligence
                max_name_res = hero["name"]
                cnt += 1

            if cnt == len(my_herous):
                break

    print(max_name_res)


if __name__ == '__main__':
    main()
