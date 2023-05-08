# class BasePage:
#     pass
#
#
# class Button:
#
#     def __init__(self, name):
#         self.name = name
#
#     def click(self):
#         print(f"Button {self.name} is clicked")
#
#
# class EULAPage(BasePage):
#
#     def __init__(self):
#         self.close_button = Button('Close')
#
#     def close(self):
#         self.close_button.click()
#
# eula_page = EULAPage()
# eula_page.close()

########################################################################################################################

class BasePage:
    pass


class CloseableMixin:

    def close(self):
        self.close_button.click()


class Button:

    def __init__(self, name):
        self.name = name

    def click(self):
        print(f"Button {self.name} is clicked")


class EULAPage(BasePage, CloseableMixin):

    def __init__(self):
        self.close_button = Button('Close')


eula_page = EULAPage()
eula_page.close()
