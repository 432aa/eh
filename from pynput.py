def on_esc_press(key):
    if key == keyboard.Key.esc:
        print("Esc key pressed, exiting...")
        listener.stop()

with keyboard.Listener(on_press=on_esc_press) as listener:
    listener.join()