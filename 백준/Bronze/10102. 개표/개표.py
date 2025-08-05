import sys

input = sys.stdin.readline

def count_votes(vote: str) -> tuple[int, int]:
    return vote.count('A'), vote.count('B')

def determine_winner(a: int, b: int) -> str:
    if a > b:
        return "A"
    elif a < b:
        return "B"
    else:
        return "Tie"

def main():
    n = int(input())
    print(determine_winner(*count_votes(input().strip())))


if __name__ == "__main__":
    main()