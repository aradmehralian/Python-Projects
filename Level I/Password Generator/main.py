import string


from src.password_generator import RandomPasswordGenerator, MemorablePasswordGenerator
from src.password_generator import PinCodeGenerator


def test_pincode_generator():
    pincode_gen = PinCodeGenerator(length=10)
    pincode = pincode_gen.generate()
    print(f"Generated pin code: {pincode}")
    assert len(pincode) == 10
    assert pincode.isdigit()
    print("Passed the tests successfully!")


def test_random_password_generator():
    password_gen = RandomPasswordGenerator(include_digits=True, include_symbols=True)
    random_password = password_gen.generate()
    print(f"Generated Password: {random_password}")
    assert len(random_password) == 12
    assert any(char in string.ascii_letters for char in random_password)
    assert any(char in string.digits for char in random_password)
    assert any(char in string.punctuation for char in random_password)
    print("Passed the tests successfully!")


def test_memorable_password_generator():
    password_gen = MemorablePasswordGenerator(num_words=4, capitalized=True)
    memorable_password = password_gen()
    print(f"Generated Password: {memorable_password}")
    assert len(memorable_password.split("-")) == 4
    assert all(word.istitle() for word in memorable_password.split("-"))
    assert all(word.isalpha() for word in memorable_password.split("-"))
    print("Passed the tests successfully!")


def main():
    print("Testing PIN code generator ...")
    test_pincode_generator()
    print("\n")
    print("Testing random password generator ...")
    test_random_password_generator()
    print("\n")
    print("Testing memorable password generator ...")
    test_memorable_password_generator()


if __name__ == "__main__":
    main()
