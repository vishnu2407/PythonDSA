# Tower of Hanoi

def towerofHanoi(n, source, helper, destination):
    if n==1:
        print(f"Move disk {n} from {source} to {destination}")
        return
    towerofHanoi(n-1, source, destination, helper)
    print(f"Move disk {n} from {source} to {destination}")
    towerofHanoi(n-1, helper, source, destination)


if __name__ == "__main__":
    towerofHanoi(2, 'Src', 'Helper', 'Destination')