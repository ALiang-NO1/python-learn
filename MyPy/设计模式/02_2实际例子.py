"""
在不同类型的社交网络（例如LinkedIn、Facebook等）上为个人或公司建立简介。
每个简介都有某些特定的组成章节。在LinkedIn的简介中，有一个章节是关于个人申请的专利或出版作品的。
在Facebook上，将在相册中看到最近度假地点的照片区。
"""
from abc import ABCMeta, abstractmethod


class Section(metaclass=ABCMeta):
    @abstractmethod
    def describe(self):
        pass


class PersonalSection(Section):
    def describe(self):
        print('Person Section')


class AlbumSection(Section):
    def describe(self):
        print('Album Section')


class PatentSection(Section):
    def describe(self):
        print('Patent Section')


class PublicSecton():
    def describe(self):
        print('Public Section')


class Profile(metaclass=ABCMeta):
    def __init__(self):
        self.sections = []
        self.createProfile()

    def createProfile(self):
        pass

    def getSections(self):
        return self.sections

    def addSection(self, section):
        self.sections.append(section)


class Linkedin(Profile):
    def createProfile(self):
        self.addSection(PersonalSection)
        self.addSection(PatentSection)
        self.addSection(AlbumSection)


class Facebook(Profile):
    def createProfile(self):
        self.addSection(PatentSection)
        self.addSection(AlbumSection)


if __name__ == '__main__':
    profile_type = input('Linkedin or Facebook?')
    profile = eval(profile_type)()
    print('Creating Profile..', type(profile).__name__)
    print('Profile has sections:', profile.getSections())
