def predict(count):
    return int(count * 1.12)


def get_density(count):

    if count >= 70:
        return "HIGH"

    elif count >= 30:
        return "MEDIUM"

    else:
        return "LOW"