"""
File: webcrawler.py
Name: Han Hsiu
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10900879
Female Number: 7946050
---------------------------
2000s
Male Number: 12977993
Female Number: 9209211
---------------------------
1990s
Male Number: 14146310
Female Number: 10644506
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, "html.parser")

        # ----- Write your code below this line ----- #
        tags = soup.find_all("tbody")
        # list the string in <td> and calculate the total numbers of male name and female name
        for tag in tags:
            data = tag.find_all("td")
            male_number = 0
            female_number = 0
            for i in range(len(data)-1):
                n = data[i].text
                if not n.isdigit():
                    if not n.isalpha() and len(n) > 0:
                        number = int(n.replace(",", ""))
                        if i % 5 == 2:
                            male_number += number
                        if i % 5 == 4:
                            female_number += number
            print("Male Number: " + str(male_number))
            print("Female Number: " + str(female_number))


if __name__ == '__main__':
    main()
