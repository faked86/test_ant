from matplotlib import image

GRID_X = 1024
GRID_Y = 1024
START_X = 512
START_Y = 512


def main():
    grid = []
    for _ in range(GRID_Y):
        grid.append([True] * GRID_X)  # True - white, False - black

    # 0 - up, 1 - right, 2 - down, 3 - left, % - to find orientation
    ant_orientation = 0
    ant_pos = [START_X - 1, START_Y - 1]

    black_count = 0
    while (
        ant_pos[0] >= 0
        and ant_pos[0] < GRID_X
        and ant_pos[1] >= 0
        and ant_pos[1] < GRID_Y
    ):
        # choose orientation
        if grid[ant_pos[1]][ant_pos[0]]:
            ant_orientation = (ant_orientation + 1) % 4
            black_count += 1
        else:
            ant_orientation = (ant_orientation - 1) % 4
            black_count -= 1

        # change color
        grid[ant_pos[1]][ant_pos[0]] = not grid[ant_pos[1]][ant_pos[0]]

        # move
        if ant_orientation == 0:
            ant_pos[1] -= 1
        elif ant_orientation == 1:
            ant_pos[0] += 1
        elif ant_orientation == 2:
            ant_pos[1] += 1
        else:
            ant_pos[0] -= 1

    print(black_count)
    image.imsave("res.png", grid)


if __name__ == "__main__":
    main()
