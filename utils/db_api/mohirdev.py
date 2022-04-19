import aiohttp
from bs4 import BeautifulSoup


async def get_data():
    url = "https://mohirdev.uz/courses/"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            result = []
            size = 10
            for i in BeautifulSoup(await response.text(), "html.parser").find_all("div", class_="row skillate-course-col align-items-lg-center"):
                for j in BeautifulSoup(str(i), "html.parser").find_all("div", class_="skillate-course-body mb-sm-0 mb-3"):
                    result.append({
                        "title": str(j.find("h3").text).replace("\n", ""),
                        "ustoz": str(j.find("h4").text).replace("\n", ""),
                        "link": i.find("a")["href"],
                        "img": BeautifulSoup(
                            str(i), "html.parser").find("img")["src"]
                    })
            return [list(result[i:i+size]) for i in range(len(result))[::size]]


async def num_course():
    url = "https://mohirdev.uz/courses/"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return int(str(BeautifulSoup(await response.text(), "html.parser").find("div", class_="d-none d-md-block").text).replace("\n", "").split(" ")[0])
