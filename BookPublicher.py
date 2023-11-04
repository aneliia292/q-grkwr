class Publisher:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def get_info(self):
        return f' - издательства: {self.location},{self.name}'

    def publish(self, message):
        return f'Готовим:{message} к публикации в {self.location} ({self.location})'


class BookPublisher (Publisher):
    def __init__(self, name, location, num_authors):
        super ().__init__ (name, location)
        self.num_authurs = num_authors


    def publish(self, book, authors):
        return f'Передаем рукопись,:{book} написанную автором:{author} в издательство: {self.name} ({self.location})'


class NewspapperPublisher (Publisher):
    def __init__(self, name, location, num_bages):
        super ().__init__ (name, location)
        self.num_bages = num_bages

    def publish(self, message):
        return (
            f'Печатаем свежий номер со статьей,:{message} на главной странице в издательстве: {self.name} ({self.location})')


pub = Publisher ('sdasda', 'alabuga')
print (pub.publish ('sdasda'))
print (pub.get_info ())
book_publisher = BookPublisher ("Московские ввксти", "Caмара", '52')
print (book_publisher.publish ('Приключения Чебурашки', 'В.И.Пупкин'))

newspapper_publisher = NewspapperPublisher ('Московские ввести', 'Москва', '12')
print (newspapper_publisher.publish ('Новая версия Midjourney будет платной'))
