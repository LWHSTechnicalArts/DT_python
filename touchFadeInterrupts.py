while True:
    if touch.value:
        print(now)
        now = now + 1
        time.sleep(0.3)

        if now < 10:
            pixels.fill(colors[now])
            pixels.show()

        if now == 10:
            fade_index = 0   # entering fade mode — start at the first fade

        if now > 10:
            now = 0
            pixels.fill(OFF)
            pixels.show()

    # --- fade mode: runs every pass while now == 10, no touch needed ---
    if now == 10:
        fades = [
            (RED, ORANGE), (ORANGE, YELLOW), (YELLOW, GREEN), (GREEN, CYAN),
            (CYAN, BLUE), (BLUE, PURPLE), (PURPLE, WHITE), (WHITE, RED),
        ]
        from_color, to_color = fades[fade_index]
        interrupted = crossfade(from_color, to_color, 0)
        if interrupted:
            time.sleep(0.3)
            now = 11
            pixels.fill(OFF)
            pixels.show()
            now = 0
        else:
            fade_index = (fade_index + 1) % len(fades)  # advance, wrap at the end

    time.sleep(0.1)
