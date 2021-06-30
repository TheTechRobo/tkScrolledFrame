"""Demonstration of the ScrolledFrame widget.
Copyright (c) 2018 Benjamin Johnson

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from tkinter import *
from . import ScrolledFrame


# EGA color palette
# Format: background, foreground
COLORS = [
    ("black",   "white"),
    ("#0000AA", "white"),
    ("#00AA00", "white"),
    ("#00AAAA", "white"),
    ("#AA0000", "white"),
    ("#AA00AA", "white"),
    ("#AA5500", "white"),
    ("#AAAAAA", "black"),
    ("#555555", "white"),
    ("#5555FF", "black"),
    ("#55FF55", "black"),
    ("#55FFFF", "black"),
    ("#FF5555", "black"),
    ("#FF55FF", "black"),
    ("#FFFF55", "black"),
    ("white",   "black"),
]


def demo():
    """Display a demonstration of the ScrolledFrame widget."""

    root = Tk()
    root.title("tkScrolledFrame Demo")

    # Plenty of ways to close the window
    for seq in "<Escape>", "<Control-w>", "<Control-q>":
        root.bind(seq, lambda event: root.destroy())

    # ScrolledFrame widget
    sf = ScrolledFrame(root, width=640, height=480)
    sf.pack(side="top", expand=1, fill="both")

    # Bind the arrow keys and scroll wheel
    sf.bind_arrow_keys(root)
    sf.bind_scroll_wheel(root)

    # Create a frame within the ScrolledFrame
    inner_frame = sf.display_widget(Frame)

    # Add a bunch of widgets to fill some space
    num_rows = 16
    num_cols = 16
    for row in range(num_rows):
        for column in range(num_cols):
            # Offset the palette each row to create a diagonal pattern
            background, foreground = COLORS[(column + row) % len(COLORS)]

            w = Label(inner_frame,
                      width=15,
                      height=5,
                      background=background,
                      foreground=foreground,
                      borderwidth=2,
                      relief="groove",
                      anchor="center",
                      justify="center",
                      text=str(row * num_cols + column))

            w.grid(row=row,
                   column=column,
                   padx=4,
                   pady=4)

    root.mainloop()


if __name__ == "__main__":
    demo()
