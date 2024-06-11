import requests
import re


def soultion():
    with open("anser.txt", "w", encoding="utf-8") as f:
        for i in range(1910):  # show different pages 1910
            url = f"https://exam.naer.edu.tw/searchResult.php?page={i}&orderBy=lastest&keyword=&selCountry=&selCategory=0&selTech=0&selYear=&selTerm=&selType=&selPublisher="
            res = requests.get(url)
            log = re.findall(
                r'<td bgcolor="#FFFFFF" class="t4">\s*(.*?)\s*</td>',
                res.text,
                re.DOTALL,
            )  ## 11 size each school need 1-4
            pdf_links = re.findall(r'href="(/otc/testStoreFile/[^"]+\.pdf)"', res.text)

            for i in range(0, len(log), 12):
                school = (
                    log[i + 1]
                    + log[i + 2]
                    + log[i + 3]
                    + log[i + 4]
                    + pdf_links[i // 11]
                )
                print(school)
                f.write(school + "\n")


if __name__ == "__main__":
    soultion()
