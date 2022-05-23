class Language:
    default_language = "English"

    def __init__(self):
        self.show = '나의 언어는' + self.default_language

    #class method 와 static method의 차이는 상속에서 두드러지게 나타남,
    @classmethod
    def class_my_language(cls): #상속받은 클래스인 Korean Lang을 받아서 "한국어"가 뜨겠구나 : cls의 클래스 속성을 가져오겠구나
        return cls()

    @staticmethod # static에서는 지금 Langeuage의 인스턴스를 띄우겠구나 : 부모 클래스 속성 값을 가져오겠구나
    def static_my_language():
        return Language()

    def print_language(self):
        print(self.show)


class KoreanLanguage(Language):
    default_language = "한국어"