from faker import Faker

faker = Faker()


def get_registered_user():
    """
    Returning dict with fake data
    """
    return {
        'name': faker.name(),
        'country': faker.country()
    }


if __name__ == '__main__':
    get_registered_user()