
def count_days(start, total):
    if start <= total:
        print(f"Day {start}")
        count_days(start+1, total)


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    count_days(1, days)
    print("Harvest time!")
