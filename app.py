def get_angles(figure):
    if figure == "трикутник":
        return 180
    elif figure == "квадрат":
        return 360
    elif figure == "прямокутник":
        return 360
    else:
        return None


if __name__ == "__main__":
    print(get_angles("трикутник"))