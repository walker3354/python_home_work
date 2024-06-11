import re


def solution():
    vip_list = list()
    member_list = list()
    total_sales = {"Computer": 0, "Notebook": 0, "Paper": 0, "Book": 0}

    with open("log.txt", "r") as f:
        log = f.read()
        vip_list = re.findall(r"^\[VIP\].*", log, re.MULTILINE)
        member_list = re.findall(r"^(?!\[VIP\]).*", log, re.MULTILINE)

    print("[VIP]")
    for VIP in vip_list:
        print(VIP)
        match = re.search(r"buys (\w+) for \$(\d+)", VIP)
        if match:
            item = match.group(1)
            price = int(match.group(2))
            if item in total_sales:
                total_sales[item] += price

    print("\n[Member]")
    for member in member_list:
        print(member)
        match = re.search(r"buys (\w+) for \$(\d+)", member)
        if match:
            item = match.group(1)
            price = int(match.group(2))
            if item in total_sales:
                total_sales[item] += price

    print("\nTotal Sales:")
    for item, total in total_sales.items():
        print(f"{item}: ${total}")


if __name__ == "__main__":
    solution()
