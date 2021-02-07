from itlaoqi.service.BaseService import BaseService


class CatalogueService(BaseService):
    def get_all(self):
        sql = "SELECT id,name,url from catalogue"
        result = self.fetchall(sql)
        return result
