with open("test_emotet.bin", "wb") as f:
    # MZ header at offset 0
    f.write(b"\x4D\x5A")

    # Pad up to 0x2854
    f.write(b"\x00" * (0x2854 - 2))

    # $_eax pattern inside required range
    f.write(bytes([
        0x89, 0xE0,
        0x8D, 0x11,
        0x24,
        0x22,
        0x89,
        0xC0,
        0xFF,
        0xD0,
        0x83,
        0xEC,
        0x04
    ]))

    # Add $cmovnz pattern
    f.write(bytes([
        0x0F,
        0x45,
        0xFB,
        0x0F,
        0x45,
        0xDE
    ]))

