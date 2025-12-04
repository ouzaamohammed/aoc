def main():
    file_path = "input.txt"
    pos = 50
    zero_count = 0
    zero_touched_count = 0
    try:
        with open(file_path, "r") as f:
            lines = f.readlines()
            for line in lines:
                if not line:
                    continue
                dir = line[0]
                dist = int(line[1:])
                for _ in range(dist):
                    if dir == "L":
                        pos = (pos - 1 + 100) % 100
                    else:
                        pos = (pos + 1) % 100
                    if pos == 0:
                        zero_touched_count += 1
                if pos == 0:
                    zero_count += 1

    except FileNotFoundError:
        print(f"Error: the file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error accured: {e}")

    print(f"Part one solution: {zero_count}")
    print(f"Part two solution: {zero_touched_count}")


main()
