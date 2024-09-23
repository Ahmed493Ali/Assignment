import random

class Card:
    FACES = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    def __init__(self, face, suit):
        """تهيئة البطاقة بالقيمة والنوع مع التحقق من صحتها."""
        if face not in Card.FACES:
            raise ValueError(f"Invalid face value: {face}. Must be one of {Card.FACES}.")
        if suit not in Card.SUITS:
            raise ValueError(f"Invalid suit value: {suit}. Must be one of {Card.SUITS}.")
        self._face = face
        self._suit = suit

    def get_face(self):
        """إرجاع قيمة الوجه للبطاقة."""
        return self._face

    def get_suit(self):
        """إرجاع نوع البطاقة."""
        return self._suit

    def get_image_name(self):
        """إرجاع اسم ملف الصورة للبطاقة."""
        return f"{self.get_face()}_{self.get_suit()}.png"

    def __repr__(self):
        """إرجاع التمثيل النصي للبطاقة."""
        return f"Card(face='{self.get_face()}', suit='{self.get_suit()}')"

    def __str__(self):
        """إرجاع التمثيل النصي للبطاقة عند الطباعة."""
        return f'{self.get_face()} of {self.get_suit()}'

    def __format__(self, format):
        """إرجاع تمثيل نصي منسق للبطاقة."""
        if format == 'short':
            return f'{self.get_face()[0]}{self.get_suit()[0]}'
        return self.__str__()

# مثال لاستخدام الكود
if __name__ == "__main__":
    # اختيار بطاقة عشوائية
    random_face = random.choice(Card.FACES)
    random_suit = random.choice(Card.SUITS)
    card = Card(random_face, random_suit)  # إنشاء بطاقة جديدة
    print(card)                            # طباعة البطاقة
    print(repr(card))                      # طباعة التمثيل النصي
    print(card.get_image_name())           # طباعة اسم الصورة
