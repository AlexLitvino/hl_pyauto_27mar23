from abc import ABC, abstractmethod


class AbstractLocalizer(ABC):

    @abstractmethod
    def localize(self, message):
        pass


class EnglishLocalizer(AbstractLocalizer):

    def localize(self, message):
        return message


class SpanishLocalizer(AbstractLocalizer):

    def __init__(self):
        self.translation = {'red': 'rojo',
                            'white': 'blanco'}

    def localize(self, message):
        return self.translation.get(message, message)


class UkrainianLocalizer(AbstractLocalizer):

    def __init__(self):
        self.translation = {'red': 'червоний',
                            'white': 'білий'}

    def localize(self, message):
        return self.translation.get(message, message)


class LocalizerFactory:

    def __init__(self):
        self.localizers = {'en': EnglishLocalizer,
                           'es': SpanishLocalizer,
                           'ua': UkrainianLocalizer}

    def get_localizer(self, code):
        return self.localizers.get(code)()


current_localizer = LocalizerFactory().get_localizer('es')
print(current_localizer.localize('red'))




