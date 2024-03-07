import sys
sys.path.append('C:\\Users\\lifet\\Documents\\GitHub\\Python-OOP\\ClassAndStaticMethods-exercise\\task3\\project')
from project.category import Category
from project.topic import Topic

class Document:

    def __init__(self, id, category_id, topic_id, file_name) -> None:
        self.id = id
        self.category_id = category_id
        self.topic_id = topic_id
        self.file_name = file_name
        self.tags = []

    
    @classmethod
    def from_instances(cls, id, category: Category, topic: Topic, file_name):
        return cls(id, category.id, topic.id, file_name)
    

    def add_tag(self, tag):
        if tag not in self.tags:
            self.tags.append(tag)


    def remove_tag(self, tag):
        if tag in self.tags:
            self.tags.remove(tag)


    def edit(self, new_file_name):
        self.file_name = new_file_name


    def __repr__(self) -> str:
        return f"Document {self.id}: {self.file_name}; category {self.category_id}, topic {self.topic_id}, tags: {', '.join(self.tags)}"