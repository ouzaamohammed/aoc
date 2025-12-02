def main():
    file_path = "input.txt"
    start = 50
    count = 0
    try:
        with open(file_path, "r") as f:
            lines = f.readlines()
            curr = start
            for line in lines:
                if not line:
                    continue

                dir = line[0]
                dist = int(line[1:])

                if dir == "L":
                    curr = (curr - dist) % 100
                    if curr == 0:
                        count += 1
                if dir == "R":
                    curr = (curr + dist) % 100
                    if curr == 0:
                        count += 1

    except FileNotFoundError:
        print(f"Error: the file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error accured: {e}")

    print(count)


main()
