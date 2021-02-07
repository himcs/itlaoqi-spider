from itlaoqi.service.CatalogueService import CatalogueService

result = CatalogueService().get_all()
for catalogue in result:
    print(catalogue)
    # print(catalogue['url'])
