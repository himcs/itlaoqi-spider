from itlaoqi.service.ChapterService import ChapterService

result = ChapterService().get_all()
for catalogue in result:
    print(catalogue)
    # print(catalogue['url'])
